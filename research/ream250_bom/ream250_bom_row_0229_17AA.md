---
row_identity:
  item: "17AA"
  cad_file: "17AA_strut_profile_20X20_271"
  source_row_number: 229
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Short 20 mm x 20 mm Bosch Rexroth aluminum T-slot strut profile used as a light structural rail/member in the reAM250 frame or fixture assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0229_17AA__views_2x2.png; https://www.boschrexroth.com/en/us/products/industrial-solutions/assembly-technology/aluminum-profile-kit/"
    cited_fact_or_basis: "BOM row 229 identifies item 17AA as 'strut profile' from Bosch Rexroth AG; CAD preview shows a 271 mm long 20 x 20 mm slotted extrusion; Bosch describes its aluminum profile system as used to construct machine frames, workstations, shelves, safety fences, and similar structures. official_alternate_route_check: original BOM link points to the Bosch Rexroth store strut-profile category; the Bosch Rexroth aluminum-profile-kit page is a first-party Bosch route for the same aluminum strut-profile product family and links to the profile catalog."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row's short profile is a frame/fixture rail rather than a precision motion guide because the BOM description, CAD cross-section, and Bosch profile family all indicate modular framing stock."
  uncertainty_notes:
    - "The parent assembly location is not specified in the leased context, so the exact frame subassembly function is inferred only at the structural-member level."
mass:
  value_kg: 0.121
  basis: "Per unit, not row total. FreeCAD measured one solid with volume 44,882.764 mm^3 and bounding box 271.00 x 20.00 x 20.00 mm. Using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives 44,882.764e-9 m^3 * 2700 = 0.12118 kg per profile. The BOM quantity is 2, so the row total is about 0.242 kg. As a catalog cross-check, the Bosch 20x20 sheet lists mass about 0.4 kg/m, which gives about 0.108 kg for 0.271 m; the CAD-volume estimate is retained because it is row-specific."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AA_strut_profile_20X20_271.step; kb/materials/properties.yaml; https://docs.rs-online.com/ea04/A700000007302204.pdf"
    cited_fact_or_basis: "FreeCAD measurement of the row STEP file returned volume 44,882.76366211526 mm^3 and bounding box 271.0, 20.0, 20.0 mm; local material table gives aluminum density 2700 kg/m^3; the Bosch Rexroth 20x20 datasheet lists anodized aluminum material and rounded mass data for the 20x20 profile. bom_url_route_check: original Bosch store URL was checked as the BOM route; it did not expose parseable row-specific technical values in this environment, so the calculation uses the local CAD package plus a Bosch-branded datasheet copy hosted by RS for the exact 20x20 strut profile family."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD solid represents the aluminum body volume for one physical profile and excludes no major inserts or fasteners."
    - "The generic local aluminum density is close enough for anodized aluminum extrusion alloy at this planning precision."
  uncertainty_notes:
    - "Assembly STEP material metadata for this product reports only 'Generic' at density 1000.0, so it was ignored as placeholder metadata."
    - "CAD-density mass and catalog mass-per-length differ by roughly 12%; downstream KB use should treat 0.121 kg as a supported estimate, not a weighed value."
material:
  primary_material: "anodized aluminum"
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Bosch Rexroth 20x20 strut-profile datasheet lists the 20x20 profile material as anodized aluminum for the matching profile/order-code family. Local assembly STEP metadata was checked for product 17AA_strut_profile_20X20_271 but returned only Generic material with density 1000.0. bom_url_route_check: original Bosch store URL was checked first as the BOM-provided route; exact material text was resolved from a Bosch-branded 20x20 datasheet copy because the store route did not expose parseable technical data here."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "No specific aluminum alloy temper was found in the BOM row, CAD metadata, or checked datasheet, so the material is kept at family/finish precision."
how_to_make:
  summary: "Prepare or specify a Bosch Rexroth 20x20 anodized aluminum strut profile cut to the 271 mm CAD length; for local manufacture, extrude an aluminum 20x20 T-slot profile, anodize or otherwise protect the surface, cut to length, and deburr/inspect the ends"
  manufacturing_steps:
    - "Cut to 271 mm if supplied oversize"
    - "Local fabrication route: extrude an aluminum billet through a die for the 20x20 four-slot profile with central bore."
    - "Apply anodized or equivalent protective finish, then saw-cut to 271 mm and deburr open ends."
    - "Inspect length, straightness, slot geometry, and end condition before assembly with standard slot hardware."
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.part-on.co.uk/product/20-x-20mm-aluminium-profile-part-on-range/; research/ream250_bom/ream250_bom_row_0229_17AA__views_2x2.png"
    cited_fact_or_basis: "The Bosch 20x20 datasheet lists specified-length order options from 50 to 3000 mm for the 20x20 strut profile; a distributor page for genuine Bosch Rexroth 20 x 20 mm aluminum strut profile states it can be cut to required size; the CAD preview confirms the row is a straight slotted extrusion. bom_url_route_check: original Bosch store URL was checked as the BOM route; because parseable manufacturing/procurement details were limited there, the route uses the Bosch-branded datasheet copy and a distributor page matching the same genuine Bosch Rexroth 20x20 strut-profile family."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The manufacturing route uses standard aluminum extrusion practice for T-slot framing, not every extrusion process parameter"
  uncertainty_notes:
    - "The exact Bosch alloy, anodizing specification, and end-finish option for this row are not stated"
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut-to-length 20x20 aluminum T-slot profile/simple structural extrusion, not as a unique machine assembly."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0229_17AA.md
source_research_sha256: "0732372e2e09f62ca74a4a5c4562f0ef0c8cd927603f6218b13a5d3fe86b58a9"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read function, quantity, CAD-derived mass with catalog cross-check, anodized aluminum evidence, extrusion/cut route, kb implications, and preview showing a 271 mm long 20x20 T-slot profile."
decomposition:
  decision: simple_part
  rationale: "The row is a single cut length of structural extrusion with no internal module structure. Slot geometry is part of the profile identity."
  proposed_subparts: []
process_abstraction:
  original_process_family: aluminum_t_slot_profile_extrusion_cut_to_length
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - extrusion
    - cutting
    - deburring
    - coating
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_extrusion_process_v0
      fit: partial
      reason: "Covers aluminum extrusion at coarse level, though the existing process is parameterized around heat-sink fins rather than T-slot framing."
    - process_id: cutting_basic_v0
      fit: supporting
      reason: "Covers cutting profile stock to the 271 mm finished length."
    - process_id: surface_treatment_anodizing_v0
      fit: supporting
      reason: "Relevant to anodized aluminum profile finish if local production includes surface treatment."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Relevant for length, slot geometry, straightness, and end-condition checks."
  abstraction_decision: keep_original_family
  rationale: "The original route already belongs to structural extrusion stock cut to length. This should merge with other aluminum frame profiles rather than become a unique machine-specific part."
  process_guardrails:
    tolerance: standard_profile_review
    surface_finish: anodized_finish_review
    sealing_quality: not_applicable
    alignment_accuracy: frame_straightness_review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: light structural rail member for frame and fixture assembly
  material: anodized_aluminum
  scale_or_capacity:
    mass_kg: 0.121
    bom_quantity: 2
    row_total_mass_kg: 0.242
    scale_class: small
  geometry_form: cut_length_20x20_t_slot_extrusion_271mm
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - t_slot_interface
    - profile_straightness
    - cut_length
    - anodized_finish
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Exact alloy, anodizing specification, and profile die availability are unresolved."
    - "If T-slot compatibility is not required, later design substitution may use simpler structural profiles."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares short aluminum frame profiles and decides profile standardization."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before assigning an item ID; likely candidate family is a small aluminum structural profile."
assumptions:
  - "BOM quantity is 2, so row total mass is about 0.242 kg from the 0.121 kg per-unit estimate."
  - "The 20x20 T-slot interface should be preserved for merge review even if later lunarized design simplifies the profile."
  - "Anodized aluminum is recorded as material/finish evidence, but exact alloy remains unresolved."
unresolved:
  - "Specific aluminum alloy and anodizing specification."
  - "Whether T-slot modular compatibility is closure-critical in the final KB abstraction."
  - "Whether multiple short Bosch profile rows should merge into one cut-to-length structural profile family."
```
