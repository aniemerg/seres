---
row_identity:
  item: "35"
  cad_file: "35_clamping_ring_ISO_KF_DN50_120BSR050"
  source_row_number: 251
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR050"
function:
  summary: "DN 50 ISO-KF clamping ring used to fasten an ISO-KF vacuum flange joint around an elastomer seal in the reAM250 gas/vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/35_clamping_ring_ISO_KF_DN50_120BSR050.step; research/ream250_bom/ream250_bom_row_0251_35__views_2x2.png; https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR050; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr050/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 251 identifies item 35 as product 120BSR050 by Pfeiffer Vacuum, quantity 4, and maps it to 35_clamping_ring_ISO_KF_DN50_120BSR050.step. The rendered CAD preview shows a hinged/segmented clamp ring with a wingnut screw feature. The Pfeiffer online-shop route identifies 120BSR050 as a clamping ring for elastomer seals with DN 50 ISO-KF connection flange. official_alternate_route_check: the original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR050; search/opening the row product resolves to the Pfeiffer Vacuum Online Shop page on vacuum-shop.com for the same order number 120BSR050 and global number 2000048700."
    evidence_basis: "bom_provided"
  assumptions:
    - "The clamping ring is used with the neighboring ISO-KF DN50 seal/flange components in the same reAM250 subsystem rather than as a standalone load-bearing clamp."
  uncertainty_notes: []
mass:
  value_kg: 0.185
  basis: "FreeCAD volume 23047.640 mm^3 equals 0.0000230476 m^3. Using stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml gives 0.185 kg per clamping ring. BOM quantity is 4, so the row total is about 0.740 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/35_clamping_ring_ISO_KF_DN50_120BSR050.step; kb/materials/properties.yaml; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr050/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 23047.640 mm^3, surface area 11116.609 mm^2, and bounding box 115.35 x 48.78 x 19.00 mm. The Pfeiffer online-shop route states material stainless steel 1.4301/304 and DN 50 ISO-KF dimensions A 115 mm, B 90 mm, C 19 mm, consistent with the CAD envelope. The local density table lists stainless_steel_304 density 8030 kg/m^3. official_alternate_route_check: the original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR050; the vacuum-shop.com Pfeiffer online-shop page matches order number 120BSR050 and global number 2000048700."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP solid is treated as the physical-volume proxy for one purchased clamping ring."
    - "Local stainless_steel_304 density is used as the calculation constant for the sourced 1.4301/304 material."
  uncertainty_notes:
    - "The STEP assembly metadata itself reports only placeholder material Generic, so mass depends on the row-matched vendor material and CAD volume rather than embedded material metadata."
material:
  primary_material: "stainless steel 1.4301/304"
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr050/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Pfeiffer online-shop route for order number 120BSR050 states material stainless steel 1.4301/304. Local assembly STEP material extraction for the row returned Generic with density 1000.0, which is placeholder-only and not used as material evidence. official_alternate_route_check: the original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR050; the vacuum-shop.com Pfeiffer online-shop page matches the same product number 120BSR050 and global number 2000048700."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Fabricate the stainless clamp halves and screw/wingnut hardware as a simple vacuum fastener"
  manufacturing_steps:
    - "For local fabrication, machine or precision-cast the two curved stainless clamp halves to the ISO-KF DN50 profile, including hinge/lug and screw-bearing features."
    - "Drill, deburr, and finish the hinge and tightening-lug interfaces; passivate or clean the stainless surfaces for vacuum service."
    - "Assemble the hinge pin, tightening screw, and wingnut or equivalent fastener, then verify fit on DN50 ISO-KF flanges with an elastomer seal at the specified 2 Nm wingnut torque."
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr050/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/35_clamping_ring_ISO_KF_DN50_120BSR050.step; research/ream250_bom/ream250_bom_row_0251_35__views_2x2.png"
    cited_fact_or_basis: "The Pfeiffer online-shop route identifies 120BSR050 as a DN 50 ISO-KF stainless 1.4301/304 clamping ring for elastomer seals and states 2 Nm wingnut torque. CAD and preview show the curved clamp body and wingnut/screw feature. targeted_web_search: searched \"Pfeiffer Vacuum 120BSR050 clamping ring ISO-KF DN50 material weight\" and \"site:pfeiffer-vacuum.com 120BSR050 clamping ring\" results resolved product identity, material, dimensions, and procurement route but did not provide a manufacturing process drawing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the CAD geometry and standard clamp function"
    - "The screw/wingnut hardware is treated as part of the external clamp row because the CAD and vendor product identify one complete clamping ring item"
  uncertainty_notes:
    - "No row-specific tolerance, heat-treatment, surface-finish, or hinge/screw subcomponent specification was found, so local manufacturing details remain approximate."
kb_implications:
  - "item_granularity: simple_part - model as reusable ISO-KF DN50 stainless clamping-ring hardware, not as raw stock or a calibrated purchased module; the BOM quantity should instantiate four units."
---

Research result for reAM250 BOM row 251.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0251_35.md
source_research_sha256: 086fd82c151295c06d1c5add5f50fd02a20cef6dbb3fd81cd4a0c49defbd424a
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Read the original function, mass basis, material evidence, inferred manufacturing route, KB implications, and CAD
    preview showing a segmented clamp ring with hinge and screw/wingnut features.
decomposition:
  decision: simple_part
  rationale: Although the commercial item includes hinge and tightening hardware, closure can treat it as one reusable service
    clamp hardware item at this row-conversion stage; detailed screw and pin closure can use generic fastener hardware later
    if needed.
  proposed_subparts: []
process_abstraction:
  original_process_family: machining_precision_casting_manual_assembly
  primary_process_bucket: general_metal_additive_with_finish_machining
  supporting_processes:
  - additive_build
  - support_removal
  - precision_machining
  - deburring
  - surface_finishing
  - dimensional_inspection
  - thread_forming
  - grinding_lapping
  - leak_testing
  candidate_existing_processes:
  - process_id: wire_arc_additive_manufacturing_v0
    fit: partial
    reason: Covers local metal additive buildup for compatible metal parts; final geometry and tolerance still need finish
      machining.
  - process_id: electron_beam_additive_manufacturing_v0
    fit: partial
    reason: Covers metal additive manufacturing in vacuum-compatible lunar context; material feedstock and resolution need
      later review.
  - process_id: machining_finish_basic_v0
    fit: supporting
    reason: Covers finish machining after additive buildup.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers dimensional checks before staging selects the final recipe.
  - process_id: fastener_kit_small_fabrication_v0
    fit: supporting
    reason: Relevant when the row depends on thread geometry.
  - process_id: precision_grinding_basic_v0
    fit: supporting
    reason: Relevant when rolling, sliding, and raceway surfaces need precision finishing.
  - process_id: leak_testing_v0
    fit: supporting
    reason: Relevant when sealing and fluid integrity matter.
  abstraction_decision: add_post_processing
  rationale: The curved clamp body can converge to the shared metal additive bucket, followed by drilling, deburring, surface
    cleanup, fit checks, and assembly with standard tightening hardware.
  process_guardrails:
    tolerance: review DN50 ISO-KF flange fit, hinge/lug hole alignment, and screw-bearing geometry
    surface_finish: finish contact and bearing surfaces after additive and casting route
    sealing_quality: indirect; clamp must apply even load to an elastomer seal but is not itself the sealing material
    alignment_accuracy: required for hinge pin, screw axis, and opposing clamp-half engagement
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: clamping hardware that fastens an ISO-KF service flange joint around an elastomer seal
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.185
    bom_quantity: 4
    row_total_mass_kg: 0.74
    scale_class: small
  geometry_form: segmented_hinged_clamp_ring_with_tightening_screw
merge_pool:
  eligible: true
  functional_purpose_key: joint_clamping
  precision_guardrails:
  - flange_fit_dimensions
  - hinge_and_screw_alignment
  - clamp_contact_surface_finish
  - tightening_torque_capacity
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - general_metal_additive_with_finish_machining
  import_risk_factors:
  - reliable clamp force and hinge/screw durability are required for service seal loading
  - local route needs compatible small stainless fastener, hinge pin, and wingnut hardware
  post_merge_decision_notes: Final import/local manufacture decision is deferred until after merge review compares this with
    other service clamp and flange hardware rows.
kb_staging:
  proposed_item_id: null
  notes: Wait for merge review before assigning an item ID; this may merge into a generic small sealed joint clamp abstraction
    if material, size, and precision guardrails align.
assumptions:
- The STEP-derived mass of 0.185 kg is accepted as one clamping ring mass, with BOM quantity 4 giving 0.740 kg row total.
- Stainless steel 1.4301/304 is represented as stainless_steel_304 for merge and later KB staging.
- The screw, wingnut, and hinge features can be represented within the clamp hardware item for this pass rather than decomposed
  into vendor-level subparts.
unresolved:
- Exact hinge pin, screw, and wingnut materials and dimensions were not separately resolved from the row evidence.
- Whether additive manufacturing and casting/machining is the preferred local route should be decided after reviewing related
  clamp hardware rows and available process capabilities.
```
