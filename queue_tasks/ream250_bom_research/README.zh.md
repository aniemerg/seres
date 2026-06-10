# reAM250 BOM 研究任務包

這個資料夾只服務 reAM250 BOM 這次單次研究任務，不是通用 research
queue 系統的一部分。

## 檔案

- `instructions/agent.md` - 給 Codex agent 的 reAM250 BOM 研究指令。
- `schemas/research_result.schema.yaml` - 結果檔應符合的結構。
- `scripts/validate_results.py` - 檢查 Markdown/YAML/JSON 結果檔的本地驗證器。
- `scripts/run_codex_batches.sh` - 選用的 batch runner，會反覆啟動新的
  `codex exec` session。

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

## 自動 Batch Runner

如果要跑大量 rows，不要手動一直 `/clear` 或開新 terminal。可以使用這個
task-local runner；它每一小批都會啟動新的 `codex exec`，所以 context 不會
在整份 BOM 期間持續累積。

保守預設：

```bash
queue_tasks/ream250_bom_research/scripts/run_codex_batches.sh
```

兩個 worker，每個新的 Codex session 最多處理 3 rows：

```bash
queue_tasks/ream250_bom_research/scripts/run_codex_batches.sh \
  --workers 2 \
  --max-items 3
```

先測一個 Codex session：

```bash
queue_tasks/ream250_bom_research/scripts/run_codex_batches.sh \
  --max-batches 1
```

只印出產生的 prompt，不實際執行 Codex：

```bash
queue_tasks/ream250_bom_research/scripts/run_codex_batches.sh --dry-run
```

log 預設會寫到 `out/ream250_bom_runner_logs/`。

### Runner 風險

- 如果 Codex session 在 lease 任務後中斷，該任務會維持 leased 到 TTL
  過期。TTL 到期後可跑 `.venv/bin/python -m src.cli queue gc` 回收。
- 平行 worker 會增加 web search/API 使用量，也更容易遇到外部 rate limit。
  建議先從 `--workers 1` 或 `--workers 2` 開始。
- runner 執行時不要跑 `python -m src.cli index`。這個流程把 research queue
  當作狀態來源。
- runner 不保證研究品質；它只負責限制 context 並自動啟動新的 Codex
  session。結果格式與 source 欄位仍要用 `scripts/validate_results.py` 檢查。

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
