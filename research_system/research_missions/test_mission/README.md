# Test Mission: Manual Multi-Agent Run

This mission is a synthetic BOM research mission for validating the research
system. It currently has 10 pending tasks after ingest.

## Reset To Clean Pending Tasks

Run this before a manual multi-agent test:

```bash
.venv/bin/python -m src.cli research ingest --mission research_system/research_missions/test_mission --reset
```

Check status:

```bash
.venv/bin/python -m src.cli research status --mission research_system/research_missions/test_mission
```

Expected starting state:

```json
{
  "pending": 10
}
```

## How Two Codex Agents Should Work

Open two Codex sessions in the same repo. Give each session a different agent
name, for example `agent-a` and `agent-b`.

Do not tell agents to manually choose files from `tasks/`. Each agent must lease
tasks through the CLI so two agents do not work on the same task.

### Prompt For Agent A

```text
You are research agent-a.

Mission directory:
/home/eastrolinux/seres/research_system/research_missions/test_mission

Process research tasks for this mission until the queue is empty or you have
completed 5 tasks.

For each task:
1. Run:
   .venv/bin/python -m src.cli research lease --mission research_system/research_missions/test_mission --agent agent-a
2. If the queue is empty, stop and report all completed task IDs.
3. Read the leased task payload and source_files.
4. Follow instructions/worker_prompt.md and schemas/result.schema.yaml.
5. Write outputs/<task_id>.result.yaml.
6. Run validate-result on that output.
7. If valid, run complete for that task using --agent agent-a.
8. If you cannot complete it, run release --failed with a short message.

Do not edit KB files. Do not overwrite input files. At the end, report the task
IDs you completed and any tasks you failed/released.
```

### Prompt For Agent B

Use the same prompt, but replace `agent-a` with `agent-b`.

## Useful Commands

Lease:

```bash
.venv/bin/python -m src.cli research lease --mission research_system/research_missions/test_mission --agent agent-a
```

Validate result:

```bash
.venv/bin/python -m src.cli research validate-result --mission research_system/research_missions/test_mission --result outputs/<task_id>.result.yaml
```

Complete:

```bash
.venv/bin/python -m src.cli research complete \
  --mission research_system/research_missions/test_mission \
  --task <task_id> \
  --agent agent-a \
  --result outputs/<task_id>.result.yaml
```

Release as failed/needs review:

```bash
.venv/bin/python -m src.cli research release \
  --mission research_system/research_missions/test_mission \
  --task <task_id> \
  --agent agent-a \
  --failed \
  --message "Could not find sufficient source support."
```

Aggregate after both agents finish:

```bash
.venv/bin/python -m src.cli research aggregate --mission research_system/research_missions/test_mission
```

Aggregate outputs:

- `aggregate/master_table.csv`: one readable summary row per completed task
- `aggregate/needs_review.csv`: subset of master rows needing human review
- `aggregate/materials_table.csv`: one row per material with source file
- `aggregate/evidence_table.csv`: one row per evidence claim
- `aggregate/manufacturing_steps_table.csv`: one row per manufacturing step
- `aggregate/summary.md`: counts and output list
