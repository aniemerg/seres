from __future__ import annotations

import argparse
from pathlib import Path


RESET = "\033[0m"


def _palette(enabled: bool) -> dict[str, str]:
    if not enabled:
        return {key: "" for key in ["cyan", "blue", "yellow", "white", "gray", "dark_gray", "dim", "green"]}
    return {
        "cyan": "\033[96m",
        "blue": "\033[94m",
        "yellow": "\033[93m",
        "white": "\033[97m",
        "gray": "\033[90m",
        "dark_gray": "\033[37m",
        "dim": "\033[2m",
        "green": "\033[32m",
    }


def _colorize(text: str, color: str, palette: dict[str, str]) -> str:
    if not palette[color]:
        return text
    return f"{palette[color]}{text}{RESET}"


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


def _color_art(lines: list[str], palette: dict[str, str]) -> str:
    output = []
    for idx, line in enumerate(lines):
        tint = "blue" if idx % 3 == 0 else "cyan"
        colored = _colorize(line.rstrip("\n"), tint, palette)
        colored = colored.replace(
            "★",
            _colorize("★", "yellow", palette),
        )
        output.append(colored)
    return "\n".join(output)


def _color_earthrise(lines: list[str], palette: dict[str, str]) -> str:
    output = []
    total = max(len(lines), 1)
    for idx, line in enumerate(lines):
        dense = sum(line.count(ch) for ch in "⣿⣷⣯⣟⣽⣻⣺⣳⣴⣶")
        if dense > 18:
            tint = "gray"
        elif idx < total * 0.35:
            tint = "blue" if idx % 2 == 0 else "white"
        else:
            tint = "cyan"
        colored = _colorize(line.rstrip("\n"), tint, palette)
        colored = colored.replace("⠄", _colorize("⠄", "dim", palette))
        colored = colored.replace("⠂", _colorize("⠂", "dim", palette))
        output.append(colored)
    return "\n".join(output)


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


def main() -> int:
    parser = argparse.ArgumentParser(description="SERES title + ascii_art_4 highlight")
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI colors")
    args = parser.parse_args()

    palette = _palette(not args.no_color)
    repo_root = Path(__file__).resolve().parents[1]
    art_path = repo_root / "design" / "ascii_art_4.txt"
    lines = art_path.read_text().splitlines()
    earthrise_path = repo_root / "design" / "earthrise.txt"
    earthrise_lines = earthrise_path.read_text().splitlines()
    earthrise_marked_path = repo_root / "design" / "earthrise_marked_2.txt"
    earthrise_marked_lines = earthrise_marked_path.read_text().splitlines()

    width = max(max((len(line) for line in lines), default=0), 72)
    print(_colorize(_seres_title(width), "white", palette))
    print()
    print(_color_art(lines, palette))
    print("\n")
    if earthrise_marked_lines:
        print(_color_earthrise_marked(earthrise_marked_lines, palette))
    else:
        print(_color_earthrise(earthrise_lines, palette))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
