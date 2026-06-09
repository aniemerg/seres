# Research System 設計介紹

## 目的

Research system 是一套獨立於現有 KB work queue 的平行研究任務系統。它的目標是讓多個 Codex agent 同時處理大量研究項目，讀取相關資料、截圖、文件或外部來源，並產出可驗證的結構化研究結果。

現有 KB queue 的核心是「indexer 發現 KB 缺口，agent 修 KB，gap 消失後完成」。Research system 的核心是「使用者定義一個 research mission，系統把資料切成 tasks，多個 agent 平行分析，最後彙整成研究成果、候選 KB changes 或後續 queue items」。

## 核心概念

### Research Mission

Research mission 是一次具體研究工作，例如：

- 針對 BOM 表裡的所有零件，列出 mass、function、material composition、how to make it。
- 針對一批論文，萃取製程條件、能耗、輸入輸出與不確定性。
- 針對一批 vendor components，判斷哪些應該 reuse、import、fold into parent 或成為 KB candidate。

每個 mission 都有自己的 input、instructions、schemas、tasks、outputs 和 aggregate results。

### Mission Manifest

`mission_manifest.yaml` 是 mission 的入口設定檔。它描述「這次研究任務是什麼、資料在哪裡、agent 要做什麼、結果要長什麼樣」，同時保留 `manifest` 這個軟體工程中常見的專業用語。

`manifest` 通常表示「一份機器可讀的清單或設定」。在這裡加上 `mission_` 前綴，可以同時保留專業慣例與使用者語意：這不是一般程式 manifest，而是一個 research mission 的 manifest。

## 建議目錄結構

```text
research_system/
  docs/
    research_system_design.zh.md
    research_system_design.en.md
  templates/
    mission_manifest.yaml
    instructions/
    schemas/

research_missions/
  mission_bom_parts_001/
    mission_manifest.yaml
    input/
    instructions/
    schemas/
    tasks/
    state.sqlite
    outputs/
    logs/
    aggregate/
```

`research_system/` 放系統程式、文件和範本。`research_missions/` 放每一次實際研究任務的資料與結果。

## Mission 必備文件

每個 research mission 至少需要：

```text
mission_manifest.yaml
input/
instructions/
schemas/
```

### `mission_manifest.yaml`

描述整個 mission：

- mission id
- objective
- input files
- task generation strategy
- worker prompt
- output schema
- execution settings
- completion rule
- aggregation outputs

範例：

```yaml
id: mission_bom_parts_001
mission_type: bom_part_research
objective: >
  For each unique BOM part, determine mass, function, material composition,
  and how it could be manufactured or modeled in SERES KB.

input:
  primary_file: input/bom.csv
  source_catalog: input/source_catalog.csv

task_generation:
  strategy: unique_part_or_part_family
  rules_file: instructions/task_generation_rules.md

worker:
  prompt_file: instructions/worker_prompt.md
  output_schema: schemas/part_research_result.schema.yaml
  max_attempts: 3

execution:
  max_workers: 20
  lease_ttl_seconds: 1800

completion_rule:
  type: schema_valid_result
  require_evidence: true

aggregation:
  policy_file: instructions/aggregation_policy.md
  outputs:
    - aggregate/parts_master.csv
    - aggregate/needs_review.csv
    - aggregate/kb_candidates.csv
    - aggregate/summary.md
```

### `input/`

存放原始資料，例如 BOM、PDF、截圖、datasheet、paper、OCR text 或 source catalog。原始資料應視為 immutable，不應被 worker 覆寫。

### `instructions/`

存放任務語意與研究規則，例如：

- `worker_prompt.md`
- `task_generation_rules.md`
- `evidence_policy.md`
- `aggregation_policy.md`

這一層讓同一套 research system 能處理完全不同的研究任務。

### `schemas/`

定義每個 worker result 必須符合的格式。Schema 是自動驗證與彙整的基礎，避免 agent 只產生難以處理的散文。

## 執行流程

```text
1. Create mission directory
2. Write mission_manifest.yaml, input, instructions, schemas
3. Ingest input into task files
4. Initialize state.sqlite
5. Launch N Codex workers
6. Workers lease tasks and write structured outputs
7. Validate each output against schema
8. Aggregate completed results
9. Review conflicts and low-confidence outputs
10. Optionally promote results to KB candidates or KB queue items
```

## CLI 指令

首版 research system 掛在現有 unified CLI 底下：

```bash
python -m src.cli research ingest --mission research_missions/mission_bom_parts_001
python -m src.cli research status --mission research_missions/mission_bom_parts_001
python -m src.cli research lease --mission research_missions/mission_bom_parts_001 --agent codex-01
python -m src.cli research validate-result --mission research_missions/mission_bom_parts_001 --result outputs/task_x.result.yaml
python -m src.cli research complete --mission research_missions/mission_bom_parts_001 --task task_x --agent codex-01 --result outputs/task_x.result.yaml
python -m src.cli research release --mission research_missions/mission_bom_parts_001 --task task_x --agent codex-01
python -m src.cli research gc --mission research_missions/mission_bom_parts_001
python -m src.cli research aggregate --mission research_missions/mission_bom_parts_001
```

`ingest` 會根據 mission manifest 產生 `tasks/*.json`，並初始化 `state.sqlite`。`lease` 使用 SQLite transaction，因此可支援多個 worker 同時請求工作。`complete` 會先驗證 result 是否符合 mission schema，再把 task 標成 completed。

### 指令說明

- `ingest`：讀取 `mission_manifest.yaml` 與 input 檔案，產生 `tasks/*.json`，並初始化或更新 `state.sqlite`。若 mission 已有 tasks，需加 `--reset` 才會清除舊狀態並重建。
- `status`：顯示目前 task 狀態計數，例如 `pending`、`leased`、`completed`、`needs_review`。
- `lease`：由指定 agent 取得下一個 pending task。回傳 JSON 會包含 task payload、source files、lease owner 與 lease expiration。
- `validate-result`：只驗證某個 result YAML/JSON 是否符合 mission schema，不改變 task 狀態。
- `complete`：完成某個 leased task。此指令會先驗證 result，且 result 內的 `task_id` 必須和 `--task` 一致。
- `release`：將 leased task 釋放回 `pending`。若加 `--failed`，則改放到 `needs_review`，適合證據不足或 agent 卡住的情況。
- `gc`：清理過期 lease，把 TTL 已過的 leased task 放回 `pending`。
- `aggregate`：彙整所有 completed task 的 result。`master_table.csv` 是一列一 task 的可讀摘要；`needs_review.csv` 是其中 `needs_human_review: true` 的子集；`materials_table.csv`、`evidence_table.csv`、`manufacturing_steps_table.csv` 則保存一對多明細。

## Worker 行為

每個 worker 的基本迴圈：

```text
lease task
read task payload
read relevant input/source files
follow worker_prompt
produce result YAML/JSON
validate result against schema
complete task
repeat
```

Worker 應該只寫：

```text
outputs/<task_id>.result.yaml
logs/<agent>/<task_id>.log
```

Worker 不應直接修改 `kb/`，也不應覆寫 `input/`。研究輸出應先進入 aggregate，再由 human reviewer 或後續 KB workflow 決定是否進 KB。

## BOM 零件研究範例

針對 BOM 表內所有零件，task grain 應優先採用 unique part 或 part family，而不是每一列 BOM row。這可以避免多個 agent 重複研究同一種螺絲、墊片或線材。

每個 part result 應至少包含：

- source BOM rows
- estimated mass
- function
- material composition
- how to make it
- evidence
- uncertainty
- KB modeling recommendation

範例 recommendation：

```yaml
kb_modeling_recommendation:
  action: reuse_existing
  rationale: "Equivalent fastener family already exists within acceptable scale bounds."
```

可用 action：

- `reuse_existing`
- `create_candidate`
- `fold_into_parent`
- `import`
- `exclude`
- `needs_review`

## 與現有 KB Queue 的關係

Research system 和 KB queue 應保持分工：

```text
Research system:
  Produce evidence-backed research results, candidate data, and recommendations.

KB queue:
  Fix concrete KB schema, closure, validation, and missing-reference gaps.
```

銜接方式可以是 aggregate 階段產生：

- `aggregate/kb_candidates.csv`
- `aggregate/proposed_yaml/`
- `aggregate/followup_queue.jsonl`

這樣 research system 提供有根據的候選資料，而不是讓多個 research workers 同時直接改 KB。

## 設計原則

- Keep research missions separate from KB validation queue.
- Use mission-specific instructions and schemas.
- Use structured outputs, not free-form prose.
- Preserve source traceability.
- Make uncertainty explicit.
- Prefer aggregation and review before KB mutation.
- Let many agents work in parallel, but avoid concurrent writes to KB.
