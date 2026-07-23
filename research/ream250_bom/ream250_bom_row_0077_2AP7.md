---
row_identity:
  item: "2AP7"
  cad_file: "2AP7_lifting_platform"
  source_row_number: 77
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin square lifting-platform plate for the reAM250 Z-axis/build-platform stack; the local CAD shows a 250 mm by 250 mm by 10 mm plate-like part with a central square opening."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP7_lifting_platform.step; research/ream250_bom/ream250_bom_row_0077_2AP7__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "BOM row 77 identifies item 2AP7 with CAD file 2AP7_lifting_platform and quantity 1. FreeCAD measured one solid with volume 552545.970 mm^3, area 127647.948 mm^2, and bounding box 250.00 x 250.00 x 10.00 mm. The rendered contact sheet shows a square plate-like platform with a central square cutout."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD file name and geometry are treated as stronger row-identity evidence than the conflicting BOM description text, which says Hexagon head bolts. Product."
  uncertainty_notes:
    - "The BOM description appears misaligned with this row because the CAD geometry is a plate/platform rather than a hex-head bolt."
mass:
  value_kg: 1.492
  basis: "Per-unit estimate for quantity 1. CAD volume is 552545.970 mm^3 = 0.000552546 m^3. Using the local aluminum density constant from kb/materials/properties.yaml, 2700 kg/m^3, gives 0.000552546 * 2700 = 1.492 kg. A generic steel interpretation at 7850 kg/m^3 would be about 4.337 kg, so material uncertainty dominates."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP7_lifting_platform.step; kb/materials/properties.yaml; web search"
    cited_fact_or_basis: "FreeCAD measured the row-specific CAD volume as 552545.970 mm^3. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3 and generic steel density as 7850 kg/m^3. targeted_web_search: searched \"2AP7_lifting_platform\", \"reAM250 2AP7 lifting_platform\", and \"Hexagon head bolts Product grade C lifting platform\"; results repeated the BOM row or described ISO 4016 fasteners and did not provide row-specific mass or material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Modeled as aluminum-family structural plate for the planning mass because a moving 250 mm lifting platform benefits from low mass and the adjacent BOM has a separate heating plate."
    - "The STEP solid volume is treated as one physical item represented by the BOM row."
  uncertainty_notes:
    - "Material is not resolved by BOM fields or STEP metadata; if the part is steel rather than aluminum-family alloy, mass would be roughly 4.34 kg."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; web search"
    cited_fact_or_basis: "The assembly STEP material extractor returned material Generic and density 1000.0 for 2AP7_lifting_platform, which is a placeholder and does not resolve material. The BOM row material fields are blank. targeted_web_search: searched \"2AP7_lifting_platform material\", \"reAM250 2AP7 lifting_platform material\", and \"Hexagon head bolts Product grade C lifting platform material\"; no row-specific usable material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A rigid structural metal/alloy is inferred from the thin load-bearing plate geometry and machine-platform role."
  uncertainty_notes:
    - "No source resolves the specific alloy or grade; downstream KB modeling should not hard-code aluminum or steel without additional evidence."
how_to_make:
  summary: "Plausible route: fabricate as a simple machined plate from metal stock, then deburr and inspect flatness and interface dimensions."
  manufacturing_steps:
    - "Cut a 250 mm square blank from about 10 mm structural metal plate or equivalent stock."
    - "Machine the central square opening and any datum edges or chamfers visible in the CAD."
    - "Deburr, clean, and inspect platform flatness, thickness, and fit in the Z-axis/build-platform assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP7_lifting_platform.step; research/ream250_bom/ream250_bom_row_0077_2AP7__views_2x2.png; web search"
    cited_fact_or_basis: "CAD and preview show a thin 250 x 250 x 10 mm square plate-like part with a central square opening. targeted_web_search: searched \"2AP7_lifting_platform manufacturing\", \"reAM250 2AP7 lifting_platform\", and \"Hexagon head bolts Product grade C lifting platform\" no row-specific manufacturing specification was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a low-complexity plate component rather than a external calibrated module"
    - "CNC machining or abrasive/waterjet cutting plus finish machining is sufficient for a coarse KB manufacturing route."
  uncertainty_notes:
    - "Actual production could use a supplier-specific process or material/finish requirement not present in the BOM or STEP metadata."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable machined structural plate/platform, not as a fastener or purchased module, unless better source evidence changes the row identity."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0077_2AP7.md
source_research_sha256: "a3a0dbc5a4304cf4908467c640fb18377c6b3795d23aa99c8d4b82eb2247dd8b"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the lifting-platform CAD identity, aluminum-scenario mass basis, unresolved structural metal evidence, plate manufacturing route, KB implications, and CAD preview before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one square lifting-platform plate with a central opening. The conflicting BOM fastener text is treated as metadata noise because the CAD and filename identify a platform plate."
  proposed_subparts: []
process_abstraction:
  original_process_family: cut_and_finish_machined_structural_plate
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - drilling
    - precision_machining
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_cutting_v0
      fit: partial
      reason: "Covers profile cutting from plate stock, though this row is a 10 mm structural plate."
    - process_id: cutting_basic_v0
      fit: supporting
      reason: "Relevant to rough cutting the square blank and central opening."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers finish machining of datum edges, central opening, chamfers, and mounting features."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant if build-platform flatness and Z-axis interface control are tight."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Covers cleanup of cut edges and platform perimeter."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers flatness, thickness, central opening, and fit checks."
  abstraction_decision: substitute_process_family
  rationale: "The source route includes machining, but the part is a plate/platform whose primary closure handle should be sheet/plate cutting and drilling, with finish machining recorded as support work."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: support the build platform within the vertical lifting stack
  material: unknown_structural_metal
  scale_or_capacity:
    mass_kg: 1.492
    bom_quantity: 1
    row_total_mass_kg: 1.492
    scale_class: small
  geometry_form: square_plate_platform_with_central_square_opening
merge_pool:
  eligible: true
  functional_purpose_key: platform_support
  precision_guardrails:
    - flatness
    - central_opening_geometry
    - z_axis_interface_fit
    - material_stiffness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Material is unresolved; aluminum planning mass is lower than a steel scenario."
    - "Build-platform support may need flatness and stiffness beyond a rough cut plate."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this row with other platform and support plate rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable platform support plate with material-specific variants if evidence diverges."
assumptions:
  - "The CAD filename and geometry override the conflicting fastener-like BOM text for row identity."
  - "The 1.492 kg aluminum-scenario mass is retained for scale grouping with material uncertainty documented."
  - "The row is one manufactured plate, not a purchased module."
unresolved:
  - "Exact alloy, stiffness requirement, flatness, central-opening tolerance, surface finish, and mating interfaces are not resolved by row evidence."
```
