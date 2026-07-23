# reAM250 BOM to KB Conversion Acceptance Criteria

## AC-001: 保留 Evidence Layer

Row conversion tasks 中，worker 不得修改 `## KB Conversion` 之前的任何內容。Validator 會把該區域與建立 row conversion tasks 時產生的 baseline hash 比對。

## AC-002: Conversion 是 Decision Layer

`## KB Conversion` section 不應只是重述 research row。它必須記錄 KB staging 需要的建模決策：

- 已讀取的原始 row evidence；
- decomposition decision；
- closure analysis 需要的 process abstraction；
- normalized merge identity；
- merge eligibility；
- 後續 import/local decision 所需的輸入；
- assumptions 與 unresolved issues。

## AC-003: 使用目前專案目標

Conversion 的目標是 lunarized closure analysis。它不是忠實重建 commercial BOM，也不是自由重新設計。只有當細節會影響 closure、simulation、process capability、material choice 或 precision risk 時，才保留到 conversion decision 中。

## AC-004: 合併前先處理拆解

Complex modules、vendor assemblies、electronics/control modules、motor/gearbox assemblies、laser/optics subassemblies、powder handling modules 等，如果其內部 closure dependencies 重要，應在 merge review 前標記為需要 decomposition。

## AC-005: 製程抽象

Process abstraction 必須從原始 `how_to_make` evidence 開始，接著把 item 放進最簡單且相容的 shared lunar process bucket。Primary bucket 是 closure-analysis handle，不是完整 manufacturing recipe。Metal additive manufacturing 對 compatible custom metal parts 是優先候選，因為它可能降低 process diversity，但它不是每一列都必須套用的替代製程。

使用這些 canonical `process_abstraction.primary_process_bucket` values：

- `general_metal_additive_with_finish_machining`
- `general_subtractive_machining`
- `sheet_plate_cutting_drilling`
- `structural_profile_stock_fabrication_cutting`
- `polymer_elastomer_forming_dispensing`
- `manual_assembly_with_general_tools`
- `fastener_forming_thread_rolling`
- `plumbing_connector_fabrication_testing`
- `precision_component_import_decompose_later`
- `not_applicable`
- `needs_human`

Worker 必須說明為何選擇 primary bucket，列出 `conversion_section.schema.yaml` 中允許的 supporting process tags，並在 `process_abstraction.candidate_existing_processes` 引用相關 existing KB process IDs。Candidate processes 是後續 staging 的 evidence anchors；它們不建立 recipes，也不強迫 final provider machine。

Process abstraction 必須檢查是否能滿足 item function 所需的 tolerance、surface finish、sealing quality、alignment accuracy。若 primary bucket 需要 secondary work，寫入 `supporting_processes` 與 process candidate reasons。`keep_original_family` 只在 original route 已落在 chosen canonical bucket 時使用。

Plate-like covers、panels、guards、shallow sheet/plate parts 通常應使用 `sheet_plate_cutting_drilling` 作 primary bucket。Local pockets、recesses、lips、ribs、counterbores、milled details 是 supporting work，不能單獨成為把 primary bucket 改成 `general_subtractive_machining` 的理由。

## AC-006: Merge Eligibility

Merge candidate pool 是粗略篩選池，不是 merge decision。Row 只有在具備 normalized functional purpose key、mass 或 scale information、material identity、geometry form，且沒有已知理由必須在 group-level review 前保持獨立時，才可進入 merge pool。

`functional_purpose_key` 只是 candidate generation 的索引。它不能取代原始 research row 中完整的 function summary、assumptions、uncertainty notes、material evidence、mass basis、manufacturing evidence。
它只能表示 functional purpose。不要把 material、process family、geometry form、精確尺寸或 mass class 寫進這個 key；這些欄位會在 Phase 2 才審查。

這個 key 也不能窄到阻止明顯的 Phase 2 candidate generation。使用較寬的 function labels，例如 `plumbing_connection`、`structural_frame_member`、`linear_guidance`、`enclosure_barrier`。flanged section、rail、carriage、panel、cut length、slot pattern、interface shape 這類 component form details 放在 `identity_for_merge.geometry_form` 與 `merge_pool.precision_guardrails`。

Recoater、powder-bed、powder-handling side plates 若功能是 containment 或 guiding powder-contact hardware，使用 `powder_containment`。不要只因 item 是 plate 就使用 `enclosure_barrier`。

同理，`identity_for_merge.functional_purpose` 應描述 item 的功能角色。Material 放在 `identity_for_merge.material`，mass/scale 放在 `identity_for_merge.scale_or_capacity`，shape 放在 `identity_for_merge.geometry_form`。

`downstream_decision_inputs.local_manufacturing_paths_considered` 應描述 selected closure path，不要列出 material unresolved 所暗示的所有可能 route。材料造成的 speculative alternatives 放進 assumptions、unresolved 或 import risk factors。

## AC-007: Merge Review

Merge review 從 same functional purpose 與 2x mass/scale candidates 開始。Worker 接著判斷 material、process、geometry 是否能透過 lunarized design 調整成同一個 closure item。Precision guardrails 可以阻止合併。

Merge review worker 必須讀每個 candidate row 的原始 research evidence 與 `## KB Conversion` section。不得只根據 `functional_purpose_key` 決定是否合併。

## AC-008: Conservative KB Creation

提出新的 closure item 前，先考慮 existing KB equivalents。若 candidate 可在 project equivalence rules 內 reuse 既有 item，記錄 reuse，而不是創造新的 ID。

## AC-009: 只做 Staging

這個 task pack 不寫入 `kb/`。KB-like YAML 應放在未來的 staging directory，並在 promotion 前人工審查。

## AC-010: 延後 Import/Local Decision

最終 import/local manufacture decision 應在 lunarized process strategy 與 formal merge review 之後進行，這符合 BOM-to-KB plan。Row conversion 可以記錄已考慮的 local manufacturing paths 與 import risk factors，但不能決定最終 import 或 local manufacture。Merge review 可以記錄 manufacturing implications，但最終 decision 屬於後續 KB staging phase。
