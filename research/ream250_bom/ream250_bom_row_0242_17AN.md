---
row_identity:
  item: "17AN"
  cad_file: "17AN_cover_sheet_hood_top"
  source_row_number: 242
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Top hood cover sheet/panel for the reAM250 enclosure group, likely closing or shielding the upper hood area while leaving a central opening or clearance cutout."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AN_cover_sheet_hood_top.step; research/ream250_bom/ream250_bom_row_0242_17AN__views_2x2.png"
    cited_fact_or_basis: "BOM row 242 identifies item 17AN as quantity 1 with CAD file 17AN_cover_sheet_hood_top. FreeCAD measured one solid with bounding box 221.40 x 428.00 x 2.00 mm. The rendered preview shows a thin U-shaped sheet panel with a large central opening."
    evidence_basis: "bom_provided"
  assumptions:
    - "The terms cover_sheet and hood_top describe the installed function because no separate product description or vendor page is present."
  uncertainty_notes:
    - "Exact mating surfaces and whether the panel is a removable service cover or fixed enclosure skin are not resolved from this isolated row."
mass:
  value_kg: 0.706
  basis: "Per unit for quantity 1. FreeCAD measured volume 89929.200 mm^3, equivalent to 0.0000899292 m^3. Planning estimate uses generic steel density 7850 kg/m^3 from kb/materials/properties.yaml: 0.0000899292 m^3 * 7850 kg/m^3 = 0.706 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AN_cover_sheet_hood_top.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 89929.200 mm^3, area 94247.200 mm^2, and bounding box 221.40 x 428.00 x 2.00 mm. kb/materials/properties.yaml lists steel density as 7850 kg/m^3 and aluminum density as 2700 kg/m^3. targeted_web_search: searched \"17AN_cover_sheet_hood_top\", \"reAM250 cover sheet hood top material\", \"reAM250 17AN cover sheet\", and \"reAM250 sheet_top sheet_side\"; results found duplicate/public BOM text and general reAM250 project pages, but no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP volume represents one physical 17AN panel."
    - "Generic steel density is used as a conservative sheet-metal enclosure planning assumption because the row material is unresolved."
  uncertainty_notes:
    - "If the panel is aluminum sheet instead of steel, the same CAD volume would imply about 0.243 kg per unit."
    - "The STEP material metadata returned only placeholder material Generic with density 1000.0, so it was not used as material evidence."
material:
  primary_material: "unknown sheet metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AN_cover_sheet_hood_top.step"
    cited_fact_or_basis: "BOM row 242 and the manifest provide no manufacturer, product ID, material family, material grade, or link URL. Local assembly STEP material extraction for 17AN_cover_sheet_hood_top returned material Generic with density 1000.0. The CAD geometry is a 2.00 mm thick sheet-like panel. targeted_web_search: searched \"17AN_cover_sheet_hood_top material\", \"reAM250 17AN cover sheet material\", and \"reAM250 cover_sheet_hood_top\"; results did not provide row-specific material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Treat as metal sheet rather than polymer because the row is a rigid 2 mm enclosure/hood panel in a metal AM machine frame group."
  uncertainty_notes:
    - "Specific alloy, coating, surface finish, and fire/laser-safety requirements remain unresolved."
how_to_make:
  summary: "Fabricate as a custom sheet-metal cover: cut the flat U-shaped outline from 2 mm sheet stock, deburr edges, add any required edge finishing/coating, and install in the hood assembly."
  manufacturing_steps:
    - "Prepare 2 mm metal sheet stock sized for at least the 221.40 x 428.00 mm bounding envelope"
    - "CNC laser, waterjet, plasma, or router-cut the outer profile and central opening from the flat sheet."
    - "Deburr and inspect the perimeter and cutout."
    - "Apply coating or surface finish if required by the final enclosure design."
    - "Fasten or bond into the hood/top cover assembly during enclosure assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AN_cover_sheet_hood_top.step; research/ream250_bom/ream250_bom_row_0242_17AN__views_2x2.png"
    cited_fact_or_basis: "The STEP/preview show one flat 2.00 mm thick sheet-like solid with a U-shaped planform and no visible multi-part, calibrated, or vendor-module features. targeted_web_search: searched \"17AN_cover_sheet_hood_top manufacturing\", \"reAM250 cover sheet hood top drawing\", and \"reAM250 sheet enclosure hood material\" results did not provide row-specific fabrication instructions."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Flat-sheet cutting is sufficient because the CAD bounding box thickness is 2.00 mm and the preview shows no bends, formed flanges, or separate attached features."
  uncertainty_notes:
    - "Mounting holes or downstream joining details may be defined by neighboring hood parts rather than this isolated STEP."
kb_implications:
  - "item_granularity: simple_part - Model as one custom cut sheet-metal hood cover panel; reuse a generic sheet-cutting/fabrication process rather than creating a purchased module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0242_17AN.md
source_research_sha256: "aa71e913f98c8d1d737f4b6f4d8d4b3a4be270fbc6f2d717e05c6a23b2404903"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the hood-panel function, steel-density mass assumption, unresolved sheet-metal evidence, sheet-cutting route, KB implications, and CAD preview before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one flat U-shaped sheet panel with no visible subassembly. It should remain a simple sheet-metal cover part."
  proposed_subparts: []
process_abstraction:
  original_process_family: flat_sheet_metal_profile_cutting
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - deburring
    - surface_finishing
    - assembly
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_cutting_v0
      fit: direct
      reason: "Covers cutting a flat sheet profile and central opening from sheet stock."
    - process_id: cutting_basic_v0
      fit: supporting
      reason: "Generic fallback for profile cutting when the exact cutting machine is not selected."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Covers edge cleanup after cutting the thin sheet panel."
    - process_id: enclosure_assembly_basic_v0
      fit: supporting
      reason: "Relevant when installing the cover sheet into the hood assembly."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers outline, cutout, thickness, and fit checks."
  abstraction_decision: keep_original_family
  rationale: "The inferred source route is flat sheet cutting, directly matching the sheet/plate cutting and drilling bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: cover and shield the upper hood area of the enclosure
  material: unknown_sheet_metal
  scale_or_capacity:
    mass_kg: 0.706
    bom_quantity: 1
    row_total_mass_kg: 0.706
    scale_class: small
  geometry_form: flat_u_shaped_sheet_panel_with_large_central_cutout
merge_pool:
  eligible: true
  functional_purpose_key: enclosure_barrier
  precision_guardrails:
    - sheet_thickness
    - outline_fit
    - cutout_geometry
    - coating_requirement
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Material, coating, and fire/laser-safety requirements remain unresolved."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this panel with other hood cover and enclosure barrier rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable sheet-metal enclosure cover panel with material and coating variants."
assumptions:
  - "Steel-density mass is retained as a conservative planning value."
  - "The 2 mm flat STEP geometry is sufficient for sheet-cutting abstraction."
  - "No bends, attached inserts, plus calibrated features are visible in this row."
unresolved:
  - "Exact alloy, coating, mounting method, fire/laser-safety requirement, and service-cover role are not resolved by row evidence."
```
