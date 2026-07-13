---
row_identity:
  item: "2AL1"
  cad_file: "2AL1_gearbox_8GA40-060--025S2PF"
  source_row_number: 63
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.br-automation.com/product/80SD100XD.C044-01"
function:
  summary: "B&R 8GA40-060 angular planetary gearbox for right-angle speed reduction and torque transmission in the reAM250 drive axis; the row product corresponds to an 8GA40 size 060, ratio 25, two-stage IP54 gearbox."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.br-automation.com/en/products/motion-control/standard-planetary-gearboxes-8g/angular-planetary-gearboxes-8ga/8ga40-060hh025klmm/; research/ream250_bom/ream250_bom_row_0063_2AL1__views_2x2.png"
    cited_fact_or_basis: "BOM row 63 and the manifest identify item 2AL1 as quantity 1 of CAD file 2AL1_gearbox_8GA40-060--025S2PF, description/product ID 8GA40-060--025S2PF, manufacturer B&R. The exact B&R 8GA40-060hh025klmm product page lists an angular planetary gearbox, ratio i = 25, 2 stages, IP54, 40 Nm nominal output torque, and 64 Nm max output torque. The CAD contact sheet shows a right-angle gearbox body with a cylindrical motor/input side and output shaft. official_alternate_route_check: the BOM Link URL https://www.br-automation.com/product/80SD100XD.C044-01 is a B&R first-party route but identifies an ACOPOSmicro stepper motor module; the cited B&R gearbox page is the first-party product route found from the BOM row product ID and matches the CAD shape, row manufacturer, and 8GA40-060 ratio-25 gearbox identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row product ID spelling with double hyphen maps to B&R's web material number form 8GA40-060hh025klmm for the base angular gearbox variant."
  uncertainty_notes:
    - "The BOM link points to a different B&R product, so the function uses the row product ID and CAD geometry as the identity lock."
mass:
  value_kg: 1.9
  basis: "Per-unit catalog mass for quantity 1. The B&R exact product page lists weight m = 1.9 kg for 8GA40-060hh025klmm; the BOM row quantity is 1, so row total is also 1.9 kg. CAD measured volume is 487659.496 mm^3 with bounding box about 159.68 x 60.00 x 85.50 mm, used only as geometry sanity check rather than density-derived mass."
  source:
    url_or_path: "https://www.br-automation.com/en/products/motion-control/standard-planetary-gearboxes-8g/angular-planetary-gearboxes-8ga/8ga40-060hh025klmm/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AL1_gearbox_8GA40-060--025S2PF.step"
    cited_fact_or_basis: "The exact B&R 8GA40-060hh025klmm product page lists weight m [kg] as 1.9. FreeCAD measured the supplied row STEP as one solid with volume 487659.496 mm^3 and bounding box about 159.68 x 60.00 x 85.50 mm. official_alternate_route_check: the BOM Link URL https://www.br-automation.com/product/80SD100XD.C044-01 is a B&R first-party route but identifies a stepper motor module; the row-matched B&R gearbox product page was found from the BOM row product ID and used for mass."
    evidence_basis: "bom_provided"
  assumptions:
    - "The catalog weight applies to one physical gearbox represented by this BOM row."
  uncertainty_notes:
    - "The row-specific STEP volume is not used for mass because the gearbox is a multi-material assembly and the local STEP material metadata is only Generic."
material:
  primary_material: "unknown metal/alloy gearbox assembly with fully hardened gear toothing"
  source:
    url_or_path: "https://www.br-automation.com/en-us/products/motion-control/standard-planetary-gearboxes-8g/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "B&R's standard 8G planetary gearbox overview states that the series uses honed sun and planets with straight-toothed, fully hardened toothing. Local assembly STEP material extraction for 2AL1_gearbox_8GA40-060--025S2PF returned only material Generic with density 1000.0, which is placeholder metadata. targeted_web_search: tried '8GA40-060hh025klmm material housing gears', '8GA40-060--025S2PF material', 'B&R 8GA planetary gearbox material', and 'standard planetary gearboxes 8G fully hardened toothing honed'; found the B&R hardened-toothing statement but no exact housing, shaft, bearing, or gear grade for this row."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A precision industrial planetary gearbox is treated as a metal mechanical assembly for KB planning; only the hardened toothing is explicitly supported by the B&R source."
  uncertainty_notes:
    - "Exact housing material, shaft alloy, bearing materials, seals, lubricant, and heat-treatment grades remain unspecified."
how_to_make:
  summary: "Treat as a external precision gearbox module for current KB granularity; Manufacturing requires machining housing and shafts, cutting/grinding hardened planetary gear components, bearing and seal installation, lubrication, right-angle gearbox assembly, and performance inspection"
  manufacturing_steps:
    - "For a future Manufacturing route, machine the gearbox housing, output shaft, input adapter, and right-angle gear carrier interfaces from suitable metal stock."
    - "Manufacture sun, planet, ring, and bevel/right-angle gear elements with heat treatment and finishing suitable for hardened gear teeth."
    - "Install bearings, seals, lubricant, and fasteners, then assemble the two-stage ratio-25 gearbox."
    - "Inspect backlash, torque capacity, shaft alignment, seal integrity, and running noise before integration."
  source:
    url_or_path: "https://www.br-automation.com/en/products/motion-control/standard-planetary-gearboxes-8g/angular-planetary-gearboxes-8ga/8ga40-060hh025klmm/; https://www.br-automation.com/en-us/products/motion-control/standard-planetary-gearboxes-8g/; research/ream250_bom/ream250_bom_row_0063_2AL1__views_2x2.png"
    cited_fact_or_basis: "The exact B&R page identifies the item as an 8GA40-060 angular planetary gearbox with ratio 25, 2 stages, IP54, torque ratings, efficiency, and weight. The B&R 8G overview states the standard series uses honed sun and planets and fully hardened toothing. The rendered contact sheet shows a right-angle gearbox housing with shaft and motor/input-side geometry. bom_url_route_check: the BOM Link URL is a B&R stepper motor module page and did not resolve the row gearbox manufacturing route. targeted_web_search: tried '8GA40-060hh025klmm manufacturing process', '8GA40-060--025S2PF gearbox manufacturing', and 'B&R 8GA planetary gearbox material manufacturing'; found row-matched specs and general B&R gearbox construction statements, but no B&R production-process details."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the resolved product type, visible CAD geometry, and standard precision gearbox construction practice."
  uncertainty_notes:
    - "B&R's actual supplier, gear finishing method, bearing selection, lubricant, seal details, and quality-control specifications are not provided by the row evidence."
kb_implications:
  - "item_granularity: complex_module - model as a functional precision angular planetary gearbox complex module for this pass; decompose later only with a sub-BOM covering gears, bearings, seals, housing, lubricant, and inspection/calibration."
---

Result generated for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0063_2AL1.md
source_research_sha256: 4a6220e03e6d01c93eab23e41c7fb9511186b5b37d7c2367df66471163e882a1
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Read function, catalog mass, unknown multi-material gearbox material evidence, inferred precision gearbox manufacturing
    route, KB implication, and CAD preview showing the right-angle gearbox before conversion.
decomposition:
  decision: decompose_into_parts
  rationale: This is a precision angular planetary gearbox module, not a simple part. Internal gears, shafts, bearings, seals,
    lubricant, housing, fasteners, and inspection/calibration requirements are closure-relevant and should be exposed before
    merge and KB staging.
  proposed_subparts:
  - gearbox_housing
  - sun_planet_ring_and_right_angle_gears
  - input_and_output_shafts
  - bearing_set
  - seal_set
  - lubricant_charge
  - gearbox_fasteners
process_abstraction:
  original_process_family: vendor_precision_angular_planetary_gearbox_assembly
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
  - decomposition_required
  - import_assumption
  - precision_machining
  - grinding_lapping
  - heat_treatment
  - dimensional_inspection
  - calibration
  - gear_tooth_machining
  - leak_testing
  candidate_existing_processes:
  - process_id: assembly_basic_v0
    fit: poor_fit
    reason: Only covers generic assembly; internal precision manufacturing needs decomposition.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers basic checks while detailed metrology remains unresolved.
  - process_id: calibration_and_test_basic_v0
    fit: supporting
    reason: Covers generic calibration and test after decomposition defines the item.
  - process_id: gear_cutting_basic_v0
    fit: supporting
    reason: Relevant when tooth geometry controls motion transfer.
  - process_id: precision_grinding_basic_v0
    fit: supporting
    reason: Relevant when rolling, sliding, and raceway surfaces need precision finishing.
  - process_id: leak_testing_v0
    fit: supporting
    reason: Relevant when sealing and fluid integrity matter.
  - process_id: calibration_and_test_basic_v0
    fit: supporting
    reason: Relevant when calibration affects functional acceptance.
  abstraction_decision: substitute_process_family
  rationale: The row evidence indicates a vendor precision gearbox with hardened honed gear toothing, two-stage ratio-25 gearing,
    IP54 sealing, bearings, lubrication, backlash and torque requirements. Generic additive, sheet, and basic machining buckets
    are not enough without decomposition and precision gear finishing/inspection.
  process_guardrails:
    tolerance: blocked_until_decomposed
    surface_finish: blocked_until_decomposed
    sealing_quality: review
    alignment_accuracy: blocked_until_decomposed
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: right-angle speed reduction and torque transmission for a machine drive axis
  material: unknown_metal_alloy_gearbox_assembly
  scale_or_capacity:
    mass_kg: 1.9
    bom_quantity: 1
    row_total_mass_kg: 1.9
    scale_class: medium
    nominal_output_torque_Nm: 40
    max_output_torque_Nm: 64
    gear_ratio: 25
  geometry_form: right_angle_planetary_gearbox_module
merge_pool:
  eligible: false
  functional_purpose_key: right_angle_speed_reduction_torque_transmission
  precision_guardrails:
  - backlash
  - gear_tooth_hardness_and_finish
  - shaft_alignment
  - bearing_fit
  - seal_integrity
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - precision_component_import_decompose_later
  import_risk_factors:
  - Exact housing, shaft, bearing, seal, lubricant, and gear material grades are unresolved.
  - Hardened honed gear toothing, backlash control, torque capacity, IP54 sealing, and right-angle alignment are precision
    blockers for a generic one-piece local process.
  - The BOM link points to a different B&R product, although the row product ID, CAD geometry, and alternate B&R product page
    support the gearbox identity.
  post_merge_decision_notes: Final import/local decision is deferred. Decompose this module before merge review; after decomposition,
    housing and shaft elements may use local machining while gears, bearings, seals, lubricant, and precision inspection may
    remain separate import/local decisions.
kb_staging:
  proposed_item_id: null
  notes: Do not assign a final closure item ID at row conversion. Stage as a precision gearbox decomposition candidate rather
    than merging the whole vendor module.
assumptions:
- The B&R catalog mass applies to one gearbox and the BOM quantity is one.
- The row product ID and CAD geometry are more reliable identity evidence than the mismatched BOM link URL.
- The gearbox should be represented at module level only until a decomposition pass creates closure-relevant subparts.
unresolved:
- Exact B&R supplier route, material grades, bearing specifications, seals, lubricant, gear finishing process, and inspection
  tolerances are unknown.
- Future decomposition must decide which subparts are local-manufacture candidates and which remain import candidates.
- Merge review should not merge this whole module with simple brackets, housings, shafts, and generic motors before decomposition.
```
