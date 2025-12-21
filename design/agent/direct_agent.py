#!/usr/bin/env python3
"""
direct_agent.py

Direct agent calling interface (bypasses work queue).

Allows calling agents with specific tasks without going through the queue system.
Useful for:
- Fixing specific KB gaps discovered during simulation
- Ad-hoc KB improvements
- Targeted fixes for known issues

Usage (from Python):
    from design.agent.direct_agent import fix_kb_gap

    result = fix_kb_gap(
        task="Add material_class='metal' to kb/items/materials/metal_powder_v0.yaml",
        agent_name="claude-direct",
        model="gpt-5-nano"
    )

Usage (from CLI):
    python -m design.agent.direct_agent --task "Fix metal_powder_v0 material_class" --agent claude-direct
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Dict, Any, Optional

from dotenv import load_dotenv
from agents import Agent, Runner, ItemHelpers

# Load environment variables
load_dotenv()

# Paths
REPO_ROOT = Path(__file__).parent.parent.parent
CACHED_CONTEXT_FILE = Path(__file__).parent / "cached_context.md"
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"


# Agent instructions for direct tasks
DIRECT_AGENT_INSTRUCTIONS = """
You are a KB gap-fixing agent operating in DIRECT MODE.

Unlike queue mode, you are given a specific task to complete (described below).

## Your Goal
Complete the specific task described in the user's request.

## Process
1. **Understand the task**: Read the task description carefully
   - Use rg_search() to find relevant files if needed
   - Use read_file() to understand current state

2. **Research if needed**: Use KB tools to gather context
   - Search for similar items to understand patterns
   - Read related files to understand context
   - Follow existing KB conventions

3. **Make changes**: Use write_file() to create or update YAML files
   - Follow KB structure and naming conventions
   - Use proper IDs, units, and field names
   - Add notes explaining assumptions if applicable

4. **Validate**: Call run_indexer() to check your changes
   - If errors appear, analyze and fix them
   - Continue until indexer passes
   - You can call run_indexer() multiple times

5. **Verify**: Explain what you changed and why
   - Summarize the fix clearly
   - Note any assumptions made
   - Mention if further work is needed

## Important Notes
- Focus on the SPECIFIC task given, don't try to fix other issues
- Follow existing KB patterns (use cached context examples)
- When uncertain, use conservative defaults from similar items
- Be explicit about what you changed and why
- If you cannot complete the task, explain why

The specific task will be provided in the user's message.
"""


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


async def run_agent_streamed(agent: Agent, user_input: str, max_turns: int = 20):
    """Run the agent with streaming to show tool calls and outputs."""
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


def build_direct_agent(model: str = "gpt-5-nano") -> Agent:
    """Build an agent for direct task execution."""
    from design.agent.kb_tools import rg_search, read_file, write_file, run_indexer

    # Load cached context if available
    cached_context = ""
    if CACHED_CONTEXT_FILE.exists():
        cached_context = CACHED_CONTEXT_FILE.read_text(encoding="utf-8")
    else:
        print(f"Warning: Cached context not found at {CACHED_CONTEXT_FILE}")
        print("Run: python design/agent/build_context.py")
        print("Continuing without cached context...\n")

    # Build full instructions
    if cached_context:
        full_instructions = f"{cached_context}\n\n---\n\n{DIRECT_AGENT_INSTRUCTIONS}"
    else:
        full_instructions = DIRECT_AGENT_INSTRUCTIONS

    agent = Agent(
        name="DirectTaskAgent",
        instructions=full_instructions,
        tools=[rg_search, read_file, write_file, run_indexer],
        model=model,
    )

    return agent


def fix_kb_gap(
    task: str,
    agent_name: str = "claude-direct",
    model: str = "gpt-5-nano",
    max_turns: int = 30,
    validate: bool = True,
) -> Dict[str, Any]:
    """
    Execute a direct KB fix task using an agent.

    Args:
        task: Description of what to fix (e.g., "Add material_class='metal' to metal_powder_v0.yaml")
        agent_name: Name for logging/tracking (not used for queue leasing)
        model: Model to use for the agent
        max_turns: Maximum conversation turns
        validate: Whether to run indexer validation after changes

    Returns:
        {
            "success": bool,
            "message": str,
            "agent_output": str,
            "indexer_result": dict (if validate=True),
        }
    """
    print(f"\n{'='*60}")
    print(f"[DIRECT AGENT] Task: {task}")
    print(f"[AGENT] {agent_name} (model: {model})")
    print("-" * 60)

    try:
        # Build agent
        agent = build_direct_agent(model)

        # Run agent
        print(f"\n[AGENT START] Processing task...")
        result = asyncio.run(run_agent_streamed(agent, task, max_turns=max_turns))

        # Extract final agent message
        final_message = "Task completed (no final message)"
        if hasattr(result, 'final_messages') and result.final_messages:
            final_msg = result.final_messages[-1]
            if hasattr(final_msg, 'content'):
                final_message = final_msg.content[0].text if final_msg.content else ""

        print(f"\n[AGENT COMPLETE]")
        print("-" * 60)

        # Validation
        indexer_result = None
        if validate:
            print(f"\n[VALIDATION] Running indexer...")
            import subprocess

            cmd = [str(VENV_PYTHON), "-m", "kbtool", "index"]
            proc = subprocess.run(
                cmd,
                cwd=str(REPO_ROOT),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )

            errors = []
            for line in proc.stdout.splitlines():
                if "error" in line.lower() and "0 errors" not in line.lower():
                    errors.append(line.strip())

            indexer_result = {
                "success": proc.returncode == 0 and len(errors) == 0,
                "exit_code": proc.returncode,
                "errors": errors,
                "output": proc.stdout,
            }

            status = "✓ PASSED" if indexer_result["success"] else "✗ FAILED"
            print(f"  Result: {status}")
            if errors:
                print(f"  Errors: {len(errors)}")
                for err in errors[:5]:
                    print(f"    - {err}")

        print(f"\n{'='*60}")
        return {
            "success": True,
            "message": "Task completed",
            "agent_output": final_message,
            "indexer_result": indexer_result,
        }

    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "message": f"Failed: {e}",
            "agent_output": None,
            "indexer_result": None,
        }


def main():
    """CLI interface for direct agent calling."""
    parser = argparse.ArgumentParser(
        description="Direct KB gap fixing (bypasses queue)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m design.agent.direct_agent --task "Add material_class='metal' to metal_powder_v0.yaml"
  python -m design.agent.direct_agent --task "Fix BOM for powder_compactor_v0" --model gpt-5-nano
  python -m design.agent.direct_agent --task "Create recipe for steel_sheet_from_ingot" --no-validate
        """,
    )
    parser.add_argument("--task", required=True, help="Task description")
    parser.add_argument("--agent", default="claude-direct", help="Agent name for tracking")
    parser.add_argument("--model", default="gpt-5-nano", help="Model to use")
    parser.add_argument("--max-turns", type=int, default=30, help="Max conversation turns")
    parser.add_argument("--no-validate", action="store_true", help="Skip indexer validation")

    args = parser.parse_args()

    try:
        result = fix_kb_gap(
            task=args.task,
            agent_name=args.agent,
            model=args.model,
            max_turns=args.max_turns,
            validate=not args.no_validate,
        )

        if result["success"]:
            print("\n✓ SUCCESS")
            sys.exit(0)
        else:
            print(f"\n✗ FAILED: {result['message']}")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\n[INTERRUPTED]")
        sys.exit(130)
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
