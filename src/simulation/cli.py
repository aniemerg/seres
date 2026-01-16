"""
Simulation CLI - Command-line interface for simulation operations.

Provides commands for managing and running simulations:
- init: Create new simulation
- import: Import items from Earth
- start-process: Start a process
- run-recipe: Run a recipe
- build-machine: Build a machine
- advance-time: Advance simulation time
- preview: Preview next step
- view-state: View current state
- list: List all simulations

Each command loads simulation, executes action, saves state, and reports results.
"""
import argparse
import json
import sys
import shutil
from pathlib import Path
from typing import Optional, Dict, Any, Iterable

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

from src.kb_core.kb_loader import KBLoader
from src.kb_core.calculations import calculate_duration, calculate_energy, CalculationError
from src.kb_core.unit_converter import UnitConverter
from src.kb_core.schema import Quantity
from src.kb_core.override_resolver import resolve_recipe_step_with_kb
from src.simulation.engine import SimulationEngine

REPO_ROOT = Path(__file__).parent.parent.parent
KB_ROOT = REPO_ROOT / "kb"
SIMULATIONS_DIR = REPO_ROOT / "simulations"


# ============================================================================
# Terminal output helpers
# ============================================================================

_COLOR_RESET = "\033[0m"
_COLOR_DIM = "\033[38;2;68;68;68m"
_COLOR_INFO = "\033[38;2;0;141;248m"
_COLOR_SUCCESS = "\033[38;2;140;225;11m"
_COLOR_WARN = "\033[38;2;255;185;0m"
_COLOR_ERROR = "\033[38;2;255;0;15m"
_COLOR_NOTE = "\033[38;2;0;216;235m"
_COLOR_TIME = "\033[38;2;0;146;255m"
_COLOR_ENERGY = "\033[38;2;255;210;66m"
_COLOR_MASS = "\033[38;2;171;225;91m"
_COLOR_ACCENT_A = "\033[38;2;255;120;70m"
_COLOR_ACCENT_B = "\033[38;2;120;255;210m"
_COLOR_ACCENT_C = "\033[38;2;190;190;255m"
_COLOR_BASE = "\033[38;2;255;0;153m"

_RUNBOOK_OUTPUT_MODE = "raw"
_SUPPRESSING_PROCESS_BLOCK = False
_SUPPRESSING_STATUS_BLOCK = False
_LAST_ADVANCE_RESULT: Optional[dict[str, Any]] = None
_DISPLAY_WIDTH = 120
_ART_DELIM = "<<<ART>>>"

_ASCII_ARTS = [
    [
        "   _.._",
        " .' .-'",
        "/  /",
        "|  |",
        "\\  \\_",
        " '.__.'",
    ],
    [
        "  _.._",
        " /__\\",
        " |  |",
        " \\__/",
    ],
    [
        "  [=]",
        " .-.-.",
        "( o o )",
        " | ^ |",
        " '---'",
        " /| |\\",
    ],
    [
        "  /\\",
        " /__\\",
        " \\  /",
        "  \\/",
    ],
    [
        "  .-.",
        " (o o)",
        " | O |",
        " |   |",
        " '~~~'",
        " /|||\\",
    ],
]


def _emit_story_footer() -> None:
    left = "-⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎽__⎽-⎻⎺⎺⎻-⎽__⎽---⎽_"
    right = "_⎽---"
    base_top = "╭─────╮"
    base_mid = "│ ▣ ▣ │"
    base_bot = "╰─┬───╯"
    line1 = _color(left, _COLOR_DIM) + _color(base_top, _COLOR_BASE) + _color(right, _COLOR_DIM)
    line2 = _color(left, _COLOR_DIM) + _color(base_mid, _COLOR_BASE) + _color(right, _COLOR_DIM)
    line3 = _color(left, _COLOR_DIM) + _color(base_bot, _COLOR_BASE) + _color(right, _COLOR_DIM)
    _emit(line1)
    _emit(line2)
    _emit(line3)


def _color(text: str, color_code: str) -> str:
    if not sys.stdout.isatty():
        return text
    return f"{color_code}{text}{_COLOR_RESET}"


def _should_suppress(message: str) -> bool:
    global _SUPPRESSING_PROCESS_BLOCK
    global _SUPPRESSING_STATUS_BLOCK
    if _RUNBOOK_OUTPUT_MODE != "story":
        return False
    raw_message = _strip_ansi(message)
    stripped = raw_message.lstrip()
    if stripped.startswith("↷ Skipped import"):
        return True
    if stripped.startswith("=== Simulation:"):
        _SUPPRESSING_STATUS_BLOCK = True
        return True
    if _SUPPRESSING_STATUS_BLOCK:
        if stripped.startswith("Events:"):
            _SUPPRESSING_STATUS_BLOCK = False
        return True
    if stripped == "Completed processes:":
        _SUPPRESSING_PROCESS_BLOCK = True
        return True
    if _SUPPRESSING_PROCESS_BLOCK:
        if stripped.startswith("-") or stripped.startswith("→") or raw_message.startswith("  -") or raw_message.startswith("      →") or raw_message.startswith("    "):
            return True
        _SUPPRESSING_PROCESS_BLOCK = False
    suppressed_prefixes = (
        "✓ Started recipe",
        "  Steps:",
        "Steps:",
        "  Duration:",
        "Duration:",
        "  Ends at:",
        "Ends at:",
        "✓ Advanced time by",
        "  New time:",
        "New time:",
        "  Processes completed:",
        "Processes completed:",
        "  Total energy consumed:",
        "Total energy consumed:",
        "✓ Imported",
    )
    return stripped.startswith(suppressed_prefixes)


def _emit(message: str, color_code: Optional[str] = None, is_error: bool = False) -> None:
    if _should_suppress(message):
        return
    if color_code:
        message = _color(message, color_code)
    print(message, file=sys.stderr if is_error else sys.stdout, flush=True)


def _emit_kv(label: str, value: str, color_code: Optional[str] = None, is_error: bool = False) -> None:
    if color_code:
        label = _color(label, color_code)
    _emit(f"{label} {value}", is_error=is_error)


def load_or_create_simulation(sim_id: str, kb_loader: KBLoader, create: bool = False) -> SimulationEngine:
    """
    Load existing simulation or create new one.

    Args:
        sim_id: Simulation ID
        kb_loader: KB loader instance
        create: If True, create new simulation (fail if exists)
               If False, load existing (fail if doesn't exist)

    Returns:
        SimulationEngine instance
    """
    sim_dir = SIMULATIONS_DIR / sim_id
    snapshot_file = sim_dir / "snapshot.json"
    exists = snapshot_file.exists()

    if create and exists:
        _emit(f"Error: Simulation '{sim_id}' already exists", _COLOR_ERROR, is_error=True)
        sys.exit(1)

    if not create and not exists:
        _emit(f"Error: Simulation '{sim_id}' not found", _COLOR_ERROR, is_error=True)
        sys.exit(1)

    # Create engine
    engine = SimulationEngine(sim_id, kb_loader, sim_dir)

    # Load existing state if not creating
    if not create:
        success = engine.load()
        if not success:
            _emit(f"Error: Failed to load simulation '{sim_id}'", _COLOR_ERROR, is_error=True)
            sys.exit(1)

    return engine


# ============================================================================
# Runbook helpers
# ============================================================================

def _parse_runbook_blocks(md_text: str) -> list[tuple[list[str], str]]:
    blocks: list[tuple[list[str], str]] = []
    in_block = False
    current: list[str] = []
    heading_path: list[str] = []
    block_heading: list[str] = []

    for line in md_text.splitlines():
        stripped = line.strip()
        if not in_block and stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            title = stripped[level:].strip()
            heading_path = heading_path[: max(level - 1, 0)]
            if title:
                heading_path.append(title)
        if stripped.startswith("```") and stripped[3:].strip() == "sim-runbook":
            in_block = True
            current = []
            block_heading = heading_path.copy()
            continue
        if stripped.startswith("```") and in_block:
            blocks.append((block_heading, "\n".join(current)))
            in_block = False
            current = []
            continue
        if in_block:
            current.append(line)

    return blocks


def _parse_markdown_story_context(md_text: str) -> dict[str, Any]:
    context: dict[tuple[str, ...], dict[str, Any]] = {}
    in_block = False
    in_admonition = False
    heading_path: list[str] = []
    intro_lines: list[str] = []
    lines = md_text.splitlines()
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        stripped = line.strip()
        if stripped.startswith("```") and not in_block:
            in_block = True
            idx += 1
            continue
        if stripped.startswith("```") and in_block:
            in_block = False
            idx += 1
            continue
        if not in_block and stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            title = stripped[level:].strip()
            heading_path = heading_path[: max(level - 1, 0)]
            if title:
                heading_path.append(title)
            idx += 1
            continue
        if not in_block and stripped.startswith("Goal:") and len(intro_lines) < 2:
            intro_lines.append(stripped)
        if not in_block and not heading_path and stripped and not stripped.startswith("Goal:"):
            if len(intro_lines) < 2:
                intro_lines.append(stripped)
        if in_block:
            idx += 1
            continue
        heading_key = tuple(heading_path)
        entry = context.setdefault(
            heading_key, {"admonitions": [], "tasks_done": 0, "tasks_total": 0, "story_lines": []}
        )
        if stripped.startswith("!!!"):
            parts = stripped.split(maxsplit=2)
            kind = parts[1] if len(parts) > 1 else "note"
            title = ""
            if len(parts) > 2:
                title = parts[2].strip().strip('"')
            body_lines: list[str] = []
            idx += 1
            in_admonition = True
            while idx < len(lines):
                next_line = lines[idx]
                if next_line.startswith("    ") or next_line.startswith("\t"):
                    body_lines.append(next_line.strip())
                    idx += 1
                    continue
                break
            in_admonition = False
            entry["admonitions"].append(
                {"kind": kind, "title": title, "body": " ".join(body_lines).strip()}
            )
            continue
        if stripped.startswith("- [") and len(stripped) >= 5:
            marker = stripped[3]
            entry["tasks_total"] += 1
            if marker.lower() == "x":
                entry["tasks_done"] += 1
        if not in_admonition and stripped and not stripped.startswith("-"):
            if stripped.startswith("```") or stripped.startswith("Goal:"):
                idx += 1
                continue
            if not stripped.startswith("Commentary:"):
                line_text = stripped
            else:
                line_text = stripped.split("Commentary:", 1)[1].strip()
            if line_text and len(entry["story_lines"]) < 2:
                entry["story_lines"].append(line_text)
        idx += 1
    return {"sections": context, "intro_lines": intro_lines}


def _load_runbook_commands(path: Path) -> list[dict]:
    if yaml is None:
        raise RuntimeError("PyYAML is required to run sim runbooks")

    md_text = path.read_text(encoding="utf-8")
    blocks = _parse_runbook_blocks(md_text)
    commands: list[dict] = []

    for heading, block in blocks:
        data = yaml.safe_load(block)
        if data is None:
            continue
        if isinstance(data, dict):
            data["_md_heading"] = heading
            commands.append(data)
            continue
        if isinstance(data, list):
            for entry in data:
                if isinstance(entry, dict):
                    entry["_md_heading"] = heading
                    commands.append(entry)
            continue
        raise RuntimeError(f"Invalid runbook block in {path}")

    return commands


def _normalize_arg_key(key: str) -> str:
    return key.replace("-", "_")


def _get_arg(args: dict, *names: str) -> Optional[Any]:
    for name in names:
        if name in args:
            return args[name]
    return None


def _reset_simulation(sim_id: str, kb_loader: KBLoader) -> int:
    sim_dir = SIMULATIONS_DIR / sim_id
    if sim_dir.exists():
        shutil.rmtree(sim_dir)
    return cmd_init(argparse.Namespace(sim_id=sim_id), kb_loader)


def _get_import_mass_kgs(engine: SimulationEngine, kb_loader: KBLoader) -> tuple[float, int]:
    total_mass = 0.0
    unknown_mass_count = 0
    for item_id, inv in engine.state.total_imports.items():
        if inv.unit == "kg":
            total_mass += inv.quantity
            continue
        if inv.unit == "unit":
            item = kb_loader.get_item(item_id)
            if item:
                item_dict = item.model_dump() if hasattr(item, "model_dump") else item
                item_mass = item_dict.get("mass")
                if item_mass is not None:
                    total_mass += item_mass * inv.quantity
                else:
                    unknown_mass_count += 1
            else:
                unknown_mass_count += 1
            continue
        unknown_mass_count += 1
    return total_mass, unknown_mass_count


def _emit_story_heading(heading: list[str], metrics: Optional[dict[str, float]]) -> None:
    if not heading:
        return
    title = " / ".join(heading)
    _emit(f"◈ {title}", _COLOR_INFO)
    if not metrics:
        return
    time_hours = metrics.get("time_hours", 0.0)
    energy_kwh = metrics.get("energy_kwh", 0.0)
    import_mass = metrics.get("import_mass", 0.0)
    if time_hours <= 0 and energy_kwh <= 0 and import_mass <= 0:
        return
    time_days = time_hours / 24.0
    _emit(
        f"  ⏱ {time_days:.1f}d  ⚡ {energy_kwh:.1f} kWh  ⇣ ~{import_mass:.1f} kg",
        _COLOR_NOTE,
    )


def _strip_ansi(text: str) -> str:
    if "\033[" not in text:
        return text
    parts: list[str] = []
    i = 0
    while i < len(text):
        if text[i] == "\033":
            end = text.find("m", i)
            if end == -1:
                break
            i = end + 1
            continue
        parts.append(text[i])
        i += 1
    return "".join(parts)


def _render_blocks(value: float, step: float = 1000.0, max_blocks: int = 10) -> str:
    if value <= 0:
        return "░" * max_blocks
    blocks = min(max_blocks, max(1, int(value / step)))
    return ("█" * blocks).ljust(max_blocks, "░")


def _render_table(headers: list[str], rows: list[list[str]]) -> list[str]:
    widths = [len(h) for h in headers]
    for row in rows:
        for idx, cell in enumerate(row):
            widths[idx] = max(widths[idx], len(cell))
    top = "┌" + "┬".join("─" * (w + 2) for w in widths) + "┐"
    mid = "├" + "┼".join("─" * (w + 2) for w in widths) + "┤"
    bot = "└" + "┴".join("─" * (w + 2) for w in widths) + "┘"
    lines = [top]
    header_cells = [" " + headers[i].ljust(widths[i]) + " " for i in range(len(headers))]
    lines.append("│" + "│".join(header_cells) + "│")
    lines.append(mid)
    for row in rows:
        cells = [" " + row[i].ljust(widths[i]) + " " for i in range(len(headers))]
        lines.append("│" + "│".join(cells) + "│")
    lines.append(bot)
    return lines


def _select_ascii_art(key: str, height: int) -> list[str]:
    if height <= 0:
        return []
    candidates = [art for art in _ASCII_ARTS if len(art) <= height]
    if not candidates:
        candidates = _ASCII_ARTS[:]
    idx = sum(ord(ch) for ch in key) % len(candidates)
    art = candidates[idx]
    pad_total = height - len(art)
    pad_top = pad_total // 2
    pad_bottom = pad_total - pad_top
    blank = " " * len(art[0])
    return ([blank] * pad_top) + art + ([blank] * pad_bottom)


def _attach_ascii_art(lines: list[str], art: list[str], gap: int = 2, indent: int = 2) -> list[str]:
    if not art:
        return [(" " * indent) + line for line in lines]
    width = max(len(line) for line in lines)
    art_width = max(len(line) for line in art)
    display_width = _get_display_width()
    remaining = max(0, display_width - (width + indent))
    if remaining > art_width + gap:
        left_gap = max(gap, (remaining - art_width) // 2)
    else:
        left_gap = gap
    art_col = indent + width + left_gap
    out: list[str] = []
    for idx, line in enumerate(lines):
        art_line = art[idx] if idx < len(art) else ""
        base = (" " * indent) + line.ljust(width)
        if art_line:
            pad = max(0, art_col - len(base))
            out.append(base + (" " * pad) + _ART_DELIM + art_line)
        else:
            out.append(base)
    return out


def _center_lines(lines: list[str], width: int) -> list[str]:
    out: list[str] = []
    for line in lines:
        pad = max(0, (width - len(line)) // 2)
        out.append((" " * pad) + line)
    return out


def _format_imports_summary(imports: dict[str, dict[str, float]]) -> list[str]:
    lines: list[str] = []
    for item_id, entry in sorted(imports.items()):
        qty = entry["quantity"]
        unit = entry["unit"]
        lines.append(f"{item_id} {qty:.2f} {unit}")
    return lines


def _emit_story_phase_summary(phase: dict[str, Any], sim_id: Optional[str], kb_loader: KBLoader, heading: Optional[list[str]] = None) -> None:
    if not phase:
        return
    imports = phase.get("imports") or {}
    recipes = phase.get("recipes") or {}
    processes = phase.get("processes") or {}
    outputs = phase.get("outputs") or {}
    energy = phase.get("energy_delta", 0.0)
    time_hours = phase.get("time_delta", 0.0)
    import_mass = phase.get("import_mass_delta", 0.0)

    complexity_map: dict[str, int] = {}
    if sim_id:
        engine = load_or_create_simulation(sim_id, kb_loader)
        complexity_map = dict(engine.state.complexity_scores or {})

    if outputs:
        rows = []
        output_items = []
        for item_id, entry in outputs.items():
            complexity = complexity_map.get(item_id, 1)
            output_items.append((item_id, entry, complexity))
        output_items.sort(key=lambda row: (-row[2], row[0]))
        filtered = [row for row in output_items if row[2] >= 4]
        if not filtered:
            filtered = output_items[:1]
        hero = filtered[0]
        for item_id, entry, complexity in filtered[:8]:
            badge = f"C{complexity}"
            rows.append([item_id, f"+{entry['quantity']:.2f} {entry['unit']}", badge])
        table = _render_table(["Made", "Qty", "Cx"], rows[:8])
        art = _select_ascii_art("outputs", len(table))
        table = _attach_ascii_art(table, art, indent=2)
        if hero[2] >= 6:
            _emit("  Outputs (priority):", _COLOR_SUCCESS)
            _emit(f"  ★ CORE OUTPUT: {hero[0]} (C{hero[2]})", _COLOR_SUCCESS)
        else:
            _emit("  Outputs:", _COLOR_NOTE)
        header_lines = 3
        for idx, line in enumerate(table):
            if _ART_DELIM in line:
                left, art = line.split(_ART_DELIM, 1)
                colored_left = _color(left, _COLOR_SUCCESS if hero[2] >= 6 else _COLOR_NOTE)
                colored_art = _color(art, _COLOR_DIM)
                _emit(colored_left + colored_art)
                continue
            if idx < header_lines:
                _emit(f"{line}", _COLOR_SUCCESS if hero[2] >= 6 else _COLOR_NOTE)
                continue
            row_idx = idx - header_lines
            if row_idx >= len(filtered[:8]):
                _emit(f"{line}", _COLOR_SUCCESS if hero[2] >= 6 else _COLOR_NOTE)
                continue
            complexity = filtered[row_idx][2]
            if complexity >= 6:
                color = _COLOR_SUCCESS
            elif complexity >= 4:
                color = _COLOR_NOTE
            else:
                color = _COLOR_DIM
            _emit(f"{line}", color)
        if sim_id:
            engine = load_or_create_simulation(sim_id, kb_loader)
            for item_id, entry in outputs.items():
                if not item_id.endswith("_v0"):
                    continue
                prov = engine.state.provenance.get(item_id)
                if not prov:
                    continue
                total = prov.in_situ_kg + prov.imported_kg + prov.unknown_kg
                if total <= 0:
                    continue
                isru_pct = (prov.in_situ_kg / total) * 100.0
                bar = _render_blocks(isru_pct, step=10.0, max_blocks=10)
                art_lines = [
                    "      ┌───┐",
                    "  ┌───┤███├───┐",
                    "  │   └───┘   │",
                    "  │  ┌─────┐  │",
                    "  └──┤ ┼ ┼ ├──┘",
                    "     └─────┘",
                ]
                art_lines = _center_lines(art_lines, _get_display_width())
                _emit(f"  Machine: {item_id}  ISRU {isru_pct:.1f}% [{bar}]", _COLOR_SUCCESS)
                _emit(
                    f"  Local {prov.in_situ_kg:.1f} kg | Imported {prov.imported_kg:.1f} kg | Unknown {prov.unknown_kg:.1f} kg",
                    _COLOR_DIM,
                )
                for line in art_lines:
                    _emit(f"{line}", _COLOR_DIM)
    if imports:
        import_list = _format_imports_summary(imports)
        if len(import_list) > 4:
            rows = [entry.split(" ", 1) for entry in import_list[:8]]
            table = _render_table(["Item", "Qty"], rows)
            art = _select_ascii_art("imports", len(table))
            table = _attach_ascii_art(table, art, indent=2)
            label = "Incoming" if heading and any("Import" in part for part in heading) else "Imports"
            _emit(f"  {label}:", _COLOR_NOTE)
            for line in table:
                if _ART_DELIM in line:
                    left, art = line.split(_ART_DELIM, 1)
                    colored_left = _color(left, _COLOR_NOTE)
                    colored_art = _color(art, _COLOR_DIM)
                    _emit(colored_left + colored_art)
                    continue
                _emit(f"{line}", _COLOR_NOTE)
        else:
            label = "Incoming" if heading and any("Import" in part for part in heading) else "Imports"
            _emit(f"  {label}: " + ", ".join(import_list), _COLOR_NOTE)
    if recipes:
        recipe_lines = [f"{rid} x{qty}" for rid, qty in recipes.items()]
        _emit(f"  Recipes: " + ", ".join(recipe_lines), _COLOR_NOTE)
    if processes:
        process_lines = [f"{pid} x{count}" for pid, count in processes.items()]
        _emit(f"  Processes: " + ", ".join(process_lines), _COLOR_NOTE)
    if energy or time_hours or import_mass:
        bar = _render_blocks(energy)
        _emit(
            f"  Δ⏱ {time_hours:.1f}h  Δ⚡ {energy:.1f} kWh [{bar}]  Δ⇣ {import_mass:.1f} kg",
            _COLOR_DIM,
        )


def _emit_story_markdown_context(context: dict[tuple[str, ...], dict[str, Any]], heading: list[str]) -> None:
    entry = context.get(tuple(heading))
    if not entry:
        for end in range(len(heading) - 1, 0, -1):
            entry = context.get(tuple(heading[:end]))
            if entry:
                break
    if not entry:
        return
    total = entry.get("tasks_total", 0)
    done = entry.get("tasks_done", 0)
    if total:
        bar = _render_blocks(done, step=1.0, max_blocks=min(10, total))
        _emit(f"  Tasks: {done}/{total} [{bar}]", _COLOR_NOTE)
    for admonition in entry.get("admonitions", []):
        kind = admonition.get("kind", "note")
        title = admonition.get("title", "").strip()
        body = admonition.get("body", "").strip()
        if kind == "note" and title.lower() == "imports":
            continue
        tag = kind.upper()
        label = f"{tag}: {title}".strip().rstrip(":")
        if body:
            _emit(f"  {label} — {body}", _COLOR_WARN if kind == "warning" else _COLOR_NOTE)
        else:
            _emit(f"  {label}", _COLOR_WARN if kind == "warning" else _COLOR_NOTE)
    for line in entry.get("story_lines", []):
        _emit(f"  Story: {line}", _COLOR_INFO)


def _get_sim_metrics(sim_id: str, kb_loader: KBLoader) -> Optional[dict[str, float]]:
    sim_dir = SIMULATIONS_DIR / sim_id
    if not (sim_dir / "snapshot.json").exists():
        return None
    engine = load_or_create_simulation(sim_id, kb_loader)
    import_mass, _unknown = _get_import_mass_kgs(engine, kb_loader)
    return {
        "time_hours": engine.state.current_time_hours,
        "energy_kwh": engine.state.total_energy_kwh,
        "import_mass": import_mass,
    }


def _emit_checkpoint(sim_id: str, kb_loader: KBLoader) -> None:
    sim_dir = SIMULATIONS_DIR / sim_id
    if not (sim_dir / "snapshot.json").exists():
        return
    engine = load_or_create_simulation(sim_id, kb_loader)
    time_days = engine.state.current_time_hours / 24.0
    import_mass, _unknown = _get_import_mass_kgs(engine, kb_loader)
    inventory_count = len(engine.state.inventory)
    imports_count = len(engine.state.total_imports)
    _emit(
        f"◆ Checkpoint  ⏱ {time_days:.1f}d  ⚡ {engine.state.total_energy_kwh:.1f} kWh  ⇣ ~{import_mass:.1f} kg",
        _COLOR_SUCCESS,
    )
    _emit(f"  Inventory: {inventory_count} items  |  Imports tracked: {imports_count}", _COLOR_DIM)

# ============================================================================
# Runbook command
# ============================================================================

def _run_runbook(
    runbook_path: Path,
    kb_loader: KBLoader,
    *,
    default_sim_id: Optional[str],
    stack: list[Path],
    allow_control: bool,
    dry_run: bool,
    continue_on_error: bool,
    story_mode: bool,
) -> int:
    if not runbook_path.exists():
        _emit(f"Error: runbook file not found: {runbook_path}", _COLOR_ERROR, is_error=True)
        return 1

    resolved_path = runbook_path.resolve()
    if resolved_path in stack:
        _emit(f"Error: runbook cycle detected at {runbook_path}", _COLOR_ERROR, is_error=True)
        return 1
    if len(stack) >= 10:
        _emit("Error: runbook nesting too deep (max 10)", _COLOR_ERROR, is_error=True)
        return 1

    try:
        md_text = runbook_path.read_text(encoding="utf-8")
        commands = _load_runbook_commands(runbook_path)
    except Exception as exc:
        _emit(f"Error parsing runbook: {exc}", _COLOR_ERROR, is_error=True)
        return 1

    command_map = {
        "sim.init": cmd_init,
        "sim.scaffold": cmd_scaffold,
        "sim.import": cmd_import,
        "sim.start-process": cmd_start_process,
        "sim.run-recipe": cmd_run_recipe,
        "sim.build-machine": cmd_build_machine,
        "sim.advance-time": cmd_advance_time,
        "sim.preview": cmd_preview,
        "sim.view-state": cmd_view_state,
        "sim.status": cmd_status,
        "sim.provenance": cmd_provenance,
        "sim.list": cmd_list,
        "sim.plan": cmd_plan,
        "sim.visualize": cmd_visualize,
    }

    parsed_context = _parse_markdown_story_context(md_text) if story_mode else {"sections": {}, "intro_lines": []}
    story_context = parsed_context.get("sections", {})
    _emit(f"== Runbook: {runbook_path} ==", _COLOR_INFO)
    if story_mode and len(stack) == 0:
        title = "SIMULATOR // STORY MODE"
        width = 54
        pad = max(0, (width - len(title)) // 2)
        line = " " * pad + title
        _emit("┏" + ("━" * width) + "┓", _COLOR_NOTE)
        _emit("┃" + line.ljust(width) + "┃", _COLOR_NOTE)
        _emit("┗" + ("━" * width) + "┛", _COLOR_NOTE)
        for intro_line in parsed_context.get("intro_lines", [])[:2]:
            _emit(intro_line, _COLOR_NOTE)
        top_keys = [k for k in story_context.keys() if len(k) == 1]
        if top_keys:
            top_key = sorted(top_keys, key=lambda k: k[0])[0]
            _emit_story_markdown_context(story_context, list(top_key))
    stack.append(resolved_path)
    try:
        last_heading: list[str] = []
        phase: dict[str, Any] = {
            "imports": {},
            "recipes": {},
            "processes": {},
            "outputs": {},
            "energy_delta": 0.0,
            "time_delta": 0.0,
            "import_mass_delta": 0.0,
        }
        last_metrics: Optional[dict[str, float]] = None
        for idx, entry in enumerate(commands, start=1):
            cmd_name = entry.get("cmd")
            cmd_args = entry.get("args") or {}
            heading = entry.get("_md_heading") or []

            if not cmd_name:
                _emit(f"Error: missing cmd in runbook step {idx}", _COLOR_ERROR, is_error=True)
                return 1
            if not cmd_name.startswith("sim."):
                _emit(f"Error: non-sim command in runbook step {idx}: {cmd_name}", _COLOR_ERROR, is_error=True)
                return 1

            if cmd_name == "sim.runbook":
                child_file = _get_arg(cmd_args, "file", "path")
                if not child_file:
                    _emit(f"Error: sim.runbook requires file (step {idx})", _COLOR_ERROR, is_error=True)
                    return 1
                child_path = (runbook_path.parent / child_file).resolve()
                result = _run_runbook(
                    child_path,
                    kb_loader,
                    default_sim_id=default_sim_id,
                    stack=stack,
                    allow_control=False,
                    dry_run=dry_run,
                    continue_on_error=continue_on_error,
                    story_mode=story_mode,
                )
                if result != 0 and not continue_on_error:
                    return result
                continue

            if cmd_name == "sim.use":
                if not allow_control:
                    continue
                sim_id = _get_arg(cmd_args, "sim-id", "sim_id")
                if not sim_id:
                    _emit(f"Error: sim.use requires sim-id (step {idx})", _COLOR_ERROR, is_error=True)
                    return 1
                default_sim_id = sim_id
                if story_mode and sim_id and not dry_run:
                    last_metrics = _get_sim_metrics(sim_id, kb_loader)
                continue

            if cmd_name == "sim.reset":
                if not allow_control:
                    continue
                sim_id = _get_arg(cmd_args, "sim-id", "sim_id") or default_sim_id
                if not sim_id:
                    _emit(f"Error: sim.reset requires sim-id (step {idx})", _COLOR_ERROR, is_error=True)
                    return 1
                if dry_run:
                    _emit(f"[dry-run] sim.reset --sim-id {sim_id}", _COLOR_DIM)
                    continue
                result = _reset_simulation(sim_id, kb_loader)
                if story_mode and sim_id:
                    last_metrics = _get_sim_metrics(sim_id, kb_loader)
                    phase = {
                        "imports": {},
                        "recipes": {},
                        "processes": {},
                        "outputs": {},
                        "energy_delta": 0.0,
                        "time_delta": 0.0,
                        "import_mass_delta": 0.0,
                    }
                if result != 0 and not continue_on_error:
                    return result
                continue

            if cmd_name == "sim.note":
                message = _get_arg(cmd_args, "message", "msg")
                style = _get_arg(cmd_args, "style") or "info"
                if not message:
                    _emit(f"Error: sim.note requires message (step {idx})", _COLOR_ERROR, is_error=True)
                    return 1
                color_map = {
                    "info": _COLOR_INFO,
                    "milestone": _COLOR_SUCCESS,
                    "warning": _COLOR_WARN,
                    "success": _COLOR_SUCCESS,
                    "dim": _COLOR_DIM,
                    "note": _COLOR_NOTE,
                }
                if story_mode and heading and heading != last_heading:
                    _emit_story_phase_summary(phase, default_sim_id, kb_loader, last_heading)
                    phase = {
                        "imports": {},
                        "recipes": {},
                        "processes": {},
                        "outputs": {},
                        "energy_delta": 0.0,
                        "time_delta": 0.0,
                        "import_mass_delta": 0.0,
                    }
                    metrics = _get_sim_metrics(default_sim_id, kb_loader) if default_sim_id else None
                    _emit_story_heading(heading, metrics)
                    _emit_story_markdown_context(story_context, heading)
                    last_heading = heading
                if story_mode:
                    icon_map = {
                        "milestone": "◆",
                        "success": "✔",
                        "warning": "▲",
                        "note": "•",
                        "info": "•",
                        "dim": "·",
                    }
                    icon = icon_map.get(style, "•")
                    _emit(f"  {icon} {message}", color_map.get(style, _COLOR_INFO))
                else:
                    _emit(str(message), color_map.get(style, _COLOR_INFO))
                continue

            handler = command_map.get(cmd_name)
            if handler is None:
                _emit(f"Error: unsupported runbook command (step {idx}): {cmd_name}", _COLOR_ERROR, is_error=True)
                return 1

            normalized_args = {_normalize_arg_key(k): v for k, v in cmd_args.items()}
            if "sim_id" not in normalized_args and default_sim_id:
                normalized_args["sim_id"] = default_sim_id

            if dry_run:
                _emit(f"[dry-run] {cmd_name} {cmd_args}", _COLOR_DIM)
                continue

            if story_mode and cmd_name == "sim.import":
                item = _get_arg(cmd_args, "item")
                qty = _get_arg(cmd_args, "quantity") or 0.0
                unit = _get_arg(cmd_args, "unit") or "unit"
                if item:
                    imports = phase["imports"]
                    entry = imports.get(item, {"quantity": 0.0, "unit": unit})
                    entry["quantity"] += float(qty)
                    entry["unit"] = unit
                    imports[item] = entry

            if story_mode and cmd_name == "sim.run-recipe":
                recipe = _get_arg(cmd_args, "recipe")
                qty = _get_arg(cmd_args, "quantity") or 0
                if recipe:
                    recipes = phase["recipes"]
                    recipes[recipe] = recipes.get(recipe, 0) + int(qty)

            result = handler(argparse.Namespace(**normalized_args), kb_loader)
            if result != 0 and not continue_on_error:
                return result

            if story_mode and cmd_name == "sim.advance-time":
                if _LAST_ADVANCE_RESULT and _LAST_ADVANCE_RESULT.get("completed"):
                    proc_counts = phase["processes"]
                    output_totals = phase["outputs"]
                    for proc in _LAST_ADVANCE_RESULT["completed"]:
                        proc_id = proc.get("process_id")
                        if not proc_id:
                            continue
                        proc_counts[proc_id] = proc_counts.get(proc_id, 0) + 1
                        outputs = proc.get("outputs") or {}
                        for item_id, inv_item in outputs.items():
                            if isinstance(inv_item, (int, float)):
                                qty = float(inv_item)
                                unit = "unit"
                            else:
                                qty = inv_item.quantity if hasattr(inv_item, "quantity") else inv_item.get("quantity", 0)
                                unit = inv_item.unit if hasattr(inv_item, "unit") else inv_item.get("unit", "unit")
                            entry = output_totals.get(item_id, {"quantity": 0.0, "unit": unit})
                            entry["quantity"] += float(qty)
                            entry["unit"] = unit
                            output_totals[item_id] = entry
            if story_mode and cmd_name == "sim.status" and default_sim_id:
                _emit_checkpoint(default_sim_id, kb_loader)

            if story_mode and default_sim_id:
                metrics = _get_sim_metrics(default_sim_id, kb_loader)
                if metrics and last_metrics:
                    phase["time_delta"] += metrics["time_hours"] - last_metrics["time_hours"]
                    phase["energy_delta"] += metrics["energy_kwh"] - last_metrics["energy_kwh"]
                    phase["import_mass_delta"] += metrics["import_mass"] - last_metrics["import_mass"]
                if metrics:
                    last_metrics = metrics
            sys.stdout.flush()
            sys.stderr.flush()

        if len(stack) == 1:
            if story_mode:
                _emit_story_phase_summary(phase, default_sim_id, kb_loader, last_heading)
                _emit_story_footer()
            _emit("== Runbook complete ==", _COLOR_SUCCESS)
        return 0
    finally:
        stack.pop()


def cmd_runbook(args, kb_loader: KBLoader):
    """Execute a Markdown runbook with sim-runbook YAML blocks."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(line_buffering=True, write_through=True)
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(line_buffering=True, write_through=True)
    import builtins
    original_print = builtins.print

    def runbook_print(*print_args, **print_kwargs):
        print_kwargs.setdefault("flush", True)
        return original_print(*print_args, **print_kwargs)

    builtins.print = runbook_print

    runbook_path = Path(args.file)
    global _RUNBOOK_OUTPUT_MODE
    previous_mode = _RUNBOOK_OUTPUT_MODE
    _RUNBOOK_OUTPUT_MODE = args.format
    try:
        return _run_runbook(
            runbook_path,
            kb_loader,
            default_sim_id=None,
            stack=[],
            allow_control=True,
            dry_run=args.dry_run,
            continue_on_error=args.continue_on_error,
            story_mode=args.format == "story",
        )
    finally:
        _RUNBOOK_OUTPUT_MODE = previous_mode
        builtins.print = original_print

# ============================================================================
# Commands
# ============================================================================

def cmd_init(args, kb_loader: KBLoader):
    """Initialize a new simulation."""
    # Check if simulation already exists
    sim_dir = SIMULATIONS_DIR / args.sim_id
    snapshot_file = sim_dir / "snapshot.json"
    if snapshot_file.exists():
        _emit(f"Error: Simulation '{args.sim_id}' already exists", _COLOR_ERROR, is_error=True)
        return 1

    # Create new simulation
    engine = SimulationEngine(args.sim_id, kb_loader, sim_dir)
    engine.load()  # This will create the initial SimStartEvent for new sims

    _emit(f"✓ Created simulation '{args.sim_id}'", _COLOR_SUCCESS)
    _emit(f"  Location: {engine.sim_dir}", _COLOR_DIM)
    _emit(f"  Snapshot: {engine.snapshot_file}", _COLOR_DIM)
    _emit(f"  Events: {engine.event_log_file}", _COLOR_DIM)
    return 0


def cmd_view_state(args, kb_loader: KBLoader):
    """View current simulation state."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)
    state = engine.get_state_dict()

    _emit(f"=== Simulation: {args.sim_id} ===", _COLOR_INFO)
    _emit_kv("Time:", f"{state['current_time_hours']:.1f} hours ({state['current_time_hours']/24:.1f} days)", _COLOR_TIME)
    _emit_kv("Energy Consumed:", f"{state.get('total_energy_kwh', 0.0):.2f} kWh", _COLOR_ENERGY)

    _emit(f"\nInventory ({len(state['inventory'])} items):", _COLOR_NOTE)
    for item_id, inv in sorted(state['inventory'].items()):
        _emit(f"  {item_id}: {inv['quantity']:.2f} {inv['unit']}")

    # Read active processes from scheduler (source of truth)
    _emit(f"\nActive Processes ({len(engine.scheduler.active_processes)}):", _COLOR_NOTE)
    for process_run in engine.scheduler.active_processes.values():
        remaining = process_run.end_time - state['current_time_hours']
        _emit(f"  {process_run.process_id} (ends at {process_run.end_time:.1f}h, {remaining:.1f}h remaining)")

    _emit(f"\nMachines Built ({len(state['machines_built'])}):", _COLOR_NOTE)
    for machine in state['machines_built']:
        _emit(f"  {machine}")

    _emit(f"\nTotal Imports ({len(state['total_imports'])} items):", _COLOR_NOTE)
    total_mass = 0.0
    unknown_mass_count = 0

    for item_id, inv in sorted(state['total_imports'].items()):
        _emit(f"  {item_id}: {inv['quantity']:.2f} {inv['unit']}")

        # Calculate mass contribution (Issue #10)
        if inv['unit'] == 'kg':
            # Direct mass measurement
            total_mass += inv['quantity']
        elif inv['unit'] == 'unit':
            # Look up item mass
            item = kb_loader.get_item(item_id)
            if item:
                item_dict = item.model_dump() if hasattr(item, 'model_dump') else item
                item_mass = item_dict.get('mass')
                if item_mass is not None:
                    total_mass += item_mass * inv['quantity']
                else:
                    unknown_mass_count += 1
            else:
                unknown_mass_count += 1
        else:
            # Unknown unit (L, m3, etc.)
            unknown_mass_count += 1

    # Display total with unknown count
    if unknown_mass_count > 0:
        _emit_kv("  Total imported mass:", f"~{total_mass:.1f} kg ({unknown_mass_count} items with unknown mass)", _COLOR_MASS)
    else:
        _emit_kv("  Total imported mass:", f"~{total_mass:.1f} kg", _COLOR_MASS)

    return 0


def cmd_import(args, kb_loader: KBLoader):
    """Import an item from Earth."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    if getattr(args, "ensure", False):
        current_qty = 0.0
        if args.item in engine.state.inventory:
            existing = engine.state.inventory[args.item]
            if existing.unit == args.unit:
                current_qty = existing.quantity
            else:
                converted = engine.converter.convert(
                    existing.quantity, existing.unit, args.unit, args.item
                )
                if converted is None:
                    _emit(
                        f"✗ Failed to import: incompatible units for '{args.item}' "
                        f"({existing.unit} -> {args.unit})",
                        _COLOR_ERROR,
                        is_error=True,
                    )
                    return 1
                current_qty = converted

        import_qty = max(0.0, args.quantity - current_qty)
        if import_qty <= 0:
            _emit(
                f"↷ Skipped import for '{args.item}' (have {current_qty:.2f} {args.unit})",
                _COLOR_NOTE,
            )
            return 0

        result = engine.import_item(args.item, import_qty, args.unit)
        if result["success"]:
            _emit(
                f"✓ Imported {import_qty:.2f} {args.unit} of '{args.item}' "
                f"(had {current_qty:.2f} {args.unit})",
                _COLOR_SUCCESS,
            )
            engine.save()
            return 0
    else:
        result = engine.import_item(args.item, args.quantity, args.unit)

    if result['success']:
        _emit(f"✓ Imported {args.quantity} {args.unit} of '{args.item}'", _COLOR_SUCCESS)
        engine.save()
        return 0
    else:
        _emit(f"✗ Failed to import: {result.get('message', 'Unknown error')}", _COLOR_ERROR, is_error=True)
        return 1


def cmd_start_process(args, kb_loader: KBLoader):
    """Start a process."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    # Duration is optional - engine will calculate if not provided
    # Can provide either duration OR (output_quantity + output_unit) for calculation
    result = engine.start_process(
        process_id=args.process,
        scale=args.scale if hasattr(args, 'scale') else 1.0,
        duration_hours=args.duration if args.duration else None,
        output_quantity=getattr(args, 'output_quantity', None),
        output_unit=getattr(args, 'output_unit', None)
    )

    if result['success']:
        duration = result.get('duration_hours', 0.0)
        calculated = result.get('duration_calculated', False)
        duration_source = "(calculated)" if calculated else "(provided)"
        _emit(f"✓ Started process '{args.process}'", _COLOR_SUCCESS)
        _emit_kv("  Duration:", f"{duration:.2f} hours {duration_source}", _COLOR_TIME)
        _emit_kv("  Ends at:", f"{result.get('ends_at', 0.0):.2f} hours", _COLOR_TIME)
        if 'energy_kwh' in result:
            _emit_kv("  Energy:", f"{result['energy_kwh']:.2f} kWh", _COLOR_ENERGY)
        engine.save()
        return 0
    else:
        _emit(f"✗ Failed to start process: {result.get('message', 'Unknown error')}", _COLOR_ERROR, is_error=True)
        if 'validation_errors' in result:
            _emit("\nValidation errors:", _COLOR_WARN, is_error=True)
            for err in result['validation_errors']:
                _emit(f"  - {err['message']}", _COLOR_WARN, is_error=True)
        return 1


def cmd_run_recipe(args, kb_loader: KBLoader):
    """Run a recipe."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    result = engine.run_recipe(args.recipe, args.quantity)

    if result['success']:
        _emit(f"✓ Started recipe '{args.recipe}' (quantity: {args.quantity})", _COLOR_SUCCESS)
        _emit_kv("  Steps:", f"{result.get('total_steps', 0)}", _COLOR_TIME)
        _emit_kv("  Duration:", f"{result.get('total_duration_hours', 0.0):.2f} hours", _COLOR_TIME)
        _emit_kv("  Ends at:", f"{result.get('ends_at', 0.0):.2f} hours", _COLOR_TIME)
        engine.save()
        return 0
    else:
        _emit(f"✗ Failed to run recipe: {result.get('message', 'Unknown error')}", _COLOR_ERROR, is_error=True)
        return 1


def _as_quantity(entry: Any) -> Quantity:
    """Normalize dict/object entries into a Quantity."""
    if isinstance(entry, dict):
        item_id = entry.get("item_id")
        qty = entry.get("qty") if entry.get("qty") is not None else entry.get("quantity")
        unit = entry.get("unit", "kg")
    else:
        item_id = getattr(entry, "item_id", None)
        qty = getattr(entry, "qty", None)
        if qty is None:
            qty = getattr(entry, "quantity", None)
        unit = getattr(entry, "unit", "kg")
    return Quantity(item_id=item_id, qty=float(qty or 0), unit=unit)


def _collect_machine_requirements(process_def: Dict[str, Any]) -> Dict[str, str]:
    """Collect required machine IDs from process definition."""
    required: Dict[str, str] = {}

    for machine_id in process_def.get("requires_ids", []) or []:
        required[machine_id] = "1 unit"

    for machine_req in process_def.get("required_machines", []) or []:
        if isinstance(machine_req, dict):
            machine_id = list(machine_req.keys())[0]
            count = machine_req[machine_id]
        elif isinstance(machine_req, str):
            machine_id = machine_req
            count = 1
        else:
            continue
        required[machine_id] = f"{count} unit"

    for req in process_def.get("resource_requirements", []) or []:
        if isinstance(req, dict) and req.get("machine_id"):
            qty = req.get("qty", 1.0)
            unit = req.get("unit", "hr")
            required[req["machine_id"]] = f"{qty} {unit}"

    return required


def _format_quantity_list(items: Iterable[Quantity]) -> list[str]:
    lines = []
    for item in items:
        lines.append(f"{item.item_id}: {item.qty:.2f} {item.unit}")
    return lines


def _calculate_readiness(process_model, converter: UnitConverter) -> Dict[str, str]:
    inputs = {_as_quantity(q).item_id: _as_quantity(q) for q in process_model.inputs}
    outputs = {_as_quantity(q).item_id: _as_quantity(q) for q in process_model.outputs}

    readiness = {"duration": "ok", "energy": "ok"}

    try:
        _ = calculate_duration(process_model, inputs, outputs, converter)
    except CalculationError as exc:
        readiness["duration"] = f"error: {exc}"
    except Exception as exc:
        readiness["duration"] = f"error: {exc}"

    if not getattr(process_model, "energy_model", None):
        readiness["energy"] = "n/a (no energy_model)"
    else:
        try:
            _ = calculate_energy(process_model, inputs, outputs, converter)
        except CalculationError as exc:
            readiness["energy"] = f"error: {exc}"
        except Exception as exc:
            readiness["energy"] = f"error: {exc}"

    return readiness


def _build_dependency_tree(item_id: str, kb_loader: KBLoader, depth: int = 0, max_depth: int = 10, visited: set = None) -> dict:
    """
    Recursively build dependency tree for an item.

    Returns dict with:
    - item_id: str
    - item_name: str
    - qty: float
    - unit: str
    - mass: float (if available)
    - recipe_id: str (if has recipe)
    - inputs: list of dependency trees
    - processes: list of process IDs
    - is_import: bool
    - is_boundary: bool (raw material)
    - warnings: list of strings
    """
    if visited is None:
        visited = set()

    if depth > max_depth:
        return {
            "item_id": item_id,
            "warnings": [f"Max depth {max_depth} reached"]
        }

    # Avoid circular dependencies
    if item_id in visited:
        return {
            "item_id": item_id,
            "warnings": ["Circular dependency detected"]
        }

    visited.add(item_id)

    # Get item info
    item = kb_loader.get_item(item_id)
    if not item:
        return {
            "item_id": item_id,
            "warnings": ["Item not found in KB"]
        }

    item_dict = item.model_dump() if hasattr(item, "model_dump") else item
    result = {
        "item_id": item_id,
        "item_name": item_dict.get("name", item_id),
        "mass": item_dict.get("mass", 0),
        "unit": item_dict.get("unit", "unit"),
        "is_import": item_dict.get("is_import", False),
        "warnings": []
    }

    # Check for recipe
    recipe_id = item_dict.get("recipe")
    if not recipe_id:
        result["warnings"].append("No recipe defined")
        result["is_import"] = True
        visited.remove(item_id)
        return result

    recipe = kb_loader.get_recipe(recipe_id)
    if not recipe:
        result["warnings"].append(f"Recipe {recipe_id} not found")
        result["is_import"] = True
        visited.remove(item_id)
        return result

    recipe_dict = recipe.model_dump() if hasattr(recipe, "model_dump") else recipe
    result["recipe_id"] = recipe_id
    result["processes"] = []
    result["inputs"] = []

    # Collect inputs from recipe steps
    all_inputs = {}

    for step in recipe_dict.get("steps", []):
        process_id = step.get("process_id")
        if not process_id:
            continue

        result["processes"].append(process_id)

        process = kb_loader.get_process(process_id)
        if not process:
            result["warnings"].append(f"Process {process_id} not found")
            continue

        process_dict = process.model_dump() if hasattr(process, "model_dump") else process

        # Check if boundary process
        if process_dict.get("process_type") == "boundary":
            result["is_boundary"] = True

        # Aggregate inputs from all processes
        for inp in process_dict.get("inputs", []):
            inp_dict = inp if isinstance(inp, dict) else inp.model_dump()
            inp_id = inp_dict.get("item_id")
            inp_qty = float(inp_dict.get("qty", 0))
            inp_unit = inp_dict.get("unit", "kg")

            if inp_id not in all_inputs:
                all_inputs[inp_id] = {"qty": 0, "unit": inp_unit}
            all_inputs[inp_id]["qty"] += inp_qty

    # Recursively build dependency trees for inputs
    for inp_id, inp_info in all_inputs.items():
        child_tree = _build_dependency_tree(inp_id, kb_loader, depth + 1, max_depth, visited.copy())
        child_tree["qty"] = inp_info["qty"]
        child_tree["unit"] = inp_info["unit"]
        result["inputs"].append(child_tree)

    visited.remove(item_id)
    return result


def _aggregate_materials(tree: dict, multiplier: float = 1.0) -> dict:
    """
    Aggregate all materials from dependency tree.

    Returns dict with:
    - raw_materials: dict of {item_id: {qty, unit, mass}}
    - imports: dict of {item_id: {qty, unit, mass}}
    - intermediates: dict of {item_id: {qty, unit, mass}}
    - processes: list of process_ids
    """
    raw_materials = {}
    imports = {}
    intermediates = {}
    processes = []

    def add_to_dict(target: dict, item_id: str, qty: float, unit: str, mass: float = 0):
        if item_id not in target:
            target[item_id] = {"qty": 0, "unit": unit, "mass": 0}
        target[item_id]["qty"] += qty
        target[item_id]["mass"] += mass

    def traverse(node: dict, mult: float):
        item_id = node.get("item_id")
        qty = node.get("qty", 1.0) * mult
        unit = node.get("unit", "unit")
        mass = (node.get("mass") or 0) * mult

        # Collect processes
        for proc in node.get("processes", []):
            if proc not in processes:
                processes.append(proc)

        # Classify this node
        if node.get("is_boundary"):
            add_to_dict(raw_materials, item_id, qty, unit, mass)
        elif node.get("is_import") or not node.get("inputs"):
            add_to_dict(imports, item_id, qty, unit, mass)
        else:
            # Has inputs, so it's an intermediate
            add_to_dict(intermediates, item_id, qty, unit, mass)

        # Recursively traverse inputs
        for child in node.get("inputs", []):
            child_qty = child.get("qty", 1.0)
            traverse(child, mult * child_qty)

    traverse(tree, multiplier)

    return {
        "raw_materials": raw_materials,
        "imports": imports,
        "intermediates": intermediates,
        "processes": processes
    }


def _print_dependency_tree(tree: dict, indent: int = 0, show_warnings: bool = True):
    """Print formatted dependency tree."""
    prefix = "  " * indent
    item_id = tree.get("item_id", "unknown")
    item_name = tree.get("item_name", item_id)
    qty = tree.get("qty", 1.0)
    unit = tree.get("unit", "unit")
    mass = tree.get("mass", 0)

    # Build line
    line = f"{prefix}├─ {item_name}"
    if qty != 1.0 or unit != "unit":
        line += f" ({qty:.2f} {unit}"
        if mass and mass > 0:
            line += f", ~{mass:.2f} kg"
        line += ")"

    # Add annotations
    annotations = []
    if tree.get("is_boundary"):
        annotations.append("ISRU/boundary")
    if tree.get("is_import"):
        annotations.append("IMPORT")
    if tree.get("recipe_id"):
        annotations.append(f"← {tree['recipe_id']}")

    if annotations:
        line += f"  [{', '.join(annotations)}]"

    print(line)

    # Show warnings
    if show_warnings and tree.get("warnings"):
        for warning in tree["warnings"]:
            print(f"{prefix}  ⚠ {warning}")

    # Show processes
    if tree.get("processes"):
        proc_str = ", ".join(tree["processes"])
        print(f"{prefix}  via: {proc_str}")

    # Recursively print inputs
    for child in tree.get("inputs", []):
        _print_dependency_tree(child, indent + 1, show_warnings)


def cmd_plan(args, kb_loader: KBLoader):
    """Preflight a process or recipe to show immediate blockers."""
    converter = UnitConverter(kb_loader)

    if args.process:
        process_model = kb_loader.get_process(args.process)
        if not process_model:
            print(f"Error: Process '{args.process}' not found", file=sys.stderr)
            return 1

        process_def = process_model.model_dump() if hasattr(process_model, "model_dump") else process_model
        required = _collect_machine_requirements(process_def)

        print(f"=== Plan: process {args.process} ===")
        if required:
            print("Required machines/resources:")
            for machine_id, detail in sorted(required.items()):
                print(f"  {machine_id}: {detail}")
        else:
            print("Required machines/resources: none")

        inputs = [_as_quantity(q) for q in process_def.get("inputs", [])]
        outputs = [_as_quantity(q) for q in process_def.get("outputs", [])]
        if inputs:
            print("Inputs:")
            for line in _format_quantity_list(inputs):
                print(f"  {line}")
        else:
            print("Inputs: none")

        if outputs:
            print("Outputs:")
            for line in _format_quantity_list(outputs):
                print(f"  {line}")
        else:
            print("Outputs: none")

        readiness = _calculate_readiness(process_model, converter)
        print("Duration calculation:", readiness["duration"])
        print("Energy calculation:", readiness["energy"])
        return 0

    if args.recipe:
        recipe_model = kb_loader.get_recipe(args.recipe)
        if not recipe_model:
            print(f"Error: Recipe '{args.recipe}' not found", file=sys.stderr)
            return 1

        recipe_def = recipe_model.model_dump() if hasattr(recipe_model, "model_dump") else recipe_model
        target_item_id = recipe_def.get("target_item_id")

        if not target_item_id:
            print(f"Error: Recipe has no target_item_id", file=sys.stderr)
            return 1

        # Get target item info
        target_item = kb_loader.get_item(target_item_id)
        if not target_item:
            print(f"Error: Target item '{target_item_id}' not found", file=sys.stderr)
            return 1

        target_dict = target_item.model_dump() if hasattr(target_item, "model_dump") else target_item
        target_name = target_dict.get("name", target_item_id)
        target_mass = target_dict.get("mass")  # None if not defined

        print(f"{'='*80}")
        print(f"PRODUCTION PLAN: {target_name}")
        print(f"{'='*80}")
        print()
        # Handle missing mass gracefully (Issue #11)
        if target_mass is not None:
            print(f"TARGET: {target_item_id} (1 unit, {target_mass:.2f} kg)")
        else:
            print(f"TARGET: {target_item_id} (1 unit, mass unknown)")
        print()

        # Build dependency tree
        print("DEPENDENCY TREE:")
        print()
        dep_tree = _build_dependency_tree(target_item_id, kb_loader, max_depth=8)
        _print_dependency_tree(dep_tree)
        print()

        # Aggregate materials
        aggregated = _aggregate_materials(dep_tree)

        # Print aggregate materials
        print("AGGREGATE MATERIALS NEEDED:")
        print()

        raw_mats = aggregated["raw_materials"]
        if raw_mats:
            print("Raw Materials (ISRU/Boundary):")
            for item_id in sorted(raw_mats.keys()):
                info = raw_mats[item_id]
                print(f"  • {item_id}: {info['qty']:.2f} {info['unit']}", end="")
                if info['mass'] > 0:
                    print(f" (~{info['mass']:.2f} kg)")
                else:
                    print()
        else:
            print("Raw Materials (ISRU/Boundary): none")
        print()

        imports = aggregated["imports"]
        if imports:
            print("Must Import or Collect:")
            for item_id in sorted(imports.keys()):
                info = imports[item_id]
                print(f"  • {item_id}: {info['qty']:.2f} {info['unit']}", end="")
                if info['mass'] > 0:
                    print(f" (~{info['mass']:.2f} kg)")
                else:
                    print()
        else:
            print("Must Import or Collect: none")
        print()

        intermediates = aggregated["intermediates"]
        if intermediates:
            print("Intermediate Materials (produced & consumed):")
            for item_id in sorted(intermediates.keys()):
                info = intermediates[item_id]
                print(f"  • {item_id}: {info['qty']:.2f} {info['unit']}", end="")
                if info['mass'] > 0:
                    print(f" (~{info['mass']:.2f} kg)")
                else:
                    print()
            print()

        # Collect machine requirements
        required = {}
        missing_steps = []

        for step in recipe_def.get("steps", []):
            resolved_step = resolve_recipe_step_with_kb(step, kb_loader)
            if "_warning" in resolved_step:
                process_id = step.get("process_id")
                if process_id:
                    missing_steps.append(process_id)
            required.update(_collect_machine_requirements(resolved_step))

        print("MACHINES REQUIRED (for this recipe's direct processes):")
        if required:
            for machine_id, detail in sorted(required.items()):
                print(f"  - {machine_id}: {detail}")
        else:
            print("  none (may need machines from sub-recipes)")
        print()

        # Show process list
        processes = aggregated["processes"]
        if processes:
            print(f"PROCESSES IN DEPENDENCY CHAIN ({len(processes)} total):")
            for i, proc_id in enumerate(processes[:20], 1):  # Limit to first 20
                print(f"  {i}. {proc_id}")
            if len(processes) > 20:
                print(f"  ... and {len(processes) - 20} more")
            print()

        # Warnings
        if missing_steps:
            print("WARNINGS:")
            print("  Missing processes:")
            for proc_id in sorted(missing_steps):
                print(f"    - {proc_id}")
            print()

        print("NOTE: Time/energy calculations require simulation execution")
        print(f"{'='*80}")
        return 0

    print("Error: Provide --process or --recipe", file=sys.stderr)
    return 1


def _parse_bootstrap_entry(entry: str) -> tuple[str, float, str]:
    """Parse bootstrap entries like item_id[:qty[:unit]]."""
    parts = entry.split(":")
    item_id = parts[0]
    qty = 1.0
    unit = "unit"
    if len(parts) >= 2 and parts[1]:
        qty = float(parts[1])
    if len(parts) >= 3 and parts[2]:
        unit = parts[2]
    return item_id, qty, unit


def cmd_scaffold(args, kb_loader: KBLoader):
    """Create a simulation with optional bootstrap imports."""
    sim_dir = SIMULATIONS_DIR / args.sim_id
    snapshot_file = sim_dir / "snapshot.json"
    if snapshot_file.exists():
        print(f"Error: Simulation '{args.sim_id}' already exists", file=sys.stderr)
        return 1

    engine = SimulationEngine(args.sim_id, kb_loader, sim_dir)
    engine.load()

    imported = []
    if args.bootstrap:
        for raw_entry in args.bootstrap.split(","):
            entry = raw_entry.strip()
            if not entry:
                continue
            item_id, qty, unit = _parse_bootstrap_entry(entry)
            result = engine.import_item(item_id, qty, unit)
            if not result.get("success"):
                print(f"✗ Failed to import {item_id}: {result.get('message', 'Unknown error')}", file=sys.stderr)
                return 1
            imported.append((item_id, qty, unit))

    engine.save()

    print(f"✓ Created simulation '{args.sim_id}'")
    print(f"  Location: {engine.sim_dir}")
    print(f"  Snapshot: {engine.snapshot_file}")
    print(f"  Events: {engine.event_log_file}")
    if imported:
        print("  Imported:")
        for item_id, qty, unit in imported:
            print(f"    - {item_id}: {qty} {unit}")
    return 0


def cmd_build_machine(args, kb_loader: KBLoader):
    """Build a machine from its BOM."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    result = engine.build_machine(args.machine)

    if result['success']:
        print(f"✓ Built machine '{args.machine}'")
        components = result.get('components_consumed', {})
        print(f"  Parts consumed: {len(components)}")
        for item_id, qty_str in components.items():
            print(f"    - {item_id}: {qty_str}")
        engine.save()
        return 0
    else:
        print(f"✗ Failed to build machine: {result.get('message', 'Unknown error')}", file=sys.stderr)
        if 'missing_parts' in result:
            print("\nMissing parts:", file=sys.stderr)
            for part_id, qty, unit in result['missing_parts']:
                print(f"  - {part_id}: need {qty} {unit}", file=sys.stderr)
        return 1


def cmd_preview(args, kb_loader: KBLoader):
    """Preview simulation state after time advancement."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    current_time = engine.state.current_time_hours
    result = engine.preview_step(args.hours)

    print(f"=== Preview: +{args.hours} hours ===")
    print(f"Current time: {current_time:.2f} hours")
    print(f"After advance: {result['new_time']:.2f} hours")

    if result.get('processes_completing'):
        print(f"\nProcesses completing ({result['completing_count']}):")
        for proc in result['processes_completing']:
            print(f"  - {proc['process_id']} (at {proc['ends_at']:.2f}h)")
            if proc.get('outputs'):
                for item_id, item_info in proc['outputs'].items():
                    print(f"      → {item_id}: {item_info['quantity']:.2f} {item_info['unit']}")
    else:
        print("\nNo processes completing")

    return 0


def cmd_advance_time(args, kb_loader: KBLoader):
    """Advance simulation time."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)

    result = engine.advance_time(args.hours)
    global _LAST_ADVANCE_RESULT
    _LAST_ADVANCE_RESULT = result

    _emit(f"✓ Advanced time by {args.hours} hours", _COLOR_SUCCESS)
    _emit_kv("  New time:", f"{result['new_time']:.2f} hours ({result['new_time']/24:.1f} days)", _COLOR_TIME)
    _emit_kv("  Processes completed:", f"{result['completed_count']}")
    _emit_kv("  Total energy consumed:", f"{result['total_energy_kwh']:.2f} kWh", _COLOR_ENERGY)

    if result['completed']:
        _emit("\nCompleted processes:", _COLOR_NOTE)
        for proc in result['completed']:
            _emit(f"  - {proc['process_id']} (energy: {proc.get('energy_kwh', 0.0):.2f} kWh)")
            if proc.get('outputs'):
                output_units = {}
                process_model = kb_loader.get_process(proc["process_id"])
                if process_model:
                    process_def = process_model.model_dump() if hasattr(process_model, "model_dump") else process_model
                    for outp in process_def.get("outputs", []):
                        output_units[outp.get("item_id")] = outp.get("unit", "unit")
                for item_id, inv_item in proc['outputs'].items():
                    if isinstance(inv_item, (int, float)):
                        qty = float(inv_item)
                        unit = output_units.get(item_id, "unit")
                    else:
                        qty = inv_item.quantity if hasattr(inv_item, 'quantity') else inv_item['quantity']
                        unit = inv_item.unit if hasattr(inv_item, 'unit') else inv_item['unit']
                    _emit(f"      → {item_id}: {qty:.2f} {unit}")

    engine.save()
    return 0


def cmd_provenance(args, kb_loader: KBLoader):
    """Show provenance breakdown for simulation inventory."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)
    state = engine.get_state_dict()
    converter = UnitConverter(kb_loader)

    # Handle JSON output
    if hasattr(args, 'json') and args.json:
        output = {
            "sim_id": args.sim_id,
            "overall": {},
            "items": {}
        }

        total_in_situ, total_imported, total_unknown = 0.0, 0.0, 0.0
        for item_id, prov_dict in state.get('provenance', {}).items():
            in_situ = prov_dict.get('in_situ_kg', 0.0)
            imported = prov_dict.get('imported_kg', 0.0)
            unknown = prov_dict.get('unknown_kg', 0.0)
            total_in_situ += in_situ
            total_imported += imported
            total_unknown += unknown

            item_total = in_situ + imported + unknown
            if item_total > 0:
                output["items"][item_id] = {
                    "total_kg": item_total,
                    "in_situ_kg": in_situ,
                    "imported_kg": imported,
                    "unknown_kg": unknown,
                    "isru_percent": (in_situ / item_total * 100)
                }

        overall_total = total_in_situ + total_imported + total_unknown
        if overall_total > 0:
            output["overall"] = {
                "total_kg": overall_total,
                "in_situ_kg": total_in_situ,
                "imported_kg": total_imported,
                "unknown_kg": total_unknown,
                "isru_percent": (total_in_situ / overall_total * 100)
            }

        print(json.dumps(output, indent=2))
        return 0

    # Calculate overall provenance
    total_in_situ, total_imported, total_unknown = 0.0, 0.0, 0.0
    item_provenance = []

    for item_id, prov_dict in state.get('provenance', {}).items():
        in_situ = prov_dict.get('in_situ_kg', 0.0)
        imported = prov_dict.get('imported_kg', 0.0)
        unknown = prov_dict.get('unknown_kg', 0.0)

        total_in_situ += in_situ
        total_imported += imported
        total_unknown += unknown

        item_total = in_situ + imported + unknown
        if item_total > 0:
            item_provenance.append({
                'item_id': item_id,
                'total': item_total,
                'in_situ': in_situ,
                'imported': imported,
                'unknown': unknown,
                'isru_pct': (in_situ / item_total * 100) if item_total > 0 else 0
            })

    overall_total = total_in_situ + total_imported + total_unknown
    overall_isru_pct = (total_in_situ / overall_total * 100) if overall_total > 0 else 0

    # Display results
    _emit(f"=== Provenance: {args.sim_id} ===", _COLOR_INFO)

    if overall_total > 0:
        _emit_kv("Overall ISRU:",
                f"{overall_isru_pct:.1f}% ({total_in_situ:.2f} kg in-situ, {total_imported:.2f} kg imported)",
                _COLOR_SUCCESS if overall_isru_pct >= 50 else _COLOR_WARN)
    else:
        _emit("No provenance data available", _COLOR_NOTE)
        return 0

    # Filter or show specific item
    if hasattr(args, 'item') and args.item:
        matching = [p for p in item_provenance if p['item_id'] == args.item]
        if not matching:
            _emit(f"\nItem '{args.item}' not found in provenance data", _COLOR_ERROR, is_error=True)
            return 1

        item = matching[0]
        _emit(f"\n=== Item: {item['item_id']} ===", _COLOR_NOTE)
        _emit_kv("Total mass:", f"{item['total']:.2f} kg")

        bar_width = 40
        in_situ_bars = int(item['isru_pct'] / 100 * bar_width)
        imported_bars = bar_width - in_situ_bars
        bar = "█" * in_situ_bars + "░" * imported_bars

        _emit(f"  In-situ:  {item['in_situ']:8.2f} kg ({item['isru_pct']:5.1f}%) {_color(bar, _COLOR_SUCCESS)}")
        _emit(f"  Imported: {item['imported']:8.2f} kg ({100-item['isru_pct']:5.1f}%)")
        if item['unknown'] > 0:
            _emit(f"  Unknown:  {item['unknown']:8.2f} kg")

        return 0

    # Show summary table
    _emit(f"\nTop Items by Mass:", _COLOR_NOTE)

    # Sort by total mass
    item_provenance.sort(key=lambda x: x['total'], reverse=True)

    # Show top 10 items
    for item in item_provenance[:10]:
        isru_pct = item['isru_pct']
        bar_width = 20
        bar_filled = int(isru_pct / 100 * bar_width)
        bar = "█" * bar_filled + "░" * (bar_width - bar_filled)

        color = _COLOR_SUCCESS if isru_pct >= 80 else (_COLOR_WARN if isru_pct >= 50 else _COLOR_DIM)
        _emit(f"  {item['item_id']:40s} {item['total']:9.2f} kg  {isru_pct:5.1f}% {_color(bar, color)}")

    if len(item_provenance) > 10:
        _emit(f"  ... and {len(item_provenance) - 10} more items", _COLOR_DIM)

    # Show items with partial ISRU (opportunities for improvement)
    partial_isru = [p for p in item_provenance if 0 < p['isru_pct'] < 100]
    if partial_isru and not (hasattr(args, 'item') and args.item):
        _emit(f"\nItems with Mixed Provenance ({len(partial_isru)} items):", _COLOR_NOTE)
        for item in partial_isru[:5]:
            _emit(f"  {item['item_id']:40s} {item['total']:6.2f} kg  ({item['in_situ']:.2f} in-situ, {item['imported']:.2f} imported)")
        if len(partial_isru) > 5:
            _emit(f"  ... and {len(partial_isru) - 5} more", _COLOR_DIM)

    return 0


def cmd_status(args, kb_loader: KBLoader):
    """Show simulation metadata summary."""
    engine = load_or_create_simulation(args.sim_id, kb_loader)
    state = engine.get_state_dict()
    schedule = engine.get_schedule_summary()
    converter = UnitConverter(kb_loader)

    def summarize_mass(
        items: Dict[str, Dict[str, Any]]
    ) -> tuple[float, int]:
        total_mass = 0.0
        unknown_mass_count = 0
        for item_id, inv in items.items():
            qty = inv.get("quantity", 0.0)
            unit = inv.get("unit")
            if unit == "kg":
                total_mass += qty
                continue
            converted = converter.convert(qty, unit, "kg", item_id)
            if converted is not None:
                total_mass += converted
                continue
            item = kb_loader.get_item(item_id)
            if item:
                item_dict = item.model_dump() if hasattr(item, "model_dump") else item
                item_mass = item_dict.get("mass")
                if item_mass is not None and unit in ("unit", "count"):
                    total_mass += item_mass * qty
                    continue
            unknown_mass_count += 1
        return total_mass, unknown_mass_count

    def summarize_volume(
        items: Dict[str, Dict[str, Any]]
    ) -> tuple[float, int]:
        total_volume = 0.0
        unknown_volume_count = 0
        for item_id, inv in items.items():
            qty = inv.get("quantity", 0.0)
            unit = inv.get("unit")
            if unit in ("m3", "liter", "L"):
                converted = converter.convert(qty, unit, "m3", item_id)
                if converted is not None:
                    total_volume += converted
                else:
                    unknown_volume_count += 1
            else:
                converted = converter.convert(qty, unit, "m3", item_id)
                if converted is not None:
                    total_volume += converted
        return total_volume, unknown_volume_count

    time_hours = state.get("current_time_hours", 0.0)
    days = time_hours / 24.0
    total_energy = state.get("total_energy_kwh", 0.0)

    inventory_count = len(state.get("inventory", {}))
    machines_built_count = len(state.get("machines_built", []))
    imports_count = len(state.get("total_imports", {}))

    import_mass, import_unknown_mass = summarize_mass(state.get("total_imports", {}))
    inventory_mass, inventory_unknown_mass = summarize_mass(state.get("inventory", {}))
    inventory_volume, inventory_unknown_volume = summarize_volume(state.get("inventory", {}))
    inventory_unit_total = 0.0
    for inv in state.get("inventory", {}).values():
        if inv.get("unit") in ("unit", "count"):
            inventory_unit_total += inv.get("quantity", 0.0)

    active_processes = schedule.get("active_processes", len(state.get("active_processes", [])))
    completed_processes = schedule.get("completed_processes", 0)
    queued_events = schedule.get("queued_events", 0)
    active_recipes = schedule.get("active_recipes", 0)
    completed_recipes = schedule.get("completed_recipes", 0)
    next_event_time = schedule.get("next_event_time")

    _emit(f"=== Simulation: {args.sim_id} ===", _COLOR_INFO)
    _emit_kv("Time:", f"{time_hours:.2f} hours ({days:.2f} days)", _COLOR_TIME)
    _emit_kv("Energy:", f"{total_energy:.2f} kWh", _COLOR_ENERGY)
    _emit_kv("Inventory items:", f"{inventory_count}")
    _emit_kv("Machines built:", f"{machines_built_count}")
    _emit_kv("Imports tracked:", f"{imports_count}")
    if import_unknown_mass > 0:
        _emit_kv("Imported mass:", f"~{import_mass:.2f} kg ({import_unknown_mass} unknown)", _COLOR_MASS)
    else:
        _emit_kv("Imported mass:", f"~{import_mass:.2f} kg", _COLOR_MASS)
    if inventory_unknown_mass > 0:
        _emit_kv("Inventory mass:", f"~{inventory_mass:.2f} kg ({inventory_unknown_mass} unknown)", _COLOR_MASS)
    else:
        _emit_kv("Inventory mass:", f"~{inventory_mass:.2f} kg", _COLOR_MASS)
    if inventory_volume > 0 or inventory_unknown_volume > 0:
        if inventory_unknown_volume > 0:
            _emit_kv("Inventory volume:", f"~{inventory_volume:.3f} m3 ({inventory_unknown_volume} unknown)")
        else:
            _emit_kv("Inventory volume:", f"~{inventory_volume:.3f} m3")
    if inventory_unit_total > 0:
        _emit_kv("Inventory count:", f"~{inventory_unit_total:.2f} units")
    _emit_kv("Processes:", f"{active_processes} active, {completed_processes} completed")
    _emit_kv("Recipes:", f"{active_recipes} active, {completed_recipes} completed")
    _emit_kv("Events queued:", f"{queued_events}")
    if next_event_time is None:
        _emit("Next event time: none")
    else:
        _emit_kv("Next event time:", f"{next_event_time:.2f} hours", _COLOR_TIME)
    _emit_kv("Snapshot:", f"{engine.snapshot_file}")
    _emit_kv("Events:", f"{engine.event_log_file}")

    return 0


def cmd_list(args, kb_loader: KBLoader):
    """List all simulations."""
    if not SIMULATIONS_DIR.exists():
        print("No simulations found")
        return 0

    sims = []
    for sim_dir in SIMULATIONS_DIR.iterdir():
        if sim_dir.is_dir():
            snapshot_file = sim_dir / "snapshot.json"
            if snapshot_file.exists():
                sim_time = None
                try:
                    snapshot_data = json.loads(snapshot_file.read_text(encoding="utf-8"))
                    sim_time = snapshot_data.get("state", {}).get("current_time_hours")
                except Exception:
                    sim_time = None
                sims.append({
                    'id': sim_dir.name,
                    'time_hours': sim_time,
                    'path': str(sim_dir)
                })

    if not sims:
        print("No simulations found")
        return 0

    print(f"Found {len(sims)} simulation(s):\n")
    for sim in sorted(sims, key=lambda x: x['id']):
        print(f"  {sim['id']}")
        if sim.get('time_hours') is not None:
            days = sim['time_hours'] / 24.0
            print(f"    Sim time: {sim['time_hours']:.2f} hours ({days:.2f} days)")
        print(f"    Path: {sim['path']}")
        print()

    return 0


def cmd_visualize(args, kb_loader: KBLoader):
    """Generate visualizations for a simulation."""
    from src.simulation.visualize import visualize_simulation
    import os

    sim_dir = SIMULATIONS_DIR / args.sim_id
    log_file = sim_dir / "events.jsonl"

    if not log_file.exists():
        print(f"Error: Simulation '{args.sim_id}' not found", file=sys.stderr)
        return 1

    try:
        if "MPLCONFIGDIR" not in os.environ:
            print(
                "Note: set MPLCONFIGDIR to a writable path if Matplotlib cache errors occur.",
                file=sys.stderr,
            )
        # Determine output directory
        output_dir = None
        if hasattr(args, 'output') and args.output:
            output_dir = Path(args.output)

        # Generate visualizations
        visualize_simulation(sim_dir, output_dir)
        return 0

    except Exception as e:
        print(f"Error generating visualizations: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


# ============================================================================
# Main CLI setup
# ============================================================================

def add_sim_subcommands(subparsers):
    """
    Add simulation subcommands to the main CLI.

    Called from src/cli.py to integrate sim commands.
    """
    sim_parser = subparsers.add_parser(
        'sim',
        help='Simulation commands'
    )

    sim_subparsers = sim_parser.add_subparsers(dest='sim_command', help='Simulation command')

    # init
    init_parser = sim_subparsers.add_parser('init', help='Initialize new simulation')
    init_parser.add_argument('--sim-id', required=True, help='Simulation ID')

    # view-state
    view_parser = sim_subparsers.add_parser('view-state', help='View simulation state')
    view_parser.add_argument('--sim-id', required=True, help='Simulation ID')

    # import
    import_parser = sim_subparsers.add_parser('import', help='Import item from Earth')
    import_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    import_parser.add_argument('--item', required=True, help='Item ID')
    import_parser.add_argument('--quantity', type=float, required=True, help='Quantity')
    import_parser.add_argument('--unit', required=True, help='Unit')
    import_parser.add_argument(
        '--ensure',
        action='store_true',
        help='Import only the missing amount to reach the requested quantity',
    )

    # start-process
    start_parser = sim_subparsers.add_parser('start-process', help='Start a process')
    start_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    start_parser.add_argument('--process', required=True, help='Process ID')
    start_parser.add_argument('--scale', type=float, default=1.0, help='Scale factor')
    start_parser.add_argument('--duration', type=float, help='Duration in hours (optional, will calculate if omitted)')
    start_parser.add_argument('--output-quantity', type=float, help='Desired output quantity (for calculated duration)')
    start_parser.add_argument('--output-unit', type=str, help='Unit for output quantity (for calculated duration)')

    # plan
    plan_parser = sim_subparsers.add_parser('plan', help='Preflight a process or recipe')
    plan_group = plan_parser.add_mutually_exclusive_group(required=True)
    plan_group.add_argument('--process', help='Process ID')
    plan_group.add_argument('--recipe', help='Recipe ID')

    # scaffold
    scaffold_parser = sim_subparsers.add_parser('scaffold', help='Create a simulation with optional bootstrap imports')
    scaffold_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    scaffold_parser.add_argument(
        '--bootstrap',
        help='Comma-separated items to import (item_id[:qty[:unit]])'
    )

    # run-recipe
    recipe_parser = sim_subparsers.add_parser('run-recipe', help='Run a recipe')
    recipe_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    recipe_parser.add_argument('--recipe', required=True, help='Recipe ID')
    recipe_parser.add_argument('--quantity', type=int, default=1, help='Batch quantity')

    # build-machine
    build_parser = sim_subparsers.add_parser('build-machine', help='Build a machine')
    build_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    build_parser.add_argument('--machine', required=True, help='Machine ID')

    # preview
    preview_parser = sim_subparsers.add_parser('preview', help='Preview time advancement')
    preview_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    preview_parser.add_argument('--hours', type=float, required=True, help='Hours to preview')

    # advance-time
    advance_parser = sim_subparsers.add_parser('advance-time', help='Advance simulation time')
    advance_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    advance_parser.add_argument('--hours', type=float, required=True, help='Hours to advance')

    # status
    status_parser = sim_subparsers.add_parser('status', help='Show simulation metadata')
    status_parser.add_argument('--sim-id', required=True, help='Simulation ID')

    # provenance
    provenance_parser = sim_subparsers.add_parser('provenance', help='Show provenance breakdown (ISRU vs imported)')
    provenance_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    provenance_parser.add_argument('--item', help='Show detailed breakdown for specific item')
    provenance_parser.add_argument('--json', action='store_true', help='Output JSON format')

    # list
    list_parser = sim_subparsers.add_parser('list', help='List all simulations')

    # visualize
    visualize_parser = sim_subparsers.add_parser('visualize', help='Generate visualizations')
    visualize_parser.add_argument('--sim-id', required=True, help='Simulation ID')
    visualize_parser.add_argument('--output', help='Output directory for plots (default: sim_dir/plots)')

    # runbook
    runbook_parser = sim_subparsers.add_parser('runbook', help='Run a simulation runbook (Markdown)')
    runbook_parser.add_argument('--file', required=True, help='Runbook markdown file path')
    runbook_parser.add_argument('--dry-run', action='store_true', help='Print commands without executing')
    runbook_parser.add_argument('--continue-on-error', action='store_true', help='Continue after errors')
    runbook_parser.add_argument('--format', choices=['raw', 'story'], default='raw', help='Output format for runbook execution')

    return sim_parser


def run_sim_command(args, kb_loader: KBLoader):
    """
    Execute a simulation command.

    Called from src/cli.py after parsing args.
    """
    if not hasattr(args, 'sim_command') or args.sim_command is None:
        print("Error: No simulation command specified", file=sys.stderr)
        print("Use: python -m src.cli sim <command> --help", file=sys.stderr)
        return 1

    # Dispatch to command handlers
    commands = {
        'init': cmd_init,
        'view-state': cmd_view_state,
        'import': cmd_import,
        'start-process': cmd_start_process,
        'plan': cmd_plan,
        'scaffold': cmd_scaffold,
        'run-recipe': cmd_run_recipe,
        'build-machine': cmd_build_machine,
        'preview': cmd_preview,
        'advance-time': cmd_advance_time,
        'status': cmd_status,
        'provenance': cmd_provenance,
        'list': cmd_list,
        'visualize': cmd_visualize,
        'runbook': cmd_runbook,
    }

    handler = commands.get(args.sim_command)
    if not handler:
        print(f"Error: Unknown simulation command '{args.sim_command}'", file=sys.stderr)
        return 1

    return handler(args, kb_loader)
def _get_display_width() -> int:
    try:
        width = shutil.get_terminal_size((120, 20)).columns
        return max(120, width)
    except Exception:
        return _DISPLAY_WIDTH
