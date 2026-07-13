---
row_identity:
  item: "1D2"
  cad_file: "1D2_part_2"
  source_row_number: 21
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Compact door-hinge leaf or knuckle component for a Pfeiffer Vacuum door hinge set in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D2_part_2.step; research/ream250_bom/ream250_bom_row_0021_1D2__views_2x2.png"
    cited_fact_or_basis: "BOM row 21 identifies item 1D2, quantity 2, CAD file 1D2_part_2, description door hinge, manufacturer Pfeiffer Vacuum; the manifest maps the row to gold_export/parts/1D2_part_2.step as matched_existing vendor_component; FreeCAD measured one solid with a 46.00 x 50.00 x 16.00 mm bounding box; the rendered preview shows a rectangular hinge-leaf-like web with two coaxial barrel/knuckle features and through bores."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD part is interpreted as one physical piece of the door hinge rather than the complete hinge assembly because adjacent BOM rows 1D1 and 1D3 are also door-hinge parts and this row's CAD is a single compact solid."
  uncertainty_notes:
    - "The row does not state which exact door or chamber product this hinge belongs to, so the function is limited to hinge hardware within the reAM250 door/chamber context."
mass:
  value_kg: 0.246
  basis: "FreeCAD volume 30583.002 mm^3 converted to 3.0583002e-5 m^3 and multiplied by the local stainless_steel_304 density of 8030 kg/m^3, yielding about 0.246 kg per 1D2 part."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D2_part_2.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073323/product/820khh0600900/high-vacuum-chamber-horizontal-khh.html; https://www.pfeiffervacuum.com/ca/en/knowledge/vacuum-technology/knowledge-book/3-mechanical-components-in-vacuum/3.2-materials.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 30583.002 mm^3, area 8824.811 mm^2, and bounding box 46.00 x 50.00 x 16.00 mm; kb/materials/properties.yaml lists stainless_steel_304 density 8030 kg/m^3; a Pfeiffer KHH chamber page says a stainless steel door has hinges and quick clamps and lists chamber body and door material as stainless steel 304/1.4301; a Pfeiffer vacuum-materials page says stainless steel 1.4301 is suitable for vacuum applications. targeted_web_search: searched \"Pfeiffer Vacuum door hinge material\", \"Pfeiffer Vacuum door hinge reAM250 1D2_part_2\", \"1D2_part_2 door hinge Pfeiffer Vacuum\", and \"reAM250 door hinge Pfeiffer Vacuum\"; found duplicate BOM text and general Pfeiffer vacuum-chamber stainless context, but no row-specific hinge mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The measured STEP solid is treated as the complete per-unit geometry for one 1D2 hinge component."
    - "Stainless steel 304/1.4301 density is used as a representative density because the part is inferred to be vacuum-compatible hinge hardware near a stainless chamber door."
  uncertainty_notes:
    - "Mass depends on the inferred stainless material family; if the part is aluminum, generic steel, or another alloy, the volume-based mass would change."
material:
  primary_material: "stainless steel family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0021_1D2__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073323/product/820khh0600900/high-vacuum-chamber-horizontal-khh.html; https://www.pfeiffervacuum.com/ca/en/knowledge/vacuum-technology/knowledge-book/3-mechanical-components-in-vacuum/3.2-materials.html"
    cited_fact_or_basis: "BOM row 21 identifies the row as a Pfeiffer Vacuum door hinge; local STEP material extraction for product 1D2_part_2 reports only Generic with density 1000.0; the rendered preview shows a metal hinge-leaf/knuckle shape; a Pfeiffer KHH chamber page says a stainless steel door has hinges and quick clamps and lists chamber body and door material as stainless steel 304/1.4301; a Pfeiffer vacuum-materials page says stainless steel 1.4301 is suitable for vacuum applications. targeted_web_search: searched \"Pfeiffer Vacuum door hinge material\", \"Pfeiffer Vacuum door hinge reAM250 1D2_part_2\", \"1D2_part_2 door hinge Pfeiffer Vacuum\", and \"reAM250 door hinge Pfeiffer Vacuum\"; found duplicate BOM text and general Pfeiffer vacuum-chamber stainless context, but no row-specific hinge material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A stainless steel family material is used as the broad KB material hypothesis because vacuum chamber door hardware typically needs corrosion-resistant, vacuum-compatible metal and the closest Pfeiffer chamber context uses stainless door construction."
  uncertainty_notes:
    - "No BOM field, CAD material metadata, product ID, or row-specific vendor page directly states the hinge material, so the exact stainless grade is not resolved."
how_to_make:
  summary: "Model as a simple machined stainless hinge component: cut or machine the hinge web and coaxial barrel features from stainless stock, finish the through bores/pin interface, deburr, clean, and inspect for door-hinge fit."
  manufacturing_steps:
    - "Start with stainless steel bar, block, or near-net hinge extrusion stock sized for a roughly 46 x 50 x 16 mm component."
    - "Mill or otherwise form the flat web/leaf faces and outside profile."
    - "Machine the two coaxial barrel or knuckle features and bore/ream the hinge-pin holes to alignment."
    - "Deburr edges and bore mouths, then clean for vacuum-adjacent service."
    - "Inspect hinge-pin fit, coaxiality, mounting/leaf geometry, and surface condition before assembly with the mating hinge pieces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D2_part_2.step; research/ream250_bom/ream250_bom_row_0021_1D2__views_2x2.png"
    cited_fact_or_basis: "The STEP/contact sheet shows one compact solid with a rectangular web, two coaxial cylindrical hinge-barrel features, through bores, and a measured 46.00 x 50.00 x 16.00 mm bounding box. targeted_web_search: searched \"Pfeiffer Vacuum door hinge material\", \"Pfeiffer Vacuum door hinge reAM250 1D2_part_2\", \"1D2_part_2 door hinge Pfeiffer Vacuum\", and \"reAM250 door hinge Pfeiffer Vacuum\" found duplicate BOM text and general Pfeiffer vacuum-chamber stainless context, but no row-specific manufacturing process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the simple metal hinge geometry and need for aligned hinge-pin bores, not from a Pfeiffer factory process sheet."
    - "For KB modeling, this can be represented as machining from stainless stock rather than a proprietary hinge subassembly"
  uncertainty_notes:
    - "The CAD gives geometry but not tolerances, surface finish, heat treatment, or whether Pfeiffer used machining, casting, extrusion, or a vendor-specific hinge blank."
kb_implications:
  - "item_granularity: simple_part - one hinge leaf/knuckle component that can be modeled as a machined stainless part; defer complete hinge assembly modeling to the adjacent 1D1/1D3 rows and mating pin/fastener context."
---

Research result for reAM250 BOM row 21.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0021_1D2.md
source_research_sha256: "b316a13417c7d761dbc0fdcf8c3f9fe17c2dd7408f77a608e4f12cd9a1dca54a"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the door-hinge component function, CAD-derived stainless mass, inferred stainless material context, machining route, and hinge-leaf/knuckle geometry before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one hinge leaf and knuckle component; mating hinge pieces, pin, fasteners, door, and seal hardware are separate rows."
  proposed_subparts: []
process_abstraction:
  original_process_family: machined_stainless_hinge_component
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - drilling
    - deburring
    - cleaning
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers machining the leaf body and outer profile from metal stock."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant to coaxial hinge bores, pin fit, and door alignment faces."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Covers through-bore preparation before reaming and finish control."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers pin-fit, bore alignment, and envelope checks."
  abstraction_decision: keep_original_family
  rationale: "The source route is a machined metal hinge component, which matches the general subtractive machining bucket with precision finishing for bores."
  process_guardrails:
    tolerance: high
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: high
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: articulated door joint component carrying hinge pin load
  material: stainless_steel
  scale_or_capacity:
    mass_kg: 0.246
    bom_quantity: 2
    row_total_mass_kg: 0.492
    scale_class: small
  geometry_form: compact_hinge_leaf_with_coaxial_knuckles_and_pin_bores
merge_pool:
  eligible: true
  functional_purpose_key: articulated_joint
  precision_guardrails:
    - bore_coaxiality
    - pin_fit
    - door_alignment
    - material_family
    - cleanliness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Door alignment and hinge-pin bore quality may affect downstream seal compression."
    - "Material is inferred from vacuum-adjacent stainless context rather than row-specific metadata."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review; compare with adjacent hinge rows before deciding whether a generic hinge component is sufficient."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with 1D1, 1D3, and related hinge hardware before assigning a closure item ID."
assumptions:
  - "The part is a hinge component, not the complete hinge assembly."
  - "Stainless steel is a reasonable planning material for chamber-adjacent door hardware."
  - "Pin and fasteners are modeled separately."
unresolved:
  - "Exact stainless grade, finish, and hinge-pin tolerance are not specified."
  - "Complete hinge assembly grouping must be reviewed with neighboring rows."
```
