from __future__ import annotations

import json
from pathlib import Path

from scripts.analysis import run_self_reproduction_demo as demo
from scripts.analysis.simplan import PlanRecipe, SimPlan


def test_main_forwards_sim2_execution_flags(tmp_path: Path, monkeypatch) -> None:
    machine_list = tmp_path / "machines.txt"
    machine_list.write_text("machine_alpha\n", encoding="utf-8")

    plans_dir = tmp_path / "plans"
    plans_dir.mkdir(parents=True)
    plan_path = plans_dir / "machine_alpha_optimized.json"
    plan_path.write_text(
        json.dumps(
            {
                "sim_id": "orig",
                "target_machine_id": "machine_alpha",
                "target_recipe_id": None,
                "imports": {},
                "recipes": [],
                "notes": [],
                "build_machine": False,
                "metadata": {},
            }
        ),
        encoding="utf-8",
    )

    sim_root = tmp_path / "sims"
    captured: dict = {}

    def _fake_execute_plan(**kwargs):
        captured.update(kwargs)
        return {"success": True}

    monkeypatch.setattr(demo, "execute_plan", _fake_execute_plan)
    monkeypatch.setattr(demo, "_load_kb_machine_ids", lambda _kb_root: set())
    monkeypatch.setattr(demo, "_load_snapshot", lambda _sim_dir: {"state": {}})
    monkeypatch.setattr(demo, "_load_events", lambda _sim_dir: [])

    argv = [
        "run_self_reproduction_demo.py",
        "--machine-list",
        str(machine_list),
        "--plans-dir",
        str(plans_dir),
        "--sim-root",
        str(sim_root),
        "--sim-id",
        "self_repro_demo_sim2",
        "--engine",
        "sim2",
        "--strategy",
        "upfront",
        "--max-no-progress",
        "42",
        "--progress-every-steps",
        "77",
        "--snapshot-interval-hours",
        "12",
        "--recipe-retry-delay-hours",
        "6",
    ]
    monkeypatch.setattr("sys.argv", argv)

    assert demo.main() == 0
    assert captured["engine_mode"] == "sim2"
    assert captured["strategy"] == "upfront"
    assert captured["max_no_progress"] == 42
    assert captured["progress_every_steps"] == 77
    assert captured["snapshot_interval_hours"] == 12
    assert captured["recipe_retry_delay_hours"] == 6


def test_main_stops_on_first_failure_by_default(tmp_path: Path, monkeypatch) -> None:
    machine_list = tmp_path / "machines.txt"
    machine_list.write_text("machine_a\nmachine_b\n", encoding="utf-8")

    plans_dir = tmp_path / "plans"
    plans_dir.mkdir(parents=True)
    for mid in ("machine_a", "machine_b"):
        (plans_dir / f"{mid}_optimized.json").write_text(
            json.dumps(
                {
                    "sim_id": "orig",
                    "target_machine_id": mid,
                    "target_recipe_id": None,
                    "imports": {},
                    "recipes": [],
                    "notes": [],
                    "build_machine": False,
                    "metadata": {},
                }
            ),
            encoding="utf-8",
        )

    sim_root = tmp_path / "sims"
    calls: list[str] = []

    def _fake_execute_plan(**kwargs):
        calls.append(kwargs["plan"].target_machine_id)
        return {"success": False, "error": "boom"}

    monkeypatch.setattr(demo, "execute_plan", _fake_execute_plan)
    monkeypatch.setattr(demo, "_load_kb_machine_ids", lambda _kb_root: set())
    monkeypatch.setattr(demo, "_load_snapshot", lambda _sim_dir: {"state": {}})
    monkeypatch.setattr(demo, "_load_events", lambda _sim_dir: [])

    argv = [
        "run_self_reproduction_demo.py",
        "--machine-list",
        str(machine_list),
        "--plans-dir",
        str(plans_dir),
        "--sim-root",
        str(sim_root),
        "--sim-id",
        "self_repro_demo_sim2",
    ]
    monkeypatch.setattr("sys.argv", argv)

    assert demo.main() == 1
    assert calls == ["machine_a"]


def test_apply_goal_tags_sets_machine_id_on_plan_and_recipes() -> None:
    plan = SimPlan(
        sim_id="demo",
        target_machine_id="machine_x",
        metadata={},
        recipes=[
            PlanRecipe(recipe_id="recipe_a", quantity=1, metadata={}),
            PlanRecipe(recipe_id="recipe_b", quantity=2, metadata={"tags": {"goal.recipe_id": "recipe_b"}}),
        ],
    )

    demo._apply_goal_tags(plan, "machine_x")

    assert plan.metadata["tags"]["goal.machine_id"] == "machine_x"
    assert plan.recipes[0].metadata["tags"]["goal.machine_id"] == "machine_x"
    assert plan.recipes[1].metadata["tags"]["goal.machine_id"] == "machine_x"
    assert plan.recipes[1].metadata["tags"]["goal.recipe_id"] == "recipe_b"


def test_main_combined_mode_executes_merged_plan_once(tmp_path: Path, monkeypatch) -> None:
    machine_list = tmp_path / "machines.txt"
    machine_list.write_text("machine_a\nmachine_b\n", encoding="utf-8")

    plans_dir = tmp_path / "plans"
    plans_dir.mkdir(parents=True)
    for mid in ("machine_a", "machine_b"):
        (plans_dir / f"{mid}_optimized.json").write_text(
            json.dumps(
                {
                    "sim_id": "orig",
                    "target_machine_id": mid,
                    "target_recipe_id": None,
                    "imports": {},
                    "recipes": [],
                    "notes": [],
                    "build_machine": False,
                    "metadata": {},
                }
            ),
            encoding="utf-8",
        )

    sim_root = tmp_path / "sims"
    calls: list[str] = []
    merge_called = {"count": 0}

    def _fake_execute_plan(**kwargs):
        calls.append(kwargs["plan"].target_machine_id)
        return {"success": True}

    def _fake_merge(plans, kb, sim_id, allow_bom):
        merge_called["count"] += 1
        assert len(plans) == 2
        assert sim_id == "self_repro_demo_sim2"
        return SimPlan(
            sim_id=sim_id,
            target_machine_id="multi_machine_plan",
            target_recipe_id=None,
            imports={},
            recipes=[],
            notes=[],
            build_machine=False,
            metadata={},
        )

    class _FakeKBLoader:
        def __init__(self, *_args, **_kwargs):
            pass

        def load_all(self):
            return None

    monkeypatch.setattr(demo, "execute_plan", _fake_execute_plan)
    monkeypatch.setattr(demo, "_merge_plans", _fake_merge)
    monkeypatch.setattr(demo, "KBLoader", _FakeKBLoader)
    monkeypatch.setattr(demo, "_load_kb_machine_ids", lambda _kb_root: set())
    monkeypatch.setattr(demo, "_load_snapshot", lambda _sim_dir: {"state": {}})
    monkeypatch.setattr(demo, "_load_events", lambda _sim_dir: [])

    argv = [
        "run_self_reproduction_demo.py",
        "--machine-list",
        str(machine_list),
        "--plans-dir",
        str(plans_dir),
        "--sim-root",
        str(sim_root),
        "--sim-id",
        "self_repro_demo_sim2",
        "--mode",
        "combined",
    ]
    monkeypatch.setattr("sys.argv", argv)

    assert demo.main() == 0
    assert merge_called["count"] == 1
    assert calls == ["multi_machine_plan"]
