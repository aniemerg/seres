---
row_identity:
  item: "3R2"
  cad_file: "3R2_seal_ISO_K_DN63_311ZRA063"
  source_row_number: 144
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA063"
function:
  summary: "DN 63 ISO-K vacuum centering ring and seal assembly; it centers the flange interface and provides the NBR elastomer sealing element."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA063 -> https://www.vacuum-shop.com/shop/en_US/category/2073005/product/311zra063/centering-ring-with-outer-ring-aluminum.html; research/ream250_bom/ream250_bom_row_0144_3R2__views_2x2.png"
    cited_fact_or_basis: "The BOM row identifies item 3R2 as Pfeiffer Vacuum product 311ZRA063. The row-matched product page identifies 311ZRA063 as a centering ring with outer ring for connection flange DN 63 ISO-K. The CAD contact sheet shows a thin annular ring form. official_alternate_route_check: the original BOM URL is on pfeiffer-vacuum.com; the alternate vacuum-shop.com page is an official Pfeiffer Vacuum Components & Solutions shop route for the same manufacturer and exact order number 311ZRA063."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.013
  basis: "FreeCAD measured one solid with volume 5586.124 mm^3, surface area 6239.540 mm^2, and bounding box 85.99 x 86.00 x 8.00 mm. The rendered preview reported an about 79.3 x 79.3 x 8.0 mm mesh bounding box for visual triage only. Estimated mass uses the CAD volume as a combined material-volume proxy and a coarse 75% aluminum / 25% NBR volume split. Local density constants from kb/materials/properties.yaml are aluminum 2700 kg/m^3 and NBR 1100 kg/m^3, giving effective density about 2300 kg/m^3 and mass about 0.01285 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3R2_seal_ISO_K_DN63_311ZRA063.step; kb/materials/properties.yaml; https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA063 -> https://www.vacuum-shop.com/shop/en_US/category/2073005/product/311zra063/centering-ring-with-outer-ring-aluminum.html"
    cited_fact_or_basis: "FreeCAD measured 5586.124 mm^3 for the row STEP. The row-matched product page and datasheet state aluminum for media-contact material and NBR for the O-ring. The local density table lists aluminum at 2700 kg/m^3 and NBR at 1100 kg/m^3. official_alternate_route_check: the original BOM URL is on pfeiffer-vacuum.com; the alternate vacuum-shop.com page is an official Pfeiffer Vacuum Components & Solutions shop route for the same manufacturer and exact order number 311ZRA063."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The single-solid STEP volume is used as a combined volume proxy for the aluminum ring and NBR O-ring because the CAD does not expose separate material volumes."
    - "A 75% aluminum / 25% NBR volume split is used as a coarse estimate."
  uncertainty_notes:
    - "targeted_web_search: searched \"311ZRA063 Pfeiffer Vacuum material seal ISO-K DN63\", \"311ZRA063 Pfeiffer Vacuum seal ISO-K DN63 NBR aluminum\", and \"311ZRA063 mass weight\"; found row-matched material and dimensional facts but no catalog mass or material-volume split."
    - "The aluminum-to-NBR volume fraction is not measured separately, so the mass should be treated as an order-of-magnitude estimate."
material:
  primary_material: "aluminum ring with NBR O-ring"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA063 -> https://www.vacuum-shop.com/shop/en_US/category/2073005/product/311zra063/centering-ring-with-outer-ring-aluminum.html"
    cited_fact_or_basis: "The row-matched product page and datasheet for 311ZRA063 state aluminum outer ring, materials in contact with media aluminum, and O-ring material NBR. official_alternate_route_check: the original BOM URL is on pfeiffer-vacuum.com; the alternate vacuum-shop.com page is an official Pfeiffer Vacuum Components & Solutions shop route for the same manufacturer and exact order number 311ZRA063."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Manufacture as a small vacuum flange seal consumable: form the aluminum centering/outer ring, mold"
  manufacturing_steps:
    - "Machine, stamp, or otherwise form the aluminum centering/outer ring profile to DN 63 ISO-K geometry."
    - "Mold, cut"
    - "Deburr and clean the aluminum ring so flange-contact and seal-contact surfaces are smooth."
    - "Install the NBR O-ring onto the aluminum ring and inspect fit, concentricity, and visible seal damage."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA063 -> https://www.vacuum-shop.com/shop/en_US/category/2073005/product/311zra063/centering-ring-with-outer-ring-aluminum.html; research/ream250_bom/ream250_bom_row_0144_3R2__views_2x2.png"
    cited_fact_or_basis: "The row-matched product page identifies an aluminum outer-ring centering ring with NBR O-ring for DN 63 ISO-K. The CAD contact sheet shows a thin annular ring/seal geometry. official_alternate_route_check: the original BOM URL is on pfeiffer-vacuum.com; the alternate vacuum-shop.com page is an official Pfeiffer Vacuum Components & Solutions shop route for the same manufacturer and exact order number 311ZRA063."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the stated aluminum plus NBR construction and the visible thin annular profile, not from a vendor process specification."
  uncertainty_notes:
    - "Targeted_web_search: searched \"311ZRA063 Pfeiffer Vacuum material seal ISO-K DN63\", \"311ZRA063 Pfeiffer Vacuum seal ISO-K DN63 NBR aluminum\", and \"311ZRA063 manufacturing process centering ring\" found product material and dimensional facts but no vendor manufacturing process description."
kb_implications:
  - "item_granularity: simple_part - replaceable ISO-K vacuum centering ring/seal assembly; later KB modeling can keep it as a purchased replaceable or applied part unless vacuum-seal fabrication becomes in scope."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0144_3R2.md
source_research_sha256: "5bfd1657f9c449bf7d47e677bc22c6252fcfbab97e14b733b7f431ba90a0ceef"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed Pfeiffer 311ZRA063 identity, DN63 ISO-K centering and sealing role, coarse aluminum/NBR mass estimate, annular CAD geometry, material evidence, and replaceable seal assembly KB implication."
decomposition:
  decision: decompose_into_parts
  rationale: "The row is a replaceable flange seal assembly made from at least two closure-relevant materials. Later local manufacture should split the aluminum centering ring from the NBR O-ring rather than treating the whole row as one homogeneous part."
  proposed_subparts:
    - aluminum_centering_outer_ring
    - nbr_o_ring_seal
process_abstraction:
  original_process_family: aluminum_centering_ring_and_elastomer_seal_assembly
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - precision_machining
    - elastomer_forming
    - deburring
    - cleaning
    - assembly
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers aluminum ring forming by stock removal, with seal-contact geometry needing tighter feature control."
    - process_id: elastomer_molding_basic_v0
      fit: supporting
      reason: "Relevant to producing the NBR O-ring subpart after decomposition."
    - process_id: seal_installation_v0
      fit: supporting
      reason: "Relevant to installing the elastomer ring onto the aluminum centering ring before inspection."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Relevant to later flange-interface validation after this seal is assembled into the gas-handling joint."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers concentricity, fit, visible seal damage, and dimensional checks."
  abstraction_decision: substitute_process_family
  rationale: "The evidence describes a replaceable flange centering/seal assembly. Plumbing connector fabrication/testing preserves the gas-interface function while recording aluminum machining and elastomer forming as supporting processes."
  process_guardrails:
    tolerance: high
    surface_finish: high
    sealing_quality: high
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: centering and elastomer sealing element for an ISO-K flanged joint
  material: aluminum_ring_with_nbr_o_ring
  scale_or_capacity:
    mass_kg: 0.013
    bom_quantity: 1
    row_total_mass_kg: 0.013
    scale_class: small
  geometry_form: thin_annular_centering_ring_with_integrated_o_ring_seal
merge_pool:
  eligible: true
  functional_purpose_key: joint_sealing
  precision_guardrails:
    - seal_material
    - flange_size
    - concentricity
    - seal_contact_surface_finish
    - leak_tightness_after_installation
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "NBR production and seal-quality control may be outside the near-term local closure path."
    - "Aluminum and NBR volume split is estimated from a single-solid CAD proxy rather than measured subpart volumes."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this DN63 flange seal with other centering rings, O-rings, and flange sealing hardware."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely staged as a reusable flange sealing assembly with separate aluminum ring and elastomer seal assumptions."
assumptions:
  - "The single CAD solid is a combined proxy for the aluminum ring and NBR O-ring."
  - "The row-matched Pfeiffer product data is reliable for material and flange-size identity."
unresolved:
  - "Exact aluminum alloy, O-ring compound details, material-volume split, seal compression specification, and leak-test requirement are not resolved."
```
