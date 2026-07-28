# EBF3 ChatGPT Review: Machining Basic Remaining Definition Issues

目的：以下只列目前仍未能直接用 `Machining (Basic)` / `multi_axis_cnc_machining_center` 判定的項目。多數幾何型 CNC 問題已改為 `keep_flagged_local`。

請判斷這些項目應如何定義，並建議是 `keep_flagged_local`、`needs_new_process_chain`、`import_until_gap_resolved` 或 `reroute_existing_process`。

## Current Process Under Review

- Process ID: `machining_basic_v0`
- Process name: Machining (Basic)
- Process notes: Basic machining operation; placeholder for converting raw metal block to machined_metal_block_v0.
- Resource machine: `multi_axis_cnc_machining_center` (Multi-axis CNC machining center)
- Machine notes: High-function multi-axis CNC machining cell. Covers milling, turning/turn-mill work, drilling, tapping, boring, reaming, contour and freeform finishing, chamfering, deburring, limited tool-based polishing, and on-machine probing/basic dimensional checks. It does not by itself close material heat treatment, magnetic-property control, chemical cleaning, specialized coating, or independent functional qualification.

## Items To Review

### 1. `ebf3_spool_retaining_ring`

- Name: EBF3 spool retaining ring
- Item intro / notes: WF-4. Retaining ring preventing spool/hub axial displacement. Intentional Level-2 single-part leaf; groove geometry and spring material remain later material/process details. See research/ebf3_bom_sources/organized/wire_feeder_level_2_audit.md. First-pass manufacturing/import route is recorded in the linked EBF3 route-review recipe.
- Mass: 0.03 kg
- Material field: metal
- Route material basis in route review: steel_retaining_ring
- Current recipe: `recipe_ebf3_spool_retaining_ring`
- Current process: `machining_basic_v0`
- Recipe inputs for this step: raw_metal_block: 0.0315 kg
- Recipe outputs for this step: ebf3_spool_retaining_ring: 1.0 unit
- Worker note: Three-layer review: CNC may be sufficient for one interpretation, but item definition is ambiguous. Definition split required: rigid collar/retaining ring is CNC-local; spring snap ring needs spring material, forming, heat treatment and fatigue validation.

Question: Which physical interpretation should this item use, and does that make the current CNC route sufficient?

### 2. `ebf3_wire_feed_encoder_target`

- Name: EBF3 wire feed encoder target
- Item intro / notes: Child of ebf3_wire_feed_encoder_sensor. Encoder target for EBF3 wire feed encoder sensor.
- Mass: 0.08 kg
- Material field: metal
- Route material basis in route review: steel_encoder_target
- Current recipe: `recipe_ebf3_wire_feed_encoder_target`
- Current process: `machining_basic_v0`
- Recipe inputs for this step: raw_metal_block: 0.084 kg
- Recipe outputs for this step: ebf3_wire_feed_encoder_target: 1.0 unit
- Worker note: Three-layer review: CNC may be sufficient for one interpretation, but item definition is ambiguous. Definition split required: simple metal index target is CNC-local; optical scale, multipole magnetic ring, or encoded target needs a separate process route.

Question: Which physical interpretation should this item use, and does that make the current CNC route sufficient?
