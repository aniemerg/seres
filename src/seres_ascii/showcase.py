from __future__ import annotations

import argparse

from src.seres_ascii import library


def _section_title(title: str) -> str:
    bar = "-" * len(title)
    return f"{title}\n{bar}"

def _colorize(text: str, color: str | None) -> str:
    if not color:
        return text
    return f"{color}{text}\033[0m"


def _palette() -> dict[str, str]:
    return {
        "cyan": "\033[96m",
        "magenta": "\033[95m",
        "yellow": "\033[93m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "white": "\033[97m",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="SERES ASCII Art Showcase")
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable ANSI color output",
    )
    args = parser.parse_args()

    palette = _palette()
    use_color = not args.no_color

    def tint(text: str, key: str) -> str:
        return _colorize(text, palette[key] if use_color else None)

    print(tint(library.render_art("banner_seres_moonseed"), "cyan"))
    print()

    print(_section_title("Tiles"))
    print(tint(library.compose_grid(library.CATEGORIES["tiles"], columns=3, gap=4, row_gap=2), "white"))
    print()

    print(_section_title("Gutters"))
    gutters = library.compose_horizontal(
        [library.get_art(name) for name in library.CATEGORIES["gutters"]],
        gap=3,
    )
    print(tint(gutters, "blue"))
    print()

    print(_section_title("Banners"))
    for name in library.CATEGORIES["banners"]:
        print(tint(library.render_art(name), "magenta"))
    print()

    print(_section_title("Scenes"))
    for name in library.CATEGORIES["scenes"]:
        print(tint(library.render_art(name), "green"))
        print()

    print(_section_title("Posters"))
    for name in library.CATEGORIES["posters"]:
        print(tint(library.render_art(name), "yellow"))
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
