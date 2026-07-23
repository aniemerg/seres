---
row_identity:
  item: "9B"
  cad_file: "9B_profile_60x60_960"
  source_row_number: 213
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Bosch Rexroth 60 x 60 mm aluminum strut profile cut to 960 mm, used as a modular machine-frame member in the reAM250 structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.boschrexroth.com/de/at/produkte/industrielle-loesungen/montagetechnik/aluminiumprofil-baukasten/"
    cited_fact_or_basis: "The BOM row and manifest identify item 9B as quantity 1, cad_file 9B_profile_60x60_960, description strut profile, manufacturer Bosch Rexroth AG. The Bosch Rexroth aluminum-profile page says system profiles are used to realize machine frames, ergonomic workplaces, shelves, or protective fences, and highlights standardized components, connection technology, and high-force-absorbing profiles."
    evidence_basis: "bom_provided"
  assumptions:
    - "The filename suffix 60x60_960 is interpreted as a 60 mm square profile cut to a 960 mm length, consistent with the CAD bounding box."
  uncertainty_notes: []
mass:
  value_kg: 3.747
  basis: "FreeCAD measured CAD volume 1387927.471 mm^3 for one 960 mm profile. Using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives 3.7474 kg per strut. As a cross-check, the Bosch Rexroth catalog lists the 60x60 strut profile mass as 3.9 kg/m, giving 3.744 kg for 0.960 m."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9B_profile_60x60_960.step; kb/materials/properties.yaml; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec2_Profiles.pdf"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1387927.471 mm^3, area 868403.520 mm^2, and bounding box 960.00 x 60.00 x 60.00 mm. The local material density table lists aluminum density 2700 kg/m^3. The Bosch Rexroth Aluminum Framing 8.0 catalog table lists 60x60 profile area 14.4 cm2 and mass 3.9 kg/m. bom_url_route_check: the BOM-provided Bosch Rexroth store URL was checked first; it identifies the strut-profile product family but did not expose row-specific 60x60 mass in the accessible page, so the Bosch Rexroth catalog PDF mirror was used for catalog mass cross-check."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The STEP solid volume is treated as the physical metal volume for one cut profile."
    - "The local aluminum density is used as the calculation constant for the aluminum extrusion."
  uncertainty_notes:
    - "The assembly STEP material extractor returned only Generic/Generisch at density 1000.0, so the mass relies on CAD volume plus catalog aluminum-profile identity rather than local STEP material metadata."
material:
  primary_material: "anodized aluminum strut-profile alloy family; Rexroth technical data lists EN AW AlMgSi / EN AW-6060 with AW-6063-T66 designation for strut profiles"
  source:
    url_or_path: "https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf; https://www.boschrexroth.com/de/at/produkte/industrielle-loesungen/montagetechnik/aluminiumprofil-baukasten/"
    cited_fact_or_basis: "Bosch Rexroth technical data for strut profiles lists EN AW-AlMgSi, EN AW-6060, and AW-6063-T66 designations, and an anodizing layer/process entry. The Bosch Rexroth aluminum-profile page identifies the product family as aluminum profiles. official_alternate_route_check: the original BOM URL is the Bosch Rexroth store strut-profile family route; the alternate Bosch Rexroth product-family page and Bosch Rexroth catalog technical-data page match the same manufacturer and strut-profile product family, while the catalog mirror preserves Bosch Rexroth document title and content for the material-grade details."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row's Bosch Rexroth strut profile follows the Rexroth strut-profile material family stated in the technical-data catalog."
  uncertainty_notes:
    - "The leased row does not include a Bosch material number, so the exact machining option or finish variant is not locked beyond the 60x60 aluminum strut-profile family."
how_to_make:
  summary: "Manufacture as a standard aluminum T-slot/strut extrusion: cast; for near-term KB modeling, treat it as reusable aluminum structural-profile stock cut to length"
  manufacturing_steps:
    - "Prepare aluminum alloy billet compatible with EN AW-6060/AW-6063-series profile extrusion."
    - "Hot-extrude through a 60x60 strut-profile die to form the slotted hollow cross-section visible in the CAD preview."
    - "Quench, stretch/straighten, and age to the required temper for structural profile service."
    - "Anodize the profile surface, then saw cut to the 960 mm BOM length and deburr the ends."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0213_9B__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/9B_profile_60x60_960.step; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "The rendered contact sheet shows a long constant-section slotted structural profile. FreeCAD measured a 960.00 x 60.00 x 60.00 mm bounding box. Bosch Rexroth technical data identifies the material family and anodizing information for strut profiles. targeted_web_search: searched \"Bosch Rexroth strut profile 60x60 aluminum material mass kg/m\", \"site:boschrexroth.com strut profile 60x60 960 aluminum Bosch Rexroth\", and \"Bosch Rexroth Strebenprofil 60x60 material gewicht kg/m\" found row-family catalog material and mass data but no source stating the actual factory process for this specific cut row."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A constant 60x60 slotted aluminum profile is produced by extrusion rather than subtractive machining from solid stock."
    - "Cut-to-length and deburring are sufficient post-processing for the BOM row unless later assembly evidence requires drilled or tapped end features."
  uncertainty_notes:
    - "The cited Bosch evidence resolves the profile family, material, and anodizing context, but not the complete vendor production routing for this exact 960 mm cut part."
kb_implications:
  - "item_granularity: simple_part - model as an aluminum structural profile cut to length, preferably reusing a generic 60x60 aluminum extrusion/strut profile item rather than creating a machine-specific frame member."
---

# reAM250 BOM Row 213 - 9B

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0213_9B.md
source_research_sha256: "09e331ba732a084676b354ff35055ad1271473c4571a898570ca653ad05998d9"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the structural-frame function, CAD and catalog mass cross-check, aluminum extrusion material evidence, manufacturing route, and constant-section CAD geometry before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one cut length of aluminum strut profile; connectors, end fasteners, panels, and attached frame hardware belong to other BOM rows."
  proposed_subparts: []
process_abstraction:
  original_process_family: aluminum_profile_extrusion_cut_to_length
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - stock_preparation
    - extrusion
    - cutting
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_extrusion_process_v0
      fit: partial
      reason: "Provides an aluminum extrusion anchor, though its current template is heat-sink oriented and would need binding to structural strut profile output."
    - process_id: metal_cutting_basic_v0
      fit: direct
      reason: "Covers sawing stock to the 960 mm row length and preparing cut ends."
    - process_id: surface_treatment_anodizing_v0
      fit: supporting
      reason: "Covers anodized aluminum surface treatment when the closure item preserves catalog-like profile finish."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers length, straightness, end squareness, and profile damage checks."
  abstraction_decision: keep_original_family
  rationale: "The original evidence already indicates an aluminum structural extrusion cut to length, which matches the selected structural profile stock fabrication and cutting bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: modular structural frame member for machine structure
  material: aluminum_alloy
  scale_or_capacity:
    mass_kg: 3.747
    bom_quantity: 1
    row_total_mass_kg: 3.747
    scale_class: medium
  geometry_form: slotted_square_structural_profile_60x60_cut_to_960mm
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - length
    - straightness
    - end_squareness
    - slot_interface_compatibility
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Exact Bosch Rexroth slot geometry and anodized finish may matter if reused with catalog connector hardware."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review; this row is a strong candidate for merging into a generic aluminum structural profile closure item."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with other 60 mm class aluminum frame profiles and cut lengths before assigning a closure item ID."
assumptions:
  - "The 60 x 60 x 960 mm filename and CAD envelope identify the profile size and cut length."
  - "The profile can be treated as reusable structural stock rather than a machine-specific part."
  - "Cut ends do not contain row-specific drilled, tapped, keyed, nor precision-milled features unless later assembly evidence shows them."
unresolved:
  - "Exact Rexroth material number and finish variant are not available in the leased row."
  - "Any connector-specific slot compatibility requirements need group-level review with related frame hardware rows."
```
