---
row_identity:
  item: "3O4"
  cad_file: "3O4_end_piece_320SWN063"
  source_row_number: 130
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130"
function:
  summary: "DN 63 ISO-K stainless end piece or flange-end connector for the Pfeiffer spring-bellows/flexible vacuum line, providing the rigid sealing and clamp interface at one end of the bellows assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O4_end_piece_320SWN063.step; research/ream250_bom/ream250_bom_row_0130_3O4__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "BOM row 130 identifies item 3O4 as 3O4_end_piece_320SWN063, product description 320SFK063: end piece, manufacturer Pfeiffer Vacuum, quantity 1. The manifest maps row 130 to one matched_existing vendor_component STEP file. FreeCAD measured one solid, and the rendered contact sheet shows a ring/flange-like end connector with a through bore and stepped outer profile. The Pfeiffer product route identifies 320SFK063-130 as a DN 63 ISO-K spring bellows with 130 mm length and flange connection length 30 mm. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; alternate URL https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html is the Pfeiffer Vacuum online shop route for the same product ID 320SFK063-130 and lists Pfeiffer Vacuum Components & Solutions contact details, so it is treated as row-matched BOM-side vendor evidence."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific CAD end piece is treated as one rigid end/flange component from the Pfeiffer 320SFK063/320SWN063 vacuum bellows family, not as the complete bellows assembly."
  uncertainty_notes:
    - "The BOM row and local STEP do not state which end of the larger flexible line this part occupies or whether it is welded, pressed, or otherwise attached to the bellows in the supplier assembly."
mass:
  value_kg: 0.412
  basis: "FreeCAD volume 51352.068 mm^3 = 0.0000513521 m^3. Using local kb/materials/properties.yaml density for stainless_steel_304, 8030 kg/m^3, gives 0.4123 kg, rounded to 0.412 kg per unit. BOM quantity is 1, so the row total is also about 0.412 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O4_end_piece_320SWN063.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "FreeCAD measured the row STEP as one solid with volume 51352.06790278328 mm^3. Pfeiffer's product route states the product material as stainless steel with flange 304 and bellows 316L. The local density table lists stainless_steel_304 at 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; alternate URL https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html is the Pfeiffer Vacuum online shop route for the same product ID 320SFK063-130 and lists Pfeiffer Vacuum Components & Solutions contact details, so it is treated as row-matched BOM-side vendor evidence."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row CAD volume represents one physical end piece, and the end piece corresponds to the flange/end-connector material rather than the thin 316L bellows material."
    - "Small CAD tessellation or export simplifications are ignored because the estimate only needs planning-scale mass."
  uncertainty_notes:
    - "If the CAD body includes weld lips, hidden sleeve geometry, or non-solid simplifications differently than the real supplier part, the actual mass could shift, but the stainless flange-density estimate should remain within planning tolerance."
material:
  primary_material: "stainless steel 304 / EN 1.4301 flange or end-piece material"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Pfeiffer product route for 320SFK063-130 states stainless steel construction with flange 304 and bellows 316L. Local assembly STEP material extraction for 3O4_end_piece_320SWN063 returned only Generic with density 1000.0, which is placeholder material metadata. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; alternate URL https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html is the Pfeiffer Vacuum online shop route for the same product ID 320SFK063-130 and lists Pfeiffer Vacuum Components & Solutions contact details, so it is treated as row-matched BOM-side vendor evidence."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because this row is named and shaped as an end piece rather than the corrugated bellows span, the flange 304 material applies to the row item."
  uncertainty_notes:
    - "The supplier page specifies material at the parent spring-bellows product level, not a separate standalone 3O4 end-piece line item."
how_to_make:
  summary: "Machine or form the 304 stainless ISO-K end ring/flange, finish the sealing/clamp surfaces, and weld or join it to the stainless bellows body during the larger bellows assembly"
  manufacturing_steps:
    - "Start from 304 stainless round bar, tube, or near-net ring stock sized for a DN 63 ISO-K end connector."
    - "Turn the bore, outside diameter, stepped faces, and sealing or clamp-interface features; deburr and clean for vacuum service."
    - "Join the end piece to the bellows or adjacent stainless connector body using a vacuum-compatible weld or supplier-equivalent joining process."
    - "Inspect concentricity, sealing faces, leak tightness, and compatibility with the DN 63 ISO-K clamp and centering-ring interface."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O4_end_piece_320SWN063.step; research/ream250_bom/ream250_bom_row_0130_3O4__views_2x2.png"
    cited_fact_or_basis: "Pfeiffer's product route identifies the parent item as a stainless DN 63 ISO-K spring bellows, material flange 304 and bellows 316L, with tightness 1e-11 Pa m3/s and axial stroke. CAD/rendered row evidence shows a one-piece annular end connector geometry. targeted_web_search: queries tried: '320SFK063 Pfeiffer end piece manufacturing', '320SWN063 end piece material', and 'ISO-K stainless bellows flange 304 welded end piece'; result: found row-matched product/material/interface facts but no supplier statement for the standalone end-piece manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Model this as a vacuum-clean machined or formed stainless end piece plus assembly joining to the bellows, because the standalone row is not exposed as a separately documented part"
  uncertainty_notes:
    - "The actual supplier process may use proprietary forming, spinning, or external subcomponents rather than the generic machining/forming route listed here"
kb_implications:
  - "item_granularity: simple_part - Model as one reusable stainless ISO-K bellows end/flange piece; keep the full spring bellows as an assembly or purchased module if later KB work models the complete 320SFK063 connector."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0130_3O4.md
source_research_sha256: "8f657553195e9ba7ad4e91aefdd1c94e25665698d05c39fb0006f2a1f7ddb020"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the bellows end-connector function, CAD-derived stainless mass basis, 304 flange material evidence, machining/joining route, KB implications, and CAD preview before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is a rigid stainless ISO-K end/flange component from a bellows connector family. It can be modeled as one simple plumbing connector part, while the full flexible bellows assembly remains separate."
  proposed_subparts: []
process_abstraction:
  original_process_family: machined_stainless_iso_k_bellows_end_connector
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - joining
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: plumbing_and_pneumatics_v0
      fit: partial
      reason: "Covers gas-plumbing fitting context and testing, but not full stainless end-piece fabrication."
    - process_id: machining_process_turning_v0
      fit: supporting
      reason: "Relevant to turning the annular bore, outer diameter, steps, and flange faces."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers additional machining of clamp and sealing-interface features."
    - process_id: welding_brazing_basic_v0
      fit: supporting
      reason: "Covers joining the end piece to bellows tube sections in a later assembly route."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Covers leak checks for the connector and bellows interface."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers concentricity, sealing face, and flange-interface checks."
  abstraction_decision: substitute_process_family
  rationale: "The source route is inferred from a commercial bellows connector, while closure analysis can group the row under reusable plumbing connector fabrication and testing with turning, joining, cleaning, and inspection support."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: provide a rigid flange end connection for a flexible gas line
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.412
    bom_quantity: 1
    row_total_mass_kg: 0.412
    scale_class: small
  geometry_form: annular_iso_k_flange_end_piece_with_stepped_bore
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - flange_fit
    - concentricity
    - sealing_surface_finish
    - leak_tightness
    - bellows_join_interface
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Commercial bellows connectors may require clean stainless joining, tight leak-rate performance, and flange surface finish beyond basic machining."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this end piece with other plumbing connector and bellows-interface rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable stainless flange/end connector hardware rather than a row-specific Pfeiffer part."
assumptions:
  - "The row-specific CAD volume represents one rigid end/flange piece, not the complete bellows assembly."
  - "Pfeiffer flange 304 material maps to stainless_steel_304 for closure identity."
  - "Gas-line service is preserved through sealing and leak-test guardrails rather than a separate key axis."
unresolved:
  - "Exact supplier process, weld lip detail, leak-rate requirement, surface finish, and attachment method to the bellows body are not resolved by row evidence."
```
