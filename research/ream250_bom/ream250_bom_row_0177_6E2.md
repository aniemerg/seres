---
row_identity:
  item: "6E2"
  cad_file: "6E2_plate_right"
  source_row_number: 177
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Right-hand stainless side plate for the reAM250 recoater/powder handling subassembly, grouped with matching left/front/back plates and nearby blade, powder-container, and chute parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/60_recoater.step; research/ream250_bom/ream250_bom_row_0177_6E2__views_2x2.png"
    cited_fact_or_basis: "BOM row 177 lists item 6E2, quantity 1, CAD file 6E2_plate_right. The manifest maps the row to gold_export/parts/6E2_plate_right.step as a matched part. 60_recoater.step contains PRODUCT and NEXT_ASSEMBLY_USAGE_OCCURRENCE entries for 6E2_plate_right beside 6E1_plate_left, 6E3_plate_front, and 6E4_plate_back. The rendered CAD preview shows a tall narrow bent/angled plate form."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted as the right-side counterpart to the adjacent recoater plate set because the BOM and recoater assembly group these plate names together."
  uncertainty_notes:
    - "The CAD/BOM evidence supports plate role and subassembly context but does not state the exact contact, guarding, or powder-containment surface it provides."
mass:
  value_kg: 0.272
  basis: "Per-unit mass for quantity 1. FreeCAD measured volume 34041.309 mm^3. Assembly STEP metadata reports Stainless Steel with density 8000 kg/m^3. Calculation: 34041.309 mm^3 * 1e-9 m^3/mm^3 * 8000 kg/m^3 = 0.27233 kg, rounded to 0.272 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6E2_plate_right.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD read 1 solid with volume 34041.309101 mm^3, surface area 68900.285809 mm^2, and bounding box 32.91 x 118.50 x 268.00 mm. Local assembly STEP material extraction for product 6E2_plate_right returned material Stainless Steel and density 8000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP solid volume represents the physical part volume for one BOM item."
    - "The STEP density value is used directly for stainless steel rather than substituting a separate generic density."
  uncertainty_notes:
    - "Mass accuracy depends on CAD export fidelity and whether the original CAD included all small features, cutouts, or manufacturing allowances."
material:
  primary_material: "Stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local material extraction for product 6E2_plate_right returned material Stainless Steel with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The assembly metadata gives the material family but not a stainless grade such as 304 or 316."
how_to_make:
  summary: "Fabricate as a custom stainless side plate: cut the flat profile from stainless sheet or thin plate, brake-form or otherwise bend to the angled profile visible in CAD, deburr/finish edges, and inspect fit against the recoater plate set."
  manufacturing_steps:
    - "Start from stainless steel sheet or thin plate stock sized for the 268 mm tall part."
    - "Cut the perimeter/profile by laser, waterjet, CNC milling, or equivalent sheet/plate cutting."
    - "Form the angled bend/profile shown by the CAD preview, or machine the angle from plate if bending is not compatible with the exact geometry."
    - "Deburr, clean, and inspect dimensions before installation in the recoater assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6E2_plate_right.step; research/ream250_bom/ream250_bom_row_0177_6E2__views_2x2.png; web search sanity check"
    cited_fact_or_basis: "CAD preview and bounding box show a simple narrow angled plate, and STEP metadata identifies stainless steel. targeted_web_search: tried \"6E2_plate_right reAM250\", \"6E2 reAM250 recoater plate\", and \"6E2_plate_right\" results only mirrored the BOM row and did not provide a row-specific vendor drawing or manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A cut-and-formed stainless plate route is the most plausible low-complexity route for this geometry and material."
    - "If the CAD angle is not a bend allowance-compatible sheet form, the alternate route is machining from stainless plate stock."
  uncertainty_notes:
    - "No source states the original manufacturing process, tolerances, finish, or whether the angle is formed or machined."
kb_implications:
  - "item_granularity: simple_part - Model as a custom stainless plate reused within a recoater plate family rather than as a purchased module or assembly."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0177_6E2.md
source_research_sha256: "7c0c897a88b56a313135b7c0869e7b2664eac404902c4fcc6285ec33ff1e3153"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed recoater-assembly context, mass basis, stainless material evidence, cut-and-formed manufacturing route, KB implication, and CAD preview geometry before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one stainless side plate in a recoater plate family, not a purchased module and not an internal assembly."
  proposed_subparts: []
process_abstraction:
  original_process_family: cut_and_formed_stainless_sheet_plate
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - forming
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_cutting_v0
      fit: partial
      reason: "Covers cutting stainless sheet and thin plate blanks for enclosure and panel-like parts."
    - process_id: sheet_metal_bending_and_forming_v0
      fit: supporting
      reason: "Covers the angled profile visible in the CAD preview when the geometry is bend-compatible."
    - process_id: metal_forming_basic_v0
      fit: supporting
      reason: "Provides a broader forming anchor if staging treats the part as formed plate instead of simple sheet bending."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Covers edge cleanup and basic finish after cutting and forming."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks against the recoater plate set before installation."
  abstraction_decision: add_post_processing
  rationale: "The source route is primarily sheet/thin-plate cutting, but closure needs an explicit forming step for the angled side-plate geometry plus finishing and inspection."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: side containment and structural plate for recoater powder-handling area
  material: stainless_steel
  scale_or_capacity:
    mass_kg: 0.272
    bom_quantity: 1
    row_total_mass_kg: 0.272
    scale_class: small
  geometry_form: angled_cut_and_formed_side_plate
merge_pool:
  eligible: true
  functional_purpose_key: powder_containment
  precision_guardrails:
    - fit_to_recoater_plate_set
    - powder_contact_surface_finish
    - bend_angle_accuracy
    - stainless_grade_review
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Stainless grade is not sourced, so corrosion and powder-contact suitability need staging review."
    - "If the angled profile is not bend-compatible, the part may need machining from stainless plate stock."
  post_merge_decision_notes: "Final import/local decision is deferred until after merge review; local sheet cutting and forming is plausible if recoater fit and surface requirements are satisfied."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with adjacent recoater plates and other powder-containment parts before assigning a closure item ID."
assumptions:
  - "Treat BOM quantity as 1 and row total mass as 0.272 kg."
  - "Treat stainless steel material family as sourced, while grade and finish remain unknown."
  - "Treat the part as a side barrier and plate member in the recoater assembly, not a separate powder module."
unresolved:
  - "Exact stainless grade and finish are not sourced."
  - "The source does not confirm whether the angled profile is brake-formed, machined, stamped, made by another route."
  - "Powder-contact tolerance and cleaning requirements are not sourced."
```
