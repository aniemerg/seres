"""
agent.py

Core agent logic for dependency usage analysis:
- Pydantic models for structured output
- Agent instructions
- Agent construction and execution
"""

from __future__ import annotations

import asyncio
import time
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple

from pydantic import BaseModel, Field
from agents import Agent, Runner, ItemHelpers
from agents.exceptions import MaxTurnsExceeded

from src.tools import rg_search, read_file_chunk
from src.output import (
    log_usage_record,
    save_report,
    format_tool_call_from_raw,
    format_tool_output_from_raw,
)
from src.history import AgentHistoryRecorder


# -----------------------------
# Pydantic models for output
# -----------------------------


class RepresentativeLocation(BaseModel):
    """Pointer to a code location (no raw code)."""

    file: str = Field(
        ..., description="File path, usually relative to the repo root."
    )
    line_spans: List[List[int]] = Field(
        ...,
        description=(
            "Inclusive line ranges [start_line, end_line] that illustrate usage. "
            "Each element must be a 2-element list like [10, 25]."
        ),
    )


class UsageRole(BaseModel):
    """
    A way in which the dependency provides value to the *project*.

    role_kind encodes the "scope" (runtime feature vs tests vs tooling, etc.)
    role_name & description describe the feature in project terms.
    how_dependency_is_used explains how the dep contributes to that feature.
    """

    role_kind: str = Field(
        ...,
        description=(
            "One of: runtime_feature | test_support | build_tooling | "
            "dev_experience | documentation | infra_support | other"
        ),
    )
    role_name: str = Field(
        ..., description="Short label for the feature/area, e.g. 'Keystore management'."
    )
    description: str = Field(
        ..., description="What this feature does in the project."
    )
    how_dependency_is_used: str = Field(
        ..., description="How the dependency contributes to this role/feature."
    )
    representative_locations: List[RepresentativeLocation] = Field(
        default_factory=list,
        description="Pointers to code locations that exemplify this usage.",
    )


class DependencyUsageReport(BaseModel):
    """
    Structured result describing how a dependency is used in a repo.

    This is what the agent returns as the final output.
    """

    repo: str = Field(
        ...,
        description=(
            "Repository identifier, e.g. 'github.com/ethereum/go-ethereum'. "
            "This is for human / downstream reference."
        ),
    )
    dependency: str = Field(
        ..., description="Dependency identifier (module path, package name, etc.)."
    )

    inclusion_type: str = Field(
        ...,
        description=(
            "How this dependency is included: "
            "'direct' | 'transitive' | 'unknown'. "
            "Use 'transitive' if evidence suggests it's only a child of another dep "
            "(e.g., only appears as // indirect in go.mod, or purely as a subdep)."
        ),
    )

    usage_class: str = Field(
        ...,
        description=(
            "One of: "
            "SinglePoint | Utility | FeatureFocused | Pervasive | Unused. "
            "SinglePoint: used once / very narrowly. "
            "Utility: used at many points for a specific, well-defined purpose "
            "(logging helper, UUID generator, etc.). "
            "FeatureFocused: used primarily in one identifiable feature/subsystem. "
            "Pervasive: used across major subsystems so its value can be inferred "
            "from the dependency's own purpose. "
            "Unused: no meaningful usage found in source code."
        ),
    )

    usage_roles: List[UsageRole] = Field(
        default_factory=list,
        description=(
            "List of roles the dependency plays in the project: runtime features, "
            "test helpers, build tooling, etc."
        ),
    )

    notes: Optional[List[str]] = Field(
        default=None,
        description="Optional free-form observations (short bullet items).",
    )

    # Responsibilities fields (for step-share reasoning)
    responsibilities_provided_by_dependency: List[str] = Field(
        default_factory=list,
        description=(
            "Short bullet points describing concrete responsibilities handled "
            "by this dependency for the project-level capabilities it supports. "
            "E.g., 'Implements 256-bit arithmetic (add, sub, mul, div) used by "
            "the EVM for gas and balance calculations.'"
        ),
    )

    responsibilities_left_to_parent: List[str] = Field(
        default_factory=list,
        description=(
            "Short bullet points describing key responsibilities that remain in "
            "the parent repo's code around this dependency. "
            "E.g., 'Implements EVM opcode semantics and decides when to invoke "
            "uint256 operations.'"
        ),
    )

    # Scope flags (runtime vs tests vs build/docs)
    appears_in_runtime_code: bool = Field(
        default=False,
        description=(
            "True if the dependency appears in code paths that are part of the "
            "normal runtime behavior of the project (non-test, non-build, "
            "non-doc tooling)."
        ),
    )

    appears_in_test_code: bool = Field(
        default=False,
        description=(
            "True if the dependency appears in test files / test-only code "
            "paths (e.g., *_test.go, test directories)."
        ),
    )

    appears_in_build_or_docs: bool = Field(
        default=False,
        description=(
            "True if the dependency appears in build scripts, CI, documentation "
            "tooling, or other non-runtime, non-test code paths."
        ),
    )


# -----------------------------
# Agent prompt
# -----------------------------

AGENT_INSTRUCTIONS = """
You are a *dependency usage mapper* for software repositories.

Your task for each run:
1. Use the tools provided to discover where and how a given dependency appears in a repo.
2. Classify the type of usage.
3. Describe the roles the dependency plays in the project, in terms of project-level features and tooling.
4. Return a single JSON object of type DependencyUsageReport as your final output.

You care about **value to the project**, not directly about end users.

--------------------------------
Key concepts
--------------------------------

- A *dependency* here means an external library/module/package that the project relies on.
  This can include:
  - runtime libraries
  - test frameworks
  - build/CI tooling
  - documentation tooling
  - linting/formatting tools
  - vendored code (copied into the repo under vendor/ or similar)

- We include direct dependencies that provide value:
  - A test framework (pytest, jest, etc.) is a real dependency: it enables testing.
  - Linting/formatting tools, build tools, doc generators, etc. all provide value to the project.
  - Vendored code itself is a valid dependency of the project.

- We do *not* want to treat transitive dependencies as separate, billable dependencies:
  - A transitive dependency is a dependency of another dependency.
  - E.g. packages marked `// indirect` in go.mod or only appearing in lock files.
  - The value of a transitive dependency is bundled under the parent dependency that imports it.

If you determine that a dependency is only transitive, you should:
  - Set `inclusion_type` to "transitive".
  - Set `usage_class` to "Unused" OR a best-effort class.
  - Add a short note explaining the evidence (e.g. "`// indirect` in go.mod, no imports in source files").
  - Continue to verify by searching for alternative name patterns before concluding.

--------------------------------
Usage roles and features
--------------------------------

You should think in terms of *project-level features* and *usage roles*:

- A *project-level feature* is an identifiable piece of functionality of the repo:
  - e.g. "keystore keyfile management", "JSON-RPC server", "EVM execution engine", "CLI tools".

- A *usage role* is how the dependency provides value to the project. Each role has:
  - role_kind:
    - runtime_feature: core runtime behavior or subsystems.
    - test_support: test harnesses, fixtures, generators, etc.
    - build_tooling: build, packaging, deployment, CI/CD.
    - dev_experience: linters, formatters, dev-only helpers.
    - documentation: doc generation, site building.
    - infra_support: logging, metrics, tracing, monitoring.
    - other: anything that doesn't fit neatly above.
  - role_name: concise label, e.g. "Keystore management", "JSON-RPC server".
  - description: what this feature does in the project.
  - how_dependency_is_used: how the dependency supports or enables that feature.

The goal is to let another model later answer:
  "For dependency X, what value does it provide to project Y?"

--------------------------------
Usage classes
--------------------------------

For each dependency, choose exactly one `usage_class`:

- SinglePoint
  - Used once or in a very narrow part of the code for a specific purpose.

- Utility
  - Appears at various points but for a single, well-defined service.
    Examples: UUID generator, logging helper, argument parser, date/time utility.

- FeatureFocused
  - Mainly used within one feature or subsystem:
    e.g. only in keystore, only in EVM, only in the RPC server, only in the CLI.

- Pervasive
  - Used across multiple core subsystems.
  - After inspecting representative samples, you can infer its value from the dependency's purpose itself.
  - Example: numeric libraries like uint256 used all across EVM execution and state handling,
    or logging libraries used throughout the code.

- Unused
  - No meaningful usage found in source code.
  - The dependency might appear only in manifests/lockfiles as a transitive or unused entry.

Also classify `inclusion_type`:

- direct
  - The repo clearly imports or configures this dependency directly (source imports, direct config).
- transitive
  - Evidence strongly suggests this is only used as a child of another dependency:
    - e.g. appears only in go.mod as `// indirect`.
    - appears only in lockfiles or generated dependency graphs.
    - appears only as part of configuration that obviously belongs to another library (e.g. Jekyll config
      when the project's declared dependency is `github-pages`).
- unknown
  - You cannot confidently tell.

If you decide `inclusion_type` is "transitive", still verify by trying alternative search patterns.

--------------------------------
Responsibilities (for step-share reasoning)
--------------------------------

For each dependency, you must produce two short lists of responsibilities:

- `responsibilities_provided_by_dependency`
  Short bullet points describing what this dependency actually does for the project.
  Focus on *concrete responsibilities* that appear in the code you inspected.
  Examples:
  - "Provides 256-bit unsigned integer type and arithmetic operations used by the EVM and state code."
  - "Generates random UUIDs used as Key.Id identifiers for keystore keys."

- `responsibilities_left_to_parent`
  Short bullet points describing important responsibilities that are clearly handled by
  the parent repo's own code around this dependency.
  Examples:
  - "Implements EVM opcode semantics and decides when arithmetic operations are invoked."
  - "Implements keystore keyfile encryption/decryption and JSON encoding; UUIDs are only used to assign and parse IDs."

These lists help downstream models reason about how much of a capability is handled by the
dependency versus the parent. Keep bullets concise, factual, and grounded in the code you
saw via the tools.

--------------------------------
Scope flags (runtime vs tests vs build/docs)
--------------------------------

You must also set three boolean flags on the report:

- `appears_in_runtime_code`
  - Set to true if the dependency appears in normal runtime code paths (e.g. under `core/`,
    `pkg/`, `src/`, main application modules).
  - This includes features like EVM execution, networking, state management, RPC servers,
    keystores, etc.

- `appears_in_test_code`
  - Set to true if the dependency appears in test code.
  - For example, files like `*_test.go`, files under `test/` directories, or obvious test modules.

- `appears_in_build_or_docs`
  - Set to true if the dependency appears in build/CI scripts, documentation tooling, or similar.
  - For example, code in `cmd/` that builds docs, scripts for packaging or deployment, or
    doc-site generators.

You can infer these flags from file paths and naming conventions. It is okay to set more than
one flag to true (e.g., a dependency used in both runtime and test code).

--------------------------------
Tools
--------------------------------

You have two tools:

1. rg_search(pattern, root, max_matches=200, include_hidden=False)

   - Use this to search the repo for occurrences of the dependency identifier.
   - Typical patterns:
     - The full import path (e.g. "github.com/google/uuid" or "github.com/holiman/uint256").
     - A canonical module name or symbol name when needed.
   - Parameters:
     - pattern: the text or regex to search for
     - root: the repo root path
     - max_matches: cap on results (default 200)
     - include_hidden: set to True to also search hidden files/directories (those starting with '.')
       Use this for config files, git hooks (.husky/, .github/), dotfiles, etc.
   - The tool returns:
     - pattern: str
     - root: str
     - total_matches_seen: int
     - hit_max_count: bool (True if rg likely stopped at max_matches)
     - matches: list of {
         "file": relative file path,
         "line": line number (int),
         "matched_text": full line where pattern matched
       }

   Guidance:
   - Always start with an rg_search on the dependency import path or canonical name.
   - Use the distribution of matches across `file` paths to infer *breadth* across directories.
   - If `hit_max_count` is true and `matches` span many directories, treat the dependency as
     potentially *pervasive* and do not try to see every match.
   - If the results seem skewed to a single directory, you may run additional rg_search calls
     restricted to other directories or with slightly different patterns.
   - For build tools, git hooks, or config-based dependencies, use include_hidden=True to
     search .husky/, .github/, and other dotfile directories.

2. read_file_chunk(path, root, start_line, end_line, max_lines=200)

   - Use this to read 20–80 lines around specific locations you care about.
   - Use only for a *small number* of representative files per dependency.
   - Example usage:
     - After seeing a match in "accounts/keystore/key.go:123", call read_file_chunk
       to see how the dependency is used in that region.

Do NOT try to read entire files or the entire repo. Sample representative locations only.

--------------------------------
Approach (step-by-step)
--------------------------------

1. Identify the dependency and repo
   - The user input will specify a repo identifier and a dependency string.
   - You may also see a filesystem root path to use with the tools.

2. Discover occurrences with MULTIPLE search patterns
   - Start with an rg_search on the full dependency path (e.g. "github.com/google/uuid").
   - IMPORTANT: If the first search only finds manifest files (go.mod, Cargo.toml, package.json),
     you MUST try alternative search patterns before concluding Unused:

     For Rust crates (github.com/serde-rs/serde):
       - Search for the crate name: "serde" or "use serde"
       - Search for derive macros: "#[derive(Serialize" or "serde::"

     For Python packages (github.com/pytest-dev/pytest):
       - Search for the package name: "import pytest" or "from pytest"

     For JavaScript/npm packages (github.com/ai/nanoid):
       - Search for the npm name: "require('nanoid')" or "from 'nanoid'"
       - Search for just the package name: "nanoid"

     For Go packages:
       - The import path usually matches, but try shorter forms if needed

     For build tools (husky, prettier, eslint):
       - Use include_hidden=True to search .husky/, .github/, config files
       - Search for the tool name in scripts and configs

   - Inspect:
     - matches[*].file to see which directories and subsystems are hit.
     - total_matches_seen and hit_max_count to reason about pervasiveness.

3. Check for transitive indicators
   - Look for evidence like `// indirect` in go.mod, or only appearing in lockfiles.
   - BUT still verify with alternative search patterns before marking as transitive+Unused.
   - A dependency is truly transitive only if NO source code imports it under any name pattern.

4. Identify candidate features / roles
   - Group matches conceptually by path prefixes (e.g. "core/vm", "core/state", "accounts/keystore",
     "cmd/...", "tests/...").
   - For each cluster of interest, choose a small number of representative files and lines.

5. Read representative chunks
   - For each representative location, call read_file_chunk to understand how the dependency is used
     in that context (e.g. generating UUIDs, doing 256-bit arithmetic, logging, building RPC routes).

6. Infer usage roles and usage_class
   - Define 1–3 usage_roles that best capture how the dependency provides value to the project:
     - runtime features
     - test support
     - build tooling, etc.
   - Decide usage_class:
     - SinglePoint, Utility, FeatureFocused, Pervasive, or Unused
       based on how broadly the dependency appears and how it is used.

7. Return a DependencyUsageReport JSON object
   - Do NOT include raw code in the JSON.
   - For representative_locations, provide file + line_spans only.
   - Keep text concise but specific.

--------------------------------
Output format (very important)
--------------------------------

Your final response must be a single JSON object matching the `DependencyUsageReport` schema:

- repo: string
- dependency: string
- inclusion_type: "direct" | "transitive" | "unknown"
- usage_class: "SinglePoint" | "Utility" | "FeatureFocused" | "Pervasive" | "Unused"
- usage_roles: array of:
  - role_kind: "runtime_feature" | "test_support" | "build_tooling"
               | "dev_experience" | "documentation" | "infra_support" | "other"
  - role_name: string
  - description: string
  - how_dependency_is_used: string
  - representative_locations: array of:
    - file: string
    - line_spans: array of [start_line, end_line] integer pairs
- notes: optional array of short strings
- responsibilities_provided_by_dependency: array of strings
- responsibilities_left_to_parent: array of strings
- appears_in_runtime_code: boolean
- appears_in_test_code: boolean
- appears_in_build_or_docs: boolean

**Important:**
Do NOT try to estimate failure severity labels, replaceability tiers, development cost,
or capability percentages. Your job is to:
- Find where the dependency is used,
- Describe the project-level features and roles it supports,
- Explain what responsibilities it handles vs the parent's code,
- Indicate whether it appears in runtime, tests, and/or build/doc tooling.

Higher-level value judgments are done later by another model that reads your report.

Do NOT include any raw code in the JSON. Only references to file paths and line ranges.

Think carefully, use the tools, then output exactly one JSON object of this shape as your final answer.
"""


# -----------------------------
# Agent construction + API
# -----------------------------


def build_dependency_usage_agent(model: str = "gpt-5-nano") -> Agent:
    """
    Construct the dependency-usage agent.

    You can reuse this agent across many (repo, dependency) calls.
    """
    agent = Agent(
        name="DependencyUsageAgent",
        instructions=AGENT_INSTRUCTIONS,
        tools=[rg_search, read_file_chunk],
        output_type=DependencyUsageReport,
        model=model,  # see https://platform.openai.com/docs/models for options
    )
    return agent


async def _run_agent_streamed(
    agent: Agent,
    user_input: str,
    max_turns: int = 30,
    quiet: bool = False,
    activity_callback: Optional[callable] = None,
    history_recorder: Optional[AgentHistoryRecorder] = None,
):
    """
    Run the agent with streaming, optionally printing tool calls and outputs in real-time.

    Args:
        agent: The agent to run
        user_input: The input prompt
        max_turns: Maximum turns before stopping
        quiet: If True, suppress all output
        activity_callback: Optional callback for activity updates (for batch progress display)
                          Called with (dependency, message) on each tool call
        history_recorder: Optional recorder for capturing agent execution history

    Returns the final RunResultStreaming object after streaming completes.
    """
    import json

    result = Runner.run_streamed(agent, user_input, max_turns=max_turns)

    # Track last tool call name for associating with output
    last_tool_name = None

    async for event in result.stream_events():
        # Handle run item events (tool calls, outputs, messages)
        if event.type == "run_item_stream_event":
            item = event.item

            if item.type == "tool_call_item":
                # Tool is being called
                raw = item.raw_item
                name = getattr(raw, "name", "unknown")
                args_str = getattr(raw, "arguments", "{}")
                call_str = format_tool_call_from_raw(name, args_str)

                if not quiet:
                    print(f"● {call_str}", flush=True)

                # Notify activity callback if provided
                if activity_callback:
                    activity_callback(call_str)

                # Record to history
                if history_recorder:
                    try:
                        args = json.loads(args_str) if args_str else {}
                    except json.JSONDecodeError:
                        args = {"raw": args_str}
                    history_recorder.record_tool_call(name, args)
                    last_tool_name = name

            elif item.type == "tool_call_output_item":
                # Tool returned results
                output_str = format_tool_output_from_raw(item.output)

                if not quiet:
                    print(f"  ⎿  {output_str}", flush=True)

                # Record to history
                if history_recorder:
                    history_recorder.record_tool_output(
                        last_tool_name or "unknown",
                        item.output,
                        summary=output_str,
                    )

            elif item.type == "message_output_item":
                # Agent generated a message
                text = ItemHelpers.text_message_output(item)

                if not quiet and text:
                    text_display = text.strip()
                    if len(text_display) > 500:
                        text_display = text_display[:500] + "..."
                    print(f"\n● Agent:", flush=True)
                    for line in text_display.split("\n")[:10]:
                        print(f"  {line}", flush=True)
                    if text_display.count("\n") > 10:
                        print(f"  ... ({text_display.count(chr(10)) - 10} more lines)", flush=True)

                # Record to history
                if history_recorder and text:
                    history_recorder.record_message(text.strip())

            elif item.type == "reasoning_item":
                if not quiet:
                    print(f"  (reasoning)", flush=True)

                # Record to history (content might not be available)
                if history_recorder:
                    reasoning_text = getattr(item, "text", None) or "(reasoning)"
                    history_recorder.record_reasoning(reasoning_text)

    return result


def analyze_dependency(
    repo_root: str,
    repo_id: str,
    dependency: str,
    model: str = "gpt-5-nano",
    quiet: bool = False,
    activity_callback: Optional[callable] = None,
) -> Tuple[Optional[DependencyUsageReport], Optional[Path]]:
    """
    High-level entry point: run the agent once for a single (repo, dependency).

    Also:
      - measures wall-clock duration
      - computes token usage and cost
      - appends a JSON record to usage_log.jsonl
      - saves the report to output/reports/{org_repo}/{dependency}-{date}.json

    Args:
      repo_root: Path to the repo root on disk
      repo_id: Human-readable repo identifier (e.g. "github.com/ethereum/go-ethereum")
      dependency: Dependency identifier (import path, package name, etc.)
      model: OpenAI model name to use
      quiet: If True, suppress all output (for batch processing)
      activity_callback: Optional callback for activity updates (for batch progress display)

    Returns:
      Tuple of (DependencyUsageReport, Path) on success.
      (None, None) if MaxTurnsExceeded or other failure.
      Usage/cost info is logged regardless of success or failure.
    """
    agent = build_dependency_usage_agent(model=model)

    root_resolved = Path(repo_root).expanduser().resolve()

    user_input = (
        f"Repository identifier: {repo_id}\n"
        f"Filesystem repo root: {root_resolved}\n"
        f"Dependency to analyze: {dependency}\n\n"
        "Use rg_search and read_file_chunk to understand how this dependency is used "
        "and then return a DependencyUsageReport JSON object."
    )

    # Create history recorder for audit trail
    history_recorder = AgentHistoryRecorder(repo_id, dependency)
    history_recorder.record_start(model=model, repo_root=str(root_resolved))

    t0 = time.time()
    result = None
    report: Optional[DependencyUsageReport] = None
    error_message: Optional[str] = None

    try:
        # Use streaming to show tool calls in real-time
        result = asyncio.run(_run_agent_streamed(
            agent, user_input, max_turns=30,
            quiet=quiet, activity_callback=activity_callback,
            history_recorder=history_recorder,
        ))
        report = result.final_output  # type: ignore[assignment]
    except MaxTurnsExceeded as e:
        error_message = f"MaxTurnsExceeded: {e}"
        if not quiet:
            print(f"\n[ERROR] {error_message}")
    except Exception as e:
        error_message = f"{type(e).__name__}: {e}"
        if not quiet:
            print(f"\n[ERROR] {error_message}")

    t1 = time.time()

    # Extract real token usage from the SDK
    input_tokens = 0
    output_tokens = 0
    reasoning_tokens = 0
    cached_tokens = 0
    total_tokens = 0
    num_requests = 0

    if result is not None and hasattr(result, "context_wrapper"):
        usage = result.context_wrapper.usage
        input_tokens = usage.input_tokens
        output_tokens = usage.output_tokens
        total_tokens = usage.total_tokens
        num_requests = usage.requests

        # Extract detailed breakdowns if available
        if hasattr(usage, "input_tokens_details") and usage.input_tokens_details:
            cached_tokens = getattr(usage.input_tokens_details, "cached_tokens", 0) or 0
        if hasattr(usage, "output_tokens_details") and usage.output_tokens_details:
            reasoning_tokens = getattr(usage.output_tokens_details, "reasoning_tokens", 0) or 0

    # GPT-5-nano pricing (current, subject to change):
    #   input:  $0.10 / 1M tokens
    #   output: $0.40 / 1M tokens
    # Note: cached input tokens are typically 50% off, reasoning tokens same as output
    input_cost_usd = input_tokens / 1_000_000 * 0.10
    output_cost_usd = output_tokens / 1_000_000 * 0.40
    total_cost_usd = input_cost_usd + output_cost_usd

    # Compute report size for reference
    report_json = report.model_dump_json() if report else None
    report_size_chars = len(report_json) if report_json else 0

    usage_record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "model": model,
        "repo_id": repo_id,
        "dependency": dependency,
        "repo_root": str(root_resolved),
        "run_duration_seconds": round(t1 - t0, 3),
        "report_size_chars": report_size_chars,
        # Real token usage from SDK
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "reasoning_tokens": reasoning_tokens,
        "cached_tokens": cached_tokens,
        "total_tokens": total_tokens,
        "num_requests": num_requests,
        # Cost breakdown
        "input_cost_usd": input_cost_usd,
        "output_cost_usd": output_cost_usd,
        "total_cost_usd": total_cost_usd,
        # Status
        "success": report is not None,
        "error": error_message,
    }

    # Save report to file if successful
    saved_path: Optional[Path] = None
    if report is not None:
        saved_path = save_report(report, repo_id, dependency)
        usage_record["saved_path"] = str(saved_path) if saved_path else None

    log_usage_record(usage_record)

    # Record end and save history
    history_recorder.record_end(
        success=report is not None,
        usage_class=report.usage_class if report else None,
        inclusion_type=report.inclusion_type if report else None,
        duration_seconds=t1 - t0,
        error=error_message,
    )
    history_path = history_recorder.save()
    if history_path and not quiet:
        print(f"# History: {history_path}")

    # Print usage summary (unless quiet mode)
    if not quiet:
        print(
            f"\n# Usage: model={model}, "
            f"duration={usage_record['run_duration_seconds']}s, "
            f"requests={num_requests}"
        )
        print(
            f"# Tokens: input={input_tokens}, output={output_tokens}, "
            f"reasoning={reasoning_tokens}, total={total_tokens}"
        )
        print(
            f"# Cost: input=${input_cost_usd:.6f}, output=${output_cost_usd:.6f}, "
            f"total=${total_cost_usd:.6f}"
        )
        if saved_path:
            print(f"# Saved: {saved_path}")
        if error_message:
            print(f"# Error: {error_message}")

    return report, saved_path
