---
row_identity:
  item: "3X1"
  cad_file: "3X1_valve_part_1"
  source_row_number: 164
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html"
function:
  summary: "Part 1 of an AMproved ISO-KF DN40 manual disc valve used to manually control or close fluid/powder flow paths on powder bottles, overflows, filler necks, or pipework in AM machines."
  source:
    url_or_path: "https://www.amproved.com/iso-kf-dn-40-scheibenventil.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0164_3X1__views_2x2.png"
    cited_fact_or_basis: "BOM row 164 identifies item 3X1 as AMproved valve part 1 for 'valve sv04_din_cc_dn40'. The AMproved page names the product ISO-KF DN 40 Scheibenventil, describes it as a disc valve for manual control of fluid streams in pipework, and says it is ideal for closing powder bottles, overflows, and filler necks in AM machines. The rendered CAD preview shows a compact cylindrical valve-body-like component with a central through bore and external lugs. official_alternate_route_check: original BOM URL https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html was checked; the reachable AMproved canonical page https://www.amproved.com/iso-kf-dn-40-scheibenventil.html is the same first-party domain and matches the row product name ISO-KF DN 40 Scheibenventil."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents the first physical CAD part of the valve rather than the complete valve assembly because adjacent row 165 is valve part 2 for the same product."
  uncertainty_notes:
    - "The exact internal role of part 1 within the two-part valve split is not named by the vendor page, so the function is stated at valve-component level."
mass:
  value_kg: 0.173
  basis: "FreeCAD measured CAD volume 21574.099 mm^3 = 2.1574099e-5 m^3. Using stainless_steel density 8000 kg/m^3 from kb/materials/properties.yaml gives 0.1726 kg per part, rounded to 0.173 kg. BOM quantity is 1, so the row total is also about 0.173 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3X1_valve_part_1.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 21574.099 mm^3, area 8200.189 mm^2, and bounding box 38.00 x 45.50 x 38.00 mm. BOM row 164 states material text '_aisi_316l-1_4404_-_epdm: part 1 valve sv04_din_cc_dn40_-'. The local material density table lists stainless_steel density 8000 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid is treated as the physical solid volume for one 3X1 valve part."
    - "The CAD solid is treated as primarily 316L/1.4404 stainless steel; any EPDM associated with the complete valve is not separately visible in this part-1 STEP."
    - "The local broad stainless_steel density is used as the calculation constant for the 316L/1.4404 stainless family."
  uncertainty_notes:
    - "Mass is CAD-derived rather than a catalog weight, and could be low or high if the STEP omits small seals, fasteners, or internal features belonging to this valve part."
material:
  primary_material: "AISI 316L / EN 1.4404 stainless steel valve component, with EPDM present in the valve material set"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 164 material/description text includes '_aisi_316l-1_4404_-_epdm: part 1 valve sv04_din_cc_dn40_-'. Local assembly STEP material extraction for product 3X1_valve_part_1 returned only placeholder material Generic at density 1000.0, which does not resolve material beyond the BOM row text."
    evidence_basis: "bom_provided"
  assumptions:
    - "For the part-1 CAD solid, the metal valve body is modeled as the dominant material, while EPDM is retained as part of the valve-level material set."
  uncertainty_notes:
    - "The BOM text does not identify whether any EPDM volume is physically included in part 1 versus adjacent valve rows, so downstream modeling should avoid assigning an EPDM fraction to this row until the valve subassembly is split."
how_to_make:
  summary: "Machined 316L stainless valve-body production, EPDM seal integration at valve assembly level, cleaning/passivation, and fit/leak inspection"
  manufacturing_steps:
    - "Manufacturing route: machine the roughly 38 x 45.5 x 38 mm stainless valve-body component from 316L/1.4404 bar or near-net blank, including the central bore and external lug features visible in CAD."
    - "Deburr, clean, and passivate the stainless surfaces for vacuum/powder-handling service."
    - "Assemble with the mating valve part and EPDM sealing element, then inspect manual positions, fit, closure, and leak/powder-tightness."
  source:
    url_or_path: "https://www.amproved.com/iso-kf-dn-40-scheibenventil.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3X1_valve_part_1.step; research/ream250_bom/ream250_bom_row_0164_3X1__views_2x2.png"
    cited_fact_or_basis: "AMproved identifies the product as an ISO-KF DN40 disc valve with 3 detent positions for manual control/closure in AM-machine pipework. FreeCAD measured a 38.00 x 45.50 x 38.00 mm one-solid part, and the contact sheet shows a compact bored cylindrical valve-body component with lugs. The detailed machining, passivation, seal integration, and inspection route is inferred from material, geometry, and valve service rather than stated by the vendor. targeted_web_search: searched 'AMPROVED ISO-KF DN 40 Scheibenventil AISI 316L 1.4404 EPDM', 'AMproved ISO-KF DN40 Scheibenventil weight material', 'sv04_din_cc_dn40 316L EPDM valve', and 'ISO-KF DN40 disc valve 316L EPDM manufacturing'; results resolved row-matched product function/material wording but did not provide a row-specific manufacturing process or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible compact bored body and stainless material make subtractive machining from stainless stock a plausible Manufacturing route."
    - "EPDM sealing is handled during valve-level assembly rather than during fabrication of the metal part-1 body."
  uncertainty_notes:
    - "The vendor page does not specify production method, tolerances, seal geometry, surface finish, or leak-test standard; those would matter for a self-manufactured replacement."
kb_implications:
  - "item_granularity: simple_part - model 3X1 as one reusable 316L stainless valve-body component within a larger ISO-KF DN40 disc-valve assembly; keep EPDM sealing as valve-level context unless later CAD or BOM evidence assigns it to this exact part."
---

Research result for reAM250 BOM row 164.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0164_3X1.md
source_research_sha256: "f3d7abf59171a5b2e8e17ffb8e7b5aef38f3a04ace4776ff5f1274c9ac507565"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the AMproved ISO-KF DN40 valve-component function, 0.173 kg CAD-derived mass, 316L/1.4404 stainless plus valve-level EPDM evidence, machined valve-body route, KB implication, and CAD preview showing a bored cylindrical body with lugs."
decomposition:
  decision: simple_part
  rationale: "This row is part 1 of a valve assembly and appears as one stainless body component; decomposition belongs at the complete valve assembly level, not inside this metal body."
  proposed_subparts: []
process_abstraction:
  original_process_family: machined_stainless_valve_body
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - deburring
    - cleaning
    - surface_finishing
    - leak_testing
    - pressure_testing
    - dimensional_inspection
    - assembly
  candidate_existing_processes:
    - process_id: machining_precision_v0
      fit: partial
      reason: "Covers the bored stainless body and lug features, but valve sealing surfaces need explicit guardrails."
    - process_id: fitting_assembly_basic_v0
      fit: supporting
      reason: "Relevant to later assembly with mating valve parts and sealing elements."
    - process_id: plumbing_and_pneumatics_v0
      fit: supporting
      reason: "Anchors the broader pipework and valve installation context for fluid and powder paths."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Relevant to closure checks after the valve body is assembled with EPDM sealing elements."
    - process_id: pressure_test_basic_v0
      fit: supporting
      reason: "Relevant if pressure retention is required for the finished DN40 valve assembly."
    - process_id: surface_treatment_basic_v0
      fit: supporting
      reason: "Covers cleaning, passivation, and surface preparation for stainless service."
  abstraction_decision: substitute_process_family
  rationale: "Although the visible body is machined, its closure role is a plumbing/powder-flow valve component where sealing, fit, and leak testing drive staging decisions."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: moderate
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "valve body component for manually closing a DN40 machine flow path"
  material: stainless_steel_316l_with_valve_level_epdm_context
  scale_or_capacity:
    mass_kg: 0.173
    bom_quantity: 1
    row_total_mass_kg: 0.173
    scale_class: small
  geometry_form: compact_bored_cylindrical_valve_body_with_external_lugs
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - sealing_quality
    - bore_surface_finish
    - dn40_interface
    - epdm_context
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Valve leak performance, seal geometry, surface finish, and manual detent fit are not specified."
    - "EPDM is known at valve material-set level, but its physical allocation across adjacent valve rows is unresolved."
  post_merge_decision_notes: "Final import/local decision is deferred until this part is reviewed with the mating DN40 valve rows and other plumbing connection components."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely staged as part of a generic DN40 stainless valve body family if adjacent valve parts converge."
assumptions:
  - "BOM quantity is 1 and row total mass is treated as 0.173 kg from the CAD stainless-density estimate."
  - "The part-1 STEP is modeled as predominantly 316L stainless steel; EPDM is retained as valve-level context."
  - "Subtractive machining from stainless stock is a sufficient closure abstraction for the body, with leak testing handled at assembly level."
unresolved:
  - "Exact surface finish, tolerance, seal groove allocation, detent geometry, leak-test standard, and mating part responsibility remain unknown."
  - "Whether this row should merge with adjacent valve parts into a complete valve module is deferred to merge review."
```
