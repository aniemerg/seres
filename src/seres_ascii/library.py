from __future__ import annotations

from dataclasses import dataclass
import textwrap
from typing import Iterable


@dataclass(frozen=True)
class AsciiArt:
    name: str
    lines: tuple[str, ...]

    @property
    def width(self) -> int:
        return max((len(line) for line in self.lines), default=0)

    @property
    def height(self) -> int:
        return len(self.lines)

    def render(self) -> str:
        return "\n".join(self.lines)


def _make_art(name: str, raw: str) -> AsciiArt:
    lines = textwrap.dedent(raw).strip("\n").splitlines()
    width = max((len(line) for line in lines), default=0)
    padded = tuple(line.ljust(width) for line in lines)
    return AsciiArt(name=name, lines=padded)


ART = {
    "moon_full": _make_art(
        "moon_full",
        r"""
          _..._
        .'     '.
        :  .-.  :
        : (   ) :
        '.'---'.'
        """,
    ),
    "moon_crater": _make_art(
        "moon_crater",
        r"""
          _..._
        .'  _  '.
        :  ( )  :
        : (_)_) :
        '.'---'.'
        """,
    ),
    "crescent": _make_art(
        "crescent",
        r"""
          _.._
        .'    '.
        :  .-.  )
        : (   )/
        '.'---'
        """,
    ),
    "bot_head": _make_art(
        "bot_head",
        r"""
         .-===-.
         |[o o]|
         |  ^  |
         | '-' |
         '-----'
        """,
    ),
    "bot_walker": _make_art(
        "bot_walker",
        r"""
          .-._.-.
         (  o o  )
          |  ^  |
          | '-' |
         /|     |\
          /___\
        """,
    ),
    "rover": _make_art(
        "rover",
        r"""
           ____
         _/ __ \_
        |__|  |__|
          O----O
        """,
    ),
    "drone": _make_art(
        "drone",
        r"""
        \o/---\o/
         |  *  |
        /o\---/o\
           |_|
        """,
    ),
    "antenna": _make_art(
        "antenna",
        r"""
          /\
         /||\
          ||
          ||
         _||_
        """,
    ),
    "habitat": _make_art(
        "habitat",
        r"""
          ______
         /_____/|
         | _  _| |
         || || | |
         |_____|/
        """,
    ),
    "fab_unit": _make_art(
        "fab_unit",
        r"""
          _||_||_
         |  __  |
         | |__| |
         |  __  |__
         |__||__|_/
        """,
    ),
    "replicator": _make_art(
        "replicator",
        r"""
        [##]==>[##]
          \__/\__/
        """,
    ),
    "swarm": _make_art(
        "swarm",
        r"""
        *  *  *
          *  *
        *  *  *
        """,
    ),
    "gutter_moon_tower": _make_art(
        "gutter_moon_tower",
        r"""
        │     .   *
        │   .   .
        │    _.._
        │  .'    '.
        │ :  .-.  :
        │ : (   ) :
        │  '.\_/.' 
        │    ||
        │   _||_
        │__|____|___
        """,
    ),
    "gutter_fab_arm": _make_art(
        "gutter_fab_arm",
        r"""
        │   [====]
        │     ||
        │    _||_
        │   /_||_\
        │     ||
        │   __||__
        │  |  __  |
        │  | |__| |
        │  |  __  |
        │__|__||__|_
        """,
    ),
    "gutter_orbit": _make_art(
        "gutter_orbit",
        r"""
        │   .     *
        │ .   .
        │    ___
        │ .-'   '-.
        │/  .-.-.  \
        │| (  ☾  ) |
        │\  '-'-'  /
        │ '-.___.-'
        │     .   *
        │___.____.__
        """,
    ),
    "banner_seres_moonseed": _make_art(
        "banner_seres_moonseed",
        r"""
        ┌────────── SERES ──────────┐
        │   moonseed replication sim │
        └───────────────────────────┘
        """,
    ),
    "banner_seres_autofab": _make_art(
        "banner_seres_autofab",
        r"""
        ╔═══╦══════════════════════╗
        ║ ☾ ║  SERES : AUTOFAB      ║
        ╚═══╩══════════════════════╝
        """,
    ),
    "banner_seres_bootstrap": _make_art(
        "banner_seres_bootstrap",
        r"""
        ┏━━━━━━━━━━━ SERES ━━━━━━━━━━━┓
        ┃   BOOTSTRAP / SEED / SWARM   ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """,
    ),
    "banner_seres_colony": _make_art(
        "banner_seres_colony",
        r"""
        +-----------[ SERES ]-----------+
        |   colony: build → copy → grow |
        +------------------------------+
        """,
    ),
    "banner_seres_telemetry": _make_art(
        "banner_seres_telemetry",
        r"""
        ╭──────── SERES // TELEMETRY ────────╮
        │  Δmass  Δpower  Δparts  Δbots      │
        ╰────────────────────────────────────╯
        """,
    ),
    "banner_seres_regolith": _make_art(
        "banner_seres_regolith",
        r"""
        ┌─ SERES ───────────────┐
        │  REGOLITH → FAB → MK+1 │
        └───────────────────────┘
        """,
    ),
    "banner_seres_console": _make_art(
        "banner_seres_console",
        r"""
        [ SERES ] :: MOON OPERATOR CONSOLE
        """,
    ),
    "banner_seres_tree": _make_art(
        "banner_seres_tree",
        r"""
        SERES ──┬─ habitat
                ├─ smelter
                └─ printer
        """,
    ),
    "banner_seres_foundry": _make_art(
        "banner_seres_foundry",
        r"""
        ╭─☾─ SERES ─ AUTONOMOUS FOUNDRY ─☾─╮
        """,
    ),
    "banner_seres_mk1": _make_art(
        "banner_seres_mk1",
        r"""
        ┌──────────────┐
        │  SERES / MK-1 │
        └──────────────┘
        """,
    ),
    "scene_seres_hub": _make_art(
        "scene_seres_hub",
        r"""
                .        *        .
                     _..-''-.._
                  .-'  _    _  '-.
                 /   _( )__( )_   \
                ;   /__/____\__\   ;
                |      SERES       |
                ;   .--.____.--.   ;
                 \  \_  ____  _/  /
                  '.  '------'  .'
                    '-.______.-'
           ___     _/\/\_   _/\/\_     ___
        __/___\___/      \_/      \___/___\__
        """,
    ),
    "scene_rover_moon": _make_art(
        "scene_rover_moon",
        r"""
           .       *            .        *
                 .       _..._
          ____        .-'     '-.      ____
         / __ \_     /  .-.-.    \   _/ __ \
        |__|  |__|  ;  /  _  \    ; |__|  |__|
          O----O     |  | (_) |    |   O----O
                     ;   \___/    ;
                      \          /
                       '.______.'    .    *
          ___..---..___    .     ___..---..___
        _/___/_____\___\___._____/___/_____\___\_
        """,
    ),
    "scene_bot_upgrade": _make_art(
        "scene_bot_upgrade",
        r"""
             .-._.-.            .-._.-.
            (  o o  )  =>       (  o o  )
             |  ^  |             |  ^  |
             | '-' |             | '-' |
            /|     |\           /|     |\
           /_|__ __|_\         /_|__ __|_\
              /_/ \_\            /_/ \_\
              MK-1               MK-2 (fresh)
        """,
    ),
    "scene_orbital_yard": _make_art(
        "scene_orbital_yard",
        r"""
        .        *                 .
           .        .      *
        .----.            .----.
     .-'  __  '-.      .-'  __  '-.
    /   .'  '.   \    /   .'  '.   \
   |   /  ()  \   |  |   /  ()  \   |
   |   \      /   |  |   \      /   |
    \   '.__.'   /    \   '.__.'   /
     '-.______. -'      '-.______. -'
          ||                   ||
      ____||____           ____||____
     /___/  \___\         /___/  \___\
           SERES ORBITAL YARD
        """,
    ),
    "scene_seres_outpost": _make_art(
        "scene_seres_outpost",
        r"""
              _.._        [__] [__]
           .-'    '-.      ||   ||
          /  .-.-.   \   __||___||__
         ;  (  ☾  )  ; /__ SERES __\
          \  '-'-'  /     /____\
           '-.___.-'     /_/  \_\
        """,
    ),
    "pipeline_seres": _make_art(
        "pipeline_seres",
        r"""
        ┌────────┐   ┌────────┐   ┌────────┐   ┌─────────┐   ┌─────────┐
        │REGOLITH│→→ │ CRUSH  │→→ │ SMELT  │→→ │  PRINT  │→→ │ ASSEMBLE│
        └────────┘   └────────┘   └────────┘   └─────────┘   └─────────┘
             ↑                                                             │
             └─────────────── repair / recycle / telemetry ────────────────┘
        """,
    ),
    "glyph_core": _make_art(
        "glyph_core",
        r"""
                 ▄▄▄▄▄▄▄▄▄▄
           ▄▄▄▄██░░░░░░░░░░██▄▄▄▄
          ████░░░▄▄▄▄▄▄▄▄░░░████
           ▀▀██░░█  ▄▄  █░░██▀▀
              ▀█░█ ▀  ▀ █░█▀
               ▀██▄▄▄▄▄▄██▀
                ▄█  ██  █▄
              ▄█▀  ▄██▄  ▀█▄
             ▀▀    ▀  ▀    ▀▀
        """,
    ),
    "aura_mid": _make_art(
        "aura_mid",
        r"""
                         ✦        ·         ✧
                    ·                             ✦
                ✧                 ░░▒▒▓▓▓▓▒▒░░
                             ░▒▓████████████▓▒░
                           ░▓██████▒░░░▒██████▓░
                          ░██████░      ░██████░
                          ▓█████░  ░▓▓░  ░█████▓
                          ██████  ░████░  ██████
                          ▓█████░  ░▓▓░  ░█████▓
                          ░██████░      ░██████░
                           ░▓██████▒░░░▒██████▓░
                             ░▒▓████████████▓▒░
                                   ░░▒▒▓▓▒▒░░
        """,
    ),
    "terrain_mid": _make_art(
        "terrain_mid",
        r"""
        ████████████████████████████████████████
        ██████████████████▓▓▓▓▓▓▓▓██████████████
        ██████████████▓▓▒▒░░░░░░░░▒▒▓▓███████████
        ██████████▓▓▒░░              ░░▒▓▓███████
        ██████▓▓▒░░                      ░░▒▓▓███
        """,
    ),
    "aura_grand": _make_art(
        "aura_grand",
        r"""
                           ✦                 ·                 ✧
                 ·                                                          ✦
        ✧                                   ░░▒▒▓▓▓▓▓▓▓▓▒▒░░
                                     ░▒▓████████████████████▓▒░
                                  ░▓████████▒░░░░░░░▒████████▓░
                                 ░███████░                ░███████░
                                 ▓██████░   ░▒▓▓▓▓▒░        ░██████▓
                                 ██████░  ░▓████████▓░       ░███████
                                 ██████  ░████████████░       ███████
                                 ██████  ░██████░░██████░      ███████
                                 ██████  ░████░    ░████░      ███████
                                 ██████  ░██████░░██████░      ███████
                                 ██████  ░████████████░       ███████
                                 ██████░  ░▓████████▓░       ░███████
                                 ▓██████░   ░▒▓▓▓▓▒░        ░██████▓
                                 ░███████░                ░███████░
                                  ░▓████████▒░░░░░░░▒████████▓░
                                     ░▒▓████████████████████▓▒░
                                           ░░▒▒▓▓▓▓▓▓▓▓▒▒░░
        """,
    ),
    "terrain_grand": _make_art(
        "terrain_grand",
        r"""
        ████████████████████████████████████████████████████████████████████████
        ██████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████████████████████████
        ██████████████████████▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓████████████████████
        ████████████████▓▓▓▒▒░░░░                               ░░░░▒▒▓▓▓██████████
        █████████████▓▓▒░░░                                           ░░░▒▓▓████████
        █████████▓▓▒░░                                                   ░░▒▓▓██████
        ███████▓▓▒░░                                                           ░░▒▓▓██
        """,
    ),
}

CATEGORIES = {
    "tiles": [
        "moon_full",
        "moon_crater",
        "crescent",
        "bot_head",
        "bot_walker",
        "rover",
        "drone",
        "antenna",
        "habitat",
        "fab_unit",
        "replicator",
        "swarm",
    ],
    "gutters": [
        "gutter_moon_tower",
        "gutter_fab_arm",
        "gutter_orbit",
    ],
    "banners": [
        "banner_seres_moonseed",
        "banner_seres_autofab",
        "banner_seres_bootstrap",
        "banner_seres_colony",
        "banner_seres_telemetry",
        "banner_seres_regolith",
        "banner_seres_console",
        "banner_seres_tree",
        "banner_seres_foundry",
        "banner_seres_mk1",
    ],
    "scenes": [
        "scene_seres_hub",
        "scene_rover_moon",
        "scene_bot_upgrade",
        "scene_orbital_yard",
        "scene_seres_outpost",
    ],
    "posters": [
        "pipeline_seres",
        "glyph_core",
        "aura_mid",
        "terrain_mid",
        "aura_grand",
        "terrain_grand",
    ],
}


def list_art() -> list[str]:
    return sorted(ART.keys())


def get_art(name: str) -> AsciiArt:
    if name not in ART:
        raise KeyError(f"Unknown art asset: {name}")
    return ART[name]


def render_art(name: str) -> str:
    return get_art(name).render()


def compose_horizontal(arts: Iterable[AsciiArt], gap: int = 2) -> str:
    arts = list(arts)
    if not arts:
        return ""
    height = max(art.height for art in arts)
    lines: list[str] = []
    spacer = " " * gap
    for row in range(height):
        row_chunks = []
        for art in arts:
            if row < art.height:
                row_chunks.append(art.lines[row])
            else:
                row_chunks.append(" " * art.width)
        lines.append(spacer.join(row_chunks))
    return "\n".join(lines)


def compose_grid(names: Iterable[str], columns: int = 3, gap: int = 2, row_gap: int = 1) -> str:
    names = list(names)
    if not names:
        return ""
    rows: list[str] = []
    for i in range(0, len(names), columns):
        row_names = names[i:i + columns]
        row_art = compose_horizontal([get_art(name) for name in row_names], gap=gap)
        rows.append(row_art)
    return ("\n" * row_gap).join(rows)
