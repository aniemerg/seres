"""Queue filtering configuration for the work queue."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

DEFAULT_CONFIG_PATH = Path("config/queue_filters.yaml")
LOCAL_CONFIG_PATH = Path(".kbconfig.yaml")


class QueueFilterConfig:
    """Queue filtering configuration loaded from YAML files."""

    def __init__(self) -> None:
        self.enabled = True
        self.current_mode: Optional[str] = None
        self.modes: Dict[str, dict] = {}
        self.exclude_kinds: List[str] = []
        self.exclude_gap_types: List[str] = []

    @classmethod
    def load(cls) -> "QueueFilterConfig":
        """
        Load config from default and local override files.

        Loads config/queue_filters.yaml first (default, committed),
        then .kbconfig.yaml (local override, gitignored) if present.
        """
        if yaml is None:
            config = cls()
            config.enabled = False
            return config

        config = cls()

        if DEFAULT_CONFIG_PATH.exists():
            config._merge_from_file(DEFAULT_CONFIG_PATH)

        if LOCAL_CONFIG_PATH.exists():
            config._merge_from_file(LOCAL_CONFIG_PATH)

        return config

    def _merge_from_file(self, path: Path) -> None:
        """Merge config from YAML file."""
        try:
            with path.open(encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
        except Exception:
            return

        if "filtering_enabled" in data:
            self.enabled = data["filtering_enabled"]
        if "current_mode" in data:
            self.current_mode = data["current_mode"]
        if "modes" in data:
            self.modes.update(data["modes"])
        if "exclude_kinds" in data:
            self.exclude_kinds = list(data["exclude_kinds"])
        if "exclude_gap_types" in data:
            self.exclude_gap_types = list(data["exclude_gap_types"])

    def should_exclude(self, gap_item: dict) -> Tuple[bool, str]:
        """
        Check if a gap item should be excluded from the queue.

        Returns (should_exclude, reason).
        """
        if not self.enabled:
            return False, ""

        gap_type = gap_item.get("gap_type")
        kind = gap_item.get("kind")

        if kind in self.exclude_kinds:
            return True, f"kind={kind} globally excluded"

        if gap_type in self.exclude_gap_types:
            return True, f"gap_type={gap_type} globally excluded"

        if self.current_mode and self.current_mode in self.modes:
            mode = self.modes[self.current_mode]

            for rule in mode.get("exclude", []):
                if self._matches_rule(gap_item, rule):
                    reason = rule.get("reason", "matches exclusion rule")
                    return True, reason

            includes = mode.get("include", [])
            if includes:
                for rule in includes:
                    if self._matches_rule(gap_item, rule):
                        return False, ""
                return True, "not in include whitelist"

        return False, ""

    def _matches_rule(self, gap_item: dict, rule: dict) -> bool:
        """Check if a gap item matches a filter rule."""
        if "gap_type" in rule:
            if gap_item.get("gap_type") != rule["gap_type"]:
                return False

        if "kind" in rule:
            if gap_item.get("kind") != rule["kind"]:
                return False

        if "field" in rule:
            context_field = gap_item.get("context", {}).get("field")
            if context_field != rule["field"]:
                return False

        if "context_has" in rule:
            if rule["context_has"] not in gap_item.get("context", {}):
                return False

        return True

    def get_stats(self) -> dict:
        """Get current configuration statistics."""
        return {
            "enabled": self.enabled,
            "current_mode": self.current_mode,
            "modes_available": list(self.modes.keys()),
            "exclude_kinds": self.exclude_kinds,
            "exclude_gap_types": self.exclude_gap_types,
        }
