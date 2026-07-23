# Agent Instructions: reAM250 BOM to KB Conversion

你正在處理 reAM250 BOM-to-KB conversion tasks。這些 tasks 使用 `research/ream250_bom/` 底下已完成的 research files 作為 source evidence。

## 只租用符合條件的 Tasks

如果 user 或 runner 提供 exact lease command，使用該 command。若沒有提供，依 phase 使用以下指令。

Row conversion：

```bash
.venv/bin/python -m src.cli queue lease \
  --agent <agent-name> \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_row_
```

Merge review：

```bash
.venv/bin/python -m src.cli queue lease \
  --agent <agent-name> \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_merge_
```

Phase 3 staging：

```bash
.venv/bin/python -m src.cli queue lease \
  --agent <agent-name> \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_kb_stage_
```

如果 queue empty，停止。

## 允許的編輯

`row_conversion` tasks 只能編輯 leased source row file：

```text
research/ream250_bom/ream250_bom_row_*.md
```

只能新增或替換檔案底部、標題完全等於以下文字的 section：

```markdown
## KB Conversion
```

不可編輯 YAML frontmatter、原始 research text、圖片檔、KB YAML、source code、docs、queue tasks 或 generated index files。

`merge_review` tasks 只能建立或更新 task output file：

```text
research/ream250_bom/kb_conversion/merge_reviews/
```

`phase3_staging` tasks 只能建立或更新 task output file：

```text
research/ream250_bom/kb_conversion/phase3_staging/
```

`phase3_staging_pilot/` 是 maintainer 寫的範例與檢討文件。處理 queue task 時不要覆蓋 pilot examples。

不要執行：

```bash
python -m src.cli index
```

## Row Conversion 目標

讀完整的原始 row research file，寫入包含 fenced YAML 的 `## KB Conversion` section。這個 section 記錄 conversion decisions，不是 source research 摘要。

做 conversion decision 前，必須使用原始 row evidence：

- `function.summary`、assumptions、uncertainty notes；
- `mass.value_kg` 與 mass basis；
- `material.primary_material` 與 material evidence；
- `how_to_make.summary` 與 manufacturing steps；
- `kb_implications`；
- 如果 geometry 會影響 conversion decision，也要讀原研究引用的 CAD preview/image evidence。

你必須判斷：

- row 是 simple part、complex module、decomposition candidate、import candidate，還是 needs human review；
- closure analysis 需要的 process abstraction。從原始 `how_to_make` 開始，選出一個 primary shared lunar process bucket。Primary bucket 是粗略 closure handle，不是完整 manufacturing recipe。用 supporting process tags 記錄 cutting、drilling、finishing、leak testing、calibration、inspection 等輔助工作。相關時，也要引用既有 `kb/processes/*.yaml` process IDs 作為 candidate；
- `process_abstraction.primary_process_bucket` 必須精確使用以下其中一個值：
  `general_metal_additive_with_finish_machining`,
  `general_subtractive_machining`, `sheet_plate_cutting_drilling`,
  `structural_profile_stock_fabrication_cutting`,
  `polymer_elastomer_forming_dispensing`,
  `manual_assembly_with_general_tools`,
  `fastener_forming_thread_rolling`,
  `plumbing_connector_fabrication_testing`,
  `precision_component_import_decompose_later`, `not_applicable`,
  `needs_human`；
- `keep_original_family` 只在原始 route 已經屬於選定 canonical bucket 時使用。如果 row-specific source route 被 generalize 到 shared bucket，使用 `substitute_process_family` 或 `add_post_processing`；
- plate-like covers、panels、guards、shallow sheet/plate parts 優先使用 `sheet_plate_cutting_drilling` 作 primary bucket。Pockets、recesses、lips、ribs、counterbores、local milled features 放進 `precision_machining` 這類 supporting processes；不要只因 source route 提到 plate stock CNC machining 就選 `general_subtractive_machining`；
- `process_abstraction.supporting_processes` 只能使用 `conversion_section.schema.yaml` 中的 vocabulary。它用來記錄預期 process chain，不把 Phase 1 擴張成 recipe authoring；
- `process_abstraction.candidate_existing_processes` 必須指向真實存在的 KB process IDs。每個 fit 標成 `direct`、`partial`、`supporting` 或 `poor_fit`。Fit 很弱也可以，但 reason 要說清楚缺口；
- 後續 merge review 需要的 normalized identity：function、material、scale/capacity、geometry form。這幾個軸要分開，不要把 material、尺寸或 geometry 寫進 `identity_for_merge.functional_purpose`；
- row 是否進入 merge candidate pool。`merge_pool.functional_purpose_key` 只能描述 function，不要把 material、process family、geometry form、精確尺寸或 mass class 寫進這個 key；
- `merge_pool.functional_purpose_key` 要夠寬，讓 Phase 2 能產生候選配對。優先使用 `plumbing_connection`，避免 `rigid_flanged_plumbing_connection_section`；優先使用 `structural_frame_member`，避免 `structural_frame_rail_member`；優先使用 `linear_guidance`，避免 `linear_guidance_carriage`；優先使用 `enclosure_barrier`，避免 `machine_enclosure_barrier_panel`。較窄的 geometry 與 interface 細節放在 `identity_for_merge.geometry_form` 與 `merge_pool.precision_guardrails`；
- recoater、powder-bed、powder-handling side plates 若功能是 containment 或 guiding powder-contact hardware，使用 `powder_containment`。不要只因為它是 plate-like part 就放進 `enclosure_barrier`；
- 後續 import/local manufacture decision 所需的輸入。Row conversion 不決定最終 import 或 local manufacture；
- `downstream_decision_inputs.local_manufacturing_paths_considered` 只記錄 selected closure path。不要只因 material unresolved 就列入無關 process buckets；材料造成的 speculative alternatives 放進 assumptions、unresolved 或 import risk factors；
- assumptions 與 unresolved issues。

除非 row 明確不可能與其他 row 合併，不要指定 final closure item ID。多數 rows 應在 merge review 前保持 `kb_staging.proposed_item_id: null`。

## Row Conversion 輸出格式

在 source row file 底部新增或替換以下 section：

````markdown
## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0002_1A1.md
source_research_sha256: "<baseline hash from task context>"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read original function, mass basis, material evidence, manufacturing route, and CAD preview before conversion."
decomposition:
  decision: simple_part
  rationale: "..."
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_machining
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - deburring
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers basic stock removal; row-specific tolerances remain guardrails."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant when bore, sliding, concentricity, and finish control matter."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks before staging selects the final recipe."
  abstraction_decision: substitute_process_family
  rationale: "..."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: structural support for machine frame and chamber interface
  material: aluminum_alloy
  scale_or_capacity:
    mass_kg: 41.21
    scale_class: large
  geometry_form: machined_plate_frame
merge_pool:
  eligible: true
  functional_purpose_key: structural_machine_frame_member
  precision_guardrails:
    - flatness
    - alignment_accuracy
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors: []
  post_merge_decision_notes: "Final import/local decision is deferred until after merge review."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before final item ID."
assumptions:
  - "..."
unresolved:
  - "..."
```
````

## Merge Review 目標

讀 task context 中列出的所有 candidate row files。使用原始 research 與各 row 的 `## KB Conversion` sections，判斷 candidate rows 是否收斂到同一個 closure item。

Candidate group 只代表 same functional purpose key 與 2x mass window。`functional_purpose_key` 只是 task generation 用的粗略索引，不可只靠這個 key 做 merge decision。

對每個 candidate row，必須讀：

- 原始 row research frontmatter；
- 原始 `function`、`mass`、`material`、`how_to_make`、`kb_implications` sections；
- 底部 `## KB Conversion` section；
- geometry 或 precision 不清楚時的 CAD preview/image evidence。

接著審查：

- material 是否可統一；
- process 是否可統一；
- geometry form 是否可統一；
- precision 是否阻止合併。

寫出一個符合 `merge_review.schema.yaml` frontmatter 的 merge review Markdown file。

## Phase 3 Staging 目標

讀 completed merge review、所有 candidate row 原始 research files、以及 row 底部 `## KB Conversion` sections，寫出一份符合 `phase3_staging.schema.yaml` 的 YAML staging file。

Phase 3 不直接寫入 `kb/`。它的工作是把 Phase 2 decision 轉成可人工審查的 KB promotion proposal。

你必須判斷：

- 每個 proposed closure item 是 `reuse_existing`、`create_new`、還是 `defer`；
- 每個 proposed item 是 import、local manufacture、local manufacture candidate with recipe gap、local manufacture candidate with precision guardrails、reuse existing local recipe、還是 needs human；
- 每個 source BOM row map 到哪個 closure item，並保留 quantity、row total mass、length、handedness、variant、nominal interface、thread size、sealing、coating、precision guardrails；
- 哪些既有 KB process 可以作為 candidate recipe anchors；
- promotion 到正式 KB 前有哪些 blockers。

做 `reuse_existing` 或 `create_new` 決策前，必須搜尋現有 KB。優先重用既有 item，除非現有 item 的 function、material、scale/capacity、geometry form 或 closure-relevant guardrails 明顯不足。

Import/local 判斷參考現有 KB 模式：

- 目前 KB 做不到、短期不值得展開、或高度專用且 closure 影響低的項目，可標記為 import；
- advanced optics、electronics、precision reducers、high-grade sensors、specialty materials 通常偏向 import；
- structural、machined、sheet、profile、ordinary fastener 類機械件，只要有合理 process anchor，通常先當 local manufacture candidate，而不是直接 import；
- import/local 是 closure boundary decision，不代表已經完成 final recipe。

`create_new` proposed item 必須提供 KB-like fields，例如 `id`、`kind`、`unit`、`unit_kind`、`material_class`、`notes`。`reuse_existing` 必須提供 existing KB path。所有 proposed item 都必須有 `promotion_blockers`；如果目前沒有已知 blocker，也要明確寫 `none_known`。

## 完成

驗證並完成 task：

```bash
.venv/bin/python -m src.cli queue complete \
  --id <leased-id> \
  --agent <agent-name> \
  --require-output \
  --validate-output
```
