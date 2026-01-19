from __future__ import annotations

from pathlib import Path
import shutil
import sys

repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

from ascii_overlay.core import Config, measure_block, render_overlay  # noqa: E402
from ascii_overlay.table import Column, Table  # noqa: E402


RESET = "\033[0m"


def _color(text: str, code: str) -> str:
    return f"{code}{text}{RESET}"


def _palette(enabled: bool) -> dict[str, str]:
    if not enabled:
        return {k: "" for k in ["cyan", "yellow", "green", "white", "magenta", "blue", "gray"]}
    return {
        "cyan": "\033[96m",
        "yellow": "\033[93m",
        "green": "\033[92m",
        "white": "\033[97m",
        "magenta": "\033[95m",
        "blue": "\033[94m",
        "gray": "\033[90m",
    }


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
                rendered.append(_color(char, palette["white"]))
                continue
            if yellow_on:
                rendered.append(_color(char, palette["yellow"]))
                continue
            if green_on:
                rendered.append(_color(char, palette["green"]))
                continue
            if city_on:
                rendered.append(_color(char, palette["gray"]))
                continue
            if earth_on:
                rendered.append(_color(char, palette["blue"]))
                continue
            rendered.append(char)
        output.append("".join(rendered))
    return output


def _color_ascii_art(lines: list[str], palette: dict[str, str]) -> list[str]:
    output = []
    for idx, line in enumerate(lines):
        tint = palette["blue"] if idx % 3 == 0 else palette["cyan"]
        colored = _color(line.rstrip("\n"), tint)
        colored = colored.replace("★", _color("★", palette["yellow"]))
        output.append(colored)
    return output


def _color_galaxy(lines: list[str], palette: dict[str, str]) -> list[str]:
    star_chars = {"⠄", "⠂", "⠈"}
    output = []
    for line in lines:
        rendered = []
        for char in line.rstrip("\n"):
            if char in star_chars:
                rendered.append(_color(char, palette["white"]))
            else:
                rendered.append(char)
        output.append("".join(rendered))
    return output


def _table_intro(palette: dict[str, str]) -> list[str]:
    table = Table(
        columns=[Column(name="", align="left", width=40)],
        rows=[
            [f"{_color('Goal', palette['cyan']):<8}: reduction_furnace_v0"],
            [f"{_color('Mode', palette['cyan']):<8}: ISRU-max / story"],
            [f"{_color('Arc', palette['cyan']):<8}: import → refine → assemble"],
            [f"{_color('Key', palette['cyan']):<8}: C7 shell + gas + power"],
        ],
        title=_color("SERES / MISSION BRIEF", palette["magenta"]),
        header=False,
    )
    return table.render()


def _table_stage(palette: dict[str, str]) -> list[str]:
    table = Table(
        columns=[Column(name="", align="left", width=40)],
        rows=[
            ["Regolith → metal feedstock"],
            ["Output: +1003.2 metal_alloy_bulk"],
            ["O2 byproduct: +668.8"],
            [f"Energy: {_color('17.7 MWh', palette['yellow'])}"],
            ["Time:   320.0h"],
        ],
        title=_color("STAGE 2", palette["yellow"]),
        header=False,
    )
    return table.render()


def _table_summary(palette: dict[str, str]) -> list[str]:
    table = Table(
        columns=[Column(name="", align="left", width=40)],
        rows=[
            ["Output: reduction_furnace_v0 (C7)"],
            [f"ISRU:   {_color('52.4%', palette['green'])}"],
            ["Energy: 21.1 MWh"],
            ["Time:   18.0 days"],
        ],
        title=_color("MISSION COMPLETE", palette["green"]),
        header=False,
    )
    return table.render()


def _render_panel(
    image_lines: list[str],
    table_lines: list[str],
    image_pos: tuple[int, int],
    table_pos: tuple[int, int],
    height: int,
    width: int,
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
    palette = _palette(True)
    term = shutil.get_terminal_size((120, 40))
    width = term.columns
    panel_height = min(28, term.lines)

    galaxy_lines = _color_galaxy((repo_root / "design" / "galaxy_2.txt").read_text().splitlines(), palette)
    earthrise_lines = _color_earthrise(
        (repo_root / "design" / "earthrise_marked_2.txt").read_text().splitlines(), palette
    )
    ascii_lines = _color_ascii_art((repo_root / "design" / "ascii_art_4.txt").read_text().splitlines(), palette)

    galaxy_w, _ = measure_block(galaxy_lines)
    earth_w, _ = measure_block(earthrise_lines)

    panel_a = _render_panel(
        image_lines=galaxy_lines,
        table_lines=_table_intro(palette),
        image_pos=(max(0, width - galaxy_w - 2), 0),
        table_pos=(4, 3),
        height=panel_height,
        width=width,
    )

    panel_b = _render_panel(
        image_lines=earthrise_lines,
        table_lines=_table_stage(palette),
        image_pos=(max(0, width - earth_w - 6), 0),
        table_pos=(10, 10),
        height=panel_height,
        width=width,
    )

    panel_c = _render_panel(
        image_lines=ascii_lines,
        table_lines=_table_summary(palette),
        image_pos=(2, 0),
        table_pos=(width // 2 - 22, 6),
        height=panel_height,
        width=width,
    )

    divider = _color("═" * min(width, 120), palette["magenta"])
    print("\n".join([panel_a, divider, panel_b, divider, panel_c]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
