---
row_identity:
  item: "1D2"
  cad_file: "1D2_part_2"
  source_row_number: 21
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Compact door-hinge leaf or knuckle component for a Pfeiffer Vacuum door hinge set in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D2_part_2.step; research/ream250_bom/ream250_bom_row_0021_1D2__views_2x2.png"
    cited_fact_or_basis: "BOM row 21 identifies item 1D2, quantity 2, CAD file 1D2_part_2, description door hinge, manufacturer Pfeiffer Vacuum; the manifest maps the row to gold_export/parts/1D2_part_2.step as matched_existing vendor_component; FreeCAD measured one solid with a 46.00 x 50.00 x 16.00 mm bounding box; the rendered preview shows a rectangular hinge-leaf-like web with two coaxial barrel/knuckle features and through bores."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD part is interpreted as one physical piece of the door hinge rather than the complete hinge assembly because adjacent BOM rows 1D1 and 1D3 are also door-hinge parts and this row's CAD is a single compact solid."
  uncertainty_notes:
    - "The row does not state which exact door or chamber product this hinge belongs to, so the function is limited to hinge hardware within the reAM250 door/chamber context."
mass:
  value_kg: 0.246
  basis: "FreeCAD volume 30583.002 mm^3 converted to 3.0583002e-5 m^3 and multiplied by the local stainless_steel_304 density of 8030 kg/m^3, yielding about 0.246 kg per 1D2 part."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D2_part_2.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073323/product/820khh0600900/high-vacuum-chamber-horizontal-khh.html; https://www.pfeiffervacuum.com/ca/en/knowledge/vacuum-technology/knowledge-book/3-mechanical-components-in-vacuum/3.2-materials.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 30583.002 mm^3, area 8824.811 mm^2, and bounding box 46.00 x 50.00 x 16.00 mm; kb/materials/properties.yaml lists stainless_steel_304 density 8030 kg/m^3; a Pfeiffer KHH chamber page says a stainless steel door has hinges and quick clamps and lists chamber body and door material as stainless steel 304/1.4301; a Pfeiffer vacuum-materials page says stainless steel 1.4301 is suitable for vacuum applications. targeted_web_search: searched \"Pfeiffer Vacuum door hinge material\", \"Pfeiffer Vacuum door hinge reAM250 1D2_part_2\", \"1D2_part_2 door hinge Pfeiffer Vacuum\", and \"reAM250 door hinge Pfeiffer Vacuum\"; found duplicate BOM text and general Pfeiffer vacuum-chamber stainless context, but no row-specific hinge mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The measured STEP solid is treated as the complete per-unit geometry for one 1D2 hinge component."
    - "Stainless steel 304/1.4301 density is used as a representative density because the part is inferred to be vacuum-compatible hinge hardware near a stainless chamber door."
  uncertainty_notes:
    - "Mass depends on the inferred stainless material family; if the part is aluminum, generic steel, or another alloy, the volume-based mass would change."
material:
  primary_material: "stainless steel family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0021_1D2__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073323/product/820khh0600900/high-vacuum-chamber-horizontal-khh.html; https://www.pfeiffervacuum.com/ca/en/knowledge/vacuum-technology/knowledge-book/3-mechanical-components-in-vacuum/3.2-materials.html"
    cited_fact_or_basis: "BOM row 21 identifies the row as a Pfeiffer Vacuum door hinge; local STEP material extraction for product 1D2_part_2 reports only Generic with density 1000.0; the rendered preview shows a metal hinge-leaf/knuckle shape; a Pfeiffer KHH chamber page says a stainless steel door has hinges and quick clamps and lists chamber body and door material as stainless steel 304/1.4301; a Pfeiffer vacuum-materials page says stainless steel 1.4301 is suitable for vacuum applications. targeted_web_search: searched \"Pfeiffer Vacuum door hinge material\", \"Pfeiffer Vacuum door hinge reAM250 1D2_part_2\", \"1D2_part_2 door hinge Pfeiffer Vacuum\", and \"reAM250 door hinge Pfeiffer Vacuum\"; found duplicate BOM text and general Pfeiffer vacuum-chamber stainless context, but no row-specific hinge material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A stainless steel family material is used as the broad KB material hypothesis because vacuum chamber door hardware typically needs corrosion-resistant, vacuum-compatible metal and the closest Pfeiffer chamber context uses stainless door construction."
  uncertainty_notes:
    - "No BOM field, CAD material metadata, product ID, or row-specific vendor page directly states the hinge material, so the exact stainless grade is not resolved."
how_to_make:
  summary: "Model as a simple machined stainless hinge component: cut or machine the hinge web and coaxial barrel features from stainless stock, finish the through bores/pin interface, deburr, clean, and inspect for door-hinge fit."
  manufacturing_steps:
    - "Start with stainless steel bar, block, or near-net hinge extrusion stock sized for a roughly 46 x 50 x 16 mm component."
    - "Mill or otherwise form the flat web/leaf faces and outside profile."
    - "Machine the two coaxial barrel or knuckle features and bore/ream the hinge-pin holes to alignment."
    - "Deburr edges and bore mouths, then clean for vacuum-adjacent service."
    - "Inspect hinge-pin fit, coaxiality, mounting/leaf geometry, and surface condition before assembly with the mating hinge pieces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D2_part_2.step; research/ream250_bom/ream250_bom_row_0021_1D2__views_2x2.png"
    cited_fact_or_basis: "The STEP/contact sheet shows one compact solid with a rectangular web, two coaxial cylindrical hinge-barrel features, through bores, and a measured 46.00 x 50.00 x 16.00 mm bounding box. targeted_web_search: searched \"Pfeiffer Vacuum door hinge material\", \"Pfeiffer Vacuum door hinge reAM250 1D2_part_2\", \"1D2_part_2 door hinge Pfeiffer Vacuum\", and \"reAM250 door hinge Pfeiffer Vacuum\"; found duplicate BOM text and general Pfeiffer vacuum-chamber stainless context, but no row-specific manufacturing process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the simple metal hinge geometry and need for aligned hinge-pin bores, not from a Pfeiffer factory process sheet."
    - "For KB modeling, this can be represented as machining from stainless stock rather than a purchased proprietary hinge subassembly."
  uncertainty_notes:
    - "The CAD gives geometry but not tolerances, surface finish, heat treatment, or whether Pfeiffer used machining, casting, extrusion, or a vendor-specific hinge blank."
kb_implications:
  - "item_granularity: simple_part - one hinge leaf/knuckle component that can be modeled as a machined stainless part; defer complete hinge assembly modeling to the adjacent 1D1/1D3 rows and mating pin/fastener context."
---

Research result for reAM250 BOM row 21.
