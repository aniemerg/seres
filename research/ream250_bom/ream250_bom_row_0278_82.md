---
row_identity:
  item: "82"
  cad_file: "82_seal_ISO_KF_DN40"
  source_row_number: 278
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://wissel-vakuum.de/vakuum-bauteile/vakuum-bauteile-iso-kf/dichtungen/zentrierring/"
function:
  summary: "DN40 ISO-KF vacuum seal or centering-ring seal used with the adjacent ISO-KF clamping ring to align KF flanges and maintain the vacuum joint seal; BOM quantity is 10."
  source:
    url_or_path: "https://wissel-vakuum.de/pc/iso-kf-dichtungen/zentrierring/?wvn_language=en; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0278_82__views_2x2.png"
    cited_fact_or_basis: "The BOM row identifies item 82 as 82_seal_ISO_KF_DN40 from Wissel GmbH and links to Wissel's ISO-KF centering-ring page; the Wissel page says a centering ring aligns and centers vacuum flanges and that the integrated O-ring provides the seal; the CAD preview shows a circular DN40 seal-like ring."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM row name, vendor page category, and adjacent row 83 clamping ring are interpreted as one ISO-KF vacuum joint seal/centering element rather than an unrelated loose gasket."
  uncertainty_notes:
    - "The BOM row does not provide a Wissel product number, so the exact DN40 centering-ring variant is not locked beyond the ISO-KF DN40 seal/centering-ring family."
mass:
  value_kg: 0.0021
  basis: "FreeCAD measured one solid with volume 1161.858 mm^3, surface area 2652.827 mm^2, and bounding box about 48.11 x 48.11 x 8.00 mm. Using the local fkm density of 1800 kg/m^3 as the representative FPM seal-material scenario gives 0.002091 kg per row item."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/82_seal_ISO_KF_DN40.step; kb/materials/properties.yaml; https://wissel-vakuum.de/pc/iso-kf-dichtungen/zentrierring/?wvn_language=en"
    cited_fact_or_basis: "FreeCAD measured volume 1161.858 mm^3 and bounding box 48.11 x 48.11 x 8.00 mm; the Wissel DN40 centering-ring rows list FPM and NBR seal-material variants; kb/materials/properties.yaml lists fkm density as 1800 kg/m^3 and nbr density as 1100 kg/m^3. targeted_web_search: searched \"Wissel 040ZR/BV DN40 centering ring weight\", \"Wissel ISO-KF DN40 seal mass\", and \"82_seal_ISO_KF_DN40 weight\"; found the BOM-provided product-family page but no row-specific catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid is used as the material-volume proxy for the row item."
    - "Because the CAD filename says seal and the preview shows a seal-like ring, the mass value uses the FPM/FKM elastomer scenario rather than treating the whole solid as stainless steel or aluminum."
  uncertainty_notes:
    - "The exact Wissel material variant is not specified by product number; if this row is a complete metal centering ring rather than only the elastomeric seal geometry, the same CAD volume would imply a higher mass, about 0.0031 kg with aluminum density or about 0.0093 kg with stainless-steel density."
material:
  primary_material: "FPM or NBR elastomer seal material, with DN40 Wissel centering-ring variants also available with stainless-steel or aluminum carrier material"
  source:
    url_or_path: "https://wissel-vakuum.de/pc/iso-kf-dichtungen/zentrierring/?wvn_language=en; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The BOM-provided Wissel page lists DN40 centering-ring variants with Stainless Steel / FPM, Stainless Steel (1.4404) / FPM, Stainless Steel (1.4571) / FPM, Aluminum / NBR, and Aluminum / FPM; the assembly STEP material extractor for 82_seal_ISO_KF_DN40 returned only Generic material with density 1000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The seal wording in the CAD filename and the ring-shaped preview are used to prioritize the elastomer seal material family for downstream modeling."
  uncertainty_notes:
    - "The row lacks a product number such as 040ZR/BV, 040ZR/CN, or 040ZR/CV, so the specific elastomer and carrier combination is not resolved."
how_to_make:
  summary: "Model as external ISO-KF vacuum sealing hardware for now; a Manufacturing route would mold or source the elastomer O-ring/seal and, if modeling the complete centering ring, form or machine the metal carrier before cleaning and vacuum fit inspection"
  manufacturing_steps:
    - "Select the resolved DN40 ISO-KF seal variant and material combination, such as FPM/FKM or NBR elastomer with stainless-steel or aluminum carrier if a centering-ring assembly is required."
    - "For the elastomer seal, compression-mold or transfer-mold the O-ring/seal geometry, then trim flash and inspect the 48.11 mm by 8.00 mm CAD envelope against the DN40 KF interface."
    - "For a complete centering ring, machine or form the stainless-steel or aluminum carrier ring and seat the replaceable elastomer O-ring."
    - "Clean for vacuum service and verify fit with the mating ISO-KF DN40 flanges and clamping ring."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0278_82__views_2x2.png; https://wissel-vakuum.de/pc/iso-kf-dichtungen/zentrierring/?wvn_language=en"
    cited_fact_or_basis: "The CAD preview shows a circular seal-like ring; the BOM-provided Wissel page identifies the product family as ISO-KF centering rings with integrated O-rings and DN40 material variants including FPM and NBR. targeted_web_search: searched \"Wissel 040ZR/BV DN40 centering ring material\", \"82_seal_ISO_KF_DN40 material\", and \"ISO-KF DN40 centering ring FPM NBR manufacturing\" found the row-matched Wissel product-family page and generic vacuum-hardware context, but no row-specific manufacturing drawing or production process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from elastomer seal geometry, ISO-KF centering-ring construction, and common vacuum seal production practice."
    - "External-hardware modeling is preferred until a later KB pass intentionally expands standard ISO-KF seal sub-BOMs"
  uncertainty_notes:
    - "The exact production method, elastomer compound, carrier-ring geometry, and cleaning specification are not stated by the BOM row or the vendor product-family page."
kb_implications:
  - "item_granularity: simple_part - replaceable ISO-KF DN40 vacuum sealing item; model as a purchased/imported seal or centering-ring seal unless the KB later adds a reusable standard vacuum-fitting family."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0278_82.md
source_research_sha256: "87ffe75427b1f1f0f13b2e5a3434f8ff5ae77c01c231bfc98b50c27ac707673d"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read row-local function, quantity, mass basis, material uncertainty, manufacturing route, kb implications, and preview showing a small circular DN40 seal-like ring."
decomposition:
  decision: simple_part
  rationale: "The row is a replaceable DN40 sealing element. If later evidence proves a metal centering carrier is included, merge review can split the carrier from the elastomer seal."
  proposed_subparts: []
process_abstraction:
  original_process_family: molded_elastomer_vacuum_seal_with_possible_carrier_ring
  primary_process_bucket: polymer_elastomer_forming_dispensing
  supporting_processes:
    - elastomer_forming
    - cutting
    - deburring
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: elastomer_molding_basic_v0
      fit: direct
      reason: "Best existing anchor for molding the FPM/FKM/NBR seal geometry at coarse closure level."
    - process_id: gasket_sheet_cut_to_part_v0
      fit: partial
      reason: "Relevant if the seal is cut from elastomer sheet stock instead of molded; less suitable for the ring profile shown."
    - process_id: sealing_and_assembly_basic_v0
      fit: supporting
      reason: "Covers installing the seal into the DN40 joint with cleanliness checks."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional and visual checks before staging selects stricter seal inspection."
  abstraction_decision: substitute_process_family
  rationale: "The source is vendor standard vacuum sealing hardware, but the closure-relevant manufacturing path is elastomer seal forming plus inspection. Possible metal carrier details stay unresolved rather than forcing a separate connector item during row conversion."
  process_guardrails:
    tolerance: review
    surface_finish: sealing_surface_review
    sealing_quality: leak_tight_review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: replaceable circular sealing element for an ISO-KF flange joint
  material: fpm_fkm_nbr_elastomer_with_possible_metal_carrier
  scale_or_capacity:
    mass_kg: 0.0021
    bom_quantity: 10
    row_total_mass_kg: 0.021
    scale_class: small
  geometry_form: circular_dn40_iso_kf_seal_ring
merge_pool:
  eligible: true
  functional_purpose_key: sealing_element
  precision_guardrails:
    - dn40_interface_geometry
    - elastomer_compound
    - leak_tightness
    - carrier_inclusion_uncertain
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - polymer_elastomer_forming_dispensing
  import_risk_factors:
    - "Exact elastomer compound, vendor variant, and inclusion of a metal carrier are unresolved."
    - "Vacuum cleanliness and leak performance may require imported seal stock until local elastomer compounding matures."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups standard DN40 sealing elements and resolves whether carrier rings are separate closure items."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before assigning an item ID; likely candidate family is a small ISO-KF sealing element."
assumptions:
  - "BOM quantity is 10, so row total mass is about 0.021 kg using the 0.0021 kg per-unit estimate."
  - "The CAD filename and preview justify prioritizing the elastomer seal identity despite vendor centering-ring variants with metal carriers."
  - "Vacuum role is recorded as a sealing guardrail, not as the merge key."
unresolved:
  - "Specific Wissel DN40 variant and elastomer compound."
  - "Whether the row includes only the elastomer seal geometry plus a separate carrier in the assembly."
  - "Cleaning and leak-test acceptance requirements for the joint."
```
