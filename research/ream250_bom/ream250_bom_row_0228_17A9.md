---
row_identity:
  item: "17A9"
  cad_file: "17A9_strut_profile_20X20_343"
  source_row_number: 228
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Short Bosch Rexroth 20 x 20 mm slotted aluminum strut profile used as a light structural frame member, rail, support, or fixture element in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A9_strut_profile_20X20_343.step; https://docs.rs-online.com/ea04/A700000007302204.pdf"
    cited_fact_or_basis: "BOM row 228 identifies item 17A9 as Bosch Rexroth AG strut profile. FreeCAD measured one solid with 358.00 x 20.00 x 20.00 mm bounding box, and the rendered contact sheet shows a straight four-slot extrusion. The Bosch Rexroth 20x20 data sheet describes 6 mm-slot strut profiles for light structures such as supports and lab fixtures. bom_url_route_check: the BOM-provided Bosch store family URL was checked as the row route but did not expose a row-specific part number or data table in the accessible source; the row-matched Bosch Rexroth PDF hosted by RS was used for the profile-family function details."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD filename's 20X20 marker and measured 20 x 20 mm section are sufficient to map this row to the Bosch Rexroth 20x20 slot-6 strut profile family."
  uncertainty_notes:
    - "The BOM row does not include the Bosch Rexroth ordering number, so the function is resolved at the 20x20 strut-profile family level rather than a unique catalog SKU."
mass:
  value_kg: 0.161
  basis: "Per unit for quantity 1. FreeCAD measured CAD volume 59721.783 mm^3, equivalent to 0.0000597218 m^3. Using the local aluminum density constant 2700 kg/m^3 gives 0.161 kg. Catalog lineal mass for the matching 20x20 profile family is 0.4 kg/m; scaled by the measured 0.358 m CAD length, that gives about 0.143 kg, a same-order check on the CAD-derived estimate."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A9_strut_profile_20X20_343.step; kb/materials/properties.yaml; https://docs.rs-online.com/ea04/A700000007302204.pdf"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 59721.783 mm^3, surface area 64838.517 mm^2, and bounding box 358.00 x 20.00 x 20.00 mm. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3. The Bosch Rexroth 20x20 data sheet lists mass m as 0.4 kg/m. bom_url_route_check: the BOM-provided Bosch store family URL was checked first but did not resolve row-specific mass in accessible text; the row-matched Bosch Rexroth PDF hosted by RS supplied the profile-family lineal mass check."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD solid volume represents one physical strut profile in the BOM row."
    - "The aluminum density constant is appropriate for the anodized aluminum extrusion family."
  uncertainty_notes:
    - "The CAD-volume calculation gives about 0.161 kg, while catalog rounded lineal mass scaled to CAD length gives about 0.143 kg; use about 0.15-0.16 kg for planning unless a Rexroth cut-list mass for this exact length is recovered."
material:
  primary_material: "anodized aluminum extrusion; Rexroth strut-profile technical data indicates EN AW-6060 / AW-6063-T66 aluminum-magnesium-silicon alloy family for strut profiles"
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Bosch Rexroth 20x20 data sheet lists material as anodized aluminum for the relevant 20x20 strut profile numbers. Bosch Rexroth technical data for strut profiles gives material designation EN AW-Al MgSi / EN AW-6060 with AW-6063-T66 noted. Local assembly STEP material extraction for this row returned only Generic with density 1000.0, which was treated as non-resolving placeholder metadata. bom_url_route_check: the BOM-provided Bosch store family URL was checked first but did not expose a row-specific material table in accessible text; Bosch Rexroth profile data sheets were used for the material."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's Bosch Rexroth 20x20 strut profile uses the standard Rexroth aluminum strut-profile material family."
  uncertainty_notes:
    - "The exact alloy temper for this cut piece is resolved from Rexroth strut-profile family data, not a material attribute embedded in the row STEP file."
how_to_make:
  summary: "Prepare as Bosch Rexroth 20x20 slot-6 anodized aluminum profile cut to the required length, or locally make by extruding an aluminum profile with the 20x20 slot geometry, solution heat treating/aging as required for the alloy, cutting to length, deburring, and anodizing"
  manufacturing_steps:
    - "Extrude EN AW-6060/AW-6063-family aluminum billet through a 20x20 slot-6 profile die."
    - "Heat treat/age to the required strut-profile temper and straighten to extrusion tolerances."
    - "Cut the extrusion to the row length indicated by the CAD model, then deburr the cut ends."
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A9_strut_profile_20X20_343.step"
    cited_fact_or_basis: "The Bosch Rexroth 20x20 data sheet identifies the row family as an anodized aluminum 20x20 strut profile with 6 mm slot and lists ordering lengths up to 3000 mm. The Rexroth technical data identifies the aluminum strut-profile material family and anodizing process parameters. FreeCAD measured the row geometry as a short 358.00 mm long 20 x 20 mm slotted extrusion. bom_url_route_check: the BOM-provided Bosch store family URL was checked first but did not provide an accessible row-specific manufacturing route; Bosch Rexroth profile data sheets and CAD geometry supplied the procurement and geometry facts."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed local manufacturing operations are inferred from the geometry and standard aluminum-extrusion practice; the cited sources identify the product and material but do not provide a complete process plan."
  uncertainty_notes:
    - "Targeted_web_search: queries tried: 'Bosch Rexroth 3842517179 20x20 profile manufacturing anodized aluminum', 'Bosch Rexroth strut profile 20x20 material AW-6060', and 'Bosch Rexroth 20x20 slot 6 mass 0.4 kg/m'. Results resolved product/material data but not a row-specific Manufacturing route."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut length of 20x20 anodized aluminum strut profile rather than a machine-specific assembly or purchased module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0228_17A9.md
source_research_sha256: "aac8775b0968b9537922066e71eca26027a0998bc678f86156a40c586e2c6d75"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the 20 x 20 mm four-slot profile geometry, 358 mm cut length, CAD-volume and catalog lineal-mass estimates, Rexroth aluminum strut-profile material evidence, and extrusion/cut-to-length manufacturing route."
decomposition:
  decision: simple_part
  rationale: "The row is one cut length of modular slotted structural profile. It is not a purchased electronics module, actuator, fastener kit, nor a hidden assembly requiring internal decomposition."
  proposed_subparts: []
process_abstraction:
  original_process_family: aluminum_profile_extrusion_cut_to_length_anodized
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - stock_preparation
    - extrusion
    - heat_treatment
    - cutting
    - deburring
    - coating
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_extrusion_process_v0
      fit: partial
      reason: "Covers aluminum extrusion energy and stock conversion, but its current output is heat-sink fin extrusion rather than a 20 x 20 slotted structural profile."
    - process_id: aluminum_tube_stock_extrusion_v0
      fit: partial
      reason: "Covers aluminum alloy extrusion from ingot into reusable stock; tube geometry differs from the slot-6 profile needed here."
    - process_id: metal_cutting_basic_v0
      fit: direct
      reason: "Covers sawing/cutting stock material to length, matching the row-specific cut from longer strut stock to 358 mm."
    - process_id: surface_treatment_anodizing_v0
      fit: supporting
      reason: "Relevant to the anodized aluminum finish called out by Rexroth profile-family evidence, though the existing process is written around heat-sink parts."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks for cut length, section size, slot geometry, and fit before frame assembly."
  abstraction_decision: keep_original_family
  rationale: "The source route already describes aluminum profile extrusion, temper/straightening, cutting to length, deburring, and anodizing, which is exactly the structural profile stock fabrication/cutting closure bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: light structural frame member rail support fixture element
  material: anodized_aluminum_6060_6063_family
  scale_or_capacity:
    mass_kg: 0.161
    bom_quantity: 1
    row_total_mass_kg: 0.161
    scale_class: small
  geometry_form: straight_20x20_four_slot_extrusion_cut_length
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - cut_length
    - slot_geometry
    - straightness
    - frame_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Local manufacture needs an extrusion die/tooling strategy for the 20 x 20 slot geometry."
    - "Anodized finish may need a surface-treatment route if corrosion, wear, electrical isolation, and assembly sliding behavior matter."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred until structural-profile rows are merge-reviewed and a shared profile-stock strategy is selected."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with other cut lengths of 20 x 20 slotted structural profile before assigning a closure item ID."
assumptions:
  - "Quantity 1 and row total mass 0.161 kg use the CAD-volume aluminum estimate from the original research."
  - "The Rexroth family material is normalized to an anodized aluminum 6060/6063-family structural extrusion for later staging."
  - "Different cut lengths of the same 20 x 20 slot profile are likely merge candidates if length differences are closure-insignificant."
unresolved:
  - "Exact Bosch Rexroth ordering number for this cut piece is not present in the row evidence."
  - "Exact alloy temper, anodizing specification, and cut-length tolerance remain inferred from profile-family data."
  - "Merge review should decide whether all 20 x 20 slot-6 strut lengths can share one closure item with length handled as a BOM quantity/note."
```
