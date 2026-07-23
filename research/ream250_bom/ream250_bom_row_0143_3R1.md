---
row_identity:
  item: "3R1"
  cad_file: "3R1_clamp_ISO_K_DN63_350BPD100"
  source_row_number: 143
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100"
function:
  summary: "Pfeiffer Vacuum 350BPD100 ISO-K single claw clamp for fastening a DN 63 to DN 100 ISO-K flange to a base plate with an O-ring groove; the BOM row quantity is 4."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "The BOM and manifest identify row 143 item 3R1 as quantity 4 of 3R1_clamp_ISO_K_DN63_350BPD100, product 350BPD100, manufacturer Pfeiffer Vacuum. The Pfeiffer Vacuum Online Shop page identifies 350BPD100 as a claw clamp for a base plate with sealing groove, suitable for metal and elastomer seals, for installing an ISO-K flange on a base plate with O-ring groove, with connection flange DN 63-DN 100 ISO-K. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 led to the Pfeiffer-branded vacuum-shop.com product page; that page carries Pfeiffer Vacuum Online Shop branding, lists the same product ID 350BPD100, links a 350BPD100 data sheet and STEP file, and matches the row manufacturer/product."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.0323
  basis: "FreeCAD measured CAD volume 4119.697 mm^3 for one row part. Using steel density 7850 kg/m^3 from kb/materials/properties.yaml gives 4119.697 mm^3 * 1e-9 m^3/mm^3 * 7850 kg/m^3 = 0.03234 kg, rounded to 0.0323 kg per unit. BOM quantity is 4, so the row total is about 0.129 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3R1_clamp_ISO_K_DN63_350BPD100.step; kb/materials/properties.yaml; https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 4119.697 mm^3, area 2345.582 mm^2, and bounding box 24.00 x 18.60 x 15.00 mm. The Pfeiffer Vacuum Online Shop page identifies the material as zinc-plated steel. The local material density table lists steel density 7850 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 led to the Pfeiffer-branded vacuum-shop.com product page; that page carries Pfeiffer Vacuum Online Shop branding, lists the same product ID 350BPD100, links a 350BPD100 data sheet and STEP file, and matches the row manufacturer/product."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical solid volume of one claw clamp."
    - "The thin zinc plating is neglected in the density calculation because the vendor identifies the base material as steel and the plating mass is negligible at this planning precision."
  uncertainty_notes:
    - "No catalog weight was found or needed for this estimate, but the result depends on the supplied CAD solid matching the purchased clamp without omitted small features or simplifications."
material:
  primary_material: "zinc-plated steel"
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "The Pfeiffer Vacuum Online Shop page title and technical table identify 350BPD100 as a claw clamp made from zinc-plated steel. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 led to the Pfeiffer-branded vacuum-shop.com product page; that page carries Pfeiffer Vacuum Online Shop branding, lists the same product ID 350BPD100, links a 350BPD100 data sheet and STEP file, and matches the row manufacturer/product."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The assembly STEP material extractor returned only Generic material at 1000 kg/m^3, so the vendor material is the useful row-specific material evidence."
how_to_make:
  summary: "Model as standard Pfeiffer ISO-K zinc-plated steel vacuum fastening hardware: prepare the finished 350BPD100 claw clamp, or manufacture locally only if the reusable standard hardware path is later modeled"
  manufacturing_steps:
    - "If local substitution is needed later, make a small steel clamp blank matching the CAD claw geometry and M8 interface."
    - "Machine the bearing faces, central clearance/hole feature, side reliefs, and clamp shoulders visible in the CAD preview."
    - "Deburr, zinc plate, and inspect the DN 63-DN 100 ISO-K flange-contact geometry."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0143_3R1__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3R1_clamp_ISO_K_DN63_350BPD100.step; https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "The rendered CAD contact sheet shows a compact claw clamp block with a central round clearance/hole feature, stepped side faces, and wedge-like clamp shoulders. FreeCAD measured bounding box 24.00 x 18.60 x 15.00 mm. The Pfeiffer Vacuum Online Shop page identifies 350BPD100 as a zinc-plated steel claw clamp, lists M8 and DN 63-DN 100 ISO-K dimensions, and offers the finished part and its STEP download. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 led to the Pfeiffer-branded vacuum-shop.com product page; that page carries Pfeiffer Vacuum Online Shop branding, lists the same product ID 350BPD100, links a 350BPD100 data sheet and STEP file, and matches the row manufacturer/product."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Vacuum flange fastening requires clean, burr-free bearing faces and dimensionally consistent clamp shoulders."
  uncertainty_notes:
    - "The row evidence resolves product identity, geometry, material, and interface, but not Pfeiffer's actual production method, coating specification, or tolerances."
    - "targeted_web_search: checked the BOM-provided Pfeiffer URL, the row-matched Pfeiffer Vacuum Online Shop page for 350BPD100, and searched for 350BPD100 manufacturing, material, datasheet, M8, DN 63 DN 100 ISO-K claw clamp, and zinc-plated steel facts; found row-matched product/material/interface facts but no row-specific production-process specification."
kb_implications:
  - "item_granularity: simple_part - standard ISO-K zinc-plated steel vacuum claw clamp hardware; later KB modeling should map it to reusable standard clamp/fastener hardware rather than a reAM250-specific purchased module."
---

# reAM250 BOM Row 143 - 3R1

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0143_3R1.md
source_research_sha256: "4d89a769631270253db6654c65b4b2215166ca324b2b904e92d3a6248efacca3"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the Pfeiffer 350BPD100 identity, DN63-DN100 ISO-K clamp function, quantity 4 mass basis, zinc-plated steel material evidence, CAD clamp geometry, and simple standard hardware KB implication."
decomposition:
  decision: simple_part
  rationale: "The row is one compact steel claw clamp repeated four times in the BOM. Its closure-relevant features are clamp shoulders, central M8 interface, bearing faces, coating, and inspection, not a hidden module needing subparts."
  proposed_subparts: []
process_abstraction:
  original_process_family: small_steel_clamp_machining_and_zinc_plating
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - drilling
    - precision_machining
    - deburring
    - coating
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers general stock removal for a compact steel clamp blank, while row-specific clamp shoulder geometry and bearing faces need more precise checks."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant to consistent flange-contact shoulders, M8 clearance features, and clean bearing faces."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Relevant to the central hole feature before final deburring and fit inspection."
    - process_id: surface_treatment_basic_v0
      fit: supporting
      reason: "Closest generic surface-treatment anchor for zinc-plated steel when later staging decides the local coating substitute."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional and fit checks for clamp geometry before use in an ISO-K flange joint."
  abstraction_decision: keep_original_family
  rationale: "The source local-substitution route already describes machining a small steel clamp blank, deburring, coating, and inspecting the flange-contact geometry, which fits the general subtractive machining bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: reusable claw clamp for fastening a flanged joint to a grooved base plate
  material: zinc_plated_steel
  scale_or_capacity:
    mass_kg: 0.0323
    bom_quantity: 4
    row_total_mass_kg: 0.129
    scale_class: small
  geometry_form: compact_stepped_claw_clamp_block_with_central_m8_interface
merge_pool:
  eligible: true
  functional_purpose_key: joint_clamping
  precision_guardrails:
    - clamp_shoulder_geometry
    - bearing_face_finish
    - flange_interface_fit
    - corrosion_protective_coating
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Zinc plating may need a local coating substitute if plating chemistry is outside current closure scope."
    - "Flange-contact geometry and burr control affect seal compression, so this should not merge with generic fastener kits without guardrails."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this clamp against other joint-clamping hardware with similar flange-interface geometry and mass scale."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a reusable small steel flange clamp closure item rather than a row-specific purchased SKU."
assumptions:
  - "The STEP solid represents one purchased clamp, and the BOM quantity of four gives the row total mass."
  - "Thin zinc plating is negligible for mass but relevant to surface protection and merge guardrails."
unresolved:
  - "Pfeiffer production method, exact coating specification, and clamp tolerances are not resolved by the row evidence."
```
