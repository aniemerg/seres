---
row_identity:
  item: "2AK1"
  cad_file: "2AK1_kinematic_bar"
  source_row_number: 62
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.dold-mechatronik.de/Praezisionswelle-16mm-h6-geschliffen-und-gehaertet-ZUSCHNITT-bis-1200mm-1800-EUR-m-025-EUR-pro-Schnitt"
function:
  summary: "Hardened and ground 16 mm h6 precision round shaft used as a kinematic/linear guide bar in the reAM250 assembly; the row CAD is a simple cylindrical shaft with no holes or attached features."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0062_2AK1__views_2x2.png; https://www.dold-mechatronik.de/Praezisionswelle-16mm-h6-geschliffen-und-gehaertet-ZUSCHNITT-bis-1200mm-1800-EUR-m-025-EUR-pro-Schnitt"
    cited_fact_or_basis: "BOM row 62 identifies item 2AK1 as quantity 4 of CAD file 2AK1_kinematic_bar from Dold Mechatronik with description 'and hardened L = 400 mm'. The BOM Link URL slug identifies a 16 mm h6 precision shaft, ground and hardened, sold as cut-to-length stock. The rendered CAD contact sheet shows a straight round bar with about 16.0 mm diameter and 350.0 mm CAD length."
    evidence_basis: "bom_provided"
  assumptions:
    - "The 'kinematic_bar' CAD name and precision shaft product route indicate use as a guide/kinematic shaft rather than a powered screw or fastener."
  uncertainty_notes:
    - "The CAD geometry confirms the shaft form but does not show the mating bearings, carriages, or axis location that would narrow the exact kinematic role."
mass:
  value_kg: 0.535
  basis: "Per-unit CAD-derived installed-part mass for one shaft. FreeCAD measured one solid with volume 69166.877 mm^3, surface area 18613.344 mm^2, and bounding box about 16.00 x 350.00 x 16.00 mm. Local assembly STEP material extraction reported Steel, Alloy with density 7730 kg/m^3. Calculation: 69166.877 mm^3 = 0.000069166877 m^3; 0.000069166877 m^3 * 7730 kg/m^3 = 0.535 kg per shaft. BOM quantity is 4, so the CAD-installed row total is about 2.14 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AK1_kinematic_bar.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured the row STEP as one solid with volume 69166.877 mm^3 and bounding box about 16.00 x 350.00 x 16.00 mm. The local assembly STEP material extractor returned material Steel, Alloy with density 7730.0 for product 2AK1_kinematic_bar."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row STEP solid is treated as the physical installed shaft volume for one BOM-row item."
    - "The STEP material density is treated as kg/m^3-like density, consistent with the reAM250 material extractor note."
  uncertainty_notes:
    - "The BOM text says L = 400 mm while the supplied row CAD measures about 350 mm long; if one physical shaft is actually a 400 mm purchased cut, the mass would be about 0.61 kg at the same diameter and density before any trimming."
material:
  primary_material: "alloy steel precision shaft material, hardened and ground"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.dold-mechatronik.de/Praezisionswelle-16mm-h6-geschliffen-und-gehaertet-ZUSCHNITT-bis-1200mm-1800-EUR-m-025-EUR-pro-Schnitt"
    cited_fact_or_basis: "The local assembly STEP material extractor returned material Steel, Alloy with density 7730.0 for product 2AK1_kinematic_bar. The BOM-provided Dold Mechatronik URL identifies the row route as a 16 mm h6 precision shaft that is ground and hardened."
    evidence_basis: "bom_provided"
  assumptions:
    - "No more specific steel grade is assigned because the row-specific STEP metadata and BOM URL route support alloy steel and hardened/ground finish but not an exact grade."
  uncertainty_notes:
    - "Exact shaft steel grade, case depth, hardness tolerance, and coating are not resolved by the row evidence."
how_to_make:
  summary: "Near-term route is to procure Dold Mechatronik 16 mm h6 hardened and ground precision shaft stock cut to the required length. A plausible local route is alloy-steel round bar preparation, straightening, heat treatment or case hardening, cylindrical/centerless grinding to h6 tolerance, cut-to-length, deburring, and inspection for diameter, straightness, surface finish, and end length."
  manufacturing_steps:
    - "Procure 16 mm h6 hardened and ground precision shaft stock from the BOM-provided Dold Mechatronik cut-to-length product route."
    - "For local manufacture, start from suitable alloy-steel round bar stock sized for finish grinding."
    - "Straighten, heat treat or case harden as required for a wear-resistant guide shaft."
    - "Cylindrically or centerlessly grind the outside diameter to the h6 precision-shaft tolerance and required surface finish."
    - "Cut to final installed length, deburr/chamfer the ends, clean, and inspect diameter, straightness, roundness, and length before assembly."
  source:
    url_or_path: "https://www.dold-mechatronik.de/Praezisionswelle-16mm-h6-geschliffen-und-gehaertet-ZUSCHNITT-bis-1200mm-1800-EUR-m-025-EUR-pro-Schnitt; research/ream250_bom/ream250_bom_row_0062_2AK1__views_2x2.png"
    cited_fact_or_basis: "The BOM-provided Dold Mechatronik URL identifies a 16 mm h6 precision shaft, ground and hardened, sold as cut-to-length stock. The rendered row CAD preview shows a plain round shaft. targeted_web_search: searched 'Dold Mechatronik Praezisionswelle 16mm h6 geschliffen gehaertet Zuschnitt', '16 mm h6 hardened ground precision shaft manufacturing', and 'DOLD precision shaft 16mm h6 material'; results supported the precision-shaft product identity but did not provide a row-specific Dold manufacturing process or exact material grade."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Procurement is the preferred current KB route because the row is standard precision shaft stock, not a machine-specific multi-part subsystem."
    - "The local manufacturing route is inferred from the sourced hardened/ground h6 shaft identity and simple cylindrical CAD geometry."
  uncertainty_notes:
    - "The actual Dold supplier process, heat-treatment specification, final hardness, and exact grinding/straightening controls are not published in the row evidence."
kb_implications:
  - "item_granularity: raw_material_or_stock - model as reusable 16 mm hardened/ground precision shaft stock or cut-to-length rod; keep length variation in BOM/recipe quantities rather than creating a machine-specific custom part."
---
