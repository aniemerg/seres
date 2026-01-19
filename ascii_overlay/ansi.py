from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable


ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


@dataclass(frozen=True)
class StyledChar:
    char: str
    style: str
    width: int


def strip_ansi(text: str) -> str:
    return ANSI_RE.sub("", text)


def _char_width(char: str) -> int:
    try:
        from wcwidth import wcwidth  # type: ignore
    except Exception:
        return 1
    width = wcwidth(char)
    return 1 if width < 1 else width


def iter_styled_chars(text: str) -> Iterable[StyledChar]:
    style = ""
    cursor = 0
    for match in ANSI_RE.finditer(text):
        segment = text[cursor:match.start()]
        for char in segment:
            yield StyledChar(char=char, style=style, width=_char_width(char))
        code = match.group(0)
        if code == "\x1b[0m":
            style = ""
        else:
            style = code
        cursor = match.end()
    tail = text[cursor:]
    for char in tail:
        yield StyledChar(char=char, style=style, width=_char_width(char))


def visible_width(text: str) -> int:
    width = 0
    for styled in iter_styled_chars(text):
        width += styled.width
    return width
