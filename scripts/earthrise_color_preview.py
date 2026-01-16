from __future__ import annotations

import argparse
from pathlib import Path


RESET = "\033[0m"


def _palette(enabled: bool) -> dict[str, str]:
    if not enabled:
        return {k: "" for k in ["white", "yellow", "green", "gray", "blue"]}
    return {
        "white": "\033[97m",
        "yellow": "\033[93m",
        "green": "\033[32m",
        "gray": "\033[90m",
        "blue": "\033[94m",
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Earthrise color preview")
    parser.add_argument("--no-color", action="store_true")
    args = parser.parse_args()

    palette = _palette(not args.no_color)
    repo_root = Path(__file__).resolve().parents[1]
    lines = (repo_root / "design" / "earthrise_marked_2.txt").read_text().splitlines()
    print("\n".join(_color_earthrise(lines, palette)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
