---
row_identity:
  item: "2AD2"
  cad_file: "2AD2_part_2"
  source_row_number: 45
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small spherical rolling element for the reAM250 top axis bearing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0045_2AD2__views_2x2.png"
    cited_fact_or_basis: "BOM row 45 lists item 2AD2, quantity 1, CAD file 2AD2_part_2, description axis bearing top; the manifest maps row 45 to gold_export/parts/2AD2_part_2.step as a matched existing part; the rendered preview shows a nearly spherical part in a 4.95 x 4.95 x 4.95 mm envelope."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row's 'axis bearing top' description is interpreted together with the spherical CAD shape as one bearing rolling element rather than a housing, race, or mount."
  uncertainty_notes:
    - "The BOM row does not name the complete top-axis bearing standard or the mating race geometry, so the exact bearing assembly role is inferred from row context and shape."
mass:
  value_kg: 0.0005
  basis: "FreeCAD volume 63.506 mm^3 converted to 6.3506e-8 m^3 and multiplied by the local generic steel density of 7850 kg/m^3, yielding about 0.0004985 kg per part."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD2_part_2.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 63.506 mm^3, area 76.977 mm^2, and bounding box 4.95 x 4.95 x 4.95 mm; kb/materials/properties.yaml lists steel density as 7850 kg/m^3. targeted_web_search: searched \"2AD2_part_2 axis bearing top material\", \"2AD2 axis bearing top reAM250 material\", \"axis bearing top reAM250\", and \"2AD2_part_2\"; found duplicate BOM text but no row-specific vendor mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid is treated as the complete per-unit geometry for one BOM row 2AD2 part."
    - "Generic steel density is used as a representative density for a small bearing rolling element because row-specific material evidence was not found."
  uncertainty_notes:
    - "Mass depends mainly on the inferred steel material family; if the rolling element is ceramic or a non-steel alloy, the mass would change materially."
material:
  primary_material: "hardened steel bearing material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0045_2AD2__views_2x2.png"
    cited_fact_or_basis: "BOM row 45 identifies the part as axis bearing top; local STEP material extraction for product 2AD2_part_2 reports only Generic with density 1000.0; the rendered preview shows a near-spherical rolling-element shape. targeted_web_search: searched \"2AD2_part_2 axis bearing top material\", \"2AD2 axis bearing top reAM250 material\", \"axis bearing top reAM250\", and \"2AD2_part_2\"; found duplicate BOM text but no row-specific vendor/material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A small spherical rolling element in an axis bearing is modeled as hardened steel bearing material unless a later row-specific bearing standard, vendor page, or CAD material source identifies ceramic or another alloy."
  uncertainty_notes:
    - "The material family is not directly sourced for this row; only the bearing context and spherical geometry support the steel rolling-element hypothesis."
how_to_make:
  summary: "Manufacture as a precision steel bearing ball by cold heading or forming, heat treatment, grinding, lapping, polishing, and inspection."
  manufacturing_steps:
    - "Cut bearing-steel wire or rod into a small blank sized for a roughly 4.95 mm finished ball."
    - "Cold head or otherwise form the blank into a near-spherical ball and remove flash."
    - "Heat treat if using bearing steel to reach the required hardness for rolling contact."
    - "Grind, lap, and polish the ball to the final diameter, roundness, and surface finish required by the top-axis bearing."
    - "Inspect diameter, roundness, surface finish, and visible defects before assembly into the bearing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD2_part_2.step; research/ream250_bom/ream250_bom_row_0045_2AD2__views_2x2.png"
    cited_fact_or_basis: "The STEP is one solid with a measured 4.95 x 4.95 x 4.95 mm bounding box; the contact-sheet preview shows a near-spherical part. targeted_web_search: searched \"2AD2_part_2 axis bearing top material\", \"2AD2 axis bearing top reAM250 material\", \"axis bearing top reAM250\", and \"2AD2_part_2\" found duplicate BOM text but no row-specific manufacturing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is chosen from the inferred bearing-ball function and spherical geometry, not from a row-specific drawing or process note."
    - "Precision finishing is included because a bearing rolling element needs better roundness and surface finish than a generic formed sphere."
  uncertainty_notes:
    - "The CAD evidence gives geometry but no tolerances, grade, hardness, or surface-finish requirements, so the process is a plausible route rather than a complete manufacturing specification."
kb_implications:
  - "item_granularity: simple_part - one small bearing rolling element that can be modeled as a precision steel sphere; defer unique bearing-grade, tolerance, and complete bearing assembly modeling until the top-axis bearing standard or mating races are resolved."
---

Research result for reAM250 BOM row 45.
