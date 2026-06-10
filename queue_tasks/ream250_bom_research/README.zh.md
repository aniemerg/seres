# reAM250 BOM 研究任務包

這個資料夾只服務 reAM250 BOM 這次單次研究任務，不是通用 research
queue 系統的一部分。

## 檔案

- `instructions/agent.md` - 給 Codex agent 的 reAM250 BOM 研究指令。
- `schemas/research_result.schema.yaml` - 結果檔應符合的結構。
- `scripts/validate_results.py` - 檢查 Markdown/YAML/JSON 結果檔的本地驗證器。

## Queue 條件

queue 裡的任務應該符合：

- `kind: research`
- `gap_type: research_task`
- ID 以 `research_task:ream250_bom_row_` 開頭
- `context.output_path` 位於 `research/ream250_bom/`

租任務時使用 hard filters：

```bash
.venv/bin/python -m src.cli queue lease \
  --agent ream250-bom-agent-01 \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_bom_row_
```

## Agent 使用方式

在 repo root 開 Codex：

```bash
cd /home/eastrolinux/seres
codex --search -C /home/eastrolinux/seres -s workspace-write -a on-request
```

進入 Codex 後貼：

```text
Read queue_tasks/ream250_bom_research/instructions/agent.md and follow it as ream250-bom-agent-01.
```

不同 terminal 使用不同 agent 名稱，例如 `ream250-bom-agent-02`。

## 每個 Session 的工作上限

每個 agent session 最多處理 3 筆 queue item。做完 3 筆就停，下一輪重新開
或 `/clear`。這可以降低 web research 把 context 撐爆的機率，也比較容易恢復。

## 驗證結果

驗證單一檔案：

```bash
.venv/bin/python queue_tasks/ream250_bom_research/scripts/validate_results.py \
  --file research/ream250_bom/ream250_bom_row_0001_11.md
```

驗證整個資料夾：

```bash
.venv/bin/python queue_tasks/ream250_bom_research/scripts/validate_results.py \
  --dir research/ream250_bom
```

驗證器會檢查 `function`、`mass`、`material`、`how_to_make` 是否各自有
source object，且包含：

- `url_or_path`
- `cited_fact_or_basis`
- `confidence`

## 完成任務

research task 完成時不要加 `--verify`：

```bash
.venv/bin/python -m src.cli queue complete --id <leased-id> --agent <agent-name>
```

這個單次研究流程期間不要跑 `python -m src.cli index`。
