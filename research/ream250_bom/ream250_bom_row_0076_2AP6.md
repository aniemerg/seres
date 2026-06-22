---
row_identity:
  item: 2AP6
  cad_file: 2AP6_inner_seal
  source_row_number: 76
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: "Thin square inner frame seal for the 2AP lifting/build-platform stack, likely sealing the inner perimeter between adjacent plates or guides."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP6_inner_seal.step; research/ream250_bom/ream250_bom_row_0076_2AP6__views_2x2.png"
    cited_fact_or_basis: "BOM row 76 names item 2AP6 as 2AP6_inner_seal from Mercateo; manifest maps it to a matched vendor-component STEP; CAD preview and FreeCAD geometry show a 250.00 mm x 250.00 mm x 5.00 mm thin square frame."
    evidence_basis: bom_provided
  assumptions:
    - "The 'inner_seal' row name and square frame geometry indicate a perimeter gasket/seal rather than a structural plate."
  uncertainty_notes:
    - "The CAD package does not show its mating surfaces, so the exact sealed interface within the 2AP assembly remains inferred from neighboring BOM context."
mass:
  value_kg: 0.13
  basis: "Per-unit estimate for quantity 1. FreeCAD measured one solid with volume 112482.832 mm^3 (0.000112483 m^3). Using a representative elastomer density range from local constants, about 1100-1200 kg/m^3, gives 0.124-0.135 kg; rounded planning value is 0.13 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP6_inner_seal.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured volume 112482.832 mm^3 and bounding box 250.00 mm x 250.00 mm x 5.00 mm. Local material constants list representative densities for nitrile rubber at 1100 kg/m^3 and silicone rubber at 1200 kg/m^3. targeted_web_search: queries tried: \"2AP6 inner seal Mercateo\", \"2AP6_inner_seal\", \"2AP6 seal 250 250 5\"; result: no row-specific usable vendor mass or material source found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - "The CAD solid volume is a reasonable proxy for one physical seal."
    - "The seal is modeled as a solid elastomer using an effective density near common NBR/silicone rubber values."
  uncertainty_notes:
    - "Exact material and any compression relief, adhesive, or porous/sponge construction are unresolved, so the per-unit mass is a coarse planning estimate."
material:
  primary_material: "elastomer sheet/seal material, exact compound not specified"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row identifies the item as an inner seal; assembly STEP material extraction for 2AP6_inner_seal reports only Generic with density 1000.0, which is placeholder metadata. targeted_web_search: queries tried: \"2AP6 inner seal Mercateo\", \"2AP6_inner_seal\", \"2AP6 seal 250 250 5\"; result: no row-specific usable vendor material source found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - "A thin 5 mm square frame seal in this location is more plausibly an elastomer gasket than a metal or rigid plastic spacer."
  uncertainty_notes:
    - "Material family is broad; downstream modeling should not assume a specific grade such as NBR, EPDM, silicone, or FKM without further source evidence."
how_to_make:
  summary: "Procure as a custom flat gasket, or locally cut the square frame from 5 mm elastomer sheet using knife cutting, die cutting, waterjet cutting, or similar flat-gasket cutting."
  manufacturing_steps:
    - "Select an elastomer sheet compatible with the thermal, powder, and compression environment."
    - "Cut the outer square and inner opening to the CAD profile from approximately 5 mm sheet."
    - "Deburr/clean the cut edges and inspect fit against the mating 2AP plates or guides."
  source:
    url_or_path: "https://www.stockwell.com/custom-gaskets/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP6_inner_seal.step"
    cited_fact_or_basis: "CAD shows a flat 250.00 mm x 250.00 mm x 5.00 mm square frame. Stockwell describes custom gasket manufacturing using molding, waterjet cutting, laminating, die cutting, and custom silicone gasket capability. targeted_web_search: queries tried: \"custom flat rubber gasket die cut sheet manufacturing\", \"square frame rubber gasket custom die cut sheet\"; result: generic custom flat-gasket suppliers support the route, but no 2AP6-specific manufacturing source was found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - "Cut-from-sheet manufacturing is suitable because the row geometry is a simple flat frame without molded lips or integrated hardware."
  uncertainty_notes:
    - "The exact production route may differ if the original vendor part uses a proprietary molded elastomer, foam, adhesive-backed, or high-temperature compound."
kb_implications:
  - "item_granularity: consumable - Model as a replaceable gasket/seal consumable unless later evidence shows it is part of a larger vendor module."
---
