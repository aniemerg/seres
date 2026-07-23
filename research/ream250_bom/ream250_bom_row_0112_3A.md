---
row_identity:
  item: "3A"
  cad_file: "3A_angle_pipe_ISO_K_DN63_320RRB063-90"
  source_row_number: 112
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB063_90"
function:
  summary: "DN 63 ISO-K 90-degree radius elbow used to turn a vacuum line while preserving ISO-K flange interfaces at both ends."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0112_3A__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073064/product/320rrb06390/elbow-90-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 112 and the manifest identify item 3A as quantity 15 of Pfeiffer Vacuum product 320RRB063-90 with CAD file 3A_angle_pipe_ISO_K_DN63_320RRB063-90. The official Pfeiffer Vacuum Shop product page identifies 320RRB063-90 as an elbow, 90 degrees, DN 63 ISO-K. The rendered CAD contact sheet shows a flanged 90-degree pipe elbow. official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB063_90; the accessible alternate route https://vacuum-shop.com/shop/en_US/category/2073064/product/320rrb06390/elbow-90-stainless-steel-1-4301-304.html is a Pfeiffer Vacuum online-shop route listing the same order number, global number, DN 63 ISO-K connection flange, and 90-degree elbow family."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.999
  basis: "Per-unit estimate for one elbow: FreeCAD measured volume 124399.904 mm^3 = 0.000124399904 m^3; multiplied by local stainless_steel_304 density 8030 kg/m^3 gives 0.998931 kg. BOM quantity is 15, so the row total is about 14.98 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3A_angle_pipe_ISO_K_DN63_320RRB063-90.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073064/product/320rrb06390/elbow-90-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 124399.904 mm^3, area 81713.913 mm^2, and direct shape bounding box about 140.57 x 140.57 x 105.13 mm. The official Pfeiffer Vacuum Shop product page states material in contact with media as stainless steel 1.4301 (AISI 304). kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3. official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB063_90; the accessible alternate route https://vacuum-shop.com/shop/en_US/category/2073064/product/320rrb06390/elbow-90-stainless-steel-1-4301-304.html is a Pfeiffer Vacuum online-shop route for the same product/order number."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents the material volume for one physical elbow, not a simplified solid envelope."
    - "The local stainless_steel_304 density is an appropriate density constant for stainless steel 1.4301/AISI 304."
  uncertainty_notes:
    - "No catalog weight was exposed in the accessible product page, so mass depends on CAD volume fidelity."
    - "The preview renderer reported a visual-triage bounding box about 135.5 x 135.5 x 95.0 mm; the mass calculation uses the direct FreeCAD STEP volume measurement instead."
material:
  primary_material: "stainless steel 1.4301 (AISI 304)"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://vacuum-shop.com/shop/en_US/category/2073064/product/320rrb06390/elbow-90-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "The official Pfeiffer Vacuum Shop product page states material in contact with media as stainless steel 1.4301 (AISI 304) for order number 320RRB063-90. Local assembly STEP material extraction for 3A_angle_pipe_ISO_K_DN63_320RRB063-90 returned only Generic with density 1000.0, which is placeholder material metadata and was not used as material evidence. official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/320RRB063_90; the accessible alternate route https://vacuum-shop.com/shop/en_US/category/2073064/product/320rrb06390/elbow-90-stainless-steel-1-4301-304.html is a Pfeiffer Vacuum online-shop route for the same product/order number."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The product page states the media-contact material; it does not separately specify weld filler, surface treatment, or non-media-contact marking/finish materials."
how_to_make:
  summary: "Would make a vacuum-compatible stainless 304/1.4301 ISO-K 90-degree elbow by forming or fabricating the elbow body, adding ISO-K flange interfaces, cleaning, and leak testing"
  manufacturing_steps:
    - "For local manufacture, form or bend stainless 304/1.4301 tube to the DN 63 90-degree elbow geometry, or fabricate the elbow from curved tube sections where bending is impractical."
    - "Fabricate/machine the ISO-K flange lips and weld or otherwise join them to both elbow ends with vacuum-compatible stainless joining practice."
    - "Clean/passivate wetted stainless surfaces, inspect flange geometry, and helium leak-test or pressure-test the finished elbow before installation with separate centering ring, seal, and clamp hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0112_3A__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073064/product/320rrb06390/elbow-90-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 112 provides the Pfeiffer Vacuum product identity and URL. The official Pfeiffer Vacuum Shop route identifies 320RRB063-90 as a standard DN 63 ISO-K 90-degree stainless 1.4301/304 elbow with pressure and temperature service data. The CAD preview shows a single flanged elbow body. targeted_web_search: searched '320RRB063-90 Pfeiffer Vacuum elbow manufacturing stainless 1.4301', 'Pfeiffer ISO-K 90 elbow DN63 fabrication stainless 304', and 'ISO-K vacuum elbow stainless leak tested manufacturing'; results resolved product identity, material, and vacuum service data but did not expose Pfeiffer's factory process for this specific elbow, so the local fabrication route is inferred from the row geometry and standard vacuum-piping practice."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A later Manufacturing route can reuse generic stainless vacuum tube forming, flange machining, stainless joining, cleaning, and leak-test processes rather than treating this as a calibrated subsystem."
  uncertainty_notes:
    - "The accessible evidence does not specify Pfeiffer's exact tube-forming method, weld design, tooling, surface finish, passivation, or acceptance leak-rate for 320RRB063-90."
kb_implications:
  - "item_granularity: simple_part - Model as reusable standard vacuum piping hardware rather than a calibrated module; later variants can be parameterized by ISO-K nominal diameter, elbow angle/radius, flange interface, and stainless grade."
---

Structured research result for reAM250 BOM row 112.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0112_3A.md
source_research_sha256: "951a4b67a783b2e1e4d735e6f51f77f221eb3e87924577fa44bf020d830ab3fb"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read DN63 vacuum elbow function, CAD-volume stainless mass basis, Pfeiffer stainless 304 evidence, inferred tube/flange fabrication route, KB implication, and preview of the flanged curved pipe fitting."
decomposition:
  decision: simple_part
  rationale: "The row is one standard vacuum elbow body with two flange interfaces; seals, centering rings, and clamps are separate hardware rows."
  proposed_subparts: []
process_abstraction:
  original_process_family: stainless_vacuum_elbow_forming_welding_machining_testing
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - stock_preparation
    - cutting
    - forming
    - joining
    - precision_machining
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: tube_stock_forming_v0
      fit: partial
      reason: "Covers metal tube forming; the DN63 elbow still needs ISO-K flange work, cleaning, and leak checks."
    - process_id: welding_tig_basic_v0
      fit: supporting
      reason: "Relevant for leak-tight stainless joining between elbow body and flange ends."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers flange face and interface feature finishing after forming and joining."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Covers pressure/vacuum leak checks for completed piping components."
    - process_id: vacuum_testing_v0
      fit: supporting
      reason: "Relevant if acceptance requires vacuum-level hold and cleanliness checks."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks of flange interfaces and elbow geometry."
  abstraction_decision: keep_original_family
  rationale: "The source route and local fallback are both stainless vacuum plumbing fabrication; the canonical bucket preserves forming, flange machining, cleaning, and leak-test needs."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: high
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: flanged elbow redirecting a vacuum plumbing line
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.999
    bom_quantity: 15
    row_total_mass_kg: 14.98
    scale_class: medium
  geometry_form: dn63_iso_k_ninety_degree_flanged_pipe_elbow
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - flange_standard_compatibility
    - sealing_surface_finish
    - weld_leak_tightness
    - vacuum_cleanliness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Quantity 15 makes local fabrication impact material and process closure more than a one-off fitting."
    - "ISO-K flange compatibility and leak-tight stainless joining may require specialized fixtures and inspection."
    - "Cleanliness and acceptance leak rate are not quantified by the row evidence."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred until after merge review with other stainless vacuum elbows and plumbing adapters."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review across vacuum plumbing elbows before assigning a closure item ID."
assumptions:
  - "Use stainless 304/1.4301 as resolved material from Pfeiffer evidence."
  - "Treat clamps, centering rings, and seals as separate rows."
  - "Use 0.999 kg per unit and 14.98 kg row total for merge and closure prioritization."
unresolved:
  - "Exact tube-forming and weld procedure."
  - "Surface finish, passivation, cleanliness standard, and acceptance leak rate."
  - "Whether DN63 and DN100 elbows can share one closure item family with diameter captured as scale/capacity."
```
