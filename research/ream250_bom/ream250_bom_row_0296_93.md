---
row_identity:
  item: "93"
  cad_file: "93_profile_60x60_710"
  source_row_number: 296
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Bosch Rexroth 60 x 60 mm modular aluminum strut profile used as a structural frame member in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/93_profile_60x60_710.step; research/ream250_bom/ream250_bom_row_0296_93__views_2x2.png"
    cited_fact_or_basis: "BOM row 296 lists item 93, quantity 1, CAD file 93_profile_60x60_710, description 'strut profile', manufacturer Bosch Rexroth AG, and the Bosch Rexroth Strebenprofil link URL. The manifest maps the same item to gold_export/parts/93_profile_60x60_710.step with status matched_existing. FreeCAD measured one solid with a 650.00 x 60.00 x 60.00 mm bounding box; the rendered preview shows a long slotted square profile."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row's 'strut profile' description and 60 x 60 mm slotted CAD geometry are interpreted as a structural framing extrusion rather than a machined custom bar."
  uncertainty_notes:
    - "The CAD filename includes 710, but the STEP bounding box is 650.00 mm long; downstream modeling should preserve the row identity while using the measured STEP length unless the source CAD export is later corrected."
mass:
  value_kg: 2.537
  basis: "FreeCAD volume 939742.559 mm^3 = 9.39742559e-4 m^3. Using the BOM-provided/local STEP aluminum density of 2700 kg/m^3 gives 2.537 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/93_profile_60x60_710.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured CAD volume 939742.559 mm^3 and a 650.00 x 60.00 x 60.00 mm bounding box. Local assembly STEP material extraction for 93_profile_60x60_710 returned material Aluminum with density 2700.0. The local density table lists aluminum at 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the aluminum material volume for this profile."
  uncertainty_notes:
    - "The mass follows the 650 mm STEP geometry. If the intended row length is actually 710 mm at the same cross-section, the mass would scale to about 2.77 kg."
material:
  primary_material: "aluminum"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "Local assembly STEP material extraction for 93_profile_60x60_710 returned material Aluminum with density 2700.0. The local density table lists aluminum at 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Model as a cut length of standard aluminum structural profile: extrude the 60 x 60 slotted cross-section, cut to the required length, deburr the ends, and optionally anodize or otherwise finish for assembly use."
  manufacturing_steps:
    - "Extrude aluminum through a die that forms the 60 x 60 mm slotted profile cross-section."
    - "Cut the extrusion to the required frame-member length."
    - "Deburr and square the cut ends; add any connector holes or end machining only if required by the local frame joint."
    - "Apply the selected surface finish and inspect slot fit, straightness, and cut length before assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/93_profile_60x60_710.step; research/ream250_bom/ream250_bom_row_0296_93__views_2x2.png; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid with a 650.00 x 60.00 x 60.00 mm bounding box; the preview shows a constant slotted profile cross-section along its length. targeted_web_search: searched \"Bosch Rexroth strut profile 60x60 material aluminum extruded\" and \"Bosch Rexroth Strebenprofil 60x60 aluminum profile\" found Bosch Rexroth aluminum profile system pages and distributor listings for 60x60 Bosch Rexroth aluminum extrusion, but no row-specific manufacturing drawing for item 93."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A constant-section aluminum strut profile is treated as an extrusion cut to length, which is the standard manufacturing route for this class of modular framing member."
  uncertainty_notes:
    - "The STEP preview does not specify alloy temper, anodizing, slot tolerance, or the final intended cut length discrepancy between the filename and measured CAD geometry."
kb_implications:
  - "item_granularity: simple_part - standard cut-to-length structural aluminum profile stock; model as reusable framing stock or a simple profile part rather than a custom assembly."
---

Research result for reAM250 BOM row 296.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0296_93.md
source_research_sha256: f34a3fdf1cad1c07c437a509417b16dc9bcf9024eb4bae058ac25f6e7e71069c
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Read the original function, mass basis, material evidence, manufacturing route, KB implications, and CAD preview
    showing a constant-section 60 x 60 mm slotted profile before conversion.
decomposition:
  decision: simple_part
  rationale: This is a single cut length of modular aluminum strut/profile stock, not a vendor module and assembly with hidden
    internal closure dependencies.
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
  rationale: 'The source route already belongs to the shared structural profile bucket: make compatible aluminum profile stock,
    cut to length, deburr, finish, and inspect. Additive manufacturing is less suitable for long straight slot geometry.'
  process_guardrails:
    tolerance: review slot fit, profile straightness, and cut length
    surface_finish: review anodized and equivalent protective finish if connector sliding/contact surfaces require it
    sealing_quality: not_applicable
    alignment_accuracy: review end squareness and frame connector alignment
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: modular structural support member for the machine frame
  material: aluminum_alloy_strut_profile
  scale_or_capacity:
    mass_kg: 2.537
    bom_quantity: 1
    row_total_mass_kg: 2.537
    scale_class: medium
  geometry_form: square_slotted_t_slot_extrusion_60x60_cut_length
merge_pool:
  eligible: true
  functional_purpose_key: modular_machine_frame_member
  precision_guardrails:
  - slot_geometry
  - profile_straightness
  - cut_length
  - end_squareness
  - connector_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - structural_profile_stock_fabrication_cutting
  import_risk_factors: []
  post_merge_decision_notes: Final import/local decision is deferred until after merge review. This row provides evidence
    for a possible local extrusion workflow.
kb_staging:
  proposed_item_id: null
  notes: Wait for merge review. Existing KB has generic aluminum struts/frames but no confirmed 60 x 60 T-slot closure item;
    consider consolidating this row with other reAM250 60 x 60 profile lengths.
assumptions:
- The aluminum material can be generalized to a locally available structural aluminum alloy compatible with extrusion.
- The Bosch Rexroth slot geometry is preserved only to the level needed for modular frame connector compatibility.
- The measured 650 mm STEP length is used for mass and scale, while the filename length discrepancy is carried as unresolved
  evidence.
unresolved:
- Exact intended installed length is unclear because the filename includes 710 but the STEP bounding box is 650 mm.
- Exact alloy temper, anodizing and finish specification, slot tolerance, and any post-cut end machining are not resolved.
```
