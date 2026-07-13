---
row_identity:
  item: 2ADC
  cad_file: 2ADC_part_C
  source_row_number: 55
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: >
    Top bearing support/bracket for the reAM250 K+C S5/0500 glass-scale axis
    installation, providing a rigid bearing bore and bolted mounting flanges
    for locating the encoder/bearing hardware near the top of the axis.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADC_part_C.step; research/ream250_bom/ream250_bom_row_0055_2ADC__views_2x2.png; https://www.top-maschinen.de/k-c-glasmassstab-s5-500-mm-5-m-verfahrweg-520-mm-812251.html"
    cited_fact_or_basis: >
      BOM row 55 identifies item 2ADC as "axis bearing top S5/0500 K+C glass
      scale S5"; FreeCAD measured one solid with 86.00 x 37.00 x 58.00 mm
      bounding box; the rendered contact sheet shows a bracket-like body with a
      large circular bore and bolt-hole flanges; the K+C S5/0500 page identifies
      the S5/0500 as a 500 mm glass scale for linear measuring systems with
      compact construction.
    evidence_basis: independent_vendor_spec
  assumptions:
    - The CAD part is one physical bearing-support bracket represented by BOM quantity 1.
  uncertainty_notes:
    - The row does not identify the exact bearing or encoder interface carried by the bore.
mass:
  value_kg: 0.173
  basis: >
    Per-unit estimate for quantity 1. FreeCAD volume is 64019.959 mm^3
    (0.000064020 m^3). Modeled as an aluminum-family machined bracket at
    2700 kg/m^3 from kb/materials/properties.yaml: 0.000064020 m^3 * 2700
    kg/m^3 = 0.1729 kg. If the part is steel instead, the same CAD volume would
    be about 0.503 kg using the local 7850 kg/m^3 steel density.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADC_part_C.step; kb/materials/properties.yaml"
    cited_fact_or_basis: >
      FreeCAD measured CAD volume 64019.959 mm^3 and bounding box 86.00 x
      37.00 x 58.00 mm for 2ADC_part_C. Local density table gives aluminum
      density 2700 kg/m^3 and generic steel density 7850 kg/m^3. targeted_web_search:
      queries tried were "2ADC_part_C material weight", "axis bearing top
      S5/0500 material", and "K+C S5/0500 bracket material weight"; results
      found the K+C glass scale product context but no row-specific bracket mass
      or material.
    evidence_basis: engineering_hypothesis
  assumptions:
    - The CAD solid volume is a usable net-volume proxy for the physical part.
    - Aluminum-family density is used as the planning estimate for this compact machined bracket.
  uncertainty_notes:
    - Mass is material-sensitive; a steel version would be roughly three times heavier.
material:
  primary_material: unknown metal/alloy
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0055_2ADC__views_2x2.png"
    cited_fact_or_basis: >
      Local assembly STEP material extraction for product 2ADC_part_C returned
      material "Generic" with density 1000.0, which is placeholder metadata and
      does not identify a real material. The CAD preview shows a rigid bracket
      geometry with bearing bore and bolted flanges. targeted_web_search:
      queries tried were "2ADC_part_C material", "axis bearing top S5/0500
      material", and "K+C glass scale S5 bearing bracket material"; no
      row-specific material source was found.
    evidence_basis: engineering_hypothesis
  assumptions:
    - The part is treated as metallic because the geometry and function are those of a bearing/encoder support bracket.
  uncertainty_notes:
    - The exact alloy or steel/aluminum choice is unresolved and should be checked against the original CAD model or build notes before detailed manufacturing planning.
how_to_make:
  summary: >
    Manufacture as a small machined metal bracket, then install bearing or
    Encoder-interface hardware during the axis/glass-scale assembly.
  manufacturing_steps:
    - Cut rectangular metal stock to a blank slightly larger than the CAD envelope.
    - CNC mill the outer profile, mounting feet, central bearing pocket/bore, and side reliefs.
    - Drill or mill the flange mounting holes and deburr all edges.
    - Inspect bore position and mounting-hole spacing, then fasten into the glass-scale axis assembly.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADC_part_C.step; research/ream250_bom/ream250_bom_row_0055_2ADC__views_2x2.png"
    cited_fact_or_basis: >
      CAD evidence shows one compact bracket-like solid with a large circular
      Bore, stepped body, and multiple mounting holes. targeted_web_search:
      Queries tried were "axis bearing top S5/0500 manufacturing", "2ADC_part_C
      Machining", and "K+C S5/0500 bearing bracket" no source stated the
      Row-specific manufacturing route.
    evidence_basis: engineering_hypothesis
  assumptions:
    - Subtractive machining is the simplest route for the observed bore, flanges, and small-batch bracket geometry.
  uncertainty_notes:
    - Heat treatment, surface finish, and tolerance class are not specified by the BOM or STEP metadata.
kb_implications:
  - "item_granularity: simple_part - Model as a reusable machined bearing-support bracket rather than a purchased calibrated module; material/alloy can be refined later if source data appears."
---

Research result for reAM250 BOM row 55.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0055_2ADC.md
source_research_sha256: ff4297304065b1f814cab8fb049a9f1668d0120718fa50727c6bf64bd9fde96a
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed function, CAD volume mass estimate, BOM quantity, unresolved metal material evidence, machining route, KB
    implications, and CAD preview showing the bearing bore, mounting feet, and bolt-hole flanges.
decomposition:
  decision: simple_part
  rationale: The row is one compact bearing-support/encoder-interface bracket body. It is not the glass scale, bearing, and
    encoder module itself, so it should remain a simple structural/locating part for merge review.
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_machining
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
  - calibration
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
  - process_id: calibration_and_test_basic_v0
    fit: supporting
    reason: Relevant when calibration affects functional acceptance.
  abstraction_decision: add_post_processing
  rationale: The compact custom bracket can converge to the shared metal additive bucket, then use finish machining for the
    bearing bore, datum faces, and mounting-hole positions. Direct as-built use is not assumed.
  process_guardrails:
    tolerance: Bearing bore diameter, bore position, and mounting-hole spacing need precision machining and reaming after
      rough fabrication.
    surface_finish: Bore and mounting faces likely require machined finish; non-critical exterior surfaces can remain rougher.
    sealing_quality: not_applicable
    alignment_accuracy: Axis/glass-scale location depends on the bore and bolted feet maintaining alignment to the axis reference.
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: locate and support bearing and encoder hardware at the top of a linear measurement axis
  material: unknown_metal_alloy_planning_as_aluminum_family
  scale_or_capacity:
    mass_kg: 0.173
    bom_quantity: 1
    row_total_mass_kg: 0.173
    scale_class: small
  geometry_form: compact_bored_mounting_body_with_bolted_feet
merge_pool:
  eligible: true
  functional_purpose_key: axis_bearing_positioning
  precision_guardrails:
  - bearing_bore_tolerance
  - bore_to_mounting_hole_position
  - mounting_face_flatness
  - axis_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - general_metal_additive_with_finish_machining
  import_risk_factors:
  - Exact material is unresolved; steel would materially change mass and possibly stiffness assumptions.
  - Axis metrology performance may require tighter alignment than generic structural brackets.
  post_merge_decision_notes: Final import/local decision is deferred until merge review compares this with other bearing-location
    and measurement-axis support parts.
kb_staging:
  proposed_item_id: null
  notes: Leave item ID open because this may merge into a reusable bearing-location support item after material and precision
    guardrails are reviewed.
assumptions:
- The CAD solid represents one physical bracket and BOM quantity is one.
- Aluminum-family density is kept as the planning mass basis while material remains unresolved.
- A lunarized additive route would still machine the bore, mounting faces, and critical holes.
unresolved:
- Exact metal and alloy is unknown; source evidence did not resolve aluminum versus steel.
- Required bore tolerance, datum scheme, and surface finish are not stated.
- Merge review must decide the condition that this can share a closure item with other axis bearing supports and requires
  a metrology-specific support item.
```
