from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Cell:
    char: str
    style: str


class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self._cells = [
            [Cell(char=" ", style="") for _ in range(width)] for _ in range(height)
        ]

    def place_row(self, row: int, col: int, cells: Iterable[Cell]) -> None:
        if row < 0 or row >= self.height:
            return
        x = col
        for cell in cells:
            if 0 <= x < self.width:
                self._cells[row][x] = cell
            x += 1

    def place_block(self, row: int, col: int, block: list[list[Cell]]) -> None:
        for y, line in enumerate(block):
            self.place_row(row + y, col, line)

    def render(self) -> str:
        lines = []
        for row in self._cells:
            line = []
            current_style = ""
            for cell in row:
                if cell.style != current_style:
                    line.append(cell.style or "\x1b[0m")
                    current_style = cell.style
                line.append(cell.char)
            if current_style:
                line.append("\x1b[0m")
            lines.append("".join(line))
        return "\n".join(lines)
