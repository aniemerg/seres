from src.simviewer.exporter import _extract_process_runs


def test_extract_process_runs_includes_goal_context_from_events():
    events = [
        {
            "type": "process_scheduled",
            "process_run_id": "run-1",
            "process_id": "process_a",
            "scheduled_start_time": 10.0,
            "scheduled_end_time": 20.0,
            "goal_context": {
                "goal_id": "goal-abc",
                "tags": {"exp.variant": "v1", "priority": "critical"},
            },
            "inputs_consumed": {},
            "machine_reservations": [],
        },
        {
            "type": "process_complete",
            "process_run_id": "run-1",
            "process_id": "process_a",
            "time_hours": 20.0,
            "outputs": {},
        },
    ]

    process_runs, _, _ = _extract_process_runs(events, recipe_id_by_run_id={})
    assert len(process_runs) == 1
    run = process_runs[0]
    assert run.goal_context.get("goal_id") == "goal-abc"
    assert run.goal_context.get("tags", {}).get("exp.variant") == "v1"
    assert run.goal_context.get("tags", {}).get("priority") == "critical"
