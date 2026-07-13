---
row_identity:
  item: "92"
  cad_file: "92_profile_60x60_2120"
  source_row_number: 295
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Structural aluminum strut profile used as a long 60 x 60 mm frame member in the reAM250 machine structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/92_profile_60x60_2120.step; https://www.boschrexroth.com/en/us/products/industrial-solutions/assembly-technology/aluminum-profile-kit/"
    cited_fact_or_basis: "BOM row 295 names item 92 as 'strut profile' from Bosch Rexroth AG; FreeCAD measured one solid with bounding box 2120.00 x 60.00 x 60.00 mm; CAD preview shows a long straight square profile; Bosch Rexroth describes its aluminum profile system for machine frames, workstations, enclosures, shelves, and safety fences."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single exported STEP body represents one physical profile cut to the row length."
  uncertainty_notes: []
mass:
  value_kg: 8.276
  basis: "Per-unit mass for quantity 1. FreeCAD volume is 3065006.499 mm^3 = 0.003065006499 m^3. Assembly STEP material metadata gives Aluminum with density 2700 kg/m^3, matching kb/materials/properties.yaml aluminum density. Calculation: 0.003065006499 m^3 * 2700 kg/m^3 = 8.2755 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/92_profile_60x60_2120.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured STEP volume 3065006.499 mm^3 and bounding box 2120.00 x 60.00 x 60.00 mm; local STEP material extractor matched product 92_profile_60x60_2120 to material Aluminum with density 2700.0; local material table lists aluminum density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume is the net aluminum volume of the profile, including hollow/slot geometry."
  uncertainty_notes:
    - "Mass depends on CAD export fidelity for the internal profile cross-section; if the supplier profile variant differs from the STEP, use the supplier kg/m value instead."
material:
  primary_material: "Aluminum strut-profile alloy family; Rexroth technical data for strut profiles lists EN AW-6060 / AW-6063-T66 family."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "Local STEP material metadata for 92_profile_60x60_2120 states Aluminum and density 2700.0. Bosch Rexroth technical data for strut profiles lists EN AW-AlMgSi, AW-6063-T66, and material designation EN AW-6060 / AW-6063-T66 for Rexroth strut profiles. bom_url_route_check: BOM Link URL is the Bosch Rexroth strut-profile shop route; the accessible Bosch Rexroth framing page confirmed the same product family but did not expose the alloy table, so the Bosch Rexroth technical-data PDF mirrored on Airline Hydraulics was used for the alloy-family table."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's Bosch Rexroth strut profile uses the standard Rexroth strut-profile alloy family rather than a special nonstandard alloy."
  uncertainty_notes:
    - "The BOM row and local STEP metadata do not state the exact Rexroth material number or surface treatment for this cut length."
how_to_make:
  summary: "Prepare a Bosch Rexroth aluminum strut profile or locally reproduce it by extruding the matching 60 x 60 mm profile from aluminum alloy, anodizing if required, cutting to 2120 mm, and deburring the cut ends"
  manufacturing_steps:
    - "Source or cast suitable aluminum extrusion billet."
    - "Extrude through a die matching the Bosch Rexroth 60 x 60 mm T-slot/profile cross-section."
    - "Straighten, age/heat treat to the target 6060/6063-T66 family properties, and anodize if the machine requires the commercial finish."
    - "Cut the profile to the CAD/BOM length of 2120 mm and deburr or machine the ends for assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/92_profile_60x60_2120.step; https://www.boschrexroth.com/en/us/products/industrial-solutions/assembly-technology/aluminum-profile-kit/; https://airlinemedia.airlinehyd.com/Literature/Manufacturer_Catalogs/Bosch%20Rexroth/AluminumFraming_Sec19_Tech_Data.pdf"
    cited_fact_or_basis: "BOM/CAD identify a 2120 mm long Bosch Rexroth strut profile; Bosch Rexroth describes the profile system as modular aluminum framing with catalog material numbers and dimensional drawings; Rexroth technical data states the profile alloy family and anodizing process data. targeted_web_search: searched 'Bosch Rexroth strut profile 60x60 material manufacturing extrusion anodized' and 'Bosch Rexroth 60x60 strut profile weight kg/m 8mm slot'; results supported aluminum strut-profile use and material data but did not provide a row-specific manufacturing route for this exact cut length."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Use standard aluminum profile extrusion practice because the part is a constant cross-section profile."
  uncertainty_notes:
    - "The exact Rexroth cross-section variant and any end-machining operations are not specified in the BOM row."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut-to-length aluminum strut profile rather than a machine-specific assembly."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0295_92.md
source_research_sha256: 0d6e96e008b3d49486e7543e53c430afc04fe68ba54982e46aac955cfabd2176
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed the original function, assumptions, CAD-derived mass basis, BOM quantity, material evidence, manufacturing
    route, KB implications, and CAD preview before conversion.
decomposition:
  decision: simple_part
  rationale: The row is one cut-to-length aluminum structural strut profile, not a complex assembly and vendor module requiring
    decomposition.
  proposed_subparts: []
process_abstraction:
  original_process_family: aluminum_profile_extrusion_cut_to_length
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
  - stock_preparation
  - extrusion
  - cutting
  - deburring
  - dimensional_inspection
  - coating
  candidate_existing_processes:
  - process_id: metal_extrusion_process_v0
    fit: partial
    reason: Covers profile stock creation when extrusion is the selected local route.
  - process_id: extrusion_basic_v0
    fit: partial
    reason: Covers generic extrusion abstraction for profile stock.
  - process_id: cutting_basic_v0
    fit: supporting
    reason: Covers cutting profile stock to length.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers dimensional checks before staging selects the final recipe.
  - process_id: surface_treatment_basic_v0
    fit: supporting
    reason: Relevant when the row needs protective surface treatment.
  abstraction_decision: keep_original_family
  rationale: 'The source route is already a structural-profile stock route: make and source a constant-section aluminum profile,
    finish as needed, cut to length, and deburr. Additive manufacturing would add unnecessary process complexity for a long
    constant-section member.'
  process_guardrails:
    tolerance: review
    surface_finish: deburred_cut_ends_and_optional_anodized_surface
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: long structural frame strut for machine structure
  material: aluminum_strut_profile_alloy_family
  scale_or_capacity:
    mass_kg: 8.276
    bom_quantity: 1
    row_total_mass_kg: 8.276
    scale_class: medium
  geometry_form: long_square_modular_strut_profile_cut_to_length
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_support_member
  precision_guardrails:
  - straightness
  - end_cut_squareness
  - alignment_accuracy
  - modular_slot_interface_geometry
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - structural_profile_stock_fabrication_cutting
  import_risk_factors:
  - Local closure may require a reusable extrusion/profile-forming route and acceptance of a simpler structural profile geometry.
  - Commercial anodized finish and exact Rexroth slot geometry may be unnecessary unless merge review preserves those interface
    requirements.
  post_merge_decision_notes: Final import/local manufacture decision is deferred until after merge review; compare against
    other frame struts and decide the condition that exact modular slot geometry is closure-relevant.
kb_staging:
  proposed_item_id: null
  notes: Wait for merge review before final item ID; likely reusable as a generic aluminum structural profile if slot geometry
    and alignment requirements converge.
assumptions:
- The exact Rexroth profile variant can be represented at aluminum strut-profile alloy family precision unless later review
  finds a unique interface requirement.
- A lunarized structural profile may substitute simpler local profile geometry if frame alignment and fastening interfaces
  remain compatible.
unresolved:
- Exact Rexroth cross-section variant, surface treatment, and any end-machining operations are not specified in the row evidence.
```
