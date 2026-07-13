# reAM250 BOM 轉 KB 任務包

這個任務包負責把已完成的 reAM250 BOM research row 轉成可審查的 KB staging 決策。它和原本的 BOM research task pack 分開。

系統分成三個 phase：

1. `row_conversion`：一個 task 對應一個 reAM250 BOM research row。
2. `merge_review`：一個 task 對應一個候選合併群。
3. `phase3_staging`：一個 completed merge review 對應一份 KB staging package。

Worker 不會直接寫入 `kb/`，不會跑 indexer，也不會改原始 research evidence。唯一例外是 row conversion worker 可以在每個 row 檔案底部新增或替換一段 `## KB Conversion`。

## Phase 1: Row Conversion

產生 row conversion tasks：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/generate_row_conversion_tasks.py \
  --replace-queue-prefix
```

租用 row conversion tasks：

```bash
.venv/bin/python -m src.cli queue lease \
  --agent ream250-kb-row-agent-01 \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_row_
```

Worker 讀原始 row research file，只能在底部新增或替換 `## KB Conversion` section。Validator 會比對該 section 之前內容的 baseline hash，所以如果 worker 改到原始 evidence layer，驗證會失敗。

Phase 1 的用途是先建立受控的 decision layer，再進入 merge review。每個 row 會記錄 decomposition、normalized merge identity、一個 primary process bucket、supporting process tags、candidate existing KB process IDs，以及 precision guardrails。它不建立 final KB items、recipes、provider machines，也不決定 import。

完成 row task：

```bash
.venv/bin/python -m src.cli queue complete \
  --id <leased-id> \
  --agent <agent-name> \
  --require-output \
  --validate-output
```

批次完成後對 row conversions 做 semantic validate：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/semantic_validate_row_conversions.py \
  --output research/ream250_bom/kb_conversion/semantic_validate_report.md
```

Schema validate 會檢查格式與 schema hard constraints。Semantic validate 會執行 schema validate、檢查 queue/conversion 一致性，並報告 semantic warnings，例如 functional key 過窄、process bucket 可疑、powder-containment row 被分到 enclosure barrier、local manufacturing paths 過度列舉。Hard errors 會讓指令回傳非 0。Warnings 只會列報告，除非使用 `--fail-on-warning`。

批次 QA workflow 是：

1. Schema validate 所有已完成 row conversion。
2. 只審查 `New Semantic Warnings` 裡列出的新增 warnings。
3. 審查 `Random Review Sample` 裡列出的無 warning rows，用來發現 semantic validate 還不知道的新錯誤模式。

## Phase 2: Merge Review

Row conversion tasks 完成後，產生候選合併 tasks：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/generate_merge_candidate_tasks.py \
  --replace-queue-prefix
```

Generator 會讀所有 `## KB Conversion` sections，並把符合以下條件的 rows 分組：

- `merge_pool.eligible: true`
- 相同的 `merge_pool.functional_purpose_key`
- mass 落在 2x 範圍內

Generator 不做最終合併判斷，只產生候選群。`functional_purpose_key` 只是粗略分組索引；merge review worker 必須讀每個 candidate row 的原始 research evidence 與 `## KB Conversion` section。

Phase 2 會檢查粗略候選池中的 rows 是否能在 material、process、geometry、precision 審查後收斂成同一個 closure item。它應使用詳細的原始 research evidence，不只看 Phase 1 的 functional key。

租用 merge review tasks：

```bash
.venv/bin/python -m src.cli queue lease \
  --agent ream250-kb-merge-agent-01 \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_merge_
```

Merge review worker 會把 group-level 決策寫到：

```text
research/ream250_bom/kb_conversion/merge_reviews/
```

## Phase 3: KB Staging

Phase 3 讀 completed merge review 與所有相關原始 row research files，輸出一份可人工審查的 KB staging YAML。這一步仍然不寫入 `kb/`，也不跑 indexer。

Phase 3 要決定：

- 每個 proposed closure item 要 `reuse_existing`、`create_new`、或 `defer`；
- 每個 proposed item 的 import/local manufacture decision；
- 每個 source BOM row 對應到哪個 closure item，並保留 quantity、mass、length、handedness、variant、nominal interface 等 row-level 資訊；
- 建議使用哪些既有 KB process 作為 recipe anchor；
- promotion 到正式 KB 前還有哪些 blocker。

Merge review files 存在後，產生 Phase 3 staging tasks：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/generate_phase3_staging_tasks.py \
  --replace-queue-prefix
```

租用 Phase 3 staging tasks：

```bash
.venv/bin/python -m src.cli queue lease \
  --agent ream250-kb-stage-agent-01 \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_stage_
```

Phase 3 worker output 放在：

```text
research/ream250_bom/kb_conversion/phase3_staging/
```

Maintainer 寫的 pilot examples 放在：

```text
research/ream250_bom/kb_conversion/phase3_staging_pilot/
```

驗證 Phase 3 staging file：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/schema_validate_row_conversions.py \
  --kind phase3_stage \
  --file research/ream250_bom/kb_conversion/phase3_staging/<file>.stage.yaml
```

## Reviewer Feedback Loop

Reviewer/maintainer 檢查 worker outputs 後，如果某個修正代表可重複發生的規則缺口，就要同步更新這個 task pack。結果修正與規則修正應一起前進。常見更新位置包括 `agent.md`、`acceptance_criteria.md`、`conversion_section.schema.yaml`、`research_scripts/schema_validate_row_conversions.py`、`research_scripts/semantic_validate_row_conversions.py`。

## Files

- `agent.md`：三個 phase 的 worker SOP。
- `acceptance_criteria.md`：品質規則與建模規則。
- `conversion_section.schema.yaml`：`## KB Conversion` 的必要結構。
- `merge_review.schema.yaml`：merge review 檔案的必要結構。
- `phase3_staging.schema.yaml`：Phase 3 KB staging file 的必要結構。
- `research_scripts/generate_row_conversion_tasks.py`：建立 Phase 1 queue tasks 與 baseline hashes。
- `research_scripts/generate_merge_candidate_tasks.py`：從 Phase 1 輸出建立 Phase 2 queue tasks。
- `research_scripts/generate_phase3_staging_tasks.py`：從 merge review files 建立 Phase 3 staging tasks。
- `research_scripts/schema_validate_row_conversions.py`：驗證 row conversion sections、merge review files 與 Phase 3 staging files。
- `research_scripts/semantic_validate_row_conversions.py`：row conversion 與 queue consistency 的批次 semantic warning report。
- `research_scripts/run_codex_batches.sh`：可選的小批次 Codex runner。

## Optional Batch Runner

跑一個小型 row-conversion batch：

```bash
queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/run_codex_batches.sh \
  --phase row \
  --max-items 1 \
  --max-batches 1 \
  --semantic-validate-after
```

跑較大的 row-conversion batch，並在 workers 結束後寫出 semantic validate report：

```bash
queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/run_codex_batches.sh \
  --phase row \
  --max-items 20 \
  --max-batches 1 \
  --semantic-validate-after \
  --semantic-validate-output research/ream250_bom/kb_conversion/semantic_validate_report.md \
  --semantic-validate-sample-size 5
```

跑一個小型 merge-review batch：

```bash
queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/run_codex_batches.sh \
  --phase merge \
  --max-items 1 \
  --max-batches 1
```

跑一個小型 Phase 3 staging batch：

```bash
queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/run_codex_batches.sh \
  --phase stage \
  --max-items 1 \
  --max-batches 1
```
