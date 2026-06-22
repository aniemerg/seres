# reAM250 BOM 研究任務包

這個資料夾只服務 reAM250 BOM 這次單次研究任務，不是通用 research
queue 系統的一部分。

## 檔案

- `agent.md` - 給 Codex agent 的 reAM250 BOM 研究指令。
- `acceptance_criteria.md` - 結果品質驗收規則，涵蓋 evidence classification、
  web-search fallback、route audit、material/mass 判斷、欄位語意與 item
  granularity。
- `research_result.schema.yaml` - 結果檔應符合的結構。
- `image_token_optimization_for_agents.md` - CAD preview image inspection 的
  token-budget 指引，包含何時適合使用 API `detail: "low"`。
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
只用於離線診斷，不作為正常 research queue run 的流程。把 CAD-derived values
寫進結果時，要先做合理 rounding：小零件 volume 約保留到 0.001 mm^3，
bounding-box dimensions 約保留到 0.01 mm，mass 則依 row 尺度保留合理精度；
除非會改變解讀，不要貼過長的 floating-point precision。

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
結果放在同一個資料夾。先檢查這張 contact sheet；只有在細節不足時才產生
需要的單一視角圖：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/<CAD file>.step" \
  --output-dir research/ream250_bom \
  --output-stem ream250_bom_row_<row>_<item> \
  --view front
```

可選視角是 `iso`、`front`、`top`、`right`。只有在四個單視角都需要時才使用
`--individual-views`。

## 研究證據規則

結果品質規則的權威文件是 `acceptance_criteria.md`。`agent.md` 是 worker SOP，
這份 README 是人類操作手冊，`research_result.schema.yaml` 是結構 contract，
`validate_results.py` 只負責可機械檢查的 subset。

高層原則：

- 先用 BOM + manifest 鎖定 row identity，再用 web/vendor evidence 補該 row 的屬性。
- BOM row、manifest、隨 BOM 提供的 CAD/STEP、local metadata、rendered preview、
  BOM-provided URL route 都屬於 `bom_provided`。
- 只有在 BOM-side evidence 沒有直接解決該值，或 BOM-side evidence 是
  placeholder/generic/conflicting 時，才使用 independent vendor/web research。
- 在寫 `engineering_hypothesis` 或 `unresolved` 前，必須做 targeted web/search，
  並在同一 section 加上 `targeted_web_search:`。
- 不同 domain 的官方 alternate route 若仍保持 `bom_provided`，使用
  `official_alternate_route_check:`。
- BOM row 有 Link URL 但使用不同 domain 的 `independent_vendor_spec` 前，使用
  `bom_url_route_check:` 說明 BOM route 為何沒有解決該值。
- `mass.value_kg` 是 BOM row 所代表的一個實體 item 的 per-unit mass。若 BOM
  quantity 不是 1，在 `mass.basis` 說明 quantity，必要時附 row total。
- material precision、mass evidence、common-density handling、field semantics、
  item granularity 等細節，以 `acceptance_criteria.md` 為準。

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
codex --search -C /home/eastrolinux/seres -s danger-full-access -a on-request
```

這個任務需要 local DNS/network 來讀 vendor pages。在目前 Codex 環境中，
`workspace-write` 可能讓 local `curl`/DNS 在連到商品頁前就失敗。
只有做 local-only debugging 時才使用 `workspace-write`。

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

### Runner Option 規格

這一節是 runner 的完整規格。下面的範例只是常用組合，不是替代規格。

| Option | 預設值 | 意義 |
|---|---:|---|
| `--repo-root PATH` | `/home/eastrolinux/seres` | repo root，也會傳給 `codex exec -C`。 |
| `--agent-prefix NAME` | `ream250-bom-agent` | worker agent name prefix，例如 `ream250-bom-agent-01`。 |
| `--workers N` | `1` | 平行 worker loop 數量。 |
| `--max-items N` | `3` | 每個 fresh Codex session 最多處理幾個 queue items。 |
| `--max-batches N` | `0` | 每個 worker 最多啟動幾個 Codex sessions；`0` 表示跑到沒有 matching pending item。 |
| `--ttl SECONDS` | `7200` | 傳給 `queue lease` 的 lease TTL。 |
| `--id-prefix PREFIX` | `research_task:ream250_bom_row_` | 傳給 `queue lease --id-prefix` 的 queue id prefix；完整 task id 可用作單筆 exact filter。 |
| `--log-dir PATH` | `out/ream250_bom_runner_logs` | batch logs 目錄；相對路徑會以 repo root 為基準。 |
| `--codex-bin PATH` | `codex` 或 `$CODEX_BIN` | Codex executable。 |
| `--codex-model MODEL` | `$CODEX_MODEL` 或 Codex config default | 傳給 `codex --model/-m` 的模型 id。用 `codex debug models` 查目前帳號可用模型。 |
| `--codex-reasoning-effort EFFORT` | `$CODEX_REASONING_EFFORT` 或 Codex config default | 以 `model_reasoning_effort` 傳給 Codex；允許值是 `low`、`medium`、`high`、`xhigh`。只對支援 reasoning level 的模型有效。 |
| `--codex-sandbox MODE` | `danger-full-access` 或 `$CODEX_SANDBOX` | 傳給 Codex 的 sandbox；允許值是 `read-only`、`workspace-write`、`danger-full-access`。 |
| `--batch-timeout SECONDS` | `0` | 每個 `codex exec` batch 的選用 timeout；`0` 表示停用。timeout 的 batch 會以非零狀態退出，並記錄到 run events 檔。 |
| `--detach` | off | 重新以 background session 啟動 runner，寫出 `run_<id>.pid` 後立刻回到 shell。適合過夜跑或 terminal 不穩定時使用。 |
| `--no-terminal-stream` | off | runner output 只寫到 run log，不把所有 worker output 串回目前 terminal。`--detach` 會自動加上這個行為。 |
| `--validate-at-end` | off | worker 結束後跑 queue/output audit，只驗證目前 queue 狀態為 `done` 的 outputs；不掃描 `research/ream250_bom` 的全部 Markdown。 |
| `--dry-run` | off | 只印出產生的 prompt 與 Codex command，不啟動 Codex。 |

當 `--max-batches` 大於 0 時，最多處理數量是 `workers * max-items *
max-batches`。例如 `--workers 2 --max-items 3 --max-batches 1` 最多跑 6 rows。
當 `--max-batches 0` 時，每個 worker 會持續啟動 fresh Codex sessions，直到沒有
matching pending queue items。

runner 預設使用 `danger-full-access`，因為 web research rows 需要 local
DNS/network access。只有 no-network/local-only debugging 才使用
`workspace-write`。

`--validate-at-end` 是 queue-aware validation。partial rerun 期間，pending 舊輸出
可能尚未符合最新 validator；runner 因此只 audit 目前標為 `done` 的 output。
只有當 `research/ream250_bom` 目錄內所有檔案都預期符合目前規則時，才使用
full-directory validation。

每次真正啟動 runner 都會在 `--log-dir` 底下寫 run-level diagnostics。
預設 run id 是 `<YYYYmmdd_HHMMSS>_<runner-pid>`，也可以用
`REAM250_BOM_RUN_ID` 覆寫。

| Diagnostic file | 意義 |
|---|---|
| `run_<run_id>.log` | runner 本身的 master stdout/stderr log，包含 worker 啟動訊息與最後 audit output。 |
| `run_<run_id>_events.tsv` | 可解析的 event log，包含 `runner_start`、`batch_start`、`batch_exit`、`signal`、`runner_exit`。 |
| `run_<run_id>.heartbeat` | 最後 heartbeat 時間。如果這個檔案停住、且沒有 `runner_exit` event，通常代表程序被外部 kill、host/session 停止，或 WSL 被硬關。 |
| `run_<run_id>_status/*.active` | active batch marker。突然停止後若仍殘留，可指出當時是哪個 worker/batch 正在跑，以及該看哪個 per-batch log。 |
| `run_<run_id>_queue_start.json`, `run_<run_id>_queue_exit.json` | start/exit 的 queue count snapshot。signal exit 也會寫 `run_<run_id>_queue_signal_<SIG>.json`。 |

如果 runner 收到 `INT`、`TERM` 或 `HUP`，會記錄 `signal` event、寫 queue snapshot，
並用慣例 signal status 退出。如果是 `SIGKILL`、斷電、WSL/session 硬終止，shell
trap 無法執行；這時用 stale heartbeat、缺少 `runner_exit`、以及殘留 active batch
marker 判斷停在哪裡。

過夜跑或 terminal 不穩定時，使用 `--detach`。父命令會印出 run id、PID file、
heartbeat path 和 log paths，然後立刻退出；背景 runner 會透過 `nohup`/`setsid`
繼續跑，進度寫在 `out/ream250_bom_runner_logs/`。

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 2 \
  --max-items 1 \
  --max-batches 30 \
  --codex-model gpt-5.5 \
  --codex-reasoning-effort medium \
  --validate-at-end \
  --detach
```

查看進度：

```bash
tail -f out/ream250_bom_runner_logs/run_<id>.log
cat out/ream250_bom_runner_logs/run_<id>_events.tsv
cat out/ream250_bom_runner_logs/run_<id>.heartbeat
```

多行 shell command 每個續行都要保留結尾的 `\`。如果少了續行符號，shell 會先啟動
runner，後面的 option 會被當成另一個命令。

### Runner 範例

標準 bounded run：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 2 \
  --max-items 3 \
  --max-batches 1 \
  --validate-at-end
```

單 worker 跑到 queue 空：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh
```

用 GPT-5.5 medium reasoning 先測一個 Codex session：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 1 \
  --max-items 1 \
  --max-batches 1 \
  --codex-model gpt-5.5 \
  --codex-reasoning-effort medium \
  --validate-at-end
```

用 GPT-5.3 Codex Spark 先測一個 Codex session：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 1 \
  --max-items 1 \
  --max-batches 1 \
  --codex-model gpt-5.3-codex-spark \
  --validate-at-end
```

只印出產生的 prompt 與 Codex command，不實際執行：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --codex-model gpt-5.5 \
  --codex-reasoning-effort medium \
  --dry-run
```

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

`queue release --id` 一次只接受一個 id，runner 的 `--id-prefix` 一次也只接受
一個 prefix。如果要重跑多個精確 row，請用完整 queue id 做 loop，每個 id 跑
一次單筆 batch：

```bash
for id in \
  research_task:ream250_bom_row_0117_3F \
  research_task:ream250_bom_row_0144_3R2
do
  .venv/bin/python -m src.cli queue release \
    --id "$id" \
    --agent rerun-targeted

  queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
    --workers 1 \
    --max-items 1 \
    --max-batches 1 \
    --id-prefix "$id"
done
```

不要為了指定重跑使用太寬的共用 prefix，例如
`research_task:ream250_bom_row_01`，因為它可能 lease 到不相關的 pending rows。

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

只有當資料夾內全部檔案都預期符合目前規則時，才用 full-directory validation。
partial rerun 期間請優先用 queue/output audit，因為 pending 舊檔可能會故意保留為
不通過最新 validator 的狀態，等待 worker 重跑。

檢查 queue/output 一致性：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/audit_queue_outputs.py
```

這個 audit 會驗證目前存在的 output files，並檢查 done queue entries 是否還有
`context.output_path`。嚴格 output-validation baseline 之前完成的歷史 done entries
可能沒有目前 artifact；這些會列為 `legacy_done_without_output_accepted`，不會讓
audit 失敗。較新的 done items 若缺 output 仍會失敗。

驗證器會檢查 frontmatter 第一個 top-level key 是否為 `row_identity`。這個
section 只保留最小 BOM row identity，再進入任何解讀。這裡只能包含以下 keys：

- `item`
- `cad_file`
- `source_row_number`
- `source_csv`: `design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv`
- `link_url`：只有 BOM row 有 Link URL 時才放；這是 BOM 表格上的原始 Link
  URL，不是 redirect/canonical 後的 final vendor URL。

驗證器也會檢查 `function`、`mass`、`material`、`how_to_make` 是否各自有
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

validator 也會在對應 evidence basis 和 URL 條件成立時，檢查部分 acceptance
markers，例如 `targeted_web_search:`、`official_alternate_route_check:`、
`bom_url_route_check:`。但它無法檢查所有 judgment rules。欄位語意、
evidence-basis 判斷、material/mass 判斷與 item granularity 規則，以
`acceptance_criteria.md` 和 `research_result.schema.yaml` 為準。

## 完成任務

research task 完成時不要加 `--verify`：

```bash
.venv/bin/python -m src.cli queue complete --id <leased-id> --agent <agent-name> --require-output --validate-output
```

這個單次研究流程期間不要跑 `python -m src.cli index`。
