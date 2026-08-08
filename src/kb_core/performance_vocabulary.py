"""Controlled vocabulary helpers for item performance requirements."""

from __future__ import annotations

from functools import lru_cache
from typing import Any

import yaml

from src.paths import REPO_ROOT


VOCABULARY_PATH = REPO_ROOT / "config" / "performance_requirement_vocabulary.yaml"


@lru_cache(maxsize=1)
def load_performance_vocabulary() -> dict[str, dict[str, set[str]]]:
    with VOCABULARY_PATH.open(encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}

    categories = raw.get("categories")
    if not isinstance(categories, dict):
        raise ValueError(f"Invalid performance vocabulary: {VOCABULARY_PATH}")

    vocabulary: dict[str, dict[str, set[str]]] = {}
    for category, groups in categories.items():
        if not isinstance(groups, dict):
            raise ValueError(f"Invalid performance category: {category}")
        vocabulary[str(category)] = {}
        for group, terms in groups.items():
            if not isinstance(terms, dict):
                raise ValueError(f"Invalid performance vocabulary group: {category}.{group}")
            vocabulary[str(category)][str(group)] = {str(term) for term in terms}
    return vocabulary


def performance_requirement_errors(requirements: Any) -> list[tuple[str, str]]:
    """Return field paths and messages for non-canonical requirement data."""
    if requirements is None:
        return []
    if not isinstance(requirements, dict):
        return [("performance_requirements", "must be a mapping")]
    if not requirements:
        return [("performance_requirements", "must not be empty")]

    vocabulary = load_performance_vocabulary()
    errors: list[tuple[str, str]] = []
    for category, groups in requirements.items():
        category_path = f"performance_requirements.{category}"
        if category not in vocabulary:
            errors.append((category_path, "unknown performance category"))
            continue
        if not isinstance(groups, dict) or not groups:
            errors.append((category_path, "must be a non-empty subgroup mapping"))
            continue

        for group, terms in groups.items():
            group_path = f"{category_path}.{group}"
            if group not in vocabulary[category]:
                errors.append((group_path, "unknown performance subgroup"))
                continue
            if not isinstance(terms, list) or not terms:
                errors.append((group_path, "must be a non-empty list of controlled term IDs"))
                continue
            string_terms = [term for term in terms if isinstance(term, str)]
            if len(string_terms) != len(set(string_terms)):
                errors.append((group_path, "contains duplicate term IDs"))
            for index, term in enumerate(terms):
                if not isinstance(term, str) or term not in vocabulary[category][group]:
                    errors.append((f"{group_path}[{index}]", f"unknown controlled term ID: {term}"))
    return errors


def flatten_performance_requirements(requirements: Any) -> list[str]:
    """Flatten canonical requirement data to dotted characteristic IDs."""
    if not isinstance(requirements, dict):
        return []
    flattened: list[str] = []
    for category, groups in requirements.items():
        if not isinstance(groups, dict):
            continue
        for group, terms in groups.items():
            if not isinstance(terms, list):
                continue
            flattened.extend(
                f"{category}.{group}.{term}"
                for term in terms
                if isinstance(term, str) and term
            )
    return flattened
