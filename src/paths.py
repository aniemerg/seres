"""Canonical filesystem locations for a SERES checkout."""
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_ROOT = REPO_ROOT / "content"
KB_ROOT = CONTENT_ROOT / "kb"
SIMULATIONS_ROOT = CONTENT_ROOT / "simulations"
