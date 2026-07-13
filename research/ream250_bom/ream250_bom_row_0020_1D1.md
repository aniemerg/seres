---
row_identity:
  item: "1D1"
  cad_file: "1D1_part_1"
  source_row_number: 20
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Large door-hinge leaf or hinge bracket component for a Pfeiffer Vacuum door hinge set in the reAM250 assembly; BOM quantity is 2."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D1_part_1.step; research/ream250_bom/ream250_bom_row_0020_1D1__views_2x2.png"
    cited_fact_or_basis: "BOM row 20 identifies item 1D1, quantity 2, CAD file 1D1_part_1, description door hinge, manufacturer Pfeiffer Vacuum; the manifest maps the row to gold_export/parts/1D1_part_1.step as matched_existing vendor_component; FreeCAD measured one solid with a 65.00 x 100.00 x 20.00 mm bounding box; the rendered preview shows a tapered rectangular hinge leaf or bracket body with a cylindrical hinge knuckle/barrel feature and mounting holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD part is interpreted as one physical piece of the door hinge rather than the complete hinge assembly because adjacent BOM rows 1D2 and 1D3 are also Pfeiffer Vacuum door-hinge parts."
  uncertainty_notes:
    - "The row does not state which exact door or chamber product this hinge belongs to, so the function is limited to hinge hardware within the reAM250 door/chamber context." 
mass:
  value_kg: 0.794
  basis: "FreeCAD volume 98896.018 mm^3 converted to 9.8896018e-5 m^3 and multiplied by the local stainless_steel_304 density of 8030 kg/m^3, yielding 0.794 kg per 1D1 part. BOM quantity is 2, so the row total would be about 1.59 kg under this stainless scenario. If later evidence shows aluminum construction, the same CAD volume at 2700 kg/m^3 would be about 0.267 kg per part."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D1_part_1.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073323/product/820khh0600900/high-vacuum-chamber-horizontal-khh.html; https://www.pfeiffervacuum.com/global/en/knowledge/vacuum-technology/knowledge-book/3-mechanical-components-in-vacuum/3_2_materials/"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 98896.018 mm^3, area 19907.929 mm^2, and bounding box 65.00 x 100.00 x 20.00 mm; kb/materials/properties.yaml lists stainless_steel_304 density 8030 kg/m^3; a Pfeiffer KHH chamber page says a stainless steel door has hinges and quick clamps and lists chamber body and door material as stainless steel 304/1.4301; a Pfeiffer vacuum-materials page says stainless steel 1.4301 is suitable for vacuum applications. targeted_web_search: searched \"Pfeiffer Vacuum door hinge material\", \"Pfeiffer Vacuum door hinge reAM250 1D1_part_1\", \"1D1_part_1 door hinge Pfeiffer Vacuum\", and \"reAM250 door hinge Pfeiffer Vacuum\"; found duplicate BOM text, general Pfeiffer vacuum-chamber stainless context, and a non-Pfeiffer vacuum hinge example using aluminum, but no row-specific hinge mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The measured STEP solid is treated as the complete per-unit geometry for one 1D1 hinge component."
    - "Stainless steel 304/1.4301 density is used as a representative density because the part is inferred to be vacuum-compatible hinge hardware near a stainless chamber door."
  uncertainty_notes:
    - "Mass depends directly on the inferred material family; a comparable vacuum-door hinge source shows aluminum hinges are also plausible, so the stainless mass should be treated as a conservative high-side estimate until a row-specific drawing or vendor page is found."
material:
  primary_material: "stainless steel family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0020_1D1__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073323/product/820khh0600900/high-vacuum-chamber-horizontal-khh.html; https://www.pfeiffervacuum.com/global/en/knowledge/vacuum-technology/knowledge-book/3-mechanical-components-in-vacuum/3_2_materials/"
    cited_fact_or_basis: "BOM row 20 identifies the row as a Pfeiffer Vacuum door hinge; local STEP material extraction for product 1D1_part_1 reports only Generic with density 1000.0; the rendered preview shows a metal hinge-leaf/bracket shape; a Pfeiffer KHH chamber page says a stainless steel door has hinges and quick clamps and lists chamber body and door material as stainless steel 304/1.4301; a Pfeiffer vacuum-materials page says stainless steel is preferred for vacuum chambers or components and lists 1.4301 as suitable for vacuum applications. targeted_web_search: searched \"Pfeiffer Vacuum door hinge material\", \"Pfeiffer Vacuum door hinge reAM250 1D1_part_1\", \"1D1_part_1 door hinge Pfeiffer Vacuum\", and \"reAM250 door hinge Pfeiffer Vacuum\"; found duplicate BOM text, general Pfeiffer vacuum-chamber stainless context, and a non-Pfeiffer vacuum hinge example using aluminum, but no row-specific hinge material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A stainless steel family material is used as the broad KB material hypothesis because vacuum chamber door hardware typically needs corrosion-resistant, vacuum-compatible metal and the closest Pfeiffer chamber context uses stainless door construction."
  uncertainty_notes:
    - "No BOM field, CAD material metadata, product ID, or row-specific vendor page directly states the hinge material, so the exact alloy and grade are unresolved."
    - "Aluminum remains a plausible alternate for vacuum-door hinge hardware; do not encode a specific stainless grade downstream unless better evidence is found."
how_to_make:
  summary: "Model as a simple machined stainless hinge component: cut or machine the tapered hinge leaf/bracket and barrel feature from stainless stock, finish the hinge-pin bore and mounting holes, deburr, clean, and inspect for door-hinge fit."
  manufacturing_steps:
    - "Start with stainless steel bar, block, or near-net hinge blank sized for a roughly 65 x 100 x 20 mm component."
    - "Mill or otherwise form the tapered rectangular leaf/bracket profile and flat bearing faces visible in the CAD preview."
    - "Machine the cylindrical barrel or knuckle feature and bore/ream the hinge-pin interface to alignment."
    - "Drill or finish the mounting holes, then deburr all edges and bore mouths."
    - "Clean for vacuum-adjacent service and inspect hinge-pin fit, mounting geometry, and surface condition before assembly with the mating hinge pieces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D1_part_1.step; research/ream250_bom/ream250_bom_row_0020_1D1__views_2x2.png; https://www.idealvac.com/en-us/Ideal-Vacuum-Cube-Hinge-Hardware-Kit-Converts-Any-Cube-Plate-Into-a-Door/pp/P106868"
    cited_fact_or_basis: "The STEP/contact sheet shows one compact solid with a tapered rectangular body, cylindrical hinge-barrel feature, mounting holes, and a measured 65.00 x 100.00 x 20.00 mm bounding box. A comparable vacuum-door hinge product page states that its hinges are machined from aluminum and use a stainless hinge pin, supporting machining as a plausible route for this geometry. targeted_web_search: searched \"Pfeiffer Vacuum door hinge material\", \"Pfeiffer Vacuum door hinge reAM250 1D1_part_1\", \"1D1_part_1 door hinge Pfeiffer Vacuum\", and \"reAM250 door hinge Pfeiffer Vacuum\" found duplicate BOM text and general/comparable vacuum hinge evidence but no row-specific manufacturing process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the simple metal hinge geometry and need for aligned hinge-pin and mounting bores, not from a Pfeiffer factory process sheet."
    - "For KB modeling, this can be represented as machining from metal stock rather than a proprietary hinge subassembly"
  uncertainty_notes:
    - "The CAD gives geometry but not tolerances, surface finish, heat treatment, hinge-pin material, or whether Pfeiffer used machining, casting, extrusion, or a vendor-specific hinge blank."
kb_implications:
  - "item_granularity: simple_part - one hinge leaf/bracket component that can be modeled as a machined metal part; defer complete hinge assembly modeling to the adjacent 1D2/1D3 rows and mating pin/fastener context."
---

Research result for reAM250 BOM row 20.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0020_1D1.md
source_research_sha256: "25d06d747a1e65d5ed3f8491707c3affe0e4f912633ac44566c224cc3b5961b9"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the hinge-bracket function, conservative stainless mass basis, material uncertainty notes, inferred machining route, and CAD preview showing a tapered hinge body with barrel feature and mounting holes."
decomposition:
  decision: simple_part
  rationale: "The evidence indicates one physical hinge leaf/bracket component; adjacent rows cover other hinge pieces, so this row should not become a complete hinge assembly."
  proposed_subparts: []
process_abstraction:
  original_process_family: machined_metal_hinge_component
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
      reason: "Covers machining from metal stock for the hinge body, mounting faces, and general profile."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for hinge-pin bore alignment, bearing surfaces, and door fit."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Matches mounting-hole creation before final inspection."
    - process_id: metal_cutting_basic_v0
      fit: supporting
      reason: "Covers stock preparation from bar/block material."
    - process_id: cleaning_basic_v0
      fit: supporting
      reason: "Covers cleaning for vacuum-adjacent service after machining."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers hinge-pin fit, mounting geometry, and surface-condition checks."
  abstraction_decision: keep_original_family
  rationale: "The inferred source route is machining a compact metal hinge leaf/bracket from stock, which directly maps to general subtractive machining with precision bore support."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: high
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: articulated door hinge support for chamber access hardware
  material: stainless_steel_family_unresolved
  scale_or_capacity:
    mass_kg: 0.794
    bom_quantity: 2
    row_total_mass_kg: 1.588
    scale_class: small
  geometry_form: tapered_hinge_leaf_bracket_with_barrel_and_mounting_holes
merge_pool:
  eligible: true
  functional_purpose_key: hinge_hardware
  precision_guardrails:
    - hinge_pin_bore_alignment
    - mounting_hole_position
    - bearing_face_finish
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Material is inferred; aluminum remains plausible and would change mass and stock selection."
    - "Hinge-pin bore alignment may require precision machining beyond ordinary bracket work."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this row with adjacent hinge pieces and other door-hardware rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review across hinge leaves, hinge brackets, and pin hardware before assigning final closure identity."
assumptions:
  - "Stainless steel family is retained as the conservative planning material from the row research, with aluminum tracked as an unresolved alternative."
  - "BOM quantity 2 represents duplicate hinge components at about 0.794 kg each."
unresolved:
  - "Exact alloy, hinge-pin material, bore tolerance, and surface finish are unknown."
  - "Relationship to adjacent 1D2 and 1D3 hinge rows needs group review before final staging."
```
