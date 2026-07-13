---
row_identity:
  item: "17AD"
  cad_file: "17AD_strut_profile_20X20_110"
  source_row_number: 232
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Short Bosch Rexroth 20 x 20 mm slotted aluminum strut profile used as a modular framing member, spacer, or light structural rail in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AD_strut_profile_20X20_110.step; research/ream250_bom/ream250_bom_row_0232_17AD__views_2x2.png; https://www.boschrexroth.com/en/us/products/industrial-solutions/assembly-technology/aluminum-profile-kit/"
    cited_fact_or_basis: "BOM row 232 names item 17AD as a Bosch Rexroth AG 'strut profile' with quantity 2. The manifest maps the row to 17AD_strut_profile_20X20_110.step. FreeCAD measured one solid with a 110.00 x 20.00 x 20.00 mm bounding box, and the rendered contact sheet shows a constant square slotted extrusion. Bosch Rexroth describes its aluminum profile system as modular structural framing for protective devices, workstations, flow racks, and related frame applications."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file is the physical item represented by this BOM row."
  uncertainty_notes:
    - "The BOM row does not identify the exact reAM250 subassembly location, so the function is resolved at the reusable profile-member level rather than a specific bracket/span role."
mass:
  value_kg: 0.0492
  basis: "Per-unit mass for one 17AD profile segment; BOM quantity is 2, so the row total is about 0.0984 kg. FreeCAD volume is 18218.096 mm^3, or 1.8218096e-5 m^3. Using the local aluminum density constant of 2700 kg/m^3 gives 0.0492 kg per segment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AD_strut_profile_20X20_110.step; kb/materials/properties.yaml; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 18218.096 mm^3 and bounding box 110.00 x 20.00 x 20.00 mm. kb/materials/properties.yaml lists aluminum density 2700 kg/m^3. Bosch Rexroth technical data for strut profiles gives aluminum alloy family/designation data for Rexroth strut profiles, supporting aluminum density use for this row. official_alternate_route_check: original BOM URL is the Bosch Rexroth store strut-profile family route; the mirrored Bosch Rexroth Aluminum Framing technical-data PDF carries Bosch Rexroth AG catalog identity R999001283 and matches the same manufacturer and strut-profile product family when the public store route does not expose row-level material data."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume is the finished profile volume for one cut segment and excludes no hidden inserts."
    - "The Bosch Rexroth strut-profile material family is treated as aluminum for density calculation."
  uncertainty_notes:
    - "The assembly STEP material extractor returned only placeholder Generic material at 1000 kg/m^3 for this row, so mass depends on the official Rexroth profile-family material rather than row-specific STEP material metadata."
material:
  primary_material: "Bosch Rexroth aluminum strut-profile alloy family, EN AW Al MgSi / EN AW-6060 with AW-6063-T66 family properties; anodized profile finish"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "BOM row 232 identifies a Bosch Rexroth AG strut profile and provides the Bosch Rexroth strut-profile shop route. Bosch Rexroth technical data for strut profiles states EN AW Al MgSi, AW-6063-T66, material designation EN AW-6060, and anodizing process data. official_alternate_route_check: original BOM URL is the Bosch Rexroth store strut-profile family route; the Bosch Rexroth aluminum-profile/catalog route and the Bosch Rexroth technical-data PDF are official same-manufacturer profile-family sources matching the BOM manufacturer, product family, and 20 x 20 slotted profile geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row uses the standard Bosch Rexroth strut-profile material family because the BOM names only a Bosch Rexroth strut profile and does not provide a separate custom material."
  uncertainty_notes:
    - "The exact Rexroth material number and any order-specific finish variant are not present in the BOM row, so the material is stated at profile-family precision rather than as a unique part-number grade."
how_to_make:
  summary: "Prepare as a Bosch Rexroth cut-to-length 20 x 20 aluminum strut profile, or locally reproduce by extruding the matching slotted aluminum profile, cutting to 110 mm, deburring the ends, and applying an anodized or equivalent protective finish"
  manufacturing_steps:
    - "Extrude an aluminum Al-Mg-Si structural profile through a die matching the 20 x 20 mm slotted cross-section."
    - "Cut the extrusion to the 110 mm row length shown by the STEP bounding box."
    - "Deburr and inspect the cut ends and slot geometry for connector fit."
    - "Anodize or apply an equivalent protective finish if matching the Bosch Rexroth profile family."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AD_strut_profile_20X20_110.step; research/ream250_bom/ream250_bom_row_0232_17AD__views_2x2.png; https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "BOM row evidence identifies a Bosch Rexroth strut profile, CAD preview shows a constant 20 x 20 mm slotted extrusion, and Bosch Rexroth technical data states the aluminum strut-profile material family and anodizing data. targeted_web_search: tried 'Bosch Rexroth strut profile 20x20 material aluminum mass kg m', 'site:boschrexroth.com strut profile 20x20 Bosch Rexroth material', and 'Bosch Rexroth Strebenprofil 20x20 Material'; results matched Bosch Rexroth profile-family and catalog/distributor pages, but did not provide a row-specific local manufacturing process for this cut segment."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Aluminum extrusion plus cut-to-length finishing is the plausible Manufacturing route for a constant-section slotted structural profile."
  uncertainty_notes:
    - "The CAD and profile-family evidence do not specify die details, temper control, anodizing thickness, cut tolerance, or any end-machining requirements for this row."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut aluminum T-slot/strut extrusion segment, parameterized by profile size and length rather than as a purchased module."
---

Result generated for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0232_17AD.md
source_research_sha256: "b1b236a9f60b11e63b9c211830f00a211eda988b7ef73514c7ffe886d42a2fdf"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the modular strut function, CAD-derived mass basis, Bosch Rexroth aluminum profile-family material evidence, extrusion/cut-to-length route, and preview showing a constant 20 x 20 mm slotted profile."
decomposition:
  decision: simple_part
  rationale: "The row is a cut length of slotted aluminum structural profile; hidden inserts and fasteners are not part of this BOM row."
  proposed_subparts: []
process_abstraction:
  original_process_family: aluminum_profile_extrusion_cut_to_length
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - extrusion
    - cutting
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_extrusion_process_v0
      fit: partial
      reason: "Covers aluminum extrusion from ingot, but is currently heat-sink-fin-specific rather than generic slotted structural profile production."
    - process_id: extrusion_basic_v0
      fit: poor_fit
      reason: "General extrusion template exists, but its inputs and outputs are polymer-focused and need adaptation for aluminum profiles."
    - process_id: metal_cutting_basic_v0
      fit: direct
      reason: "Matches cut-to-length preparation of the extruded profile segment."
    - process_id: surface_treatment_anodizing_v0
      fit: supporting
      reason: "Relevant to the anodized finish stated by Bosch Rexroth profile-family evidence, though the process is currently heat-sink-oriented."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers length, slot geometry, and connector-fit checks before frame assembly."
  abstraction_decision: keep_original_family
  rationale: "The original evidence already indicates aluminum extrusion followed by cut-to-length finishing, which maps directly to the structural-profile stock fabrication bucket."
  process_guardrails:
    tolerance: standard
    surface_finish: anodized_equivalent
    sealing_quality: not_applicable
    alignment_accuracy: standard
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: modular slotted framing member for light structural support and spacing
  material: aluminum_6060_6063_profile_family
  scale_or_capacity:
    mass_kg: 0.0492
    bom_quantity: 2
    row_total_mass_kg: 0.0984
    scale_class: small
  geometry_form: cut_length_20x20_slotted_square_extrusion
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - profile_slot_geometry
    - cut_length
    - connector_fit
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Extrusion die for the slotted profile is a nontrivial reusable tooling dependency."
    - "Anodized finish may be substituted with another protective finish if connector fit remains acceptable."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this with other slotted framing profile rows."
kb_staging:
  proposed_item_id: null
  notes: "Hold final item identity for merge review across aluminum structural profile segments; length and 20 x 20 profile size are guardrails."
assumptions:
  - "The row uses standard aluminum profile-family material and finish rather than a custom alloy."
  - "BOM quantity 2 represents duplicate cut segments at 0.0492 kg each."
unresolved:
  - "Exact Rexroth part number, finish thickness, cut tolerance, and end-machining requirements are not specified."
  - "Whether local closure should model the extrusion die explicitly is deferred to later staging."
```
