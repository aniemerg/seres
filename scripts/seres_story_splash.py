from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import shutil
import sys
import textwrap

repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

from ascii_overlay.table import Column, Table  # noqa: E402
from src.seres_ascii import library  # noqa: E402


RESET = "\033[0m"


def _palette(enabled: bool) -> dict[str, str]:
    if not enabled:
        return {key: "" for key in ["cyan", "blue", "yellow", "white", "gray", "dark_gray", "dim", "green", "magenta", "purple"]}
    return {
        "cyan": "\033[96m",
        "blue": "\033[94m",
        "yellow": "\033[93m",
        "white": "\033[97m",
        "gray": "\033[90m",
        "dark_gray": "\033[37m",
        "dim": "\033[2m",
        "green": "\033[32m",
        "magenta": "\033[95m",
        "purple": "\033[35m",
    }


def _colorize(text: str, color: str, palette: dict[str, str]) -> str:
    if not palette[color]:
        return text
    return f"{palette[color]}{text}{RESET}"


def wrap(text: str, width: int) -> list[str]:
    return textwrap.fill(text, width=width).splitlines()


def center_lines(lines: list[str], width: int) -> list[str]:
    return [line.center(width) for line in lines]


def bar(value: float, total: float, width: int = 16, fill: str = "█", empty: str = "░") -> str:
    if total <= 0:
        return empty * width
    filled = max(0, min(width, int(round(value / total * width))))
    return fill * filled + empty * (width - filled)


def box(title: str, lines: list[str], width: int, style: str = "double") -> str:
    inner = width - 2
    if style == "rounded":
        top_left, top_right, horiz, vert = "╭", "╮", "─", "│"
        bot_left, bot_right = "╰", "╯"
    elif style == "single":
        top_left, top_right, horiz, vert = "┌", "┐", "─", "│"
        bot_left, bot_right = "└", "┘"
    else:
        top_left, top_right, horiz, vert = "╔", "╗", "═", "║"
        bot_left, bot_right = "╚", "╝"

    title_line = f" {title} ".ljust(inner, horiz)
    output = [f"{top_left}{title_line}{top_right}"]
    for line in lines:
        output.append(f"{vert}{line.ljust(inner)}{vert}")
    output.append(f"{bot_left}{horiz * inner}{bot_right}")
    return "\n".join(output)


@dataclass
class Stage:
    name: str
    story: str
    time_h: float
    energy_kwh: float
    mass_kg: float
    outputs: list[str]
    complexity: str | None = None
    warning: str | None = None


RUNBOOK = {
    "title": "Reduction Furnace v0",
    "subtitle": "Optimized ISRU",
    "goal": "Build reduction_furnace_v0 with maximum local content by producing major metal components from regolith.",
    "summary": {
        "time_days": 18.0,
        "energy_kwh": 21074.7,
        "isru": 52.4,
        "local_kg": 537.1,
        "imported_kg": 487.9,
    },
    "stages": [
        Stage(
            name="Stage 1: Import fabrication equipment",
            story="Land the starter toolchain and awaken the fab bay.",
            time_h=0.0,
            energy_kwh=0.0,
            mass_kg=3630.0,
            outputs=["tools + fixtures"],
        ),
        Stage(
            name="Stage 2: Regolith → metal feedstock",
            story="Molten regolith electrolysis yields a 1000 kg alloy bank.",
            time_h=320.0,
            energy_kwh=17688.0,
            mass_kg=2815.0,
            outputs=["metal_alloy_bulk +1003.2", "oxygen_gas +668.8"],
            warning="Energy spike: dominant draw of the mission.",
        ),
        Stage(
            name="Stage 3: Reduction furnace shell",
            story="Cast, weld, and sinter the C7 shell.",
            time_h=15.0,
            energy_kwh=2350.0,
            mass_kg=125.0,
            outputs=["reduction_furnace_shell +1", "cast_metal_parts +380"],
            complexity="C7",
        ),
        Stage(
            name="Stage 4: Gas handling system",
            story="Build the exhaust spine and manifolds.",
            time_h=60.0,
            energy_kwh=770.1,
            mass_kg=31.0,
            outputs=["gas_handling_system +1", "machined_part_raw +145"],
            complexity="C7",
        ),
        Stage(
            name="Stage 5: Power bus",
            story="High-current bus for sustained burn.",
            time_h=30.0,
            energy_kwh=266.6,
            mass_kg=3.5,
            outputs=["power_bus_high_current +50"],
            complexity="C7",
        ),
        Stage(
            name="Stage 6: Insulation pack",
            story="Regolith-based insulation stabilizes the core.",
            time_h=6.0,
            energy_kwh=0.0,
            mass_kg=120.0,
            outputs=["insulation_pack_high_temp +1"],
            complexity="C2",
        ),
        Stage(
            name="Stage 7: Import remaining components",
            story="Precision electronics and sensors arrive from orbit.",
            time_h=0.0,
            energy_kwh=0.0,
            mass_kg=220.0,
            outputs=["control_compute_module +1", "sensor_suite_general +1"],
        ),
        Stage(
            name="Stage 8: Final assembly",
            story="Lock the stack and declare operational.",
            time_h=3.0,
            energy_kwh=0.0,
            mass_kg=0.0,
            outputs=["reduction_furnace_v0 +1"],
            complexity="C7",
        ),
    ],
}


def _seres_title(width: int) -> str:
    title = [
        "   _____ ______ _____  ______  _____",
        "  / ____|  ____|  __ \\|  ____|/ ____|",
        " | (___ | |__  | |__) | |__  | (___",
        "  \\___ \\|  __| |  _  /|  __|  \\___ \\",
        "  ____) | |____| | \\ \\| |____ ____) |",
        " |_____/|______|_|  \\_\\______|_____/",
    ]
    max_len = max(len(line) for line in title)
    padded = [line.ljust(max_len) for line in title]
    return "\n".join(line.center(width) for line in padded)


def _color_earthrise_marked(lines: list[str], palette: dict[str, str]) -> str:
    output = []
    star_chars = {"⠄", "⠂", "⠈"}
    for line in lines:
        earth_on = False
        city_on = False
        green_on = False
        yellow_on = False
        rendered = []
        for char in line.rstrip("\n"):
            if char == "*":
                earth_on = not earth_on
                continue
            if char == ",":
                city_on = not city_on
                continue
            if char == "%":
                green_on = not green_on
                continue
            if char == "#":
                yellow_on = not yellow_on
                continue
            if char in star_chars:
                rendered.append(_colorize(char, "white", palette))
                continue
            if yellow_on:
                rendered.append(_colorize(char, "yellow", palette))
                continue
            if green_on:
                rendered.append(_colorize(char, "green", palette))
                continue
            if city_on:
                rendered.append(_colorize(char, "dark_gray", palette))
                continue
            if earth_on:
                rendered.append(_colorize(char, "blue", palette))
                continue
            rendered.append(char)
        output.append("".join(rendered))
    return "\n".join(output)


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


def _stage_lines(stage: Stage) -> list[str]:
    return [
        f"{stage.name}",
        f"  {stage.story}",
        f"  MADE: {', '.join(stage.outputs)}",
        f"  Cx {stage.complexity or 'C1'}  Δt {stage.time_h:.1f}h  ΔE {stage.energy_kwh:.1f} kWh  Δm {stage.mass_kg:.1f} kg",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="SERES story splash output")
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI colors")
    args = parser.parse_args()

    palette = _palette(not args.no_color)
    width = shutil.get_terminal_size((120, 40)).columns

    earthrise_path = repo_root / "design" / "earthrise_marked_2.txt"
    earthrise_lines = earthrise_path.read_text().splitlines()

    top_banner = library.render_art("banner_seres_moonseed")
    top = "\n".join(
        [
            _colorize(top_banner, "magenta", palette),
            "",
            _colorize(_seres_title(width), "white", palette),
        ]
    )

    narrative = box(
        "SCENARIO",
        wrap(RUNBOOK["goal"], min(88, width - 8))
        + ["", "Story arc: import → refine → fabricate → assemble."],
        width=min(92, width - 6),
        style="double",
    )

    earthrise = _color_earthrise_marked(earthrise_lines, palette)

    target_box = box(
        "TARGET // reduction_furnace_v0",
        _furnace_art().splitlines(),
        width=40,
        style="rounded",
    )

    steps_header = _colorize("STAGE FLOW", "cyan", palette)
    steps = [steps_header]
    for stage in RUNBOOK["stages"]:
        lines = _stage_lines(stage)
        if stage.warning:
            lines.append(_colorize(f"  ⚠ {stage.warning}", "yellow", palette))
        lines.append(f"  t {bar(stage.time_h, 320.0, 18)}  E {bar(stage.energy_kwh, 21074.7, 18)}  m {bar(stage.mass_kg, 3630.0, 18)}")
        stage_title = _colorize(stage.name.split(":")[0], "magenta", palette)
        steps.append(box(stage_title, lines[1:], width=min(92, width - 6), style="single"))
    steps_block = "\n\n".join(steps)

    summary = RUNBOOK["summary"]
    summary_table = Table(
        columns=[Column(name="MISSION COMPLETE", align="center", width=40)],
        rows=[
            ["PRIMARY OUTPUT: reduction_furnace_v0  (C7)"],
            [f"ISRU {summary['isru']:.1f}%  {bar(summary['isru'], 100, 22)}"],
            [f"TIME {summary['time_days']:.1f} days   ENERGY {summary['energy_kwh']:.1f} kWh"],
            [f"LOCAL {summary['local_kg']:.1f} kg | IMPORT {summary['imported_kg']:.1f} kg"],
        ],
        title=_colorize("MISSION COMPLETE", "green", palette),
        header=False,
    )
    footer = "\n".join(summary_table.render())

    layout = [
        top,
        "",
        _colorize(narrative, "magenta", palette),
        "",
        earthrise,
        "",
        _colorize(target_box, "green", palette),
        "",
        steps_block,
        "",
        _colorize(footer, "green", palette),
    ]

    print("\n".join(layout))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
