#!/usr/bin/env python3
"""Render compact STEP preview images for reAM250 BOM research.

Run this with the task wrapper, for example:

    queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
      design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B2_handle.step

The default output is one compact 2x2 contact sheet containing iso, front, top,
and right views. It is intended for low-token visual triage, not measurement.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from pathlib import Path
from typing import Iterable

os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-seres")

try:
    import matplotlib.pyplot as plt
    import numpy as np
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
except Exception as exc:  # pragma: no cover - dependency/environment guard
    raise SystemExit(f"missing render dependency: {exc}") from exc

try:
    import Part
except Exception as exc:  # pragma: no cover - must run under FreeCAD python
    raise SystemExit(
        "FreeCAD Part module is unavailable. Run this script with "
        ".tools/freecad/freecadcmd, not plain python."
    ) from exc


VIEWS = {
    "iso": (30, -45),
    "front": (0, -90),
    "top": (90, -90),
    "right": (0, 0),
}


def default_output_dir(step_path: Path) -> Path:
    if step_path.parent.name == "parts":
        return step_path.parent.parent / "renders"
    return step_path.parent / "renders"


def load_mesh(step_path: Path, linear_deflection: float) -> tuple[np.ndarray, list[tuple[int, ...]]]:
    shape = Part.Shape()
    shape.read(str(step_path))
    vertices, facets = shape.tessellate(linear_deflection)
    points = np.array([[vertex.x, vertex.y, vertex.z] for vertex in vertices], dtype=float)
    faces = [tuple(int(index) for index in facet) for facet in facets]
    if len(points) == 0 or not faces:
        raise ValueError(f"STEP file produced no renderable mesh: {step_path}")
    return points, faces


def face_polygons(points: np.ndarray, faces: Iterable[tuple[int, ...]]) -> list[np.ndarray]:
    return [points[list(face)] for face in faces if len(face) >= 3]


def set_equal_axes(ax, points: np.ndarray) -> None:
    mins = points.min(axis=0)
    maxs = points.max(axis=0)
    centers = (mins + maxs) / 2.0
    span = float(max(maxs - mins))
    if not math.isfinite(span) or span <= 0:
        span = 1.0
    radius = span / 2.0
    ax.set_xlim(centers[0] - radius, centers[0] + radius)
    ax.set_ylim(centers[1] - radius, centers[1] + radius)
    ax.set_zlim(centers[2] - radius, centers[2] + radius)
    try:
        ax.set_box_aspect((1, 1, 1))
    except Exception:
        pass


def draw_view(ax, polygons: list[np.ndarray], points: np.ndarray, view_name: str) -> None:
    elev, azim = VIEWS[view_name]
    collection = Poly3DCollection(
        polygons,
        facecolor="#d9dde3",
        edgecolor="#4b5563",
        linewidth=0.18,
        alpha=1.0,
    )
    ax.add_collection3d(collection)
    set_equal_axes(ax, points)
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    ax.set_title(view_name, fontsize=8, pad=0)


def render_contact_sheet(
    points: np.ndarray,
    faces: list[tuple[int, ...]],
    output_path: Path,
    title: str,
    dpi: int,
    figsize: float,
) -> None:
    polygons = face_polygons(points, faces)
    fig = plt.figure(figsize=(figsize, figsize), dpi=dpi)
    for index, view_name in enumerate(("iso", "front", "top", "right"), start=1):
        ax = fig.add_subplot(2, 2, index, projection="3d")
        draw_view(ax, polygons, points, view_name)
    fig.suptitle(title, fontsize=7, y=0.995)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=0.93, wspace=0.01, hspace=0.01)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, facecolor="white", bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)


def render_individual_views(
    points: np.ndarray,
    faces: list[tuple[int, ...]],
    output_dir: Path,
    stem: str,
    dpi: int,
    figsize: float,
    view_names: Iterable[str],
) -> list[Path]:
    polygons = face_polygons(points, faces)
    paths: list[Path] = []
    output_dir.mkdir(parents=True, exist_ok=True)
    for view_name in view_names:
        output_path = output_dir / f"{stem}__{view_name}.png"
        fig = plt.figure(figsize=(figsize, figsize), dpi=dpi)
        ax = fig.add_subplot(1, 1, 1, projection="3d")
        draw_view(ax, polygons, points, view_name)
        fig.subplots_adjust(left=0, right=1, bottom=0, top=0.96)
        fig.savefig(output_path, facecolor="white", bbox_inches="tight", pad_inches=0.02)
        plt.close(fig)
        paths.append(output_path)
    return paths


def mesh_metadata(points: np.ndarray, faces: list[tuple[int, ...]]) -> dict[str, object]:
    mins = points.min(axis=0)
    maxs = points.max(axis=0)
    return {
        "vertex_count": int(len(points)),
        "face_count": int(len(faces)),
        "bbox_mm": {
            "x": float(maxs[0] - mins[0]),
            "y": float(maxs[1] - mins[1]),
            "z": float(maxs[2] - mins[2]),
        },
    }


def bbox_label(points: np.ndarray) -> str:
    mins = points.min(axis=0)
    maxs = points.max(axis=0)
    size = maxs - mins
    return f"bbox {size[0]:.1f} x {size[1]:.1f} x {size[2]:.1f} mm"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render compact STEP preview images")
    parser.add_argument("step", type=Path, help="STEP file to render")
    parser.add_argument("--output-dir", type=Path, help="Directory for PNG outputs")
    parser.add_argument("--linear-deflection", type=float, default=0.5)
    parser.add_argument("--dpi", type=int, default=128)
    parser.add_argument("--figsize", type=float, default=4.0, help="Contact sheet size in inches")
    parser.add_argument(
        "--individual-views",
        action="store_true",
        help="Also render all individual views.",
    )
    parser.add_argument(
        "--view",
        action="append",
        choices=tuple(VIEWS),
        help=(
            "Also render one selected individual view. May be repeated. "
            "Use this before --individual-views when only one orientation is needed."
        ),
    )
    parser.add_argument(
        "--output-stem",
        help="Base filename for generated PNGs. Defaults to the STEP file stem.",
    )
    args = parser.parse_args(argv)

    step_path = args.step.resolve()
    if not step_path.exists():
        raise FileNotFoundError(step_path)
    output_dir = args.output_dir.resolve() if args.output_dir else default_output_dir(step_path)
    stem = args.output_stem or step_path.stem

    points, faces = load_mesh(step_path, args.linear_deflection)
    contact_sheet = output_dir / f"{stem}__views_2x2.png"
    render_contact_sheet(
        points,
        faces,
        contact_sheet,
        f"{stem} - {bbox_label(points)}",
        args.dpi,
        args.figsize,
    )
    individual_paths = []
    individual_view_names: list[str] = []
    if args.individual_views:
        individual_view_names = list(VIEWS)
    elif args.view:
        individual_view_names = list(dict.fromkeys(args.view))
    if individual_view_names:
        individual_paths = render_individual_views(
            points, faces, output_dir, stem, args.dpi, args.figsize, individual_view_names
        )

    result = {
        "step": str(step_path),
        "contact_sheet": str(contact_sheet),
        "individual_views": [str(path) for path in individual_paths],
        "individual_view_names": individual_view_names,
        "views": ["iso", "front", "top", "right"],
        "intended_detail": "low",
        "metadata": mesh_metadata(points, faces),
        "note": "Preview images are for visual triage only, not exact measurement.",
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
