---
row_identity:
  item: "3B"
  cad_file: "3B_valve_ISO_K_DN63_310VEP063-01"
  source_row_number: 113
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02"
function:
  summary: "Pfeiffer EVB 063 PA DN 63 ISO-K electro-pneumatic angle valve used as a vacuum shut-off/isolation valve in the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02; https://www.vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; https://vacuum-shop.com/2075819/downloads/manuals/vp0002ben.pdf"
    cited_fact_or_basis: "BOM row 113 identifies item 3B as Pfeiffer Vacuum product 310VEP063 with link URL for 310VEP063_02. The Pfeiffer online shop route identifies 310VEP063-02 as an EVB 063 PA angle valve with DN 63 ISO-K connection, electro-pneumatic actuator, normally closed behavior, visual position indicator, and 24 V DC input. The operating instructions state the angle valve is used as a shut-off or venting device. official_alternate_route_check: the BOM URL is on pfeiffer-vacuum.com for product 310VEP063_02; the vacuum-shop.com page is an official Pfeiffer Vacuum online shop page showing Pfeiffer Vacuum contact/copyright and the same row-matched order number 310VEP063-02."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM description_or_product_id 310VEP063 maps to the linked 310VEP063-02 24 V DC variant because the row link URL and CAD filename both carry the same 310VEP063 product family."
  uncertainty_notes:
    - "The local row STEP is a simplified 5.8 x 8.5 x 8.5 mm proxy shape and is not dimensionally representative of the full DN 63 valve body."
mass:
  value_kg: 3.9
  basis: "Per-unit vendor weight for one 310VEP063-02 EVB 063 PA valve is 3.9 kg. BOM quantity is 1, so the row total is also about 3.9 kg. FreeCAD measured the local row STEP as one solid with volume 257.185 mm^3 and bounding box about 5.80 x 8.50 x 8.50 mm, which is inconsistent with the vendor DN 63 valve dimensions and was not used for the physical valve mass."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02; https://www.vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3B_valve_ISO_K_DN63_310VEP063-01.step"
    cited_fact_or_basis: "The Pfeiffer online shop route lists weight 3.9 kg for order number 310VEP063-02. Local FreeCAD geometry check measured only a tiny proxy solid, so the vendor product weight is the controlling mass fact. official_alternate_route_check: the original BOM URL points to Pfeiffer product 310VEP063_02; the vacuum-shop.com page is an official Pfeiffer Vacuum shop route for the same order number and exposes the weight field."
    evidence_basis: "bom_provided"
  assumptions:
    - "The vendor catalog weight includes the complete valve assembly, including actuator, position indicator, pilot/control valve hardware, seals, and housing."
  uncertainty_notes:
    - "The CAD package cannot independently verify mass because the exported per-row STEP is not the full-size valve geometry."
material:
  primary_material: "Aluminum housing with stainless steel bellows feedthrough, FKM seal, microswitch/position-indicator and electro-pneumatic actuator materials not further resolved."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02; https://www.vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; .venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/extract_step_materials.py --step design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step --product-name 3B_valve_ISO_K_DN63_310VEP063-01"
    cited_fact_or_basis: "The Pfeiffer online shop route lists housing as Aluminum, feedthrough as Bellows/Stainless steel, and seal as FKM. Local assembly STEP material extraction returned only Generic with density 1000.0 for this product, so it was treated as placeholder metadata. official_alternate_route_check: the BOM URL is the Pfeiffer product route for 310VEP063_02; the vacuum-shop.com page is an official Pfeiffer Vacuum shop page and matches order number 310VEP063-02."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Electrical and pneumatic actuator subcomponent materials are not itemized by the accessible product facts, so the material set is partial but adequate for coarse BOM modeling."
how_to_make:
  summary: "Treat as a external Pfeiffer Vacuum valve module for near-term KB closure; install it into the ISO-K vacuum line with compatible DN 63 hardware, clean sealing practice, compressed-air supply, and 24 V DC electrical connection"
  manufacturing_steps:
    - "Inspect product identity and sealing surfaces, keeping protective covers in place until installation."
    - "Mount to clean ISO-K counter flanges using suitable ISO-K connection components."
    - "Connect clean dry or slightly oiled compressed air in the specified pressure range and connect the 24 V DC pilot valve/position-indicator wiring."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02; https://www.vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; https://vacuum-shop.com/2075819/downloads/manuals/vp0002ben.pdf"
    cited_fact_or_basis: "The Pfeiffer shop route identifies 310VEP063-02 as a purchasable EVB 063 PA angle valve with DN 63 ISO-K connection, electro-pneumatic actuator, 24 V DC input, and compressed-air requirement. The operating instructions state scope of delivery as one angle valve plus operating instructions and describe installation on a system with appropriate ISO-K flange components, clean sealing surfaces, compressed air, and electrical connection. official_alternate_route_check: the BOM-provided Pfeiffer URL identifies the 310VEP063_02 product route; the vacuum-shop.com page and manual are official Pfeiffer Vacuum routes for the same product family/order number."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "A self-manufacturing route would require a separate decomposition of valve body machining, bellows/feedthrough manufacture, sealing surfaces, actuator, pilot valve, microswitch, leak testing, and qualification."
kb_implications:
  - "item_granularity: complex_module - Model as a functional valve complex module for this pass because it is a calibrated multi-material vacuum component with actuator, seals, feedthrough, and position-indicator hardware; later self-manufacturing would need a sub-BOM and leak-test workflow.; defer internal decomposition until a focused sub-BOM and manufacturing workflow are modeled."
---

Research result for reAM250 BOM row 113.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0113_3B.md
source_research_sha256: "309096dfc88d516e031e70bc7a292a6e1b47e6708727b51bcd1f95219cde8ad2"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: false
  notes: "Reviewed the Pfeiffer EVB 063 PA electro-pneumatic vacuum valve function, 3.9 kg catalog mass with BOM quantity 1, aluminum/stainless/FKM partial material evidence, external-module installation route, and KB implication. CAD proxy was inspected but not used for identity because it is not dimensionally representative."
decomposition:
  decision: complex_module
  rationale: "The row is a calibrated multi-material vacuum valve with body, actuator, bellows feedthrough, seals, position indicator, pilot/control hardware, wiring, and leak qualification dependencies."
  proposed_subparts:
    - valve_body
    - electro_pneumatic_actuator
    - bellows_feedthrough
    - fkm_seal_set
    - position_indicator_microswitch
    - pilot_valve_and_wiring
process_abstraction:
  original_process_family: vendor_electro_pneumatic_vacuum_valve_module
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - decomposition_required
    - import_assumption
    - precision_machining
    - assembly
    - leak_testing
    - pressure_testing
    - calibration
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: plumbing_and_pneumatics_v0
      fit: partial
      reason: "Covers installation of vacuum/pneumatic line hardware but not fabrication of the calibrated valve module."
    - process_id: valve_set_gas_handling_assembly_v0
      fit: partial
      reason: "Relevant to assembling gas-handling valve sets, but this row is a catalog electro-pneumatic angle valve."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Critical for validating vacuum isolation performance after installation and after any future local fabrication."
    - process_id: pressure_test_basic_v0
      fit: supporting
      reason: "Relevant to pneumatic actuator and line integrity checks."
    - process_id: electrical_assembly_basic_v0
      fit: supporting
      reason: "Relevant to pilot valve and position indicator wiring if decomposed."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Basic QA anchor; later staging needs valve actuation, leak rate, and position indication checks."
  abstraction_decision: needs_human
  rationale: "Near-term closure should treat this as a precision vendor module. Local manufacture would need decomposition across vacuum valve body fabrication, bellows/feedthrough, seals, actuator, electrical controls, assembly, and qualification."
  process_guardrails:
    tolerance: high
    surface_finish: sealing_face_review
    sealing_quality: high
    alignment_accuracy: moderate
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: "electro pneumatic vacuum shutoff isolation valve for DN63 vacuum line"
  material: aluminum_stainless_fkm_mixed_valve_module
  scale_or_capacity:
    mass_kg: 3.9
    bom_quantity: 1
    row_total_mass_kg: 3.9
    scale_class: medium
  geometry_form: dn63_iso_k_angle_valve_module_with_actuator
merge_pool:
  eligible: false
  functional_purpose_key: flow_control
  precision_guardrails:
    - vacuum_leak_tightness
    - actuator_function
    - position_indication
    - fkm_seal_material
    - cad_proxy_not_physical
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Valve body, bellows feedthrough, FKM sealing, electro-pneumatic actuation, position indication, leak testing, and qualification create a high closure burden."
    - "CAD geometry is a tiny proxy and cannot support local manufacturing geometry."
  post_merge_decision_notes: "Final import/local decision is deferred; review with other vacuum valves and gas-handling modules before deciding module import versus decomposition."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a simple closure item ID at row conversion; keep as a complex vacuum valve module pending merge/decomposition review."
assumptions:
  - "BOM quantity is 1 and row total mass is the vendor catalog mass of 3.9 kg."
  - "Material identity is partial but sufficient for module-level staging: aluminum housing, stainless feedthrough, FKM seal, plus unresolved actuator materials."
  - "The CAD preview is recorded only as proxy evidence and not used for scale."
unresolved:
  - "Internal sub-BOM, valve body geometry, bellows/feedthrough details, actuator materials, electrical details, leak specification, and qualification workflow remain unresolved."
  - "Whether this valve remains an import module and how it groups with other vacuum flow-control rows are deferred."
```
