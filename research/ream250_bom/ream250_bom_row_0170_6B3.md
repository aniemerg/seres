---
row_identity:
  item: "6B3"
  cad_file: "6B3_glue"
  source_row_number: 170
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Long, narrow adhesive bead or glue strip used in the row-6 recoater belt/gliding-surface/ceramic-pole/blade area, plausibly to bond or retain the adjacent ceramic pole or gliding-surface elements."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B3_glue.step; research/ream250_bom/ream250_bom_row_0170_6B3__views_2x2.png; research/ream250_bom/ream250_bom_row_0168_6B1.md; research/ream250_bom/ream250_bom_row_0169_6B2.md"
    cited_fact_or_basis: "BOM row 170 names item 6B3 with quantity 1 and CAD file 6B3_glue; manifest row 170 maps it to one matched part STEP. Neighboring BOM rows are 6B1_gliding_surface, 6B2_ceramic_pole, and 6C1_blade. FreeCAD measured one solid with a 1.41 x 2.83 x 274.00 mm bounding box, and the rendered preview shows a very long thin bead-like strip."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM/CAD word 'glue' is interpreted as the functional role of an adhesive bead rather than as a rigid machined insert."
    - "The row-6 neighborhood is interpreted as the recoater belt/gliding-surface/ceramic-pole/blade subassembly."
  uncertainty_notes:
    - "The isolated part export does not show the exact bonded faces or whether the bead bonds 6B2 to 6B1, bonds another mating surface, or represents a modeled adhesive volume for several nearby contacts."
mass:
  value_kg: 0.000282
  basis: "Per-unit mass for quantity 1. FreeCAD volume is 235.204 mm^3 = 0.000000235204 m^3. Using an assumed cured adhesive density of 1200 kg/m^3 gives 0.000282245 kg, rounded to 0.000282 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B3_glue.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 235.204 mm^3 and bounding box 1.41 x 2.83 x 274.00 mm. Local assembly STEP material extraction for product 6B3_glue returned placeholder material 'Generic' with density 1000.0, which does not resolve material. targeted_web_search: queries tried '6B3_glue', 'reAM250 6B3 glue', 'reAM250 6B3_glue material', and 'reAM250 glue ceramic pole'; results found only public BOM repeats or non-row-specific pages, with no row-specific adhesive density or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The exported single-solid STEP volume represents one physical adhesive bead for the BOM row."
    - "A representative cured adhesive density of 1200 kg/m^3 is used because the row does not identify adhesive chemistry and the local density table has no adhesive entry."
  uncertainty_notes:
    - "A typical adhesive density range near 1000-1500 kg/m^3 would move the per-unit mass by roughly -17% to +25% from this estimate."
    - "If the BOM row represents multiple adhesive beads hidden behind the single exported part, total row adhesive mass would be higher than the isolated-part estimate."
material:
  primary_material: "unspecified adhesive/glue polymer"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B3_glue.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 170 and the CAD filename identify the item as 6B3_glue. The per-part STEP geometry is a long bead-like solid. Local assembly STEP material extraction returned only placeholder material 'Generic' with density 1000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because the row identity says glue, the material is kept at the broad adhesive/polymer family level rather than assigning an unsupported epoxy, silicone, acrylic, or cyanoacrylate grade."
  uncertainty_notes:
    - "No adhesive chemistry, cure method, service temperature, vacuum compatibility, or bonding-substrate compatibility is provided."
how_to_make:
  summary: "Plausible route: prepare a compatible structural or retaining adhesive, clean and mask the mating surfaces, dispense a controlled 274 mm bead matching the CAD volume, assemble the mating recoater parts, cure, and inspect squeeze-out and bond continuity"
  manufacturing_steps:
    - "Select an adhesive compatible with the bonded substrates and the recoater operating environment."
    - "Clean and abrade or otherwise prepare the mating surfaces according to the adhesive process requirement."
    - "Dispense a narrow bead approximately matching the CAD envelope and volume."
    - "Position the adjacent recoater components and hold them in alignment during cure."
    - "Cure at the adhesive-specified temperature and time, then inspect bead continuity, squeeze-out, and bonded alignment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B3_glue.step; research/ream250_bom/ream250_bom_row_0170_6B3__views_2x2.png"
    cited_fact_or_basis: "BOM/CAD identify the item as glue, and CAD/preview show a simple long thin adhesive-like strip. targeted_web_search: queries tried 'reAM250 6B3 glue manufacturing', 'reAM250 glue ceramic pole', 'reAM250 6B3_glue adhesive', and 'adhesive bead ceramic pole gliding surface manufacturing'; results did not find a row-specific adhesive specification or process, so the route is inferred from the adhesive-bead geometry and BOM neighborhood."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row is modeled as an applied cured adhesive volume, not a reusable mechanical part or external calibrated module"
    - "Surface preparation, controlled dispensing, fixturing, and cure are included because they are normally required to turn an adhesive into the installed bonded feature represented by the CAD bead."
  uncertainty_notes:
    - "The actual adhesive may require a specific primer, mix ratio, cure schedule, vacuum bake-out, or cleanroom handling not stated by the BOM/CAD row."
kb_implications:
  - "item_granularity: simple_part - Model as a replaceable or applied part adhesive application or cured glue bead tied to an assembly step, not as a standalone reusable part or purchased module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0170_6B3.md
source_research_sha256: f732177eae2853ce5177d1527f385ba1d6bd915f41764b8fa40d115e75e5ae30
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Read the original row evidence, CAD-derived mass and bounding box, material uncertainty, inferred adhesive application
    route, row-6 neighborhood, and preview image showing a long thin bead before conversion.
decomposition:
  decision: simple_part
  rationale: The row represents a tiny applied cured adhesive bead and glue strip with no internal subparts. For closure it
    should be treated as an applied material/assembly feature, not a reusable mechanical part and vendor module.
  proposed_subparts: []
process_abstraction:
  original_process_family: adhesive_application_curing
  primary_process_bucket: polymer_elastomer_forming_dispensing
  supporting_processes:
  - elastomer_forming
  - curing
  - cleaning
  - assembly
  - dimensional_inspection
  - joining
  candidate_existing_processes:
  - process_id: elastomer_molding_basic_v0
    fit: partial
    reason: Covers basic elastomer forming when the row becomes a local seal element.
  - process_id: potting_and_sealing_v0
    fit: partial
    reason: Covers dispensed sealing material and encapsulation style work.
  - process_id: drying_and_curing_v0
    fit: supporting
    reason: Covers curing after polymer and elastomer placement.
  - process_id: seal_installation_v0
    fit: supporting
    reason: Covers installation when the row is treated as a seal in an assembly.
  - process_id: welding_basic_v0
    fit: supporting
    reason: Relevant when the row needs permanent joining.
  abstraction_decision: keep_original_family
  rationale: 'The source route already belongs to the shared polymer dispensing bucket: surface preparation, bead dispensing,
    fixturing, cure, and inspection.'
  process_guardrails:
    tolerance: review - bead placement and thickness affect retention but no machined tolerance is stated
    surface_finish: required - substrate cleaning, abrasion, masking, and primer may be needed
    sealing_quality: not_primary_seal - no evidence that this bead is a pressure and sealed boundary seal
    alignment_accuracy: required - adjacent recoater components must be held in position during cure
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: bond and retain adjacent recoater gliding-surface, ceramic-pole, and blade-area elements
  material: unspecified_adhesive_polymer
  scale_or_capacity:
    mass_kg: 0.000282
    bom_quantity: 1
    row_total_mass_kg: 0.000282
    scale_class: tiny
  geometry_form: long_narrow_dispensed_bead
merge_pool:
  eligible: true
  functional_purpose_key: bonded_component_retention
  precision_guardrails:
  - substrate_compatibility
  - bond_strength
  - cure_schedule
  - cleanliness_outgassing
  - alignment_during_cure
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - polymer_elastomer_forming_dispensing
  import_risk_factors:
  - adhesive chemistry is unspecified
  - service compatibility, outgassing, service temperature, primer, and cure schedule are unknown
  - local polymer and adhesive synthesis may be outside near-term closure scope
  post_merge_decision_notes: Final import/local decision is deferred until adhesive rows are merged and the closure model
    decides the condition that adhesive chemistry is locally produced, imported, and replaced by a mechanical retention feature.
kb_staging:
  proposed_item_id: null
  notes: Defer item ID until merge review; likely converges with other applied adhesive and bond-retention rows rather than
    becoming a unique 6B3 item.
assumptions:
- The STEP solid represents one cured adhesive bead for BOM quantity 1.
- The representative cured adhesive density and tiny mass are adequate for closure-scale accounting despite unknown chemistry.
- General adhesive application equipment plus labor/fixturing can reproduce the installed feature if the adhesive itself is
  available.
unresolved:
- Actual adhesive family, substrate pair, primer, cure method, service temperature, and outgassing requirements are not identified.
- The exact bonded interfaces in the recoater subassembly are not visible from the isolated row export.
- Later staging must decide the condition that the lunar abstraction keeps adhesive bonding, substitutes mechanical retention,
  and treats adhesive as an import.
```
