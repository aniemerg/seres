from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .ansi import iter_styled_chars, visible_width
from .grid import Cell, Grid


@dataclass(frozen=True)
class Config:
    width: int
    height: int
    image_pos: tuple[int, int] = (0, 0)
    table_pos: tuple[int, int] = (0, 0)
    wide_mode: str = "reject"  # reject | flex
    table_opaque: bool = True


@dataclass(frozen=True)
class OverlayResult:
    text: str
    clipped: bool


@dataclass(frozen=True)
class Layer:
    lines: Iterable[str]
    pos: tuple[int, int]
    opaque: bool = True


def _line_to_cells(text: str, wide_mode: str) -> list[Cell]:
    cells: list[Cell] = []
    for styled in iter_styled_chars(text):
        if wide_mode == "reject" and styled.width > 1:
            raise ValueError(f"Wide glyph not allowed in reject mode: {styled.char!r}")
        cells.append(Cell(char=styled.char, style=styled.style))
        if styled.width > 1:
            for _ in range(styled.width - 1):
                cells.append(Cell(char=" ", style=styled.style))
    return cells


def _block_from_lines(lines: Iterable[str], wide_mode: str) -> list[list[Cell]]:
    return [_line_to_cells(line, wide_mode) for line in lines]


def _clip_block(block: list[list[Cell]], width: int, height: int) -> list[list[Cell]]:
    clipped = []
    for row in block[:height]:
        clipped.append(row[:width])
    return clipped


def render_overlay(
    image_lines: Iterable[str],
    table_lines: Iterable[str],
    config: Config,
) -> OverlayResult:
    grid = Grid(config.width, config.height)
    clipped = False

    image_block = _block_from_lines(image_lines, config.wide_mode)
    table_block = _block_from_lines(table_lines, config.wide_mode)

    image_block = _clip_block(image_block, config.width, config.height)
    table_block = _clip_block(table_block, config.width, config.height)

    if any(len(row) > config.width for row in image_block):
        clipped = True
    if any(len(row) > config.width for row in table_block):
        clipped = True
    if len(image_block) > config.height or len(table_block) > config.height:
        clipped = True

    grid.place_block(config.image_pos[1], config.image_pos[0], image_block)

    if config.table_opaque:
        grid.place_block(config.table_pos[1], config.table_pos[0], table_block)
    else:
        for y, row in enumerate(table_block):
            for x, cell in enumerate(row):
                if cell.char != " ":
                    grid.place_row(config.table_pos[1] + y, config.table_pos[0] + x, [cell])

    return OverlayResult(text=grid.render(), clipped=clipped)


def measure_block(lines: Iterable[str]) -> tuple[int, int]:
    widths = [visible_width(line) for line in lines]
    return (max(widths, default=0), len(widths))


def render_layers(layers: Iterable[Layer], config: Config) -> OverlayResult:
    grid = Grid(config.width, config.height)
    clipped = False

    for layer in layers:
        block = _block_from_lines(layer.lines, config.wide_mode)
        block = _clip_block(block, config.width, config.height)
        if any(len(row) > config.width for row in block) or len(block) > config.height:
            clipped = True
        if layer.opaque:
            grid.place_block(layer.pos[1], layer.pos[0], block)
        else:
            for y, row in enumerate(block):
                for x, cell in enumerate(row):
                    if cell.char != " ":
                        grid.place_row(layer.pos[1] + y, layer.pos[0] + x, [cell])

    return OverlayResult(text=grid.render(), clipped=clipped)
