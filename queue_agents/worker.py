#!/usr/bin/env python3
"""
worker.py

Autonomous queue worker agent.

Processes queue items autonomously:
1. Auto-lease queue item (before agent starts)
2. Research and fix the gap
3. Validate with indexer
4. Check if gap resolved
5. Auto-complete and recycle (or release if failed)

Usage:
    python -m queue_agents.worker --agent <agent_name> [--model <model>] [--max-items <n>]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, Any, Optional, List

from dotenv import load_dotenv
from agents import Agent, Runner, ItemHelpers

from queue_agents import cost_tracker

# Load environment variables from .env file
load_dotenv()


def format_tool_call(name: str, args: dict) -> str:
    """Format a tool call for display."""
    args_str = ", ".join(f"{k}={repr(v)[:50]}" for k, v in args.items())
    return f"{name}({args_str})"


def format_tool_output(output: Any) -> str:
    """Format tool output for display."""
    if isinstance(output, dict):
        if "error" in output:
            return f"Error: {output['error']}"
        if "success" in output:
            return f"Success: {output.get('message', 'OK')}"
        # Summarize dict
        keys = list(output.keys())[:5]
        return f"Dict with keys: {', '.join(keys)}"
    elif isinstance(output, str):
        return output[:200] + ("..." if len(output) > 200 else "")
    else:
        return str(output)[:200]


# Paths
REPO_ROOT = Path(__file__).parent.parent
CACHED_CONTEXT_FILE = Path(__file__).parent / "cached_context.md"
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"
WORK_QUEUE_FILE = REPO_ROOT / "out" / "work_queue.jsonl"


# Agent instructions
AGENT_INSTRUCTIONS = """
You are an autonomous KB gap-filling agent.

A queue item has been leased for you (you will see the lease result below).

## Your Goal
Make the necessary changes to resolve this gap completely.

## Process
1. **Research the gap**: Use rg_search() and read_file() to understand what's needed
   - Search for similar items in the KB to understand patterns
   - Read related files to understand context
   - Search papers if needed for technical details

2. **Make edits**: Use write_file() to create or update YAML files
   - Follow the structure shown in the cached context examples
   - Use proper IDs, units, and field names
   - Add notes explaining your assumptions

3. **Validate**: Call run_indexer() to check your changes
   - If errors appear, analyze and fix them
   - Continue until indexer passes

4. **Check resolution**: After indexer passes, read out/work_queue.jsonl to see if your gap is gone
   - If gap is resolved: You're done! The system will auto-complete.
   - If gap persists: Continue working to resolve it.

5. **Give up if stuck**: After 3 full attempts, if you cannot resolve the gap, call queue_release()

## Output Format
Be verbose so monitoring agents can follow your work:
- Explain your reasoning before each action
- Print search queries and what you're looking for
- Show file contents when you create/edit them
- Explain validation results
- State clearly when you believe the gap is resolved

## Important Notes
- Focus on doing ONE item WELL, not many items quickly
- Follow existing KB patterns (use the examples in cached context)
- Don't try to anticipate downstream gaps - let the indexer find them
- When uncertain, use conservative defaults from similar items
- You do NOT call queue_complete() - the system does this automatically if you succeed

Begin by analyzing the leased queue item below.
"""


def execute_queue_lease(agent_name: str) -> Dict[str, Any]:
    """Execute queue lease command and parse result."""
    cmd = [
        str(VENV_PYTHON),
        "-m",
        "kbtool",
        "queue",
        "lease",
        "--agent",
        agent_name,
    ]

    try:
        proc = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )

        output = proc.stdout.strip()

        # Parse the lease output
        # Format: "Leased: <item_id>" or "No pending items"
        if "No pending items" in output or "no items" in output.lower():
            return {"available": False, "message": "No work available"}

        # Try to parse as JSON (if output is JSON)
        try:
            result = json.loads(output)
            if isinstance(result, dict):
                result["available"] = True
                return result
        except json.JSONDecodeError:
            pass

        # Parse text format
        if "Leased:" in output:
            lines = output.split("\n")
            item_id = None
            gap_type = None
            context = {}

            for line in lines:
                if "Leased:" in line:
                    item_id = line.split("Leased:")[-1].strip()
                elif "Gap:" in line:
                    gap_type = line.split("Gap:")[-1].strip()
                elif "Item:" in line:
                    context["item"] = line.split("Item:")[-1].strip()
                elif "Context:" in line:
                    context["raw"] = line.split("Context:")[-1].strip()

            if item_id:
                return {
                    "available": True,
                    "item_id": item_id,
                    "gap_type": gap_type,
                    "context": context,
                    "raw_output": output,
                }

        return {"available": False, "error": "Failed to parse lease output", "output": output}

    except Exception as e:
        return {"available": False, "error": str(e)}


def execute_queue_complete(item_id: str, agent_name: str) -> Dict[str, Any]:
    """Execute queue complete command."""
    cmd = [
        str(VENV_PYTHON),
        "-m",
        "kbtool",
        "queue",
        "complete",
        "--id",
        item_id,
        "--agent",
        agent_name,
    ]

    try:
        proc = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )

        return {
            "success": proc.returncode == 0,
            "output": proc.stdout,
            "error": proc.stderr if proc.returncode != 0 else None,
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


def check_gap_resolved(item_id: str) -> bool:
    """Check if a gap is still present in the work queue."""
    if not WORK_QUEUE_FILE.exists():
        return False

    try:
        with WORK_QUEUE_FILE.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                    if entry.get("id") == item_id:
                        return False  # Gap still exists
                except json.JSONDecodeError:
                    continue
        return True  # Gap not found = resolved
    except Exception:
        return False


def execute_run_indexer() -> Dict[str, Any]:
    """Execute the indexer (plain Python function, not a tool)."""
    cmd = [str(VENV_PYTHON), "-m", "kbtool", "index"]

    try:
        proc = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to run indexer: {e}",
            "errors": [str(e)],
            "warnings": [],
        }

    output = proc.stdout
    stderr = proc.stderr

    errors = []
    warnings = []
    gap_count = 0

    for line in output.splitlines():
        line_lower = line.lower()
        if "error" in line_lower and "0 errors" not in line_lower:
            errors.append(line.strip())
        if "warning" in line_lower:
            warnings.append(line.strip())
        if "gaps" in line_lower or "gap" in line_lower:
            import re
            match = re.search(r'(\d+)\s+gaps?', line)
            if match:
                gap_count = int(match.group(1))

    if stderr:
        for line in stderr.splitlines():
            if line.strip():
                errors.append(line.strip())

    success = proc.returncode == 0 and len(errors) == 0

    summary_lines = []
    for line in output.splitlines():
        if "processed" in line.lower() or "total" in line.lower() or "gaps" in line.lower():
            summary_lines.append(line.strip())
    summary = " | ".join(summary_lines[:3]) if summary_lines else "Indexer completed"

    return {
        "success": success,
        "exit_code": proc.returncode,
        "output": output,
        "errors": errors,
        "warnings": warnings,
        "summary": summary,
        "gap_count": gap_count,
    }


def execute_queue_release_direct(item_id: str, agent_name: str) -> Dict[str, Any]:
    """Execute queue release (plain Python function, not a tool)."""
    cmd = [
        str(VENV_PYTHON),
        "-m",
        "kbtool",
        "queue",
        "release",
        "--id",
        item_id,
        "--agent",
        agent_name,
    ]

    try:
        proc = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )

        if proc.returncode == 0:
            return {
                "success": True,
                "message": f"Released {item_id}",
                "output": proc.stdout,
            }
        else:
            return {
                "success": False,
                "message": f"Failed to release {item_id}",
                "error": proc.stderr or proc.stdout,
            }
    except Exception as e:
        return {
            "success": False,
            "message": f"Failed to release {item_id}",
            "error": str(e),
        }


async def run_agent_streamed(agent: Agent, user_input: str, max_turns: int = 20):
    """Run the agent with streaming to show tool calls and outputs."""
    import json

    result = Runner.run_streamed(agent, user_input, max_turns=max_turns)
    last_tool_name = None

    async for event in result.stream_events():
        if event.type == "run_item_stream_event":
            item = event.item

            if item.type == "tool_call_item":
                # Tool is being called
                raw = item.raw_item
                name = getattr(raw, "name", "unknown")
                args_str = getattr(raw, "arguments", "{}")

                try:
                    args = json.loads(args_str) if args_str else {}
                except json.JSONDecodeError:
                    args = {"raw": args_str}

                call_str = format_tool_call(name, args)
                print(f"  ● TOOL: {call_str}", flush=True)
                last_tool_name = name

            elif item.type == "tool_call_output_item":
                # Tool returned results
                output_str = format_tool_output(item.output)
                print(f"    ⎿ OUTPUT: {output_str}", flush=True)

            elif item.type == "message_output_item":
                # Agent generated a message
                text = ItemHelpers.text_message_output(item)
                if text:
                    text_display = text.strip()
                    if len(text_display) > 300:
                        text_display = text_display[:300] + "..."
                    print(f"\n  ● AGENT: {text_display}\n", flush=True)

            elif item.type == "reasoning_item":
                print(f"    (reasoning...)", flush=True)

    return result


def build_agent(model: str = "gpt-5-nano") -> Agent:
    """Build the agent with cached context."""
    import hashlib
    from queue_agents.kb_tools import rg_search, read_file, write_file, run_indexer, queue_release

    # Load cached context
    if not CACHED_CONTEXT_FILE.exists():
        print(f"Error: Cached context not found at {CACHED_CONTEXT_FILE}")
        print("Run: python design/agent/build_context.py")
        sys.exit(1)

    cached_context = CACHED_CONTEXT_FILE.read_text(encoding="utf-8")

    # Build full instructions
    full_instructions = f"{cached_context}\n\n---\n\n{AGENT_INSTRUCTIONS}"

    # Log hash of instructions to verify they're static
    instructions_hash = hashlib.sha256(full_instructions.encode('utf-8')).hexdigest()[:16]
    print(f"[AGENT] System message hash: {instructions_hash}")

    agent = Agent(
        name="QueueWorkerAgent",
        instructions=full_instructions,
        tools=[rg_search, read_file, write_file, run_indexer, queue_release],
        model=model,
    )

    return agent


def run_worker(
    agent_name: str,
    model: str = "gpt-5-nano",
    max_items: Optional[int] = None,
    quiet: bool = False,
) -> int:
    """
    Run the worker agent.

    Returns:
        Exit code (0 = success, 1 = failure, 2 = no work)
    """
    items_processed = 0

    while True:
        # Check max items limit
        if max_items is not None and items_processed >= max_items:
            print(f"\n[LIMIT] Processed {items_processed} items (limit reached)")
            return 0

        # Auto-lease queue item
        print(f"\n{'='*60}")
        print(f"[LEASE] Agent {agent_name} requesting work...")
        lease_result = execute_queue_lease(agent_name)

        if not lease_result.get("available"):
            print(f"[NO WORK] {lease_result.get('message', 'Queue empty')}")
            return 2 if items_processed == 0 else 0

        # Build fresh agent for this queue item (improves prompt caching)
        print(f"[AGENT] Building fresh agent for this item...")
        agent = build_agent(model)

        # Use the full gap ID (with prefix like "no_recipe:"), not just the item_id
        item_id = lease_result["id"]
        print(f"[LEASED] {item_id}")
        print(f"  Gap type: {lease_result.get('gap_type', 'unknown')}")
        if lease_result.get("context"):
            print(f"  Context: {lease_result['context']}")

        # Build messages with auto-injected lease
        # The agent's instructions are already in the agent object
        # We just need to inject the lease result as a tool response

        user_input = "Please process the queue item that has been leased for you."

        # Run agent with streaming
        print(f"\n[AGENT START] Processing {item_id}...")
        print("-" * 60)

        max_iterations = 3
        success = False

        # Track token usage across iterations
        total_input_tokens = 0
        total_output_tokens = 0
        total_cached_tokens = 0

        for iteration in range(1, max_iterations + 1):
            print(f"\n[ITERATION {iteration}/{max_iterations}]")

            try:
                # For first iteration, we inject the lease result
                if iteration == 1:
                    # We'll pass the lease result via the user input
                    input_with_lease = (
                        f"{user_input}\n\n"
                        f"Queue item leased:\n```json\n{json.dumps(lease_result, indent=2)}\n```"
                    )
                    result = asyncio.run(run_agent_streamed(agent, input_with_lease, max_turns=40))
                else:
                    # Subsequent iterations: agent continues with feedback
                    result = asyncio.run(run_agent_streamed(agent, user_input, max_turns=40))

                # Extract token usage from result if available
                try:
                    if hasattr(result, 'context_wrapper') and hasattr(result.context_wrapper, 'usage'):
                        u = result.context_wrapper.usage
                        total_input_tokens += getattr(u, 'input_tokens', 0)
                        total_output_tokens += getattr(u, 'output_tokens', 0)
                        # Cached tokens are in input_tokens_details
                        if hasattr(u, 'input_tokens_details') and u.input_tokens_details:
                            total_cached_tokens += getattr(u.input_tokens_details, 'cached_tokens', 0)
                except Exception as e:
                    pass  # Usage tracking is optional

                # Check if agent called queue_release
                # (This is simplified - in reality we'd check the actual tool calls)
                # For now, assume agent completes naturally

                # Run indexer
                print("\n[VALIDATION] Running indexer...")
                # We would check if agent already ran indexer, but let's run it anyway
                indexer_result = execute_run_indexer()

                print(f"  Result: {'✓ PASSED' if indexer_result['success'] else '✗ FAILED'}")
                print(f"  Summary: {indexer_result.get('summary', 'N/A')}")

                if indexer_result["errors"]:
                    print(f"  Errors: {len(indexer_result['errors'])}")
                    for err in indexer_result["errors"][:5]:
                        print(f"    - {err}")

                if not indexer_result["success"]:
                    print(f"\n[RETRY] Indexer failed, continuing to iteration {iteration + 1}...")
                    user_input = (
                        f"The indexer failed with errors. Please fix them:\n"
                        f"{chr(10).join(indexer_result['errors'][:10])}"
                    )
                    continue

                # Indexer passed - check if gap resolved
                print("\n[CHECK] Verifying gap resolution...")
                gap_resolved = check_gap_resolved(item_id)

                if gap_resolved:
                    print(f"  ✓ Gap {item_id} is RESOLVED")
                    success = True
                    break
                else:
                    print(f"  ✗ Gap {item_id} still exists in queue")
                    if iteration < max_iterations:
                        print(f"\n[CONTINUE] Gap persists, continuing to iteration {iteration + 1}...")
                        user_input = (
                            "The indexer passed but the gap still exists in out/work_queue.jsonl. "
                            "Please continue working to fully resolve it."
                        )
                    continue

            except Exception as e:
                print(f"\n[ERROR] Agent exception: {e}")
                if iteration >= max_iterations:
                    break
                continue

        # Post-processing
        print("\n" + "=" * 60)

        # Determine final status
        if success:
            final_status = "completed"
            print(f"[SUCCESS] Gap {item_id} resolved!")
            print("[AUTO-COMPLETE] Marking item complete...")
            complete_result = execute_queue_complete(item_id, agent_name)
            if complete_result["success"]:
                print(f"  ✓ Completed")
            else:
                print(f"  ✗ Failed to complete: {complete_result.get('error')}")
            items_processed += 1
        else:
            final_status = "released"
            print(f"[TIMEOUT] Could not resolve {item_id} after {max_iterations} iterations")
            print("[AUTO-RELEASE] Releasing item back to queue...")
            # Execute release
            release_result = execute_queue_release_direct(item_id, agent_name)
            if release_result["success"]:
                print(f"  ✓ Released")
            else:
                print(f"  ✗ Failed to release: {release_result.get('error')}")

        # Log usage
        if total_input_tokens > 0 or total_output_tokens > 0:
            cost_tracker.log_usage(
                agent_name=agent_name,
                item_id=item_id,
                gap_type=lease_result.get("gap_type", "unknown"),
                model=model,
                input_tokens=total_input_tokens,
                output_tokens=total_output_tokens,
                cached_tokens=total_cached_tokens,
                status=final_status,
            )
            cost = cost_tracker.calculate_cost(total_input_tokens, total_output_tokens, total_cached_tokens)
            print(f"[USAGE] Tokens: {total_input_tokens:,} in + {total_output_tokens:,} out + {total_cached_tokens:,} cached | Cost: ${cost:.4f}")

        # Agent will be rebuilt at top of loop for next item (fresh conversation for better caching)
        print(f"\n[STATS] Items processed: {items_processed}")

    return 0


def main():
    parser = argparse.ArgumentParser(description="Autonomous queue worker agent")
    parser.add_argument("--agent", required=True, help="Agent name for queue leasing")
    parser.add_argument("--model", default="gpt-5-nano", help="Model to use")
    parser.add_argument("--max-items", type=int, help="Max items to process (default: unlimited)")
    parser.add_argument("--quiet", action="store_true", help="Suppress verbose output")

    args = parser.parse_args()

    try:
        exit_code = run_worker(
            agent_name=args.agent,
            model=args.model,
            max_items=args.max_items,
            quiet=args.quiet,
        )
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n[INTERRUPTED] Stopping agent...")
        sys.exit(130)
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
