---
row_identity:
  item: 2AD8
  cad_file: 2AD8_part_8
  source_row_number: 51
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Small spherical rolling element for the top axis bearing set.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD8_part_8.step; research/ream250_bom/ream250_bom_row_0051_2AD8__views_2x2.png
    cited_fact_or_basis: "BOM row 51 names item 2AD8 as 'axis bearing top'; the matched STEP is one solid with a 4.95 x 4.95 x 4.95 mm bounding box, and the rendered preview shows a near-spherical ball."
    evidence_basis: bom_provided
  assumptions:
    - The repeated neighboring rows 2AD1 through 2ADB with the same description represent individual balls in the same top-axis bearing group.
  uncertainty_notes:
    - The BOM does not name the bearing assembly type or the race/cage that uses this ball.
mass:
  value_kg: 0.000499
  basis: "Per-unit mass for quantity 1. FreeCAD measured volume is 63.506 mm^3, or 6.3506e-8 m^3. Using the local steel density constant 7850 kg/m^3 gives 0.0004985 kg, rounded to 0.000499 kg."
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD8_part_8.step; kb/materials/properties.yaml; https://www.metal-ball.com/wp-content/uploads/2016/02/manufacturing-std.pdf
    cited_fact_or_basis: "CAD measures a 63.506 mm^3 spherical solid; local properties list generic steel density as 7850 kg/m^3; bearing balls are covered by standard families such as ISO 3290-1 and DIN 5401."
    evidence_basis: standard_part_convention
  assumptions:
    - The part is treated as a steel bearing ball because the BOM description and CAD sphere match a standard bearing-ball use.
  uncertainty_notes:
    - Assembly STEP material extraction returned only Generic with density 1000.0, so the CAD package does not provide a usable material-specific mass.
material:
  primary_material: bearing steel / chrome steel bearing-ball material family
  source:
    url_or_path: https://www.grw.de/files/grw/FINALE%20BILDDATEN/INFOTHEK/DOWNLOADS/BROSCHUEREN/EN/GRW_Bearing%20Materials_2023.pdf; https://www.metal-ball.com/wp-content/uploads/2016/02/manufacturing-std.pdf
    cited_fact_or_basis: "Standard precision ball-bearing material references identify chrome steel and stainless bearing steels for bearing balls, and manufacturing standards cover bearing steel balls under ISO 3290-1 / DIN 5401 classes."
    evidence_basis: standard_part_convention
  assumptions:
    - For KB planning, use the broad bearing-steel family rather than a specific grade because the BOM row has no manufacturer, grade, or product designation.
  uncertainty_notes:
    - The row-specific local STEP material is a placeholder, and targeted_web_search: queries '2AD8 axis bearing top reAM250', 'axis bearing top 2AD8_part_8', and '4.95 mm bearing ball material steel' found the BOM text and generic bearing-ball material examples, but no row-specific vendor material record.
how_to_make:
  summary: "Follow bearing-ball forming, hardening, grinding, lapping, polishing, and inspection"
  manufacturing_steps:
    - Select a standard steel bearing-ball size matching the CAD diameter near 4.95 mm.
    - For local manufacture, cut steel wire slug stock and cold-head or forge it into a ball blank.
    - Heat treat the blank for bearing hardness, then grind, lap, polish, and sort to the required ball grade.
    - Inspect diameter, roundness, and surface finish before installing it in the top-axis bearing group.
  source:
    url_or_path: https://www.metal-ball.com/wp-content/uploads/2016/02/manufacturing-std.pdf; https://www.grw.de/files/grw/FINALE%20BILDDATEN/INFOTHEK/DOWNLOADS/BROSCHUEREN/EN/GRW_Bearing%20Materials_2023.pdf
    cited_fact_or_basis: "Standard bearing-ball documents define ISO/DIN ball classes and bearing material families; the row has enough standard parameters for procurement planning only at the family/diameter level, not a complete grade designation."
    evidence_basis: standard_part_convention
  assumptions: []
  uncertainty_notes:
    - The exact tolerance grade, hardness, and corrosion-resistance requirement are not present in the BOM or CAD evidence.
kb_implications:
  - "item_granularity: simple_part - Model 2AD8 with the other 2AD top-axis rows as a reusable bearing ball part, not as a separate machine or assembly."
---

Research result for reAM250 BOM row 51.
