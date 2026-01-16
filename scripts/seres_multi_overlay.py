from __future__ import annotations

from pathlib import Path
import random
import shutil
import sys

repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

from ascii_overlay import Column, Config, Layer, Table, measure_block, render_layers  # noqa: E402


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
        if text.strip() and rng.random() < 0.45:
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
            if char in {" ", "⠀"} and rng.random() < 0.02:
                rendered.append(_color("★", "yellow", palette))
                continue
            rendered.append(char)
        output.append("".join(rendered))
    return output


def _stage_table(title: str, lines: list[str], palette: dict[str, str]) -> list[str]:
    table = Table(
        columns=[Column(name="", align="left", width=32)],
        rows=[[line] for line in lines],
        title=_color(title, "magenta", palette),
        header=False,
    )
    return table.render()


def main() -> int:
    palette = _palette(True)
    term = shutil.get_terminal_size((140, 48))
    width = term.columns
    height = term.lines

    earthrise = _color_earthrise(
        (repo_root / "design" / "earthrise_marked_2.txt").read_text().splitlines(), palette
    )
    ascii_art = _color_ascii_art((repo_root / "design" / "ascii_art_4.txt").read_text().splitlines(), palette)
    galaxy = _color_galaxy((repo_root / "design" / "galaxy_2.txt").read_text().splitlines(), palette)

    earth_w, earth_h = measure_block(earthrise)
    ascii_w, ascii_h = measure_block(ascii_art)
    galaxy_w, galaxy_h = measure_block(galaxy)

    gap = 2
    total_height = earth_h + ascii_h + galaxy_h + (gap * 2)
    height = total_height

    earth_y = 0
    ascii_y = earth_y + earth_h + gap
    galaxy_y = ascii_y + ascii_h + gap

    earth_x = 2
    ascii_x = max(2, width - ascii_w - 2)
    galaxy_x = 2

    stages = [
        ("STAGE 1 / TOOLS", ["Import core tools", "Cx C1  Δt 0h  ΔE 0.0"]),
        ("STAGE 2 / MRE", ["metal_alloy_bulk +1003.2", "Cx C4  Δt 320h  ΔE 17.7"]),
        ("STAGE 3 / SHELL", ["reduction_furnace_shell +1", "Cx C7  Δt 15h  ΔE 2.35"]),
        ("STAGE 4 / GAS", ["gas_handling_system +1", "Cx C7  Δt 60h  ΔE 0.77"]),
        ("STAGE 5 / BUS", ["power_bus_high_current +50", "Cx C7  Δt 30h  ΔE 0.27"]),
        ("STAGE 6 / INSUL", ["insulation_pack +1", "Cx C2  Δt 6h  ΔE 0.0"]),
        ("STAGE 7 / IMPRT", ["electronics + sensors", "Cx C1  Δt 0h  ΔE 0.0"]),
        ("STAGE 8 / FINAL", ["reduction_furnace_v0 +1", "Cx C7  ISRU 52.4%"]),
    ]
    stage_tables = [_stage_table(title, lines, palette) for title, lines in stages]
    table_w, table_h = measure_block(stage_tables[0])

    center_shift = int(width * 0.15)
    left_x = max(2, 2 + center_shift)
    right_x = max(2, width - table_w - 2 - center_shift)
    mid_x = max(2, (width // 2) - (table_w // 2))

    earth_positions = [
        (left_x, earth_y + 2),
        (right_x, earth_y + 10),
        (mid_x, earth_y + 18),
    ]
    ascii_positions = [
        (max(2, int(width * 0.33) - 10), ascii_y + 2),
        (max(2, left_x - 5), ascii_y + 14),
    ]
    galaxy_positions = [
        (left_x, galaxy_y + 2),
        (right_x, galaxy_y + 10),
        (mid_x, galaxy_y + 18),
    ]

    table_positions = earth_positions + ascii_positions + galaxy_positions

    layers = [
        Layer(lines=earthrise, pos=(earth_x, earth_y)),
        Layer(lines=ascii_art, pos=(ascii_x, ascii_y)),
        Layer(lines=galaxy, pos=(galaxy_x, galaxy_y)),
    ]

    for table_lines, pos in zip(stage_tables, table_positions):
        layers.append(Layer(lines=table_lines, pos=pos))

    config = Config(width=width, height=height, image_pos=(0, 0), table_pos=(0, 0), wide_mode="flex")
    result = render_layers(layers, config)

    print(result.text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
