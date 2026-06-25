---
row_identity:
  item: "17AL"
  cad_file: "17AL_sheet_side"
  source_row_number: 240
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Side sheet/panel for the reAM250 chamber/enclosure group, used as one of two flat side skins or covers around the machine body."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AL_sheet_side.step; research/ream250_bom/ream250_bom_row_0240_17AL__views_2x2.png"
    cited_fact_or_basis: "BOM row 240 identifies item 17AL as quantity 2 with CAD file 17AL_sheet_side. The manifest maps the row to gold_export/parts/17AL_sheet_side.step. FreeCAD measured one solid with bounding box 2.00 x 468.70 x 457.50 mm, and the rendered preview shows a plain thin rectangular sheet."
    evidence_basis: "bom_provided"
  assumptions:
    - "The sheet_side CAD name describes the installed function because no separate product description, vendor page, or drawing note is present."
  uncertainty_notes:
    - "The isolated part file does not show how the side sheet is attached or whether it is removable, fixed, or paired left/right by orientation."
mass:
  value_kg: 3.367
  basis: "Per unit for one physical side sheet; BOM quantity is 2, so the row total would be about 6.73 kg using this estimate. FreeCAD measured volume 428860.500 mm^3, equivalent to 0.0004288605 m^3. Planning estimate uses generic steel density 7850 kg/m^3 from kb/materials/properties.yaml: 0.0004288605 m^3 * 7850 kg/m^3 = 3.367 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AL_sheet_side.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 428860.500 mm^3, area 432565.300 mm^2, and bounding box 2.00 x 468.70 x 457.50 mm. kb/materials/properties.yaml lists steel density as 7850 kg/m^3 and aluminum density as 2700 kg/m^3. targeted_web_search: searched \"17AL_sheet_side material\", \"reAM250 17AL sheet side material\", \"17AL_sheet_side reAM250\", and \"reAM250 sheet_side\"; results found duplicate/public BOM text but no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP volume represents one physical 17AL side sheet."
    - "Generic steel density is used as a conservative sheet-metal enclosure planning assumption because the row material is unresolved."
  uncertainty_notes:
    - "If the panel is aluminum sheet instead of steel, the same CAD volume would imply about 1.158 kg per unit and about 2.32 kg for the quantity-2 row."
    - "Local assembly STEP material extraction for 17AL_sheet_side returned only placeholder material Generic with density 1000.0, so it was not used as material evidence."
material:
  primary_material: "unknown sheet metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AL_sheet_side.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 240 and the manifest provide no manufacturer, product ID, material family, material grade, or link URL. Local assembly STEP material extraction for 17AL_sheet_side returned material Generic with density 1000.0. The CAD geometry is a 2.00 mm thick sheet-like panel. targeted_web_search: searched \"17AL_sheet_side material\", \"reAM250 17AL sheet side material\", and \"reAM250 sheet_side material\"; results did not provide row-specific material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Treat as metal sheet rather than polymer because the row is a rigid 2 mm chamber/enclosure side panel in a metal AM machine."
  uncertainty_notes:
    - "Specific alloy, coating, surface treatment, and whether the sheet is steel, stainless steel, or aluminum remain unresolved."
how_to_make:
  summary: "Fabricate as a custom flat sheet-metal side panel: cut a 2 mm rectangular blank to the CAD envelope, deburr the edges, apply any required finish, and install as one of the chamber/enclosure side sheets."
  manufacturing_steps:
    - "Prepare 2 mm sheet-metal stock large enough for the 468.70 x 457.50 mm face"
    - "Cut the rectangular panel by shear, laser, waterjet, CNC router, or saw from sheet stock."
    - "Deburr and inspect edges for flatness and fit."
    - "Apply coating, brushing, passivation, or other finish if required by the final enclosure material."
    - "Install two panels in the chamber/enclosure assembly as indicated by the BOM quantity."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AL_sheet_side.step; research/ream250_bom/ream250_bom_row_0240_17AL__views_2x2.png"
    cited_fact_or_basis: "The STEP/preview show one flat 2.00 mm thick rectangular sheet solid with no visible bends, holes, slots, flanges, attached hardware, calibrated module features, or formed geometry. targeted_web_search: searched \"17AL_sheet_side manufacturing\", \"reAM250 sheet side drawing\", and \"reAM250 side sheet material\" results did not provide row-specific fabrication instructions."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Flat-sheet cutting is sufficient because the CAD bounding box thickness is 2.00 mm and the preview shows a plain rectangular panel."
  uncertainty_notes:
    - "Mounting, sealing, or fastener details may be represented by neighboring parts or assembly constraints rather than by this isolated sheet STEP."
kb_implications:
  - "item_granularity: simple_part - Model as one custom cut sheet-metal side panel; use a generic sheet cutting/deburring process and account for quantity 2 in the BOM rather than creating a purchased module."
---
