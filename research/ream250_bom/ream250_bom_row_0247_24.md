---
row_identity:
  item: "24"
  cad_file: "24_seal_left_right"
  source_row_number: 247
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
function:
  summary: "Long, thin left/right side seal strip formed from black silicone sealing compound; it fills the joint between mating machine panels or cover surfaces to prevent leakage and tolerate vibration."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/24_seal_left_right.step; research/ream250_bom/ream250_bom_row_0247_24__views_2x2.png; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "BOM row 247 names item 24 as quantity 2, CAD file 24_seal_left_right, product 6185 black silicone sealant from Liqui Moly. FreeCAD measured a 3.0 x 355.0 x 917.0 mm solid, and the rendered contact sheet shows a flat rectangular seal strip. The Liqui Moly BOM URL describes the product as a silicone-based sealing compound that remains elastic, resists chemicals/oils, and is used for sealing mating housings and covers."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid represents the applied/cured seal geometry for one left or right side seal, not the full 200 ml aerosol container."
  uncertainty_notes:
    - "The STEP file gives the seal envelope but not its installation preload, compression state, or exact sealed interface."
mass:
  value_kg: 0.0891
  basis: "Per physical seal strip. FreeCAD volume is 74218.672 mm^3 = 0.000074218672 m^3. Using the local silicone_rubber representative density of 1200 kg/m^3 gives 0.000074218672 * 1200 = 0.089062 kg per strip. BOM quantity is 2, so row total is about 0.178 kg; the two modeled strips occupy about 148.4 ml, within one 200 ml product container."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/24_seal_left_right.step; kb/materials/properties.yaml; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 74218.672 mm^3 and bounding box 3.0 x 355.0 x 917.0 mm. BOM/vendor evidence identifies the material as black silicone sealing compound. kb/materials/properties.yaml lists silicone_rubber density as 1200 kg/m^3. The Liqui Moly BOM URL lists article 6185 as a 200 ml container."
    evidence_basis: "bom_provided"
  assumptions:
    - "Representative silicone rubber density is suitable for the applied/cured sealant volume for coarse BOM modeling."
  uncertainty_notes:
    - "Actual mass may vary with bead squeeze-out, voids, cure chemistry, and the density of the specific uncured Liqui Moly 6185 formulation."
material:
  primary_material: "black silicone-based sealing compound / cured silicone elastomer"
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "BOM row 247 gives description 6185: black silicone sealant and manufacturer Liqui Moly. The BOM-provided Liqui Moly page describes Silikondichtmasse schwarz as a silicone-based sealing compound and lists article 6185."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Assembly STEP material metadata returned only Generic with density 1000, so it was not used as material evidence."
    - "The public product page supports silicone-based sealant but does not expose a complete cured elastomer formulation or filler package."
how_to_make:
  summary: "Prepare Liqui Moly 6185 black silicone sealing compound or an equivalent silicone gasket compound, clean and degrease the mating faces, dispense an even 3 mm-thick seal path matching the CAD strip, and join the mating parts immediately so the compound cures in place"
  manufacturing_steps:
    - "Prepare 200 ml Liqui Moly 6185 black silicone sealing compound or equivalent silicone gasket compound"
    - "Clean the sealing faces so they are dry and free of oil and grease."
    - "Apply a continuous bead/strip following the left or right side seal path represented by the CAD geometry."
    - "Assemble the mating parts immediately, without a waiting/flash-off period, and allow the sealant to cure in place."
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/24_seal_left_right.step"
    cited_fact_or_basis: "The BOM-provided Liqui Moly page identifies article 6185 as a 200 ml black silicone sealing compound and states that surfaces should be clean, oil-free, grease-free, and dry; material is applied evenly and parts are joined immediately without flash-off time. The STEP file gives the long, flat seal geometry."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The exact dispensing tool, cure time, and applied bead tolerance are not specified in the row evidence."
kb_implications:
  - "item_granularity: simple_part - Model as applied silicone sealant/seal material consumed during assembly rather than as a reusable machine part or purchased module."
---
## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0247_24.md
source_research_sha256: "91e0f10efe602fa1059b0432d4fa945603d5017be0523a63a626feb51a46d321"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed silicone side-seal function, per-strip and row-total mass basis, Liqui Moly black silicone evidence, dispense-and-cure route, and CAD envelope for the long thin strip."
decomposition:
  decision: simple_part
  rationale: "The row is an applied/cured sealant geometry consumed in assembly, not a reusable module with internal subparts."
  proposed_subparts: []
process_abstraction:
  original_process_family: silicone_sealant_dispensing_and_curing
  primary_process_bucket: polymer_elastomer_forming_dispensing
  supporting_processes:
    - elastomer_forming
    - cleaning
    - curing
    - assembly
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: elastomer_molding_basic_v0
      fit: partial
      reason: "Covers basic elastomer shaping, though this row is dispensed in place rather than molded as a standalone gasket."
    - process_id: silicone_polymerization_v0
      fit: supporting
      reason: "Relevant upstream if local closure produces silicone elastomer material instead of importing compound."
    - process_id: sealing_and_assembly_basic_v0
      fit: supporting
      reason: "Covers applying sealing material and joining mating parts during assembly."
    - process_id: drying_and_curing_v0
      fit: supporting
      reason: "Covers cure time after the silicone compound is applied."
  abstraction_decision: keep_original_family
  rationale: "The source process is already elastomer compound dispensing and curing, matching the polymer/elastomer forming and dispensing closure bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: not_applicable
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: compliant joint leakage prevention between mating covers and panels
  material: silicone_elastomer
  scale_or_capacity:
    mass_kg: 0.0891
    bom_quantity: 2
    row_total_mass_kg: 0.178
    scale_class: small
  geometry_form: long_thin_applied_side_strip_3_mm_thick
merge_pool:
  eligible: true
  functional_purpose_key: leakage_prevention
  precision_guardrails:
    - continuous_bead
    - surface_cleanliness
    - cured_elasticity
    - compression_fit
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - polymer_elastomer_forming_dispensing
  import_risk_factors:
    - "Silicone chemistry and filler package may stay imported if local polymer production is outside the current closure scope."
    - "Seal performance depends on surface preparation, cure state, and chemical compatibility."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups applied sealing compounds and checks elastomer supply assumptions."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable as applied silicone sealant material with geometry and quantity captured at BOM level."
assumptions:
  - "The CAD solid is treated as cured applied sealant, not the original 200 ml product container."
  - "Representative silicone rubber density remains adequate for closure-scale mass accounting."
unresolved:
  - "Exact cured formulation, filler package, cure time, and dispensing tolerance are not specified."
  - "The specific sealed interface and compression state are unknown."
```
