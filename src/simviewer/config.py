from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

import yaml


@dataclass
class SimviewerConfig:
    sim_id: str
    article_paths: List[str]
    checkpoint_every_processes: int = 150
    checkpoint_every_hours: float = 24.0
    homepage_article_id: str = "simulation_overview"
    strict: bool = False

    def to_dict(self) -> dict:
        return asdict(self)

DEFAULT_ARTICLE_PATHS = ["docs/simviewer_articles/**/*.md"]


def load_config(config_path: Path | None, sim_id: str) -> SimviewerConfig:
    """Load optional simviewer config and apply defaults."""
    if config_path is None:
        return SimviewerConfig(sim_id=sim_id, article_paths=list(DEFAULT_ARTICLE_PATHS))

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    raw = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if raw is None:
        raw = {}
    if not isinstance(raw, dict):
        raise ValueError(f"Invalid config format in {config_path}: expected mapping")

    resolved_sim_id = str(raw.get("sim_id") or sim_id)
    article_paths = raw.get("article_paths") or list(DEFAULT_ARTICLE_PATHS)
    if not isinstance(article_paths, list):
        raise ValueError("simviewer config field 'article_paths' must be a list")

    return SimviewerConfig(
        sim_id=resolved_sim_id,
        article_paths=[str(p) for p in article_paths],
        checkpoint_every_processes=int(raw.get("checkpoint_every_processes", 150)),
        checkpoint_every_hours=float(raw.get("checkpoint_every_hours", 24.0)),
        homepage_article_id=str(raw.get("homepage_article_id", "simulation_overview")),
        strict=bool(raw.get("strict", False)),
    )
