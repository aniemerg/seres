---
row_identity:
  item: "3U"
  cad_file: "3U_flow_rectifier"
  source_row_number: 161
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "One long narrow passive gas-flow rectifier for the reAM250, likely straightening or conditioning inert gas flow through an internal duct or chamber passage."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3U_flow_rectifier.step; research/ream250_bom/ream250_bom_row_0161_3U__views_2x2.png; https://www.riitalia.online/wp-content/uploads/2017/05/Riitalia-H-5800-1065-02-A_PlusPac_brochure_print.pdf"
    cited_fact_or_basis: "BOM row 161 names item 3U as '3U_flow_rectifier' with quantity 1. FreeCAD measured one solid and the contact sheet shows a long duct-like part with repeated internal vane/fin features, about 259.70 x 26.00 x 42.00 mm. The AM250 PlusPac brochure describes gas-flow and filtration systems used to keep the AM250 process environment clean."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents the single physical flow-rectifier item for this BOM row."
  uncertainty_notes:
    - "The BOM and CAD identify the part as a flow rectifier but do not state its exact location in the gas path or the intended flow direction."
mass:
  value_kg: 0.678
  basis: "Per-unit planning estimate for quantity 1. FreeCAD volume is 86341.951 mm^3, equal to 8.6341951e-5 m^3. Using the local generic steel density constant of 7850 kg/m^3 gives 0.678 kg; if the same CAD volume were aluminum at 2700 kg/m^3, it would be about 0.233 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3U_flow_rectifier.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 86341.951 mm^3 and bounding box 259.70 x 26.00 x 42.00 mm. kb/materials/properties.yaml lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. targeted_web_search: tried '3U_flow_rectifier material weight', '3U flow rectifier selective laser melting reAM250', 'flow rectifier additive manufacturing machine material', and 'Renishaw flow rectifier AM250'; results gave general AM250 gas-flow or flow-rectifier context but no row-specific mass or material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A steel-like density is used as the conservative single-value planning estimate because the part is a rigid machine gas-path insert and no row-specific material is provided."
  uncertainty_notes:
    - "Actual mass could be closer to 0.233 kg if this flow rectifier is aluminum; no catalog weight or non-placeholder STEP material resolves the material-dependent range."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 161 gives no manufacturer, product ID, material hint, or link URL. Assembly STEP material extraction for product 3U_flow_rectifier returned material 'Generic' with density 1000.0, which is placeholder metadata. targeted_web_search: tried '3U_flow_rectifier material weight', '3U flow rectifier selective laser melting reAM250', 'flow rectifier additive manufacturing machine material', and 'Renishaw flow rectifier AM250'; no row-specific usable material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The rigid finned duct geometry and build-machine gas-path service indicate a metal component rather than a polymer seal, filter element, or consumable."
  uncertainty_notes:
    - "Material family is intentionally broad; downstream KB modeling should not choose steel, stainless steel, or aluminum without checking the full gas-flow assembly design intent."
how_to_make:
  summary: "Fabricate as a one-piece machined or additively manufactured metal gas-flow insert"
  manufacturing_steps:
    - "Start from metal bar, plate, extrusion, or a near-net additive-manufactured blank sized for the roughly 260 mm long duct-like body."
    - "Machine the outer rectangular profile and internal vane/fin channels, or print the vane geometry near-net if the internal features are not accessible by simple milling."
    - "Deburr and clean all flow-facing edges to avoid loose particles in the gas path."
    - "Verify fit and flow orientation against the mating gas-path housing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3U_flow_rectifier.step; research/ream250_bom/ream250_bom_row_0161_3U__views_2x2.png"
    cited_fact_or_basis: "CAD preview shows a long one-piece rectifier with repeated vane/fin features rather than a calibrated purchased module. FreeCAD reports one solid with a narrow 259.70 x 26.00 x 42.00 mm envelope. targeted_web_search: tried '3U_flow_rectifier material weight', '3U flow rectifier selective laser melting reAM250', 'flow rectifier additive manufacturing machine material', and 'Renishaw flow rectifier AM250'; no source stated the manufacturing route for this row."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Machining or metal additive manufacturing are the most plausible local routes because the CAD geometry appears to be a single rigid part with internal flow-conditioning fins."
  uncertainty_notes:
    - "The contact sheet is sufficient for route triage but not for internal channel accessibility, tolerance, surface finish, or whether the OEM made the row by machining, printing, casting, or joining."
kb_implications:
  - "item_granularity: simple_part - Model later as one reusable metal gas-flow rectifier insert rather than as a purchased module or raw stock."
---

Result generated for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0161_3U.md
source_research_sha256: 057680357e8971bc8a717c49f5b4095335d4e0add0e68da193d026fe6c7bc5bc
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed the function, quantity, CAD-derived mass range, unknown-metal material evidence, plausible machining/additive
    route, KB implication, and CAD preview showing a long finned gas-path insert.
decomposition:
  decision: simple_part
  rationale: The row is a one-piece passive flow-conditioning insert, not a vendor module and assembly with internal closure-relevant
    subparts.
  proposed_subparts: []
process_abstraction:
  original_process_family: machining_metal_additive_manufacturing
  primary_process_bucket: general_metal_additive_with_finish_machining
  supporting_processes:
  - additive_build
  - support_removal
  - precision_machining
  - deburring
  - surface_finishing
  - dimensional_inspection
  - leak_testing
  - joining
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
  - process_id: leak_testing_v0
    fit: supporting
    reason: Relevant when sealing and fluid integrity matter.
  - process_id: welding_basic_v0
    fit: supporting
    reason: Relevant when the row needs permanent joining.
  abstraction_decision: add_post_processing
  rationale: The internal vane geometry can converge to the shared metal additive bucket. Post-processing remains required
    for fit surfaces, loose-particle cleanup, and flow-facing edge quality.
  process_guardrails:
    tolerance: review - external fit to the mating duct and housing must be checked.
    surface_finish: review - flow-facing surfaces and vane edges may need deburring and smoothing.
    sealing_quality: review - sealing is not explicit, but duct-interface faces may need adequate flatness.
    alignment_accuracy: review - vane orientation and installed flow direction matter for gas-flow conditioning.
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: passive gas-flow rectification and conditioning inside a machine gas path
  material: unknown_metal_alloy
  scale_or_capacity:
    mass_kg: 0.678
    bom_quantity: 1
    row_total_mass_kg: 0.678
    scale_class: small
  geometry_form: long_rectangular_finned_flow_insert
merge_pool:
  eligible: true
  functional_purpose_key: gas_flow_rectification
  precision_guardrails:
  - vane_geometry
  - duct_fit
  - flow_facing_surface_finish
  - particle_cleanliness
  - material_compatibility_with_inert_gas_path
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - general_metal_additive_with_finish_machining
  import_risk_factors:
  - Material family is unresolved; stainless steel, aluminum, and alternate alloy may be required by the gas-path environment.
  - Internal vane geometry and cleanliness requirements could exceed simple local machining if fine channels trap powder and
    burrs.
  post_merge_decision_notes: Final import/local manufacture decision is deferred until merge review compares this with other
    gas-flow inserts and determines the condition that a shared metal flow-rectifier abstraction is acceptable.
kb_staging:
  proposed_item_id: null
  notes: Wait for merge review; this likely belongs in a reusable gas-flow rectifier and duct-insert class rather than a row-specific
    item.
assumptions:
- The row is treated as quantity 1 with a conservative steel-density planning mass of 0.678 kg.
- Unknown material is kept broad because source evidence does not resolve steel, stainless steel, aluminum, and alternate
  alloy.
- The CAD preview is used to classify the part as a finned flow insert with geometry important to function.
unresolved:
- Exact material, surface finish, interface tolerances, and gas-path location are not specified.
- Merge review must determine the condition that the vane geometry is functionally generic and unique to this machine gas-flow
  path.
```
