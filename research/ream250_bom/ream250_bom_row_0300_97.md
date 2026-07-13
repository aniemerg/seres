---
row_identity:
  item: "97"
  cad_file: "97_profile_60x60_1020"
  source_row_number: 300
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Structural 60 x 60 mm Bosch Rexroth aluminum strut profile used as a machine-frame member; the longitudinal slots accept compatible connectors, brackets, and accessories."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0300_97__views_2x2.png; https://www.boschrexroth.com/en/nz/products/industrial-solutions/assembly-technology/aluminum-profile-kit/"
    cited_fact_or_basis: "BOM row 300 and manifest row 300 identify item 97 as quantity 2, `97_profile_60x60_1020`, description `strut profile`, manufacturer Bosch Rexroth AG. The CAD preview shows a long 60 mm square slotted extrusion. Bosch Rexroth describes its aluminum profile construction kit as profiles used for machine frames, workstations, shelves, and safety fences with matched connection technology."
    evidence_basis: "bom_provided"
  assumptions:
    - "The 1020 mm CAD length represents one physical profile in the row, not the total row quantity."
  uncertainty_notes:
    - "The exact installed location in the reAM250 frame is not identified by the isolated part file."
mass:
  value_kg: 3.982
  basis: "Per-unit mass estimate from FreeCAD volume 1474672.938 mm^3 = 0.001474672938 m^3 multiplied by local aluminum density 2700 kg/m^3 from kb/materials/properties.yaml, giving 3.9816 kg per 1020 mm profile. BOM quantity is 2, so the row total is about 7.963 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/97_profile_60x60_1020.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 1474672.9382343262 mm^3, surface area 922498.0201314631 mm^2, and bounding box 1020.0 x 60.0 x 60.0 mm. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP volume is treated as the solid metal volume of one cut profile."
    - "The broad aluminum density entry is close enough for this BOM planning estimate."
  uncertainty_notes:
    - "The assembly STEP material extractor returned only `Generic` with density 1000.0, so the mass depends on the Bosch aluminum-profile family evidence rather than row-specific material metadata."
material:
  primary_material: "aluminum profile extrusion"
  source:
    url_or_path: "https://www.boschrexroth.com/en/nz/products/industrial-solutions/assembly-technology/aluminum-profile-kit/; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "BOM row 300 identifies a Bosch Rexroth AG strut profile and links to the Bosch Rexroth Strebenprofil product-family route. Bosch Rexroth's profile construction kit page identifies the product family as aluminum profiles."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row uses the standard Bosch Rexroth aluminum profile material family rather than a non-aluminum special variant."
  uncertainty_notes:
    - "The exact alloy, temper, and surface finish are not encoded in the row fields or local STEP material metadata."
how_to_make:
  summary: "Prepare as a Bosch Rexroth standard aluminum strut profile cut to 1020 mm, or locally make by aluminum extrusion of the 60 x 60 mm slotted cross-section, straightening/aging as required, cutting to length, deburring, and applying the required protective finish"
  manufacturing_steps:
    - "Produce"
    - "Extrude the 60 x 60 mm slotted profile through a matched die."
    - "Straighten and age or heat-treat according to the selected aluminum profile alloy."
    - "Cut the extrusion to 1020 mm length."
    - "Deburr cut ends and apply or preserve the profile finish."
    - "Inspect length, straightness, slot geometry, and fit with Rexroth-compatible connectors."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/97_profile_60x60_1020.step; research/ream250_bom/ream250_bom_row_0300_97__views_2x2.png; https://www.boschrexroth.com/en/nz/products/industrial-solutions/assembly-technology/aluminum-profile-kit/"
    cited_fact_or_basis: "CAD geometry and preview show a constant-section 1020 mm long 60 x 60 mm slotted profile. Bosch Rexroth identifies the product family as aluminum profiles in a modular profile construction kit. targeted_web_search: queries tried were `Bosch Rexroth strut profile 60x60 aluminum weight kg m` and `site:boschrexroth.com Strebenprofil 60x60 Bosch Rexroth Aluminium weight`; results confirmed the aluminum-profile family but did not provide a row-specific manufacturing process for this exact cut length."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the constant cross-section CAD shape and common aluminum profile practice; the Bosch source supports product identity, not detailed process steps."
  uncertainty_notes:
    - "A self-manufacturing KB entry would need a specific alloy, extrusion die design, temper, and finish specification before detailed process modeling."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut-to-length structural aluminum extrusion/profile, not as a calibrated purchased module; quantity variants can share one profile family with length-specific BOM notes."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0300_97.md
source_research_sha256: "848359d695a1db73f774b2adb9a36f02f91851c507234ed1b53d0db13d3158a0"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the machine-frame strut function, CAD-derived per-unit and row-total mass basis, Bosch Rexroth aluminum-profile evidence, extrusion/cut-to-length route, and preview showing a long 60 x 60 mm slotted extrusion."
decomposition:
  decision: simple_part
  rationale: "The row is a cut length of structural aluminum profile; connectors and fasteners are separate hardware."
  proposed_subparts: []
process_abstraction:
  original_process_family: aluminum_profile_extrusion_cut_to_length
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - extrusion
    - heat_treatment
    - cutting
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_extrusion_process_v0
      fit: partial
      reason: "Covers aluminum extrusion, but is currently specific to heat-sink fin extrusion rather than generic structural profiles."
    - process_id: extrusion_basic_v0
      fit: poor_fit
      reason: "General extrusion template exists, but its inputs and outputs are polymer-focused and need adaptation for aluminum profile stock."
    - process_id: metal_cutting_basic_v0
      fit: direct
      reason: "Matches cut-to-length preparation of the 1020 mm profile."
    - process_id: surface_treatment_anodizing_v0
      fit: supporting
      reason: "Relevant if the Bosch-style protective finish is modeled as anodizing."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers length, straightness, slot geometry, and connector-fit checks."
  abstraction_decision: keep_original_family
  rationale: "The source route is aluminum profile extrusion followed by cutting and finishing, directly matching the structural-profile stock bucket."
  process_guardrails:
    tolerance: standard
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: standard
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: modular slotted framing member for machine-frame structure
  material: aluminum_profile_family
  scale_or_capacity:
    mass_kg: 3.982
    bom_quantity: 2
    row_total_mass_kg: 7.963
    scale_class: medium
  geometry_form: cut_length_60x60_slotted_square_extrusion
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - profile_slot_geometry
    - cut_length
    - straightness
    - connector_fit
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Extrusion die and profile finish are reusable tooling/process dependencies."
    - "Exact alloy, temper, and finish are unresolved."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this with other structural profile rows."
kb_staging:
  proposed_item_id: null
  notes: "Hold final item identity for merge review across structural aluminum profile segments; length and 60 x 60 profile size are guardrails."
assumptions:
  - "The 1020 mm CAD length is per profile, with BOM quantity two."
  - "Standard Bosch-style aluminum profile material family is used for planning mass."
unresolved:
  - "Exact alloy, temper, finish, cut tolerance, and extrusion die details are not specified."
  - "Whether length-specific profiles become separate closure items depends on merge review."
```
