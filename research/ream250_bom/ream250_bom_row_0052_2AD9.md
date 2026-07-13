---
row_identity:
  item: "2AD9"
  cad_file: "2AD9_part_9"
  source_row_number: 52
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin annular retaining or spacer ring in the top axis-bearing group, likely providing axial location or clearance around the top-axis bearing stack."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD9_part_9.step; research/ream250_bom/ream250_bom_row_0052_2AD9__views_2x2.png"
    cited_fact_or_basis: "BOM row 52 identifies item 2AD9, quantity 1, CAD file 2AD9_part_9, description 'axis bearing top'. The manifest maps the same row to gold_export/parts/2AD9_part_9.step with matched_existing part status. FreeCAD measured one solid with volume 760.144 mm^3 and bounding box about 24.04 x 6.27 x 24.04 mm; the rendered contact sheet shows a thin annular ring with a central bore and four radial relief/cutout features."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because the row is grouped with adjacent top-axis bearing components, the annular CAD shape is interpreted as a retaining, spacer, or race-adjacent ring rather than a decorative washer."
  uncertainty_notes:
    - "The BOM row does not name the exact bearing architecture, so the distinction between retainer, spacer, and bearing-race support remains unresolved."
mass:
  value_kg: 0.00597
  basis: "Per-unit estimate for one 2AD9 ring. FreeCAD STEP volume 760.144 mm^3 = 7.60144e-7 m^3; using the local generic steel density constant 7850 kg/m^3 from kb/materials/properties.yaml gives 0.005967 kg, rounded to 0.00597 kg. BOM quantity is 1, so row total is also about 0.00597 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD9_part_9.step; kb/materials/properties.yaml; https://isccompanies.com/parts-distribution/pt-accessories/retaining-rings/; https://www.smalley.com/blog/retaining-ring-types-and-selection"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 760.144 mm^3, area 1067.282 mm^2, and bounding box about 24.04 x 6.27 x 24.04 mm. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. ISC describes retaining rings as thin circular metal components used to retain assemblies and notes spring steel and stainless steel availability; Smalley notes retaining rings are available in carbon and stainless steel. targeted_web_search: searched '2AD9_part_9 axis bearing top material', '2AD9 axis bearing top reAM250 material', 'axis bearing top 2AD9_part_9', and 'slotted bearing retaining ring material steel axial bearing retainer'; found duplicate BOM text and generic retaining-ring sources, but no row-specific material or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the physical volume of one BOM item."
    - "Generic steel density is used as the local calculation constant for a likely carbon/spring/stainless steel retaining-ring family."
  uncertainty_notes:
    - "Assembly STEP material extraction returned only placeholder material 'Generic' with density 1000.0, so the mass depends on inferred metal family rather than row-specific material metadata."
    - "If the part is aluminum, polymer, or a lower-density bearing cage material rather than steel, the per-unit mass would be materially lower."
material:
  primary_material: "unknown metal/alloy retaining-ring material family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD9_part_9.step; research/ream250_bom/ream250_bom_row_0052_2AD9__views_2x2.png; https://isccompanies.com/parts-distribution/pt-accessories/retaining-rings/; https://www.smalley.com/blog/retaining-ring-types-and-selection"
    cited_fact_or_basis: "The BOM labels 2AD9 as 'axis bearing top' and the CAD preview shows a thin annular metal-like ring form. Local assembly material extraction for 2AD9_part_9 returned only placeholder material 'Generic' with density 1000.0. ISC states retaining rings are thin circular metal components and lists spring steel and stainless steel variants; Smalley lists carbon and stainless steel retaining rings. targeted_web_search: searched '2AD9_part_9 axis bearing top material', '2AD9 axis bearing top reAM250 material', and 'slotted bearing retaining ring material steel'; found no row-specific material grade."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A steel retaining-ring material family is used because the part's annular cutout geometry and bearing context match common bearing retention hardware better than a soft washer or polymer spacer."
  uncertainty_notes:
    - "No BOM field, vendor link, standard designation, or non-placeholder STEP material resolves the exact alloy or heat treatment."
how_to_make:
  summary: "Prepare as small bearing-retention hardware if it matches a standard ring; otherwise manufacture locally by cutting or machining the annular profile from steel sheet/plate or flat stock, deburring, heat treating if spring action is required, and inspecting fit in the bearing stack"
  manufacturing_steps:
    - "Start from steel sheet, plate, or flat wire stock near the required thickness."
    - "Blank, laser/waterjet cut, wire-EDM, or mill the outside diameter, central bore, and four relief/cutout features."
    - "Deburr and finish edges so the ring does not damage mating bearing surfaces."
    - "Heat treat or spring temper only if the final design requires elastic retention rather than simple spacing."
    - "Inspect outer diameter, bore diameter, thickness, flatness, and cutout clearance against the top-axis bearing assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD9_part_9.step; research/ream250_bom/ream250_bom_row_0052_2AD9__views_2x2.png; https://isccompanies.com/parts-distribution/pt-accessories/retaining-rings/; https://www.smalley.com/blog/retaining-ring-types-and-selection"
    cited_fact_or_basis: "The local STEP/contact sheet shows a thin annular part with a central bore and radial reliefs. ISC describes retaining rings as stamped from sheet or coiled from wire and installed to create a shoulder that retains an assembly. Smalley describes retaining-ring families made from flat wire by edgewinding, with carbon and stainless steel material options. targeted_web_search: searched '2AD9_part_9 axis bearing top manufacturing', 'slotted bearing retaining ring manufacturing stamped sheet steel', and 'retaining ring bearing material spring steel stainless'; found generic retaining-ring manufacturing sources, but no row-specific production drawing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the CAD profile and common retaining-ring practice because the row has no vendor process or drawing notes."
    - "For KB planning, this should be modeled as simple precision metal hardware unless later evidence shows it is part of a calibrated bearing cartridge."
  uncertainty_notes:
    - "Required tolerances, surface finish, spring properties, and whether the ring is a external standard or custom-machined part are not specified by the BOM or CAD export"
kb_implications:
  - "item_granularity: simple_part - model as reusable small bearing retaining/spacer ring hardware rather than a unique reAM250-only item; capture approximate 24 mm OD, 6.27 mm thickness, steel-family material, and top-axis bearing context in later KB notes."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0052_2AD9.md
source_research_sha256: "a514bc7e53a3142b0b69faf170c6f2e1abe258be88704064e5ff05d2b8a786dc"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the top-axis bearing retaining/spacer function, 0.00597 kg steel-family mass estimate, unresolved metal retaining-ring material evidence, cutting/machining route, KB implication, and CAD preview showing a small annular ring with relief cutouts."
decomposition:
  decision: simple_part
  rationale: "The row is one small annular hardware part with no internal assemblies; it should stay a simple reusable retaining/spacer ring unless later evidence places it inside a calibrated bearing cartridge."
  proposed_subparts: []
process_abstraction:
  original_process_family: cut_machined_bearing_retaining_ring
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - deburring
    - heat_treatment
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_cutting_v0
      fit: partial
      reason: "Covers cutting a flat ring blank from sheet/plate stock, but small bearing-fit features may need tighter control."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant to bore, outer diameter, relief features, and thickness control if the ring is custom machined."
    - process_id: heat_treatment_hardening_v0
      fit: supporting
      reason: "Relevant only if the final design needs spring-tempered retaining-ring behavior."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Covers edge cleanup so the ring does not damage bearing-adjacent surfaces."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers checks of diameter, thickness, flatness, and cutout clearance."
  abstraction_decision: substitute_process_family
  rationale: "The source route is unresolved retaining-ring practice, but the geometry is shallow annular sheet/plate hardware; primary closure can use sheet/plate cutting with precision machining and heat treatment as conditional support."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: moderate
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "bearing stack axial retaining and spacing hardware"
  material: unresolved_steel_retaining_ring_family
  scale_or_capacity:
    mass_kg: 0.00597
    bom_quantity: 1
    row_total_mass_kg: 0.00597
    scale_class: small
  geometry_form: small_annular_ring_with_radial_relief_cutouts
merge_pool:
  eligible: true
  functional_purpose_key: mechanical_retention
  precision_guardrails:
    - bore_diameter
    - outer_diameter
    - flatness
    - spring_temper_requirement
    - bearing_stack_context
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Exact material, spring property, heat treatment, and bearing-stack tolerance are unresolved."
    - "If this is a standard precision retaining ring, importing a standard hardware family may be simpler than custom local manufacture."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this with other retaining rings, spacers, and small bearing hardware."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable as a generic small steel retaining/spacer ring if precision requirements remain modest."
assumptions:
  - "BOM quantity is 1 and row total mass is treated as 0.00597 kg from the steel-density CAD estimate."
  - "The part is modeled as steel-family retaining hardware based on geometry and bearing context."
  - "Heat treatment is conditional; simple spacer use may not need spring-tempered behavior."
unresolved:
  - "Exact alloy, heat treatment, standard designation, tolerance, surface finish, and role as retainer versus spacer remain unknown."
  - "Whether the ring is standard hardware versus a custom-machined bearing-adjacent part is unresolved."
```
