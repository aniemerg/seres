from __future__ import annotations

from pathlib import Path
import shutil
import sys

repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

from ascii_overlay.core import Config, measure_block, render_overlay  # noqa: E402


RESET = "\033[0m"


def _table_lines() -> list[str]:
    return [
        "┌──────────────────────────────────────────┐",
        "│ SERES / SCENARIO TABLE                   │",
        "├──────────────────────────────────────────┤",
        "│ Goal: reduction_furnace_v0 (ISRU-max)    │",
        "│ Stage 2: MRE alloy batch                 │",
        "│ Energy: 17.7 MWh (spike)                 │",
        "│ Output: +1003.2 metal_alloy_bulk         │",
        "│ Risk:   power bus bottleneck             │",
        "│ Status: GREEN / proceed to C7 shell      │",
        "└──────────────────────────────────────────┘",
    ]


def _colorize(text: str, color: str) -> str:
    return f"{color}{text}{RESET}"


def _earthrise_colored(lines: list[str]) -> list[str]:
    colors = {
        "blue": "\033[94m",
        "white": "\033[97m",
        "dark_gray": "\033[37m",
        "green": "\033[32m",
        "yellow": "\033[93m",
    }
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
                rendered.append(_colorize(char, colors["white"]))
                continue
            if yellow_on:
                rendered.append(_colorize(char, colors["yellow"]))
                continue
            if green_on:
                rendered.append(_colorize(char, colors["green"]))
                continue
            if city_on:
                rendered.append(_colorize(char, colors["dark_gray"]))
                continue
            if earth_on:
                rendered.append(_colorize(char, colors["blue"]))
                continue
            rendered.append(char)
        output.append("".join(rendered))
    return output


def main() -> int:
    term = shutil.get_terminal_size((120, 40))
    earthrise_lines = (repo_root / "design" / "earthrise_marked_2.txt").read_text().splitlines()
    image_lines = _earthrise_colored(earthrise_lines)
    table_lines = _table_lines()

    image_width, _ = measure_block(image_lines)
    image_x = max(0, term.columns - image_width - 10)
    config = Config(
        width=term.columns,
        height=min(term.lines, 40),
        image_pos=(image_x, 0),
        table_pos=(6, 13),
        wide_mode="flex",
        table_opaque=True,
    )
    result = render_overlay(image_lines, table_lines, config)
    print(result.text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
