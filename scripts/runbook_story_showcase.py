from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import shutil
import sys
import textwrap

repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

from src.seres_ascii import library  # noqa: E402


RESET = "\033[0m"


def _palette(enabled: bool) -> dict[str, str]:
    if not enabled:
        return {key: "" for key in ["cyan", "magenta", "yellow", "green", "blue", "white", "dim", "red"]}
    return {
        "cyan": "\033[96m",
        "magenta": "\033[95m",
        "yellow": "\033[93m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "white": "\033[97m",
        "dim": "\033[2m",
        "red": "\033[91m",
    }


def colorize(text: str, color: str, palette: dict[str, str]) -> str:
    if not palette[color]:
        return text
    return f"{palette[color]}{text}{RESET}"


def bar(value: float, total: float, width: int = 16, fill: str = "█", empty: str = "░") -> str:
    if total <= 0:
        return empty * width
    filled = max(0, min(width, int(round(value / total * width))))
    return fill * filled + empty * (width - filled)


def box(title: str, lines: list[str], width: int, style: str = "single") -> str:
    inner = width - 2
    if style == "double":
        top_left, top_right, horiz, vert = "╔", "╗", "═", "║"
        bot_left, bot_right = "╚", "╝"
    elif style == "rounded":
        top_left, top_right, horiz, vert = "╭", "╮", "─", "│"
        bot_left, bot_right = "╰", "╯"
    else:
        top_left, top_right, horiz, vert = "┌", "┐", "─", "│"
        bot_left, bot_right = "└", "┘"

    title_line = f" {title} ".ljust(inner, horiz)
    output = [f"{top_left}{title_line}{top_right}"]
    for line in lines:
        output.append(f"{vert}{line.ljust(inner)}{vert}")
    output.append(f"{bot_left}{horiz * inner}{bot_right}")
    return "\n".join(output)


def side_by_side(left: str, right: str, gap: int = 2) -> str:
    left_lines = left.splitlines()
    right_lines = right.splitlines()
    left_width = max((len(line) for line in left_lines), default=0)
    right_width = max((len(line) for line in right_lines), default=0)
    height = max(len(left_lines), len(right_lines))
    spacer = " " * gap
    lines = []
    for i in range(height):
        l = left_lines[i] if i < len(left_lines) else ""
        r = right_lines[i] if i < len(right_lines) else ""
        lines.append(l.ljust(left_width) + spacer + r.ljust(right_width))
    return "\n".join(lines)


def wrap(text: str, width: int) -> list[str]:
    return textwrap.fill(text, width=width).splitlines()


def center_lines(lines: list[str], width: int) -> list[str]:
    return [line.center(width) for line in lines]


def sparkline(values: list[float]) -> str:
    ticks = "▁▂▃▄▅▆▇█"
    if not values:
        return ""
    min_v = min(values)
    max_v = max(values)
    span = max(max_v - min_v, 1e-6)
    chars = []
    for value in values:
        idx = int((value - min_v) / span * (len(ticks) - 1))
        chars.append(ticks[idx])
    return "".join(chars)


@dataclass
class Stage:
    name: str
    story: str
    time_h: float
    energy_kwh: float
    mass_kg: float
    key: list[str] | None = None
    outputs: list[str] | None = None
    warning: str | None = None
    complexity: str | None = None


RUNBOOK = {
    "title": "Reduction Furnace v0",
    "subtitle": "v2 - Optimized ISRU",
    "goal": "Build reduction_furnace_v0 with maximum ISRU by producing major metal components from regolith.",
    "mission": "Import core tooling, smelt local feedstock, fabricate subassemblies, and lock in a C7-class furnace.",
    "summary": {
        "time_days": 18.0,
        "energy_kwh": 21074.7,
        "isru": 52.4,
        "local_kg": 537.1,
        "imported_kg": 487.9,
    },
    "stages": [
        Stage(
            name="Stage 1 // Import fabrication equipment",
            story="Land the starter toolchain and boot up the fab bay.",
            time_h=0.0,
            energy_kwh=0.0,
            mass_kg=3630.0,
            key=["assembly_tools_basic", "casting_mold_set", "crucible_refractory", "hot_press_v0"],
        ),
        Stage(
            name="Stage 2 // Regolith → metal feedstock",
            story="Molten regolith electrolysis at scale to bank 1000 kg of alloy.",
            time_h=320.0,
            energy_kwh=17688.0,
            mass_kg=2815.0,
            outputs=["metal_alloy_bulk +1003.2", "oxygen_gas +668.8"],
            warning="Energy spike: this stage dominates the total burn.",
        ),
        Stage(
            name="Stage 3 // Furnace shell (local)",
            story="Cast and weld the primary shell — first big local win.",
            time_h=15.0,
            energy_kwh=2350.0,
            mass_kg=125.0,
            outputs=["reduction_furnace_shell +1", "welded_assemblies +375", "cast_metal_parts +380"],
            complexity="C7",
        ),
        Stage(
            name="Stage 4 // Gas handling (local)",
            story="Build the exhaust spine and manifolds.",
            time_h=60.0,
            energy_kwh=770.1,
            mass_kg=31.0,
            outputs=["gas_handling_system +1", "machined_part_raw +145", "cast_metal_parts +150"],
            complexity="C7",
        ),
        Stage(
            name="Stage 5 // Power bus (local)",
            story="High-current bus set for sustained burn.",
            time_h=30.0,
            energy_kwh=266.6,
            mass_kg=3.5,
            outputs=["power_bus_high_current +50", "machined_part_raw +50", "cast_metal_parts +52"],
            complexity="C7",
        ),
        Stage(
            name="Stage 6 // Insulation pack",
            story="Regolith-based insulation to stabilize the core.",
            time_h=6.0,
            energy_kwh=0.0,
            mass_kg=120.0,
            outputs=["insulation_pack_high_temp +1"],
            complexity="C2",
        ),
        Stage(
            name="Stage 7 // Import remaining components",
            story="Bring in electronics and precision parts.",
            time_h=0.0,
            energy_kwh=0.0,
            mass_kg=220.0,
            key=["control_compute_module_imported", "cooling_loop_basic", "sensor_suite_general"],
        ),
        Stage(
            name="Stage 8 // Final assembly",
            story="Lock the stack, validate the furnace, declare operational.",
            time_h=3.0,
            energy_kwh=0.0,
            mass_kg=0.0,
            outputs=["reduction_furnace_v0 +1"],
            complexity="C7",
        ),
    ],
}


def c7_crest() -> str:
    return "\n".join(
        [
            "      ┌──────────┐",
            "      │  C7 CORE │",
            "      ├──────────┤",
            "      │ COMPLEX  │",
            "      │  FORGE   │",
            "      └──────────┘",
        ]
    )


def style_briefing(palette: dict[str, str]) -> str:
    header = colorize("SERES // RUNBOOK STORY BRIEF", "cyan", palette)
    banner = library.render_art("banner_seres_moonseed")
    goal_lines = wrap(RUNBOOK["goal"], 56)
    mission_lines = wrap(RUNBOOK["mission"], 56)

    left_panel = box(
        "MISSION OBJECTIVE",
        goal_lines + [""] + mission_lines,
        width=64,
        style="double",
    )

    summary = RUNBOOK["summary"]
    summary_lines = [
        f"ISRU:   {summary['isru']:.1f}%   [{bar(summary['isru'], 100, 18)}]",
        f"TIME:   {summary['time_days']:.1f} days",
        f"ENERGY: {summary['energy_kwh']:.1f} kWh",
        f"LOCAL:  {summary['local_kg']:.1f} kg",
        f"IMPORT: {summary['imported_kg']:.1f} kg",
    ]

    right_panel = box(
        "MISSION SUMMARY",
        summary_lines + [""] + c7_crest().splitlines(),
        width=46,
        style="double",
    )

    arc_lines = []
    for idx, stage in enumerate(RUNBOOK["stages"], 1):
        marker = f"{idx:02d}"
        arc_lines.append(f"◉ {marker} {stage.name.split('//')[-1].strip()}")
        arc_lines.append(f"  {stage.story}")
        if stage.warning:
            arc_lines.append(colorize(f"  WARNING: {stage.warning}", "red", palette))
        arc_lines.append("")
    arc_box = box("STORY ARC", arc_lines[:-1], width=112, style="double")

    art = colorize(library.render_art("scene_orbital_yard"), "blue", palette)
    top = "\n".join([banner, "", header, ""])
    side = side_by_side(left_panel, right_panel, gap=4)
    return "\n".join([top, side, "", arc_box, "", art])


def style_timeline(palette: dict[str, str]) -> str:
    title = colorize("SIMULATOR // STORY MODE — TIMELINE", "magenta", palette)
    gutter = library.render_art("gutter_orbit")
    timeline_lines = []
    for stage in RUNBOOK["stages"]:
        timeline_lines.append(f"┌─ {stage.name}")
        timeline_lines.append(f"│  {stage.story}")
        if stage.outputs:
            timeline_lines.append("│  OUTPUTS:")
            for item in stage.outputs[:3]:
                timeline_lines.append(f"│   • {item}")
        if stage.key:
            timeline_lines.append("│  KEY IMPORTS:")
            for item in stage.key[:3]:
                timeline_lines.append(f"│   • {item}")
        timeline_lines.append(
            f"│  Δt {stage.time_h:.1f}h  ΔE {stage.energy_kwh:.1f} kWh  Δm {stage.mass_kg:.1f} kg"
        )
        if stage.complexity:
            timeline_lines.append(f"│  COMPLEXITY: {stage.complexity}")
        timeline_lines.append("└──────────────────────────────────────────────────────────────")
        timeline_lines.append("")
    timeline = "\n".join(timeline_lines)
    left = colorize(gutter, "blue", palette)
    right = colorize(timeline, "white", palette)
    return "\n".join([title, "", side_by_side(left, right, gap=3)])


def style_schematic(palette: dict[str, str]) -> str:
    title = colorize("SERES // FABRICATION SCHEMATIC", "yellow", palette)
    pipeline = library.render_art("pipeline_seres")
    outpost = library.render_art("scene_seres_outpost")
    dependency = "\n".join(
        [
            "DEPENDENCY TRACE",
            "  regolith",
            "    ├─ MRE → metal_alloy_bulk",
            "    ├─ cast_metal_parts",
            "    ├─ machined_part_raw",
            "    └─ welded_assemblies",
            "      └─ reduction_furnace_shell  [C7]",
            "      └─ gas_handling_system      [C7]",
            "      └─ power_bus_high_current   [C7]",
        ]
    )
    energy_focus = "\n".join(
        [
            "ENERGY SIGNATURE",
            f"  Stage 2: {bar(17688.0, 21074.7, 26)}  17.7 MWh",
            f"  Total  : {bar(21074.7, 21074.7, 26)}  21.1 MWh",
            "  Note: MRE dominates; schedule during peak power windows.",
        ]
    )
    assembly = "\n".join(
        [
            "FINAL ASSEMBLY",
            "  reduction_furnace_v0 [C7]",
            "  ISRU: 52.4%  (LOCAL 537.1 kg | IMPORT 487.9 kg)",
            "  STATUS: OPERATIONAL ✓",
        ]
    )
    left = colorize(pipeline, "cyan", palette)
    mid = colorize(dependency + "\n\n" + energy_focus, "white", palette)
    right = colorize(outpost + "\n" + assembly, "green", palette)
    return "\n".join([title, "", side_by_side(side_by_side(left, mid, gap=4), right, gap=4)])


def style_broadcast(palette: dict[str, str]) -> str:
    title = colorize("SERES // ORBITAL BROADCAST", "cyan", palette)
    skyline = colorize(library.render_art("scene_orbital_yard"), "blue", palette)
    banner = colorize(library.render_art("banner_seres_console"), "magenta", palette)
    scanline = colorize("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»", "dim", palette)

    headline = [
        "MISSION FEED: reduction_furnace_v0 v2",
        "BREAKING: ISRU passes 50% threshold — local fabrication confirmed.",
        "FORECAST: final assembly window opens at T+18.0d.",
    ]
    headline_box = box("HEADLINES", headline, width=78, style="double")

    ticker = [
        "STAGE 2 MRE: 17.7 MWh | METAL ALLOY +1003.2 | O2 +668.8",
        "STAGE 3 C7 SHELL: cast + weld + sinter",
        "STAGE 8 FINAL: reduction_furnace_v0 operational ✓",
    ]
    ticker_box = box("TICKER", ticker, width=78, style="single")

    return "\n".join([title, banner, scanline, headline_box, ticker_box, scanline, skyline])


def style_ledger(palette: dict[str, str]) -> str:
    title = colorize("SERES // MANUFACTURING LEDGER", "yellow", palette)
    divider = colorize("─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─", "dim", palette)
    columns = [
        "STEP",
        "FOCUS",
        "OUTPUT",
        "C",
        "Δt",
        "ΔE",
    ]
    header = " | ".join(f"{col:<14}" for col in columns)
    rows = []
    for idx, stage in enumerate(RUNBOOK["stages"], 1):
        focus = stage.name.split("//")[-1].strip()
        output = (stage.outputs[0] if stage.outputs else "imports staged")
        complexity = stage.complexity or "-"
        rows.append(
            f"{idx:02d} | {focus:<14} | {output:<18} | {complexity:<2} | {stage.time_h:>4.0f}h | {stage.energy_kwh:>6.1f}"
        )
    body = "\n".join(rows)
    footer = "C7 CORE: shell + gas + power + final assembly"
    return "\n".join([title, divider, header, divider, body, divider, footer])


def style_comic(palette: dict[str, str]) -> str:
    title = colorize("SERES // COMIC STRIP", "magenta", palette)
    panels = []
    panels.append(
        box(
            "PANEL 1 — ARRIVAL",
            wrap("We land with a lean toolkit. The fab bay lights up.", 40)
            + ["", "Tools staged: assembly, casting, hot press."],
            width=52,
            style="rounded",
        )
    )
    panels.append(
        box(
            "PANEL 2 — MRE FIRE",
            wrap("Regolith melts. Alloy pours. Oxygen vents shimmer.", 40)
            + ["", "Energy spike: 17.7 MWh"],
            width=52,
            style="rounded",
        )
    )
    panels.append(
        box(
            "PANEL 3 — C7 FORGE",
            wrap("Shell, gas, and power bus assemble into a C7 stack.", 40)
            + ["", "Core output: reduction_furnace_shell"],
            width=52,
            style="rounded",
        )
    )
    panels.append(
        box(
            "PANEL 4 — OPERATIONAL",
            wrap("Final assembly locks. Furnace goes live.", 40)
            + ["", "ISRU 52.4% ✓"],
            width=52,
            style="rounded",
        )
    )
    row1 = side_by_side(panels[0], panels[1], gap=4)
    row2 = side_by_side(panels[2], panels[3], gap=4)
    art = colorize(library.render_art("scene_bot_upgrade"), "green", palette)
    return "\n".join([title, row1, "", row2, "", art])


def style_dense_matrix(palette: dict[str, str]) -> str:
    title = colorize("SERES // DENSE OPS MATRIX", "cyan", palette)
    grid = [
        "┌───────────┬───────────────┬───────────────┬───────────────┐",
        "│ STAGE     │ OUTPUT        │ ENERGY        │ STORY         │",
        "├───────────┼───────────────┼───────────────┼───────────────┤",
    ]
    for idx, stage in enumerate(RUNBOOK["stages"], 1):
        output = stage.outputs[0] if stage.outputs else "imports staged"
        energy = f"{stage.energy_kwh:>6.1f} kWh"
        story = stage.story[:26]
        grid.append(
            f"│ {idx:02d}        │ {output:<13} │ {energy:<13} │ {story:<13} │"
        )
    grid.append("└───────────┴───────────────┴───────────────┴───────────────┘")

    status = [
        f"ISRU {RUNBOOK['summary']['isru']:.1f}%  {bar(RUNBOOK['summary']['isru'], 100, 24)}",
        f"TIME {RUNBOOK['summary']['time_days']:.1f}d   ENERGY {RUNBOOK['summary']['energy_kwh']:.1f} kWh",
        "C7 CORE: shell + gas + power + final",
    ]
    status_box = box("SYSTEM STATUS", status, width=78, style="double")
    aura = colorize(library.render_art("aura_mid"), "yellow", palette)
    return "\n".join([title, "\n".join(grid), "", status_box, "", aura])


def _furnace_art() -> str:
    return "\n".join(
        [
            "      .-======-.",
            "     /  ____   \\",
            "    |  |====|   |",
            "    |  |    |   |",
            "    |  |____|   |",
            "    |   ____    |",
            "    |  |____|   |",
            "     \\________/",
            "       |    |",
            "      _|____|_",
        ]
    )


def _stage_block(stage: Stage, palette: dict[str, str], width: int) -> str:
    importance = stage.complexity or "-"
    energy_bar = bar(stage.energy_kwh, RUNBOOK["summary"]["energy_kwh"], width=18)
    time_bar = bar(stage.time_h, 320.0, width=18)
    mass_bar = bar(stage.mass_kg, 3630.0, width=18)
    lines = [
        f"{stage.name}",
        f"  {stage.story}",
        f"  Cx: {importance}   Δt {stage.time_h:.1f}h  {time_bar}",
        f"  ΔE {stage.energy_kwh:.1f} kWh  {energy_bar}",
        f"  Δm {stage.mass_kg:.1f} kg   {mass_bar}",
    ]
    if stage.outputs:
        outputs = ", ".join(stage.outputs[:2])
        lines.append(f"  MADE: {outputs}")
    if stage.warning:
        lines.append(colorize(f"  ⚠ {stage.warning}", "red", palette))
    return "\n".join(center_lines(lines, width))


def style_splashflow(palette: dict[str, str]) -> str:
    width = shutil.get_terminal_size((120, 40)).columns
    title = [
        "███████╗ ███████╗ ██████╗ ███████╗ ███████╗",
        "██╔════╝ ██╔════╝ ██╔══██╗██╔════╝ ██╔════╝",
        "███████╗ █████╗   ██████╔╝█████╗   ███████╗",
        "╚════██║ ██╔══╝   ██╔══██╗██╔══╝   ╚════██║",
        "███████║ ███████╗██║  ██║███████╗ ███████║",
        "╚══════╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚══════╝",
    ]
    header = "\n".join(center_lines(title, width))
    narrative = wrap(
        "We are running Reduction Furnace v0 in story mode: import core tools, "
        "push molten regolith to alloy, fabricate C7 subassemblies, and lock a high-ISRU furnace.",
        min(96, width - 8),
    )
    narrative_block = box("NARRATIVE", narrative, width=min(96, width - 4), style="double")
    target = box(
        "TARGET // reduction_furnace_v0",
        _furnace_art().splitlines(),
        width=40,
        style="rounded",
    )
    star = library.render_art("aura_mid")
    target_block = side_by_side(colorize(star, "yellow", palette), colorize(target, "green", palette), gap=4)

    steps = []
    steps.append(colorize("STAGE FLOW", "cyan", palette))
    for stage in RUNBOOK["stages"]:
        block = _stage_block(stage, palette, width=min(96, width - 8))
        steps.append(block)
        steps.append("")
    steps_text = "\n".join(steps).rstrip()

    summary = RUNBOOK["summary"]
    summary_lines = [
        "SUCCESS // CORE FURNACE ONLINE",
        f"ISRU {summary['isru']:.1f}%  {bar(summary['isru'], 100, 22)}",
        f"TIME {summary['time_days']:.1f} days   ENERGY {summary['energy_kwh']:.1f} kWh",
        f"LOCAL {summary['local_kg']:.1f} kg | IMPORT {summary['imported_kg']:.1f} kg",
        "PRIMARY OUTPUT: reduction_furnace_v0  (C7)",
    ]
    footer = box("MISSION COMPLETE", summary_lines, width=min(96, width - 4), style="double")

    return "\n".join(
        [
            colorize(header, "white", palette),
            "",
            colorize(narrative_block, "magenta", palette),
            "",
            target_block,
            "",
            steps_text,
            "",
            colorize(footer, "green", palette),
        ]
    )


def style_starlog(palette: dict[str, str]) -> str:
    width = shutil.get_terminal_size((120, 40)).columns
    splash = center_lines(["┏━━━━━━━━ SERES ━━━━━━━━┓", "┃ ORBITAL LOGBOOK v2   ┃", "┗━━━━━━━━━━━━━━━━━━━━━━┛"], width)
    narrative = wrap(
        "Objective: maximize ISRU for reduction_furnace_v0. The logbook records every burn, every cast, every assembly.",
        min(88, width - 6),
    )
    narrative_block = box("LOGBOOK BRIEF", narrative, width=min(88, width - 6), style="rounded")

    target_art = _furnace_art().splitlines()
    try:
        starfield = library.render_art("stars_field")
    except KeyError:
        starfield = "   .    *        .   *    .      *\n      *    .  *       .        *\n  *        .     *         .      *\n     .  *     .     *   .     *\n   *      .       *    .   *     ."
    target = box("TARGET ITEM", target_art, width=34, style="double")
    target_block = side_by_side(colorize(starfield, "blue", palette), colorize(target, "green", palette), gap=4)

    energy_series = [s.energy_kwh for s in RUNBOOK["stages"]]
    time_series = [s.time_h for s in RUNBOOK["stages"]]
    mass_series = [s.mass_kg for s in RUNBOOK["stages"]]
    metrics = [
        f"ENERGY {sparkline(energy_series)}",
        f"TIME   {sparkline(time_series)}",
        f"MASS   {sparkline(mass_series)}",
    ]
    metrics_box = box("SPARKLINES", metrics, width=40, style="single")

    steps_lines = []
    for stage in RUNBOOK["stages"]:
        emphasis = f"[{stage.complexity}]" if stage.complexity else "[C1]"
        steps_lines.append(f"◉ {emphasis} {stage.name.split('//')[-1].strip()}")
        steps_lines.append(f"  Δt {stage.time_h:>5.1f}h  ΔE {stage.energy_kwh:>7.1f} kWh  Δm {stage.mass_kg:>6.1f} kg")
        if stage.outputs:
            steps_lines.append(f"  → MADE {', '.join(stage.outputs[:2])}")
        steps_lines.append("")
    steps_block = box("RUN SEQUENCE", steps_lines[:-1], width=min(96, width - 4), style="double")

    summary = RUNBOOK["summary"]
    success = [
        "FURNACE ONLINE",
        f"ISRU {summary['isru']:.1f}% {bar(summary['isru'], 100, 18)}",
        f"TOTAL {summary['time_days']:.1f}d  {summary['energy_kwh']:.1f} kWh",
        "C7 CORE COMPLETE ✓",
    ]
    success_box = box("SEND-OFF", success, width=44, style="rounded")

    return "\n".join(
        [
            "\n".join(splash),
            "",
            colorize(narrative_block, "magenta", palette),
            "",
            side_by_side(target_block, colorize(metrics_box, "yellow", palette), gap=4),
            "",
            colorize(steps_block, "white", palette),
            "",
            colorize(success_box, "green", palette),
        ]
    )


def style_console_wall(palette: dict[str, str]) -> str:
    width = shutil.get_terminal_size((120, 40)).columns
    splash = center_lines(["╔════════ SERES ════════╗", "║ AUTOFAB COMMAND WALL ║", "╚══════════════════════╝"], width)
    narrative = wrap(
        "Scenario: Build reduction_furnace_v0 with maximum local content. Prioritize C7 subassemblies.",
        min(92, width - 6),
    )
    narrative_block = box("SCENARIO", narrative, width=min(92, width - 6), style="double")

    target = box("TARGET", _furnace_art().splitlines(), width=28, style="double")
    pipeline = library.render_art("pipeline_seres")
    target_block = side_by_side(colorize(target, "green", palette), colorize(pipeline, "cyan", palette), gap=4)

    steps = []
    for stage in RUNBOOK["stages"]:
        importance = stage.complexity or "C1"
        tag = f"{importance}".rjust(2)
        line = f"{tag} ▸ {stage.name.split('//')[-1].strip():<28}  Δt {stage.time_h:>5.1f}h  ΔE {stage.energy_kwh:>7.1f}"
        steps.append(line)
        bars = f"    t {bar(stage.time_h, 320.0, 14)}  E {bar(stage.energy_kwh, 21074.7, 14)}  m {bar(stage.mass_kg, 3630.0, 14)}"
        steps.append(bars)
        if stage.outputs:
            steps.append(f"    MADE {stage.outputs[0]}")
        if stage.warning:
            steps.append(colorize(f"    ⚠ {stage.warning}", "red", palette))
    steps_block = box("EXECUTION TRACE", steps, width=min(108, width - 4), style="rounded")

    summary = RUNBOOK["summary"]
    footer_lines = [
        "PRIMARY OUTPUT: reduction_furnace_v0",
        f"ISRU {summary['isru']:.1f}% {bar(summary['isru'], 100, 22)}",
        f"TIME {summary['time_days']:.1f}d  ENERGY {summary['energy_kwh']:.1f} kWh",
        "LOCAL 537.1 kg | IMPORT 487.9 kg",
    ]
    footer = box("SUCCESS // SYSTEM GREEN", footer_lines, width=min(92, width - 6), style="double")

    return "\n".join(
        [
            "\n".join(splash),
            "",
            colorize(narrative_block, "magenta", palette),
            "",
            target_block,
            "",
            colorize(steps_block, "white", palette),
            "",
            colorize(footer, "green", palette),
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Runbook story UI mockups")
    parser.add_argument(
        "--style",
        choices=[
            "briefing",
            "timeline",
            "schematic",
            "broadcast",
            "ledger",
            "comic",
            "dense",
            "splashflow",
            "starlog",
            "console",
            "all",
        ],
        default="all",
        help="Which layout to render",
    )
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI colors")
    args = parser.parse_args()

    palette = _palette(not args.no_color)
    width = shutil.get_terminal_size((120, 40)).columns

    outputs = []
    if args.style in ("briefing", "all"):
        outputs.append(style_briefing(palette))
    if args.style in ("timeline", "all"):
        outputs.append(style_timeline(palette))
    if args.style in ("schematic", "all"):
        outputs.append(style_schematic(palette))
    if args.style in ("broadcast", "all"):
        outputs.append(style_broadcast(palette))
    if args.style in ("ledger", "all"):
        outputs.append(style_ledger(palette))
    if args.style in ("comic", "all"):
        outputs.append(style_comic(palette))
    if args.style in ("dense", "all"):
        outputs.append(style_dense_matrix(palette))
    if args.style in ("splashflow", "all"):
        outputs.append(style_splashflow(palette))
    if args.style in ("starlog", "all"):
        outputs.append(style_starlog(palette))
    if args.style in ("console", "all"):
        outputs.append(style_console_wall(palette))

    divider = "\n" + ("═" * min(width, 120)) + "\n"
    print(divider.join(outputs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
