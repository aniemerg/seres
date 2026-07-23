---
row_identity:
  item: "2AA"
  cad_file: "2AA_left_support_plate"
  source_row_number: 33
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Left-side custom support plate in the reAM250 Z-axis inside assembly; it likely braces and locates the left side of the Z-axis plate/linear-guide/bearing structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/20_z_axis.step; research/ream250_bom/ream250_bom_row_0033_2AA__views_2x2.png"
    cited_fact_or_basis: "BOM row 33 lists item 2AA, quantity 1, CAD file 2AA_left_support_plate. Manifest row 33 maps it to a matched part STEP. The 20_z_axis STEP places 2AA_left_support_plate in the Z-axis assembly near 2AB_right_support_plate, side plates, distance pieces, linear guide rails/slides, and top/bottom axis bearing rows. The rendered CAD preview shows a wedge-like plate/web with a row of through holes on one narrow mounting face."
    evidence_basis: "bom_provided"
  assumptions:
    - "The 'left_support_plate' name is interpreted as a handed structural support in the Z-axis inside subassembly, paired with row 34 2AB_right_support_plate."
  uncertainty_notes:
    - "The CAD/BOM evidence identifies placement and support-plate geometry, but not the exact interface loads or mating fasteners."
mass:
  value_kg: 1.13
  basis: "FreeCAD measured one solid with volume 417843.199 mm^3, equal to 0.000417843199 m^3. Nominal mass uses aluminum density 2700 kg/m^3 from kb/materials/properties.yaml: 0.000417843199 m^3 * 2700 kg/m^3 = 1.128 kg, rounded to 1.13 kg per plate. BOM quantity is 1, so row total is also about 1.13 kg. If the part is generic steel at 7850 kg/m^3, the same CAD volume would be about 3.28 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AA_left_support_plate.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 417843.199 mm^3, area 53914.917 mm^2, and bounding box 135.00 x 218.60 x 23.00 mm. The local density table lists aluminum density 2700 kg/m^3 and steel density 7850 kg/m^3. targeted_web_search: searched \"2AA_left_support_plate\", \"2AA left support plate reAM250 material\", \"reAM250 left support plate\", and \"reAM250 2AA support plate material\"; results found duplicate/open reAM250 BOM references but no row-specific mass, material, or drawing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid volume is treated as the physical volume of one support plate."
    - "Aluminum alloy is used as the nominal mass scenario because the item is a custom machined support plate in a precision motion assembly; a steel scenario is retained in the basis because material is unresolved."
  uncertainty_notes:
    - "Mass is directly material-sensitive; use 1.13 kg as an aluminum-scenario estimate and about 3.28 kg if later evidence shows steel construction."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AA_left_support_plate.step"
    cited_fact_or_basis: "BOM row 33 has blank material fields. The assembly STEP material extractor matched 2AA_left_support_plate but returned material Generic and density 1000.0, which is placeholder material metadata under the task rules. CAD geometry is a thick, machined structural plate/web. targeted_web_search: searched \"2AA_left_support_plate\", \"2AA left support plate reAM250 material\", \"reAM250 2AA support plate material\", and \"Renishaw AM250 Z axis support plate material\"; no row-specific material grade or supplier drawing was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a structural metal component because of its 23 mm thick plate/web geometry, through-hole mounting pattern, and placement among Z-axis guide/bearing hardware."
  uncertainty_notes:
    - "The exact alloy family and grade are unresolved; aluminum alloy and steel remain plausible mass scenarios, but downstream modeling should avoid encoding either as the material until a drawing or designer note resolves it."
how_to_make:
  summary: "Fabricate as a custom structural support plate from metal plate or billet stock; likely route is CNC machining or rough cutting plus milling/drilling, followed by deburring and dimensional inspection."
  manufacturing_steps:
    - "Select structural metal stock after the alloy is resolved; use plate or billet thick enough for the 23 mm envelope."
    - "Rough cut the triangular/wedge outline by saw, waterjet, or CNC milling."
    - "CNC mill faces, angled web/profile features, and mounting edges to the STEP geometry."
    - "Drill and, if required by the mating hardware, ream/countersink/counterbore the row of mounting holes visible on the narrow face."
    - "Deburr, clean, and inspect the plate against the Z-axis assembly interfaces before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AA_left_support_plate.step; research/ream250_bom/ream250_bom_row_0033_2AA__views_2x2.png"
    cited_fact_or_basis: "FreeCAD measured a 135.00 x 218.60 x 23.00 mm one-solid part. The rendered contact sheet shows a wedge-like support plate/web and a row of through holes on one narrow face. targeted_web_search: searched \"2AA_left_support_plate manufacturing\", \"reAM250 left support plate drawing\", \"reAM250 2AA support plate\", and \"Renishaw AM250 support plate material\" results did not provide a row-specific manufacturing drawing or process specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the simple monolithic machined-plate geometry rather than from a sourced process note."
    - "The hole pattern is assumed to be a mechanical mounting interface requiring normal machined-part tolerances rather than precision bearing races."
  uncertainty_notes:
    - "Exact tolerances, surface finish, heat treatment, and whether any holes are threaded are not specified by the BOM or CAD preview."
kb_implications:
  - "item_granularity: simple_part - custom handed Z-axis support plate should be modeled as one fabricated structural metal part, with material unresolved and left broad until better evidence is available."
---

# reAM250 BOM Row 33 - 2AA

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0033_2AA.md
source_research_sha256: "048c7f02a79f54516e2c243606924505cd693c96fd7d0600fd021464776328e4"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the Z-axis support function, CAD-derived aluminum-scenario mass basis, unresolved structural-metal material evidence, inferred machined-plate route, and preview showing a wedge-like support web with a row of mounting holes."
decomposition:
  decision: simple_part
  rationale: "The row is one monolithic handed support plate; no subparts are visible in the evidence."
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_machined_structural_plate
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - drilling
    - precision_machining
    - deburring
    - cleaning
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers general stock removal for the wedge/web body and mounting faces."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant if Z-axis guide, bearing, and side-plate interfaces require controlled alignment."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Matches the visible mounting-hole row before any reaming, countersinking, and inspection."
    - process_id: metal_cutting_basic_v0
      fit: supporting
      reason: "Covers rough cutting of plate/billet stock before milling."
    - process_id: cleaning_basic_v0
      fit: supporting
      reason: "Covers chip and surface contamination removal before assembly."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers checks of hole locations, mounting faces, flatness, and Z-axis interface dimensions."
  abstraction_decision: keep_original_family
  rationale: "The inferred source route is CNC machining from thick plate/billet stock, and the Z-axis support function makes general subtractive machining the primary closure handle."
  process_guardrails:
    tolerance: review
    surface_finish: standard
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: handed structural support and locator for Z-axis guide/bearing hardware
  material: metal_alloy_unresolved
  scale_or_capacity:
    mass_kg: 1.13
    bom_quantity: 1
    row_total_mass_kg: 1.13
    scale_class: medium
  geometry_form: wedge_like_machined_support_plate_with_mounting_hole_row
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - hole_position_accuracy
    - mounting_face_flatness
    - z_axis_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Material is unresolved; aluminum versus steel selection changes mass and machining effort."
    - "Z-axis guide and bearing interfaces may require tighter alignment than ordinary frame plates."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this with right-hand and related Z-axis support plates."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with mirrored/support-plate rows before assigning a final item ID."
assumptions:
  - "The nominal mass uses the aluminum scenario from the source research while keeping material unresolved."
  - "The mounting-hole row is treated as a normal mechanical interface unless later drawings show precision bearing-seat requirements."
unresolved:
  - "Exact alloy, grade, surface treatment, threaded-hole details, and tolerances are unknown."
  - "Handed geometry and relationship to row 34 need merge-stage review before consolidation."
```
