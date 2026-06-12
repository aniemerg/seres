# reAM250 BOM 研究任務包

這個資料夾只服務 reAM250 BOM 這次單次研究任務，不是通用 research
queue 系統的一部分。

## 檔案

- `agent.md` - 給 Codex agent 的 reAM250 BOM 研究指令。
- `research_result.schema.yaml` - 結果檔應符合的結構。
- `research_scripts/generate_queue_tasks.py` - 從 gold CSV/manifest 產生 queue
  items，可選擇用 FreeCAD 抽 STEP metadata。
- `research_scripts/render_step_views.py` - 從 STEP 檔產生 compact 2x2 PNG CAD
  preview，供低 image-token 視覺檢查。
- `research_scripts/render_step_views.sh` - preview renderer 的 FreeCAD 包裝器；
  agent prompt 應使用這支腳本。
- `research_scripts/validate_results.py` - 檢查 Markdown/YAML/JSON 結果檔的本地驗證器。
- `research_scripts/run_codex_batches.sh` - 選用的 batch runner，會反覆啟動新的
  `codex exec` session。

## Queue 條件

queue 裡的任務應該符合：

- `kind: research`
- `gap_type: research_task`
- ID 以 `research_task:ream250_bom_row_` 開頭
- `context.output_path` 位於 `research/ream250_bom/`
- `context.output_validator` 指到這個任務包的 validator

從 gold CSV/manifest 產生或刷新 401 筆 queue items：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/generate_queue_tasks.py \
  --replace-queue-prefix
```

這只會替換 ID 以 `research_task:ream250_bom_row_` 開頭的既有 queue entries。

CAD 幾何資料刻意由 agent 在 lease 到特定 row 後才讀取。`--extract-cad-metadata`
只用於離線診斷，不作為正常 research queue run 的流程。

Agent 也應該把 lease 到的 canonical STEP 檔 render 成一張 compact 2x2 contact
sheet，用於視覺初篩：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/<CAD file>.step" \
  --output-dir research/ream250_bom \
  --output-stem ream250_bom_row_<row>_<item>
```

輸出會寫到
`research/ream250_bom/ream250_bom_row_<row>_<item>__views_2x2.png`，和 Markdown
結果放在同一個資料夾。先檢查這張 contact sheet；只有在細節不足時才加
`--individual-views` 產生單一視角圖。

## 研究證據規則

判斷流程：

- 先用 BOM + manifest 鎖定 row identity。Web/vendor 證據只能補這個 identity
  的缺漏屬性，不應把 row 重新解讀成另一個產品。
- 如果 BOM row 直接寫出該值，使用 `bom_row`，不要為了反查而上網質疑它。
- 只有在 BOM/CAD/本地證據沒有直接解決該值，或本地證據是 placeholder/generic/
  conflict 時，才用 vendor/web research 補資料。

`evidence_basis` 標籤：

允許的 `evidence_basis` 是證據來源類型，不是全域真實性排名：

- BOM row 本身寫出該值 -> `bom_row`
- vendor/catalog/drawing/product page 明確寫出 matched product 的該值 -> `vendor_spec`
- FreeCAD geometry、STEP metadata、CAD preview、manifest 或本地抽取資料支持該值 -> `cad_or_local_metadata`
- DIN/ISO/SKF/SMC 等 designation 或標準件類型支持該值 -> `standard_part_convention`
- 根據功能、裝配脈絡、可見形狀或製造路徑推論 -> `engineering_hypothesis`
- 已檢查的證據仍不支持可靠值 -> `unresolved`

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
Read queue_tasks/research_pack/ream250_bom_research/agent.md and follow it as ream250-bom-agent-01.
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
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh
```

兩個 worker，每個新的 Codex session 最多處理 3 rows：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 2 \
  --max-items 3
```

先測一個 Codex session：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --max-batches 1
```

只印出產生的 prompt，不實際執行 Codex：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh --dry-run
```

log 預設會寫到 `out/ream250_bom_runner_logs/`。

### 指定 Row 重跑

runner 有選用的 `--id-prefix` filter。不加時會使用正常的寬 prefix：

```text
research_task:ream250_bom_row_
```

這個預設值代表「任何 reAM250 BOM research row」。正常批次執行不需要加
`--id-prefix`。

它叫 `--id-prefix` 是因為 queue lease API 用的是 `startswith(...)` 過濾，
不是 exact-id matching。把完整 queue id 傳進去仍然等同於指定單一 row，
因為完整 id 也是它自己的 prefix。

如果要重跑已完成 row，先把該 queue item release 回 `pending`，再用完整
queue id 當 prefix 跑一個單筆 batch：

```bash
.venv/bin/python -m src.cli queue release \
  --id research_task:ream250_bom_row_0195_6Q \
  --agent rerun-targeted

queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 1 \
  --max-items 1 \
  --max-batches 1 \
  --id-prefix research_task:ream250_bom_row_0195_6Q
```

runner prompt 會要求 agent 在重新檢查證據後覆寫既有 output file。若你是在測試
是否真的重寫，請檢查檔案 mtime，或看 log 裡是否有實際寫檔動作。

用一行 shell loop 重跑前三筆 smoke-test 結果：

```bash
for id in research_task:ream250_bom_row_0308_174 research_task:ream250_bom_row_0195_6Q research_task:ream250_bom_row_0380_4122; do .venv/bin/python -m src.cli queue release --id "$id" --agent rerun-targeted && queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh --workers 1 --max-items 1 --max-batches 1 --id-prefix "$id"; done
```

### Runner 風險

- 如果 Codex session 在 lease 任務後中斷，該任務會維持 leased 到 TTL
  過期。TTL 到期後可跑 `.venv/bin/python -m src.cli queue gc` 回收。
- 平行 worker 會增加 web search/API 使用量，也更容易遇到外部 rate limit。
  建議先從 `--workers 1` 或 `--workers 2` 開始。
- runner 執行時不要跑 `python -m src.cli index`。這個流程把 research queue
  當作狀態來源。
- runner 不保證研究品質；它只負責限制 context 並自動啟動新的 Codex
  session。結果格式與 source 欄位仍要用 `research_scripts/validate_results.py` 檢查。

## 驗證結果

驗證單一檔案：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/validate_results.py \
  --file research/ream250_bom/ream250_bom_row_0001_11.md
```

驗證整個資料夾：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/validate_results.py \
  --dir research/ream250_bom
```

驗證器會檢查 `function`、`mass`、`material`、`how_to_make` 是否各自有
source object，且包含：

- `url_or_path`
- `cited_fact_or_basis`
- `evidence_basis`

同樣四個 section 也都必須各自包含 section-local list：

- `assumptions`
- `uncertainty_notes`

請把假設和不確定性放在影響到的 section 裡。例如材料查不到放在
`material.uncertainty_notes`，CAD 密度造成的質量 caveat 放在
`mass.uncertainty_notes`，製造路徑推論放在 `how_to_make.assumptions` 或
`how_to_make.uncertainty_notes`。`kb_implications` 保持 top-level list。

## 完成任務

research task 完成時不要加 `--verify`：

```bash
.venv/bin/python -m src.cli queue complete --id <leased-id> --agent <agent-name> --require-output --validate-output
```

這個單次研究流程期間不要跑 `python -m src.cli index`。
