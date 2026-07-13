---
row_identity:
  item: "41D"
  cad_file: "41D_belt_pulley_D7-575457"
  source_row_number: 259
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small flanged AT5 toothed timing-belt pulley for the reAM250 powder-inlet drivetrain, finish-bored 7 mm H7 so it can mount to a shaft and transmit synchronous belt motion without slip."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.lenze-selection.com/en-at/products/belt-drives; https://www.optibelt.com/fileadmin/pdf/produkte/scheiben/optibelt-timing-belt-pulleys.pdf"
    cited_fact_or_basis: "BOM row 259 identifies item 41D as quantity 2, CAD file 41D_belt_pulley_D7-575457, manufacturer zahriemen24.de, and description 'Toothed belt pulley 21 AT5/18-2 with 7 mm H7 bore'. The manifest maps the row to the 410_powder_inlet assembly context with cad_export_status assembly_only. Lenze describes toothed belt drives as synchronous, slip-free power transmission, and the Optibelt timing-pulley table lists the exact 21 AT5 / 18-2 pulley designation."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row belongs to the powder-inlet drivetrain because the manifest retained it in the 410_powder_inlet assembly context."
    - "The 7 mm H7 bore is interpreted as the shaft interface for one physical pulley."
  uncertainty_notes:
    - "The row-level STEP export is assembly_only, so the exact mating shaft, belt path, and installed orientation are inferred from the BOM identity and parent assembly rather than isolated part geometry."
mass:
  value_kg: 0.031
  basis: "Per-unit estimate for one pulley. The exact standard catalog line 21 AT5 / 18-2 is listed at about 0.031 kg. BOM quantity is 2, so the row total is about 0.062 kg before any small mass change from the 7 mm H7 finished bore. Parent assembly FreeCAD geometry is not used for mass because it measured the whole 410_powder_inlet assembly context: 91 solids, volume 7316733.187 mm^3, area 2248637.223 mm^2, bounding box 609.50 x 282.00 x 626.20 mm."
  source:
    url_or_path: "https://www.optibelt.com/fileadmin/pdf/produkte/scheiben/optibelt-timing-belt-pulleys.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/410_powder_inlet.step"
    cited_fact_or_basis: "Optibelt's metric timing-belt-pulley table lists 21 AT5 / 18-2 with material AL, 18 teeth, type 6F, pitch diameter 28.65 mm, outside diameter 27.40 mm, flange diameter 32 mm, F 15 mm, L 21 mm, Dm 20 mm, maximum finished bore 12 mm, and weight about 0.031 kg. FreeCAD measured only the parent assembly because the row export status is assembly_only."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The Optibelt 21 AT5 / 18-2 catalog mass is used as the closest supported per-unit mass for the same standard pulley designation."
    - "The custom 7 mm H7 bore is within the catalog's 12 mm maximum finished bore and is treated as a small machining change that does not materially change the catalog mass at this precision."
  uncertainty_notes:
    - "The exact Zahriemen24 part number 575457 was not resolved to a live row-specific datasheet, and the local CAD export does not isolate the pulley volume."
material:
  primary_material: "aluminum timing-pulley body, exact alloy not specified"
  source:
    url_or_path: "https://www.optibelt.com/fileadmin/pdf/produkte/scheiben/optibelt-timing-belt-pulleys.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Optibelt's exact 21 AT5 / 18-2 standard pulley line lists material 'AL'. The local assembly STEP material extractor matched 41D_belt_pulley_D7-575457 but returned only material Generic and density 1000.0, which the task acceptance criteria treats as placeholder rather than resolved material evidence."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The catalog abbreviation AL is interpreted as aluminum/aluminum alloy for the pulley body."
    - "The row-specific 7 mm H7 bore does not imply a different body material from the standard 21 AT5 / 18-2 pulley."
  uncertainty_notes:
    - "No source identified the exact aluminum alloy, surface treatment, or whether the supplied pulley includes any separate steel retaining hardware."
how_to_make:
  summary: "Manufacture as a standard 21 AT5/18-2 aluminum timing pulley, then finish-bore or verify the 7 mm H7 bore for the reAM250 shaft interface"
  manufacturing_steps:
    - "Start from an aluminum AT5 pulley blank or standard 21 AT5/18-2 pulley body with two flanges."
    - "Generate or finish the AT5 tooth profile and flange geometry by pulley hobbing/form cutting or equivalent CNC turning and milling operations."
    - "Finish-bore the hub to 7 mm H7 while keeping the bore concentric with the tooth pitch diameter."
    - "Deburr, clean, and inspect bore tolerance, runout, tooth profile, and belt fit before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.lenze-selection.com/en-at/products/belt-drives/toothed-belt-pulleys-and-clamping-plates-and-taper-bushes; https://www.optibelt.com/fileadmin/pdf/produkte/scheiben/optibelt-timing-belt-pulleys.pdf"
    cited_fact_or_basis: "BOM row 259 states the custom 7 mm H7 bore requirement. Lenze states that belt pulleys can be made according to drawing with special drilled holes, special tolerances, different surface treatments, different materials, and single-piece or large-series production. Optibelt gives the base 21 AT5 / 18-2 pulley geometry, aluminum material, maximum finished bore, and catalog mass. targeted_web_search: searched 'zahriemen24 21 AT5/18-2 toothed belt pulley 7 mm H7 575457', 'site:zahriemen24.de 575457', 'site:zahriemen24.de 21 AT5/18-2', and '21 AT5/18-2 7 mm H7'; found duplicate BOM text and standard pulley catalog matches, but no row-specific manufacturing drawing for the exact Zahriemen24 575457 modification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A external standard pulley plus secondary bore finishing or row-matched bore customization is the most plausible route because the BOM names a standard pulley designation plus a custom H7 bore"
  uncertainty_notes:
    - "The exact surface finish, balance grade, tooth-tolerance class, and vendor modification drawing are not present in the BOM row or resolved catalog evidence."
kb_implications:
  - "item_granularity: simple_part - standard aluminum timing pulley with row-specific finish bore; model as reusable pulley hardware rather than a calibrated purchased subsystem."
---

Research result for reAM250 BOM row 259.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0259_41D.md
source_research_sha256: ba2cd6fce4ec03f5fe71c3e0844a760cccfce4ce8f44c3281238caac8572ce27
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed function, catalog mass basis, aluminum material evidence, standard pulley manufacturing route, assembly-only
    CAD context, and KB implications before conversion.
decomposition:
  decision: simple_part
  rationale: A single standard flanged timing pulley with a finish-bored shaft interface; no motor, gearbox, bearing, and
    internal module structure is present in this row.
  proposed_subparts: []
process_abstraction:
  original_process_family: pulley_hobbing_form_cutting_and_finish_boring
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
  - stock_preparation
  - cutting
  - precision_machining
  - deburring
  - surface_finishing
  - dimensional_inspection
  - gear_tooth_machining
  - coating
  candidate_existing_processes:
  - process_id: machining_basic_v0
    fit: partial
    reason: Covers basic stock removal; row-specific precision features remain guardrails.
  - process_id: machining_precision_v0
    fit: supporting
    reason: Relevant when bore, sliding, concentricity, and finish control matter.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers dimensional checks before staging selects the final recipe.
  - process_id: gear_cutting_basic_v0
    fit: supporting
    reason: Relevant when tooth geometry controls motion transfer.
  - process_id: surface_treatment_basic_v0
    fit: supporting
    reason: Relevant when the row needs protective surface treatment.
  abstraction_decision: add_post_processing
  rationale: The row-specific function depends on accurate AT5 tooth geometry, flange geometry, concentricity, and a 7 mm
    H7 bore. General subtractive machining is the closest shared lunar bucket, with finish boring, deburring, and inspection
    retained as required post-processing. Metal additive manufacturing is not preferred for the belt tooth profile and shaft
    bore without substantial machining afterward.
  process_guardrails:
    tolerance: h7_bore_and_tooth_profile_review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: concentricity_and_runout_review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: synchronous belt motion transmission
  material: aluminum_alloy
  scale_or_capacity:
    mass_kg: 0.031
    bom_quantity: 2
    row_total_mass_kg: 0.062
    scale_class: tiny
  geometry_form: flanged_toothed_timing_pulley_with_finish_bore
merge_pool:
  eligible: true
  functional_purpose_key: synchronous_motion_transmission
  precision_guardrails:
  - tooth_pitch_profile
  - bore_tolerance_h7
  - bore_to_tooth_concentricity
  - pulley_runout
  - belt_width_and_flange_fit
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - general_subtractive_machining
  import_risk_factors:
  - AT5 tooth profile and belt-fit tolerances may require specialized cutter geometry and inspection.
  - The 7 mm H7 bore requires precision finish boring and reaming with concentricity control.
  - Exact aluminum alloy, surface treatment, balance grade, and vendor modification drawing are unresolved.
  post_merge_decision_notes: Final import/local manufacture decision is deferred until after merge review; compare with other
    pulley and drivetrain rows before deciding the condition that to stage a generic timing pulley closure item.
kb_staging:
  proposed_item_id: null
  notes: Wait for merge review across drivetrain pulley rows; preserve the precision bore and tooth-profile guardrails if
    merged.
assumptions:
- The Optibelt 21 AT5 / 18-2 catalog line is a suitable evidence proxy for mass, aluminum material, and base geometry.
- The row-specific 7 mm H7 bore is treated as secondary finishing rather than a different closure item by itself.
- General subtractive machining can represent pulley tooth generation if suitable tooling and inspection are available.
unresolved:
- Exact Zahriemen24 575457 modification drawing.
- Aluminum alloy, surface treatment, balance grade, and tooth-tolerance class.
- Whether local tooling for AT5 tooth generation should be modeled separately during KB staging.
- Mating shaft and belt path details in the powder-inlet drivetrain.
```
