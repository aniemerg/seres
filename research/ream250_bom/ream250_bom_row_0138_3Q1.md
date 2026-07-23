---
row_identity:
  item: "3Q1"
  cad_file: "3Q1_pipe_ISO_K_DN100_320RZS100"
  source_row_number: 138
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS100"
function:
  summary: "Pfeiffer Vacuum 320RZS100 ISO-K full nipple, DN 100 ISO-K, used as a straight vacuum piping component between ISO-K flange connections."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html; research/ream250_bom/ream250_bom_row_0138_3Q1__views_2x2.png"
    cited_fact_or_basis: "The BOM row identifies Pfeiffer Vacuum product 320RZS100. The official shop route lists 320RZS100 under ISO-K Full Nipple, connection flange DN 100 ISO-K, dimensions A 108 mm and B 102 mm. The rendered CAD preview shows a straight cylindrical pipe/fitting with ISO-K flange lips at both ends. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS100 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 320RZS100."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 1.55
  basis: "FreeCAD measured CAD volume 192923.105 mm^3 for one full nipple. Converting to 0.000192923105 m^3 and multiplying by stainless_steel_1_4301 density 8030 kg/m^3 from kb/materials/properties.yaml gives 1.549 kg, rounded to 1.55 kg. BOM quantity is 1, so the row total is also about 1.55 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q1_pipe_ISO_K_DN100_320RZS100.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 192923.105 mm^3, area 100992.531 mm^2, and bounding box 108.00 x 143.02 x 143.02 mm. The official shop route identifies 320RZS100 as stainless steel 1.4301/304. The local material density table lists stainless_steel_1_4301 density 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS100 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 320RZS100."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical solid volume for one purchased full nipple."
    - "The product's stated stainless steel 1.4301/304 material is mapped to the local stainless_steel_1_4301 density constant."
  uncertainty_notes:
    - "No row-specific catalog weight was found on the checked product route or targeted searches, so this is a CAD-derived mass estimate rather than a vendor-stated weight."
material:
  primary_material: "stainless steel 1.4301/304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html"
    cited_fact_or_basis: "The official shop route lists ISO-K Full Nipple subcategory/material as stainless steel 1.4301/304 and includes 320RZS100 in that material table. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS100 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 320RZS100."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The assembly STEP metadata returned only Generic material with density 1000.0, so material is taken from the row-matched official shop route rather than local STEP metadata."
how_to_make:
  summary: "Prepare as a standard Pfeiffer Vacuum DN 100 ISO-K stainless full nipple. make it from 1.4301/304 stainless tube and ISO-K flange geometry, then weld, clean, and helium leak test it for vacuum service"
  manufacturing_steps:
    - "Cut stainless steel 1.4301/304 tube or rolled tube stock to the required 108 mm nominal length."
    - "Form or machine DN 100 ISO-K flange lips/rings with the required sealing interface at both ends."
    - "TIG weld or otherwise join the flange features to the tube body, then deburr and clean all vacuum-wetted surfaces."
    - "Inspect ISO-K interface dimensions and perform vacuum leak testing before installation."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html; https://www.pfeiffervacuum.com/global/en/products/components-accessories/vacuum-components/; research/ream250_bom/ream250_bom_row_0138_3Q1__views_2x2.png"
    cited_fact_or_basis: "The row-matched official shop route identifies 320RZS100 as a DN 100 ISO-K full nipple in stainless steel 1.4301/304 with A 108 mm and B 102 mm dimensions. Pfeiffer's vacuum components page states piping components provide stable secure pathways for volume flows, flanges join and seal vacuum-system parts, and components undergo helium leak testing. The rendered CAD contact sheet shows a straight cylindrical nipple with flange lips at both ends. targeted_web_search: searched \"320RZS100 weight\", \"320RZS100 mass\", \"320RZS100 datasheet manufacturing\", and \"Pfeiffer 320RZS100 full nipple material weight\" found row-matched function, material, and dimensions but no row-specific manufacturing-process statement or catalog weight."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the stainless ISO-K full-nipple geometry and common vacuum piping fabrication practice."
    - "Helium leak testing is included because the row is a vacuum component and Pfeiffer describes leak testing as a general vacuum-component quality practice."
  uncertainty_notes:
    - "The vendor/CAD evidence resolves product family, material, and interface geometry, but not the actual Pfeiffer fabrication sequence, weld details, surface finish, or acceptance limit for this specific part number."
kb_implications:
  - "item_granularity: simple_part - standard DN 100 ISO-K stainless full nipple/vacuum pipe fitting; later KB work should model it as reusable vacuum plumbing hardware, not as a reAM250-specific custom machine part."
---

# reAM250 BOM Row 138 - 3Q1

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0138_3Q1.md
source_research_sha256: "7252c05ccc141bb250513008f36cbe154f5b9388cbdd8589b84df18991410c5f"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read function, CAD-derived mass, stainless 1.4301/304 material evidence, fabrication route, kb implications, and preview showing a straight DN100 ISO-K full nipple."
decomposition:
  decision: simple_part
  rationale: "The row is a single straight vacuum pipe fitting with integral ISO-K interface lips. It has no internal module structure."
  proposed_subparts: []
process_abstraction:
  original_process_family: stainless_vacuum_tube_flange_fabrication_and_leak_testing
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - stock_preparation
    - cutting
    - forming
    - precision_machining
    - joining
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: tube_stock_forming_v0
      fit: partial
      reason: "Relevant to making tube stock for the nipple body, though material and DN100 ISO-K details need staging."
    - process_id: welding_tig_basic_v0
      fit: supporting
      reason: "Relevant if flange lips/rings are welded to the tube body."
    - process_id: pressure_test_basic_v0
      fit: supporting
      reason: "Basic integrity check anchor; final staging may need helium leak testing."
    - process_id: cleaning_basic_v0
      fit: supporting
      reason: "Relevant for vacuum-wetted surface cleanliness after fabrication."
  abstraction_decision: keep_original_family
  rationale: "The original route is standard stainless vacuum plumbing hardware. Closure should model it as reusable connector fabrication/testing rather than a reAM250-specific custom part."
  process_guardrails:
    tolerance: dn100_interface_review
    surface_finish: vacuum_wetted_surface_review
    sealing_quality: vacuum_leak_tight_review
    alignment_accuracy: flange_coaxiality_review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: straight pipe connection between flanged gas line interfaces
  material: stainless_steel_1_4301_304
  scale_or_capacity:
    mass_kg: 1.55
    bom_quantity: 1
    row_total_mass_kg: 1.55
    scale_class: small
  geometry_form: dn100_iso_k_straight_full_nipple
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - dn100_iso_k_interface
    - leak_tightness
    - flange_coaxiality
    - vacuum_surface_cleanliness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Weld details, surface finish, and leak-test acceptance limit are unresolved."
    - "DN100 ISO-K interface tooling and gauge standards must be available for local manufacture."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups stainless vacuum plumbing connectors by function, interface, and scale."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before assigning an item ID; likely candidate family is a stainless DN100 plumbing connector."
assumptions:
  - "BOM quantity is 1, so row total mass equals the 1.55 kg per-unit estimate."
  - "The stated 1.4301/304 material and CAD geometry are sufficient for row conversion."
  - "Leak testing is modeled as a guardrail due to vacuum component use."
unresolved:
  - "Exact fabrication sequence, weld details, and acceptance leak-rate limit."
  - "Surface finish and cleaning specification for vacuum-wetted surfaces."
```
