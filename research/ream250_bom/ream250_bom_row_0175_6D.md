---
row_identity:
  item: "6D"
  cad_file: "6D_rod_sleeve"
  source_row_number: 175
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small stainless rod sleeve or bushing, likely used as a spacer, guide, or wear sleeve around a rod in the reAM250 mechanism."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6D_rod_sleeve.step; research/ream250_bom/ream250_bom_row_0175_6D__views_2x2.png"
    cited_fact_or_basis: "BOM row 175 names item 6D as 6D_rod_sleeve with quantity 1; FreeCAD measured one solid with about 815.309 mm^3 volume and a 10.91 x 12.00 x 14.00 mm bounding box; rendered views show a short cylindrical sleeve-like part with a larger collar/head. targeted_web_search: queries 'stainless steel rod sleeve bushing function manufacturing' and 'rod sleeve bushing stainless steel sleeve bearing function' found generic sleeve/bushing descriptions, not a row-specific source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD part name is interpreted literally: rod_sleeve is treated as a sleeve/bushing associated with a rod, not as an unrelated cover or cap."
  uncertainty_notes:
    - "The parent assembly context was not provided in the leased row, so the exact interface and load case remain uncertain."
mass:
  value_kg: 0.00652
  basis: "Per-unit mass for quantity 1. CAD volume 815.308552 mm^3 = 8.15308552e-7 m^3; assembly STEP material metadata gives Stainless Steel density 8000 kg/m^3, yielding 0.006522 kg per sleeve."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6D_rod_sleeve.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD shape read measured one solid, volume 815.309 mm^3, area 670.633 mm^2, and bounding box 10.91 x 12.00 x 14.00 mm; local assembly STEP material extraction matched product 6D_rod_sleeve to Stainless Steel with density 8000.0 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The matched CAD solid represents one physical item for BOM quantity 1."
    - "The STEP material density is applied uniformly to the measured CAD volume."
  uncertainty_notes:
    - "Mass does not include any separate coating, lubricant, or press-fit allowance that may exist outside the exported part solid."
material:
  primary_material: "Stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 6D_rod_sleeve returned material Stainless Steel and density 8000.0 in the reAM250 export's kg/m^3-like density convention."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata does not identify a stainless grade such as 304, 316, or hardened stainless."
how_to_make:
  summary: "Make as a small precision-machined stainless sleeve from bar stock"
  manufacturing_steps:
    - "Cut stainless bar or rod stock slightly oversize."
    - "Turn the outside diameter, collar/head, and end faces on a lathe."
    - "Drill and bore or ream the internal passage if the sleeve is hollow in the mating assembly."
    - "Add flats/chamfers or head features visible in CAD, deburr, clean, and inspect critical diameters."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6D_rod_sleeve.step; https://gjl8888.en.made-in-china.com/product/IXBxfvSKbiYm/China-Custom-Made-CNC-Turning-Stainless-Steel-Shaft-Sleeve-Bushing.html"
    cited_fact_or_basis: "CAD evidence shows a small sleeve-like stainless component with turned cylindrical features; the searched vendor example shows custom stainless shaft sleeve bushings are commonly made with CNC turning. targeted_web_search: query 'stainless steel rod sleeve bushing function manufacturing' found generic custom CNC-turned stainless sleeve/bushing routes, but no row-specific manufacturing drawing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Lathe turning is the most plausible route because the part is mostly rotationally symmetric and only about 14 mm tall."
    - "Secondary machining is allowed for the non-axisymmetric flats or local features visible in the rendered preview."
  uncertainty_notes:
    - "No tolerances, surface finish, heat treatment, or internal bore specification were available in the BOM row or CAD evidence."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable small stainless machined sleeve/bushing rather than a machine-specific assembly or purchased module."
---

