from __future__ import annotations

import argparse
from pathlib import Path
import shutil

from .core import Config, render_overlay


def main() -> int:
    parser = argparse.ArgumentParser(description="ASCII overlay renderer")
    parser.add_argument("--image", required=True, help="Path to image text")
    parser.add_argument("--table", required=True, help="Path to table text")
    parser.add_argument("--width", type=int, default=None)
    parser.add_argument("--height", type=int, default=None)
    parser.add_argument("--image-x", type=int, default=0)
    parser.add_argument("--image-y", type=int, default=0)
    parser.add_argument("--table-x", type=int, default=0)
    parser.add_argument("--table-y", type=int, default=0)
    parser.add_argument("--wide-mode", choices=["reject", "flex"], default="reject")
    args = parser.parse_args()

    term = shutil.get_terminal_size((120, 40))
    width = args.width or term.columns
    height = args.height or term.lines

    image_lines = Path(args.image).read_text().splitlines()
    table_lines = Path(args.table).read_text().splitlines()

    config = Config(
        width=width,
        height=height,
        image_pos=(args.image_x, args.image_y),
        table_pos=(args.table_x, args.table_y),
        wide_mode=args.wide_mode,
        table_opaque=True,
    )
    result = render_overlay(image_lines, table_lines, config)
    print(result.text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
