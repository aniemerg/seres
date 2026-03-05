from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import yaml

WIKI_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def _split_frontmatter(md: str) -> tuple[dict, str]:
    if not md.startswith("---\n"):
        return {}, md

    parts = md.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, md

    header = parts[0][4:]
    body = parts[1]
    try:
        frontmatter = yaml.safe_load(header) or {}
        if not isinstance(frontmatter, dict):
            return {}, md
        return frontmatter, body
    except Exception:
        return {}, md


def _normalize_article_id(path: Path, frontmatter: dict) -> str:
    if "id" in frontmatter and frontmatter["id"]:
        return str(frontmatter["id"])
    return path.stem


def discover_article_files(repo_root: Path, patterns: Iterable[str]) -> List[Path]:
    files: set[Path] = set()
    for pattern in patterns:
        files.update(repo_root.glob(pattern))
    return sorted(path for path in files if path.is_file())


def parse_articles(repo_root: Path, article_files: Iterable[Path]) -> tuple[List[dict], Dict[str, List[str]]]:
    """Parse markdown articles and collect wiki-link backlinks.

    Returns:
        - list of article records
        - backlinks: target_id -> [source_article_id]
    """
    articles: List[dict] = []
    backlinks: Dict[str, List[str]] = {}

    for path in article_files:
        text = path.read_text(encoding="utf-8")
        frontmatter, body = _split_frontmatter(text)
        article_id = _normalize_article_id(path, frontmatter)
        title = str(frontmatter.get("title") or article_id)

        link_targets: List[str] = []
        for m in WIKI_LINK_RE.finditer(body):
            target = m.group(1).strip()
            if not target:
                continue
            link_targets.append(target)
            backlinks.setdefault(target, []).append(article_id)

        rel_path = path.relative_to(repo_root)
        articles.append(
            {
                "id": article_id,
                "title": title,
                "path": str(rel_path),
                "frontmatter": frontmatter,
                "content": body,
                "wiki_links": link_targets,
            }
        )

    return articles, backlinks


def merge_backlinks(*maps: Dict[str, List[str]]) -> Dict[str, List[str]]:
    merged: Dict[str, List[str]] = {}
    for mapping in maps:
        for key, refs in mapping.items():
            bucket = merged.setdefault(key, [])
            for ref in refs:
                if ref not in bucket:
                    bucket.append(ref)
    return merged
