from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .ansi import visible_width


@dataclass(frozen=True)
class Column:
    name: str
    align: str = "left"  # left | center | right
    width: int | None = None


def _pad(text: str, width: int, align: str) -> str:
    delta = max(0, width - visible_width(text))
    if align == "right":
        return (" " * delta) + text
    if align == "center":
        left = delta // 2
        right = delta - left
        return (" " * left) + text + (" " * right)
    return text + (" " * delta)


class Table:
    def __init__(
        self,
        columns: Sequence[Column],
        rows: Sequence[Sequence[str]],
        title: str | None = None,
        header: bool = True,
    ) -> None:
        self.columns = list(columns)
        self.rows = [list(row) for row in rows]
        self.title = title
        self.header = header

    def _col_widths(self) -> list[int]:
        widths = []
        for idx, col in enumerate(self.columns):
            max_width = visible_width(col.name) if self.header else 0
            for row in self.rows:
                if idx < len(row):
                    max_width = max(max_width, visible_width(row[idx]))
            widths.append(col.width or max_width)
        return widths

    def render(self) -> list[str]:
        widths = self._col_widths()
        inner = sum(widths) + (3 * len(widths)) - 1
        top = f"┌{'─' * inner}┐"
        bottom = f"└{'─' * inner}┘"
        sep = f"├{'─' * inner}┤"

        lines = [top]
        if self.title:
            title_line = _pad(self.title, inner, "center")
            lines.append(f"│{title_line}│")
            lines.append(sep)
        if self.header:
            header_cells = [
                _pad(col.name, widths[i], col.align) for i, col in enumerate(self.columns)
            ]
            lines.append("│ " + " │ ".join(header_cells) + " │")
            lines.append(sep)
        for row in self.rows:
            cells = []
            for i, col in enumerate(self.columns):
                cell = row[i] if i < len(row) else ""
                cells.append(_pad(cell, widths[i], col.align))
            lines.append("│ " + " │ ".join(cells) + " │")
        lines.append(bottom)
        return lines
