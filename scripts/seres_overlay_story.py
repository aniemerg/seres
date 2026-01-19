from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import random
import shutil
import sys
import textwrap

repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

from ascii_overlay.core import Config, measure_block, render_overlay  # noqa: E402
from ascii_overlay.table import Column, Table  # noqa: E402
from src.seres_ascii import library  # noqa: E402


RESET = "\033[0m"


def _palette(enabled: bool) -> dict[str, str]:
    if not enabled:
        return {k: "" for k in ["cyan", "yellow", "green", "white", "magenta", "blue", "gray", "purple"]}
    return {
        "cyan": "\033[96m",
        "yellow": "\033[93m",
        "green": "\033[92m",
        "white": "\033[97m",
        "magenta": "\033[95m",
        "blue": "\033[94m",
        "gray": "\033[90m",
        "purple": "\033[35m",
    }


def _color(text: str, color: str, palette: dict[str, str]) -> str:
    if not palette[color]:
        return text
    return f"{palette[color]}{text}{RESET}"


def wrap(text: str, width: int) -> list[str]:
    return textwrap.fill(text, width=width).splitlines()


def bar(value: float, total: float, width: int = 16, fill: str = "█", empty: str = "░") -> str:
    if total <= 0:
        return empty * width
    filled = max(0, min(width, int(round(value / total * width))))
    return fill * filled + empty * (width - filled)


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


def _color_earthrise(lines: list[str], palette: dict[str, str]) -> list[str]:
    star_chars = {"⠄", "⠂", "⠈"}
    output = []
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
                rendered.append(_color(char, "white", palette))
                continue
            if yellow_on:
                rendered.append(_color(char, "yellow", palette))
                continue
            if green_on:
                rendered.append(_color(char, "green", palette))
                continue
            if city_on:
                rendered.append(_color(char, "gray", palette))
                continue
            if earth_on:
                rendered.append(_color(char, "blue", palette))
                continue
            rendered.append(char)
        output.append("".join(rendered))
    return output


def _color_ascii_art(lines: list[str], palette: dict[str, str]) -> list[str]:
    output = []
    for idx, line in enumerate(lines):
        tint = "blue" if idx % 3 == 0 else "cyan"
        colored = _color(line.rstrip("\n"), tint, palette)
        colored = colored.replace("★", _color("★", "yellow", palette))
        output.append(colored)
    return output


def _color_galaxy(lines: list[str], palette: dict[str, str]) -> list[str]:
    star_chars = {"⠄", "⠂", "⠈"}
    rng = random.Random()
    probes = ["⊳", "⊲", "➤"]
    output = []
    for line in lines:
        text = line.rstrip("\n")
        if text.strip() and rng.random() < 0.54:
            candidates = [i for i, ch in enumerate(text) if ch not in {" ", "⠀"}]
            if candidates:
                if len(candidates) > 1 and candidates[0] == 0:
                    candidates = candidates[1:]
                if candidates:
                    idx = rng.choice(candidates)
                    probe = _color(rng.choice(probes), "purple", palette)
                    text = text[:idx] + probe + text[idx + 1 :]
        rendered = []
        for char in text:
            if char in star_chars:
                rendered.append(_color(char, "white", palette))
                continue
            if char in {" ", "⠀"} and rng.random() < 0.015:
                rendered.append(_color("★", "yellow", palette))
                continue
            rendered.append(char)
        output.append("".join(rendered))
    return output


def _scenario_table(palette: dict[str, str]) -> list[str]:
    table = Table(
        columns=[Column(name="", align="left", width=44)],
        rows=[
            [f"{_color('Goal', 'cyan', palette):<8}: reduction_furnace_v0"],
            [f"{_color('Mode', 'cyan', palette):<8}: ISRU-max / story"],
            [f"{_color('Arc', 'cyan', palette):<8}: import → refine → assemble"],
            [f"{_color('Focus', 'cyan', palette):<8}: C7 shell + gas + power"],
        ],
        title=_color("SERES / SCENARIO", "magenta", palette),
        header=False,
    )
    return table.render()


def _stage_table(palette: dict[str, str]) -> list[str]:
    table = Table(
        columns=[
            Column(name="Stage", align="left", width=16),
            Column(name="Δt", align="right", width=7),
            Column(name="ΔE", align="right", width=9),
            Column(name="Cx", align="center", width=4),
        ],
        rows=[
            ["Import tools", "0.0h", "0.0", "C1"],
            ["Regolith MRE", "320h", "17.7MWh", "C4"],
            ["Shell", "15h", "2.35MWh", "C7"],
            ["Gas system", "60h", "0.77MWh", "C7"],
            ["Power bus", "30h", "0.27MWh", "C7"],
            ["Insulation", "6h", "0.0", "C2"],
            ["Imports", "0.0h", "0.0", "C1"],
            ["Final", "3h", "0.0", "C7"],
        ],
        title=_color("STAGE SNAPSHOT", "yellow", palette),
        header=True,
    )
    return table.render()


def _mission_table(palette: dict[str, str]) -> list[str]:
    summary = RUNBOOK["summary"]
    table = Table(
        columns=[Column(name="", align="left", width=44)],
        rows=[
            ["PRIMARY OUTPUT: reduction_furnace_v0 (C7)"],
            [f"ISRU {summary['isru']:.1f}%  {bar(summary['isru'], 100, 22)}"],
            [f"TIME {summary['time_days']:.1f} days   ENERGY {summary['energy_kwh']:.1f} kWh"],
            [f"LOCAL {summary['local_kg']:.1f} kg | IMPORT {summary['imported_kg']:.1f} kg"],
        ],
        title=_color("MISSION COMPLETE", "green", palette),
        header=False,
    )
    return table.render()


def _overlay_panel(
    image_lines: list[str],
    table_lines: list[str],
    image_pos: tuple[int, int],
    table_pos: tuple[int, int],
    width: int,
    height: int,
) -> str:
    config = Config(
        width=width,
        height=height,
        image_pos=image_pos,
        table_pos=table_pos,
        wide_mode="flex",
        table_opaque=True,
    )
    return render_overlay(image_lines, table_lines, config).text


def main() -> int:
    parser = argparse.ArgumentParser(description="SERES overlay story splash")
    parser.add_argument("--no-color", action="store_true")
    args = parser.parse_args()

    palette = _palette(not args.no_color)
    term = shutil.get_terminal_size((120, 40))
    width = term.columns
    panel_height = min(28, term.lines)

    earthrise_lines = _color_earthrise(
        (repo_root / "design" / "earthrise_marked_2.txt").read_text().splitlines(), palette
    )
    galaxy_lines = _color_galaxy(
        (repo_root / "design" / "galaxy_2.txt").read_text().splitlines(), palette
    )
    ascii_lines = _color_ascii_art(
        (repo_root / "design" / "ascii_art_4.txt").read_text().splitlines(), palette
    )

    earth_w, _ = measure_block(earthrise_lines)
    galaxy_w, _ = measure_block(galaxy_lines)

    top = _color(_seres_title(width), "white", palette)

    scenario_panel = _overlay_panel(
        image_lines=earthrise_lines,
        table_lines=_scenario_table(palette),
        image_pos=(max(0, width - earth_w - 6), 0),
        table_pos=(6, 4),
        width=width,
        height=panel_height,
    )

    mission_panel = _overlay_panel(
        image_lines=galaxy_lines,
        table_lines=_mission_table(palette),
        image_pos=(max(0, width - galaxy_w - 16), 0),
        table_pos=(max(0, int(width * 0.10)), 6),
        width=width,
        height=panel_height,
    )

    stages = []
    stages.append(_color("STAGE FLOW", "cyan", palette))
    for stage in RUNBOOK["stages"]:
        stages.append(_color(f"◉ {stage.name}", "magenta", palette))
        stages.append(f"  {stage.story}")
        stages.append(f"  MADE: {', '.join(stage.outputs)}")
        stages.append(f"  Cx {stage.complexity or 'C1'}  Δt {stage.time_h:.1f}h  ΔE {stage.energy_kwh:.1f} kWh  Δm {stage.mass_kg:.1f} kg")
        if stage.warning:
            stages.append(_color(f"  ⚠ {stage.warning}", "yellow", palette))
        stages.append(f"  t {bar(stage.time_h, 320.0, 18)}  E {bar(stage.energy_kwh, 21074.7, 18)}  m {bar(stage.mass_kg, 3630.0, 18)}")
        stages.append("")
    stages_block = "\n".join(stages).rstrip()

    divider = _color("═" * min(width, 120), "magenta", palette)
    print("\n".join([top, "", scenario_panel, divider, stages_block, divider, mission_panel]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
