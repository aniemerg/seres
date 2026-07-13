---
row_identity:
  item: "1B2"
  cad_file: "1B2_handle"
  source_row_number: 10
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.ganternorm.com/de/produkte/1.2-Bedienen-mit-Maschinen-und-Geraetegriffen/Buegelgriffe/GN-328.5-Edelstahl-Buegelgriffe#l1%3Dc(120)%3BForm%3Du(5e72aa81-7282-4de6-aa3f-99d6b8e98e5d)%3BOberfl%C3%A4che%3Du(5ac173de-c979-4e10-ab22-480f0ce07560)"
function:
  summary: "Stainless steel U-shaped machine/device bow handle used as a manually gripped pull or carry handle on the reAM250 assembly, with two mounting ends and underside finger recesses for ergonomic grip."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B2_handle.step; research/ream250_bom/ream250_bom_row_0010_1B2__views_2x2.png; https://www.ganternorm.com/de/produkte/1.2-Bedienen-mit-Maschinen-und-Geraetegriffen/Buegelgriffe/GN-328.5-Buegelgriffe-Edelstahl"
    cited_fact_or_basis: "BOM row 10 identifies item 1B2, quantity 1, CAD file 1B2_handle, product GN 328.5-140-B-GS, manufacturer GanterNorm. The manifest maps row 10 to gold_export/parts/1B2_handle.step as a matched_existing vendor_component. FreeCAD measured one solid with bounding box 166.50 x 60.03 x 28.00 mm; the rendered contact sheet shows a U-shaped handle with two mounting ends and finger recesses. The Ganter BOM URL canonical route identifies GN 328.5 as stainless steel precision-cast bow handles and states that the handles are stable, ergonomic, and have finger recesses on the underside."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted as a pull/carry handle because the BOM name is handle, the supplier product family is a bow-handle family, and the CAD preview shows the matching U-handle geometry."
  uncertainty_notes:
    - "The local evidence does not identify the exact panel, cover, or door face that this specific handle mounts to."
mass:
  value_kg: 0.56
  basis: "FreeCAD volume 69,983.609 mm^3 equals 0.000069983609 m^3. Using the local stainless_steel density constant of 8000 kg/m^3 gives 0.560 kg per handle. BOM quantity is 1, so the row total is also about 0.56 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B2_handle.step; kb/materials/properties.yaml; https://www.ganternorm.com/de/produkte/1.2-Bedienen-mit-Maschinen-und-Geraetegriffen/Buegelgriffe/GN-328.5-Buegelgriffe-Edelstahl"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 69,983.609 mm^3, area 18,157.086 mm^2, and bounding box 166.50 x 60.03 x 28.00 mm. The Ganter BOM URL canonical route identifies the part family as stainless steel precision casting 1.4408. kb/materials/properties.yaml lists stainless_steel density as 8000 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "Generic stainless_steel density is used as the density constant for stainless precision-cast 1.4408 because the local density table has stainless steel but no separate 1.4408 entry."
    - "The isolated STEP solid volume is used as the physical-volume proxy for one purchased handle."
  uncertainty_notes:
    - "The assembly STEP material extractor returned only placeholder material Generic with density 1000.0, so it was not used for mass."
    - "The Ganter/Hanser page HTML exposed a displayed weight of 0.318 kg while also showing a default selected article number for a 120-A variant; because this row and CAD geometry are GN 328.5-140-B-GS with a 166.5 mm envelope, the CAD-volume estimate is used for this row."
material:
  primary_material: "Stainless steel precision casting 1.4408, matte blasted GS finish"
  source:
    url_or_path: "https://www.ganternorm.com/de/produkte/1.2-Bedienen-mit-Maschinen-und-Geraetegriffen/Buegelgriffe/GN-328.5-Buegelgriffe-Edelstahl"
    cited_fact_or_basis: "The Ganter BOM URL canonical route identifies GN 328.5 as stainless steel precision-cast bow handles and lists execution as Edelstahl-Feinguss 1.4408 with matt blasted GS finish."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The row-specific assembly STEP material metadata was placeholder Generic, so material is taken from the BOM-provided manufacturer route rather than STEP material metadata."
how_to_make:
  summary: "Treat it as a stainless precision-cast handle with finish machining of the mounting features and matte blasting"
  manufacturing_steps:
    - "Receive and inspect the handle against the CAD envelope and mounting-end geometry."
    - "For a local manufacturing approximation, investment-cast stainless steel 1.4408 to the U-handle shape, finish-machine or drill the mounting holes/counterbores for the Form B interface, deburr, and matte blast the surface."
    - "Install with the mating fasteners or mounting hardware required by the reAM250 panel or door assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B2_handle.step; research/ream250_bom/ream250_bom_row_0010_1B2__views_2x2.png; https://www.ganternorm.com/de/produkte/1.2-Bedienen-mit-Maschinen-und-Geraetegriffen/Buegelgriffe/GN-328.5-Buegelgriffe-Edelstahl"
    cited_fact_or_basis: "BOM row 10 gives product GN 328.5-140-B-GS and manufacturer GanterNorm. The Ganter BOM URL canonical route identifies GN 328.5 as stainless steel precision-cast bow handles, material 1.4408, finish GS matte blasted, and includes Form B in the product-family variants. The CAD preview shows a single U-shaped handle with two mounting ends."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local manufacturing approximation is inferred from the sourced precision-cast material description and visible mounting geometry; the source does not provide a full process plan."
  uncertainty_notes:
    - "Targeted_web_search: BOM-provided Ganter URL and canonical Ganter page were checked first"
kb_implications:
  - "item_granularity: simple_part - model later as one catalog stainless steel bow handle GN 328.5-140-B-GS; do not split into raw casting, finish, and mounting features unless this handle becomes a major import-mass contributor."
---

Research result for reAM250 BOM row 10.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0010_1B2.md
source_research_sha256: "437112cf4efc5c394dc584d96c90a5106ae56896bd8f0457559f593f80ab5e7b"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the vendor handle function, CAD-derived mass, stainless precision-cast material evidence, manufacturer route, and U-handle geometry before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one stainless U-shaped bow handle with two mounting ends and grip recesses; mounting fasteners plus mating panel hardware belong to separate rows."
  proposed_subparts: []
process_abstraction:
  original_process_family: stainless_precision_casting_with_finish_machining
  primary_process_bucket: general_metal_additive_with_finish_machining
  supporting_processes:
    - additive_build
    - support_removal
    - drilling
    - precision_machining
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: wire_arc_additive_manufacturing_v0
      fit: partial
      reason: "Provides a metal additive anchor for near-net stainless handle geometry, but small ergonomic features need finish machining."
    - process_id: metal_casting_basic_v0
      fit: poor_fit
      reason: "Matches the vendor precision-cast evidence only at a coarse casting level; it adds mold dependency and does not capture the selected closure path."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers finish machining of mounting faces, drilled interfaces, and local cleanup after near-net forming."
    - process_id: surface_finishing_basic_v0
      fit: supporting
      reason: "Covers matte blasting style surface finishing, deburring, and grip-surface cleanup."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks of mounting spacing, envelope, and ergonomic clearance."
  abstraction_decision: substitute_process_family
  rationale: "The source route is stainless precision casting, but the lunar closure model can reduce tooling diversity by treating this non-critical custom handle as a near-net metal additive part with machined mounting features and basic finishing."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: low
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: manually gripped pull and carry handle for a machine panel
  material: stainless_steel
  scale_or_capacity:
    mass_kg: 0.56
    bom_quantity: 1
    row_total_mass_kg: 0.56
    scale_class: small
  geometry_form: u_shaped_bow_handle_with_two_mounting_ends_and_finger_recesses
merge_pool:
  eligible: true
  functional_purpose_key: manual_handle
  precision_guardrails:
    - mounting_hole_spacing
    - grip_clearance
    - surface_finish
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_metal_additive_with_finish_machining
  import_risk_factors:
    - "Vendor catalog part has stainless precision-cast finish and ergonomic recess details that may be cheaper to import if handle mass remains low."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review; this row can likely merge with other non-precision machine handles if material and mounting scale remain compatible."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with other machine handles before assigning a closure item ID."
assumptions:
  - "The handle is structurally non-critical beyond normal manual pull and carry loads."
  - "Exact Ganter finish can be approximated by local deburring and matte surface finishing for closure analysis."
  - "Mounting fasteners and panel inserts are modeled through other rows."
unresolved:
  - "The mounted panel location and load rating are not identified in the local evidence."
  - "Manufacturer page weight conflicts with CAD-volume estimate for this row-specific variant; the conversion keeps the CAD-derived mass."
```
