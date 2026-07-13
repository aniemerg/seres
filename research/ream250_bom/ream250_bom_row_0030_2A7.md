---
row_identity:
  item: "2A7"
  cad_file: "2A7_right_plate"
  source_row_number: 30
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom right-side structural plate in the reAM250 Z-axis inside assembly; it likely forms or braces the right side of the Z-axis plate stack that carries the linear-guide, distance-piece, support-plate, and bearing-related components."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/20_z_axis.step; research/ream250_bom/ream250_bom_row_0030_2A7__views_2x2.png"
    cited_fact_or_basis: "BOM row 30 lists item 2A7, quantity 1, CAD file 2A7_right_plate. Manifest row 30 maps the row to gold_export/parts/2A7_right_plate.step as a matched part export. The 20_z_axis STEP places 2A7_right_plate inside 2A0_z_axis_inside near 2A6_left_plate, left/right distance pieces, left/right support plates, linear guide rails/slides, and axis-bearing rows. The rendered CAD preview shows a triangular or wedge-like ribbed side plate with a row of mounting holes along one long edge."
    evidence_basis: "bom_provided"
  assumptions:
    - "The 'right_plate' name is interpreted as a handed structural plate paired with row 29 2A6_left_plate in the 2A0_z_axis_inside subassembly."
  uncertainty_notes:
    - "The CAD/BOM evidence identifies the part as a right-side plate in the Z-axis context, but not the exact load path, mating fasteners, or whether it primarily supports fixed frame elements or moving-axis guide hardware."
mass:
  value_kg: 3.49
  basis: "FreeCAD volume 1293512.090 mm^3 equals 0.001293512 m^3. Nominal mass uses aluminum density 2700 kg/m^3 from kb/materials/properties.yaml: 0.001293512 m^3 * 2700 kg/m^3 = 3.492 kg, rounded to 3.49 kg per plate. BOM quantity is 1, so row total is also about 3.49 kg. If the part is generic steel at 7850 kg/m^3, the same CAD volume would be about 10.15 kg; stainless steel at 8000 kg/m^3 would be about 10.35 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A7_right_plate.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1293512.090 mm^3, area 149920.786 mm^2, and bounding box 240.00 x 400.00 x 23.00 mm. The local density table lists aluminum density 2700 kg/m^3, steel density 7850 kg/m^3, and stainless_steel density 8000 kg/m^3. targeted_web_search: searched \"2A7_right_plate reAM250\", \"2A7 right_plate reAM250\", \"reAM250 right plate 2A7\", and \"Renishaw AM250 right plate\"; results found duplicate/open reAM250 BOM references but no row-specific mass, material, or drawing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid volume is treated as the physical volume of one right plate."
    - "Aluminum alloy is used as the nominal mass scenario because the item is a custom machined plate in a precision motion/structural assembly; steel and stainless alternatives are retained because the material is unresolved."
  uncertainty_notes:
    - "Mass is directly material-sensitive; use 3.49 kg as an aluminum-scenario estimate and about 10.15-10.35 kg if later evidence shows steel or stainless construction."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A7_right_plate.step; research/ream250_bom/ream250_bom_row_0030_2A7__views_2x2.png"
    cited_fact_or_basis: "BOM row 30 has blank manufacturer, product, link, material-family, and grade fields. The assembly STEP material extractor matched 2A7_right_plate but returned material Generic and density 1000.0, which is placeholder material metadata under the task rules. CAD geometry is a 23 mm thick ribbed structural plate. targeted_web_search: searched \"2A7_right_plate material reAM250\", \"reAM250 2A7 right plate material\", \"reAM250 right plate 2A7\", and \"Renishaw AM250 Z axis right plate material\"; no row-specific material grade or supplier drawing was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a structural metal component because of its thick plate/web geometry, mounting-hole pattern, and placement among Z-axis guide, spacer, support, and bearing hardware."
  uncertainty_notes:
    - "The exact alloy family and grade are unresolved; aluminum alloy and steel remain plausible mass scenarios, but downstream modeling should keep the material broad until a drawing, designer note, or verified CAD metadata resolves it."
how_to_make:
  summary: "Fabricate as a custom structural side plate from metal plate or billet stock; likely route is rough profiling followed by CNC machining of faces, ribs/reliefs, mounting holes, and datum features."
  manufacturing_steps:
    - "Select structural metal stock after the alloy is resolved; use plate or billet thick enough for the 23 mm envelope."
    - "Rough cut the triangular or wedge-like outline by saw, waterjet, or CNC milling, leaving machining allowance."
    - "CNC mill the broad faces, tapered profile, rib or relief geometry, and mating edges to the STEP geometry."
    - "Drill and, if required by mating hardware, ream, tap, countersink, or counterbore the visible mounting-hole row and any hidden interface holes."
    - "Finish-machine datum or rail/support mating faces for alignment, then deburr, clean, and inspect hole locations, flatness, and plate geometry before assembly."
    - "Apply anodizing, passivation, blackening, or other finish only if later drawing evidence identifies a required material and surface treatment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A7_right_plate.step; research/ream250_bom/ream250_bom_row_0030_2A7__views_2x2.png"
    cited_fact_or_basis: "FreeCAD measured a one-solid 240.00 x 400.00 x 23.00 mm part. The rendered contact sheet shows a wedge-like side plate with ribbed/relieved faces and a row of mounting holes along one long edge. targeted_web_search: searched \"2A7_right_plate manufacturing\", \"reAM250 right plate drawing\", \"reAM250 2A7 right plate\", and \"Renishaw AM250 right plate material\" results did not provide a row-specific manufacturing drawing, material callout, or process specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the monolithic machined-plate geometry rather than from a sourced process note."
    - "The part is treated as a custom simple part because the BOM row has no manufacturer, product ID, or link URL and the CAD name is assembly-specific"
  uncertainty_notes:
    - "Exact tolerances, threaded-hole details, surface finish, heat treatment, coating, and inspection datums are not specified by the BOM or CAD preview."
kb_implications:
  - "item_granularity: simple_part - custom handed Z-axis side plate should be modeled as one fabricated structural metal part, with material unresolved and left broad until better evidence is available."
---

Research result for reAM250 BOM row 30.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0030_2A7.md
source_research_sha256: "06f4f458f34b83e718ff42ab62681c086e5ed062ff8031a5be46d20acddadb9f"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed Z-axis right-side structural function, CAD context near guide and bearing hardware, aluminum-scenario mass with steel alternatives, unresolved structural metal material, inferred machining route, and simple-part KB implication."
decomposition:
  decision: simple_part
  rationale: "The row is a monolithic handed structural side plate. Holes, ribbed reliefs, datum faces, and finish requirements are features of one fabricated item rather than separable closure subparts."
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
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers stock removal from plate stock, but the ribbed reliefs and datum faces need added precision machining guardrails."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for rail, spacer, support, and bearing mating features where alignment affects Z-axis motion."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Relevant to the long row of mounting holes and hidden interface holes before final finishing."
    - process_id: surface_finishing_basic_v0
      fit: supporting
      reason: "Relevant if later evidence selects anodizing, passivation, blackening, and comparable protective finishing."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks for hole locations, flatness, datum faces, and fit into the Z-axis stack."
  abstraction_decision: keep_original_family
  rationale: "The inferred source route is plate/billet stock followed by rough profiling, CNC milling, drilling, finishing, and inspection, which directly fits the general subtractive machining bucket."
  process_guardrails:
    tolerance: high
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: high
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: handed structural side support for Z-axis guide and bearing assembly interfaces
  material: unknown_structural_metal_alloy
  scale_or_capacity:
    mass_kg: 3.49
    bom_quantity: 1
    row_total_mass_kg: 3.49
    scale_class: medium
  geometry_form: thick_handed_ribbed_wedge_side_plate_with_mounting_hole_row
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - guide_interface_alignment
    - bearing_interface_alignment
    - datum_face_flatness
    - hole_location_accuracy
    - material_family_unresolved
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Unresolved alloy drives a large mass spread between aluminum and steel scenarios."
    - "Z-axis guide and bearing interfaces may require tighter machining and inspection than ordinary structural plates."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this right plate with matching left-side and similar Z-axis structural members."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic machined Z-axis structural side plate family with handed geometry captured in notes."
assumptions:
  - "The aluminum scenario mass is used for planning because no row-specific material callout exists."
  - "The row is a custom machined simple part based on CAD context and absence of a vendor product record."
unresolved:
  - "Exact alloy, heat treatment, coating, thread details, tolerance stack, and inspection datums remain unresolved."
  - "Load path between this side plate, linear-guide hardware, support plates, and bearing components is not fully specified by the row evidence."
```
