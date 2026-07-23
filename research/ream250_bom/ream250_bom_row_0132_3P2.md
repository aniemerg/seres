---
row_identity:
  item: "3P2"
  cad_file: "3P2_flange_ISO_K_DN63"
  source_row_number: 132
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320FAN063_76"
function:
  summary: "DN 63 ISO-K stainless weld-ring flange for joining a 76.1 x 3 mm vacuum tube into an ISO-K vacuum line interface."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P2_flange_ISO_K_DN63.step; research/ream250_bom/ream250_bom_row_0132_3P2__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073040/product/320fan06376/welding-flange-ring-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 132 identifies item 3P2 as 3P2_flange_ISO_K_DN63, quantity 2, product 320FAN063-76 from Pfeiffer Vacuum; the refreshed STEP contact sheet shows a single annular flange/ring form; the row-matched Pfeiffer shop page identifies 320FAN063-76 as a welding flange ring with connection flange DN 63 ISO-K and tube dimension 76.1 mm x 3 mm. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320FAN063_76 returned HTTP 403 to curl on 2026-06-18; vacuum-shop.com is a Pfeiffer Vacuum Components & Solutions GmbH shop page for the same order number 320FAN063-76 and product family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The ISO-K DN63 row name, order number, vendor page, and ring geometry are interpreted as a vacuum flange interface rather than a blind cover."
  uncertainty_notes: []
mass:
  value_kg: 0.247
  basis: "FreeCAD measured one solid with volume 30755.131 mm^3. Using stainless steel 304/1.4301 density 8030 kg/m^3 from kb/materials/properties.yaml gives 0.247 kg per flange. BOM quantity is 2, so the row total is about 0.494 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P2_flange_ISO_K_DN63.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073040/product/320fan06376/welding-flange-ring-stainless-steel-1-4301-304.html; https://vacuum-shop.com/2073853/downloads/datasheets/Datasheet_320FAN063-76_en.pdf"
    cited_fact_or_basis: "FreeCAD measured volume 30755.131 mm^3, area 13367.404 mm^2, and bounding box about 105.13 x 105.13 x 12.00 mm; the refreshed renderer metadata reported a visual triage box about 95.0 x 95.0 x 12.0 mm; the row-matched Pfeiffer shop page and datasheet identify 320FAN063-76 as stainless steel 1.4301/AISI 304, DN 63 ISO-K, A 95 mm, B 70 mm, C 12 mm, D 76.4 mm, E 6 mm, tube dimension 76.1 mm x 3 mm; kb/materials/properties.yaml lists stainless_steel_304 and stainless_steel_1_4301 density 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320FAN063_76 returned HTTP 403 to curl on 2026-06-18; vacuum-shop.com is a Pfeiffer Vacuum Components & Solutions GmbH shop page and datasheet route matching the same order number 320FAN063-76."
    evidence_basis: "bom_provided"
  assumptions:
    - "The measured STEP volume is treated as the physical stainless volume for one purchased flange."
    - "The local stainless_steel_304 density is used as the calculation constant for stainless steel 1.4301/304."
  uncertainty_notes:
    - "The visual preview bounding box is for triage only and differs from the FreeCAD bounding box because of CAD orientation/preview processing; the mass uses the FreeCAD volume."
material:
  primary_material: "stainless steel 1.4301/304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073040/product/320fan06376/welding-flange-ring-stainless-steel-1-4301-304.html; https://vacuum-shop.com/2073853/downloads/datasheets/Datasheet_320FAN063-76_en.pdf"
    cited_fact_or_basis: "The row-matched Pfeiffer shop page names the product Welding flange ring, stainless steel 1.4301/304 for order number 320FAN063-76; the English datasheet states materials in contact with media are stainless steel 1.4301 (AISI 304). official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320FAN063_76 returned HTTP 403 to curl on 2026-06-18; vacuum-shop.com is a Pfeiffer Vacuum Components & Solutions GmbH shop page and datasheet route matching the same order number 320FAN063-76. Local assembly STEP material extraction for 3P2_flange_ISO_K_DN63 returned only Generic with density 1000.0, so it was not used to resolve material."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Model as a simple stainless ISO-K weld-ring flange made from 304/1.4301 stainless ring stock or plate by cutting/turning the annular profile, machining the sealing/clamp geometry, deburring, cleaning, and inspection for vacuum service."
  manufacturing_steps:
    - "Start with stainless steel 304/1.4301 ring stock, tube-end stock, or plate thick enough for the 12 mm flange height."
    - "Cut or rough-turn the outside diameter, inside bore, and weld-neck/tube landing to the DN63 ISO-K geometry."
    - "Finish-machine sealing and clamping faces, including the 95 mm outside diameter, 70 mm interface diameter, 76.4 mm tube-side diameter, and 6 mm lip feature indicated by the row-matched vendor dimensions."
    - "Deburr, clean for vacuum compatibility, and inspect dimensions and surface condition before assembly into the vacuum line."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P2_flange_ISO_K_DN63.step; research/ream250_bom/ream250_bom_row_0132_3P2__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073040/product/320fan06376/welding-flange-ring-stainless-steel-1-4301-304.html; https://vacuum-shop.com/2073853/downloads/datasheets/Datasheet_320FAN063-76_en.pdf"
    cited_fact_or_basis: "The refreshed STEP/contact sheet shows a single annular ring/flange; the row-matched Pfeiffer shop page and datasheet identify 320FAN063-76 as a DN 63 ISO-K welding flange ring with stainless steel 1.4301/304 and dimensions A 95 mm, B 70 mm, C 12 mm, D 76.4 mm, E 6 mm. targeted_web_search: searched \"320FAN063-76 Pfeiffer Vacuum ISO-K DN 63 weld ring flange stainless 1.4301 304\", \"320FAN063_76 Pfeiffer Vacuum 320FAN063-76\", \"site:pfeiffer-vacuum.com 320FAN063-76\", and \"320FAN063-76 1.4301\" found row-matched Pfeiffer shop/catalog data for product identity, material, and dimensions but no process sheet specifying the factory route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The fabrication route is inferred from the simple rotationally symmetric stainless flange geometry and standard vacuum-flange manufacturing practice."
    - "Small-batch KB modeling can represent this as machining from stainless stock rather than a vendor-specific forged or cast preform."
  uncertainty_notes:
    - "The vendor source resolves material and dimensions, but not the actual Pfeiffer factory process route."
kb_implications:
  - "item_granularity: simple_part - one stainless annular vacuum flange that can be modeled as a machined stock part rather than a sub-assembly."
---

Research result for reAM250 BOM row 132.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0132_3P2.md
source_research_sha256: c83c7a5287c22492f4a22a4abfee3dfcf05663a1aff0db6df55e484ee8ba87ed
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Read the original function, mass basis, material evidence, inferred manufacturing route, KB implications, and CAD
    preview showing a single annular ISO-K weld-ring flange.
decomposition:
  decision: simple_part
  rationale: The row is one stainless annular service flange with no internal subassemblies; its closure-relevant properties
    are material, flange geometry, sealing/clamping faces, and cleanliness.
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_turning_machining
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
  - stock_preparation
  - forming
  - precision_machining
  - joining
  - cleaning
  - leak_testing
  - dimensional_inspection
  candidate_existing_processes:
  - process_id: fitting_assembly_basic_v0
    fit: partial
    reason: Covers generic fitting and connector assembly work.
  - process_id: plumbing_and_pneumatics_v0
    fit: partial
    reason: Covers fluid and gas handling connector work at the system level.
  - process_id: leak_testing_v0
    fit: supporting
    reason: Covers leak checks when sealing function matters.
  - process_id: cleaning_basic_v0
    fit: supporting
    reason: Covers cleaning before connector assembly and test.
  - process_id: leak_testing_v0
    fit: supporting
    reason: Relevant when sealing and fluid integrity matter.
  - process_id: welding_basic_v0
    fit: supporting
    reason: Relevant when the row needs permanent joining.
  abstraction_decision: substitute_process_family
  rationale: The stainless ring is a plumbing connection interface. Use the shared plumbing connector bucket with turning,
    sealing-surface finishing, cleaning, and interface inspection rather than a service-specific process label.
  process_guardrails:
    tolerance: review DN63 ISO-K interface diameters, tube landing, and clamp engagement dimensions
    surface_finish: required on sealing and clamping faces; finish machining is retained
    sealing_quality: required for plumbing line service; cleaning and inspection remain part of the route
    alignment_accuracy: moderate; maintain concentricity between bore, weld neck, and flange faces
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: weld-ring flange joining a service tube to an ISO-K plumbing line interface
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.247
    bom_quantity: 2
    row_total_mass_kg: 0.494
    scale_class: small
  geometry_form: annular_weld_ring_flange
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
  - sealing_face_surface_finish
  - clamp_interface_dimensions
  - bore_and_weld_neck_concentricity
  - service_cleanliness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - plumbing_connector_fabrication_testing
  import_risk_factors:
  - connector sealing quality depends on surface finish and cleanliness controls
  - stainless 304/1.4301 supply chain must be available and substituted deliberately
  post_merge_decision_notes: Final import/local manufacture decision is deferred until after merge review compares this with
    other service flange rows and available stainless machining capability.
kb_staging:
  proposed_item_id: null
  notes: Do not assign a closure item ID during row conversion; likely merge with other stainless ISO-K and service weld flange
    abstractions if material, scale, and precision guardrails align.
assumptions:
- The STEP-derived mass of 0.247 kg is accepted as one flange mass, with BOM quantity 2 giving 0.494 kg row total.
- Stainless steel 1.4301/304 is represented as stainless_steel_304 for merge and later KB staging.
- General machining and turning can meet the required DN63 ISO-K flange geometry when paired with finish machining, cleaning,
  and inspection.
unresolved:
- Exact connector sealing surface finish and dimensional tolerances were not present in the row evidence and should be checked
  during merge and staging.
- Whether this remains a distinct ISO-K flange item and merges into a broader service flange closure item is deferred to merge
  review.
```
