---
row_identity:
  item: "3P1"
  cad_file: "3P1_cyclone_separator"
  source_row_number: 131
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Cyclone separator vessel for removing entrained particulate or powder from a gas/process stream by tangential vortex flow; the CAD shows a tall conical cyclone body with side inlet, top outlet, and lower discharge."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0131_3P1__views_2x2.png; https://unitedstatessystems.com/cyclone-separator/"
    cited_fact_or_basis: "The BOM and manifest identify row 131 item 3P1 as quantity 1 of 3P1_cyclone_separator. The rendered CAD contact sheet shows a cyclone-like conical body with tangential side inlet, vertical top outlet, and bottom discharge. US Systems describes mechanical dust collector cyclones as using cyclonic airflow to separate particulates from an air stream, with particles moving to the walls and falling to a hopper while air exits upward."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row name and cyclone geometry indicate this separator handles powder/particulate carried in gas or vacuum flow in the reAM250 system."
  uncertainty_notes:
    - "The row evidence does not identify the exact particle size range, pressure drop, or capture efficiency."
mass:
  value_kg: 12.6
  basis: "FreeCAD measured CAD volume 1576521.047 mm^3 for one solid. Using the row-specific STEP material density 8000 kg/m^3 gives 1576521.047 mm^3 * 1e-9 m^3/mm^3 * 8000 kg/m^3 = 12.612 kg, rounded to 12.6 kg per unit. BOM quantity is 1, so the row total is also about 12.6 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P1_cyclone_separator.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1576521.047 mm^3, area 652239.626 mm^2, and bounding box 320.13 x 183.08 x 788.00 mm. Local STEP material extraction for product 3P1_cyclone_separator found material Stainless Steel with density 8000.0. The local material density table lists stainless_steel density 8000 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP solid volume is treated as the physical stainless steel volume of one cyclone separator."
    - "The STEP density value and the local stainless_steel density table are equivalent for this calculation."
  uncertainty_notes:
    - "The estimate depends on the supplied CAD solid including the relevant wall thickness and fittings; any omitted internal vanes, seals, clamps, or weld hardware would add mass."
material:
  primary_material: "stainless steel cyclone separator body"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 3P1_cyclone_separator returned row-specific material Stainless Steel with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata resolves the material family but not a specific stainless grade such as 304, 316, or 316L."
how_to_make:
  summary: "Model as a welded stainless cyclone vessel: procure as a custom stainless cyclone separator, or locally fabricate from rolled/conical stainless sheet and tube with welded inlet, outlet, and discharge fittings, followed by cleaning and leak/fit inspection."
  manufacturing_steps:
    - "Cut stainless sheet blanks for the cylindrical upper body and tapered cone; cut tube or formed duct stock for the tangential inlet, top outlet, and lower discharge."
    - "Roll/form the cylindrical and conical shell sections to match the CAD envelope."
    - "Fit and weld the tangential inlet, top outlet tube, bottom discharge stub, and any mounting tabs or flanges visible in the CAD."
    - "Grind/deburr internal flow edges, clean the stainless surfaces, and passivate or otherwise finish as needed for powder/vacuum service."
    - "Inspect critical connection dimensions, weld integrity, and leak tightness before installation."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0131_3P1__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P1_cyclone_separator.step; https://unitedstatessystems.com/cyclone-separator/"
    cited_fact_or_basis: "The rendered CAD contact sheet shows a tall conical cyclone shell with tangential inlet, vertical outlet, bottom discharge, and small mounting/connection features. FreeCAD measured a bounding box of 320.13 x 183.08 x 788.00 mm. US Systems states that it manufactures standard cyclone separators and custom-engineers cyclones from stainless steel, aluminum, or painted carbon steel."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local manufacturing route is inferred from the stainless material, cyclone shell geometry, and common welded vessel/sheet-metal practice."
    - "Vacuum or powder handling service requires smooth cleaned internal surfaces and leak-tight welded joints."
  uncertainty_notes:
    - "The row evidence does not state the actual supplier's production process, weld procedure, wall thickness tolerance, pressure rating, or surface finish."
    - "targeted_web_search: searched `cyclone separator stainless steel conical body tangential inlet manufacturing fabrication welding`; found general cyclone function/material/vendor manufacturing evidence but no row-specific 3P1 production specification."
kb_implications:
  - "item_granularity: simple_part - one custom stainless cyclone vessel/body with welded fittings; later KB modeling should treat it as a fabricated stainless separator body rather than a calibrated purchased module unless a vendor subsystem spec is found."
---

# reAM250 BOM Row 131 - 3P1

Research result for the leased reAM250 BOM row.
