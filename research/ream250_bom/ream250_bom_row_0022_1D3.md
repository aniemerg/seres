---
row_identity:
  item: "1D3"
  cad_file: "1D3_part_3"
  source_row_number: 22
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Door hinge component for the reAM250 chamber door area; the CAD shows one hinge-side machined strap/leaf with two cylindrical knuckle barrels and pin bores, used with the neighboring 1D1/1D2 hinge rows and adapter hardware to let the door swing while carrying door load."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D3_part_3.step; research/ream250_bom/ream250_bom_row_0022_1D3__views_2x2.png"
    cited_fact_or_basis: "BOM row 22 identifies item 1D3, quantity 2, CAD file 1D3_part_3, description 'door hinge', manufacturer Pfeiffer Vacuum. Manifest row 22 maps that row to gold_export/parts/1D3_part_3.step as a matched_existing vendor_component. FreeCAD measured one solid with an 80.00 x 100.00 x 20.00 mm bounding box; the rendered contact sheet shows a hinge leaf/strap with two cylindrical hinge knuckles and pin bores."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The row is one exported hinge component, not the full hinge assembly; neighboring rows 1D1 and 1D2 are also Pfeiffer Vacuum door-hinge rows and likely complete the hinge set."
mass:
  value_kg: 1.02
  basis: "Per unit, not multiplied by BOM quantity. FreeCAD volume is 126541.504 mm^3, equal to 0.000126541504 m^3. Using the local kb/materials/properties.yaml stainless_steel_304 density constant of 8030 kg/m^3 gives 0.000126541504 * 8030 = 1.016 kg, rounded to 1.02 kg per hinge component; BOM quantity 2 implies about 2.03 kg row total."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D3_part_3.step; kb/materials/properties.yaml; https://www.pfeiffervacuum.com/za/en/knowledge/vacuum-technology/knowledge-book/3-mechanical-components-in-vacuum/3.2-materials.html; https://www.shop.buschgroup.com/global/en/products/820KHH0500_750/; https://vacuum-shop.com/shop/en_US/category/2073323/product/820khh0600900/high-vacuum-chamber-horizontal-khh.html"
    cited_fact_or_basis: "FreeCAD measured 126541.504 mm^3 for 1D3_part_3. kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3. Targeted vendor/context searches for 'Pfeiffer Vacuum door hinge 1D3_part_3 reAM250', 'Pfeiffer Vacuum door hinge material stainless steel vacuum chamber hinge', and 'Pfeiffer Vacuum door hinge catalog material weight' found Pfeiffer vacuum-chamber context and KHH chamber pages, but no row-specific hinge mass or material datasheet; targeted_web_search: no row-specific 1D3/Pfeiffer hinge weight source found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Mass calculation assumes the exported solid volume represents one physical hinge component and uses stainless steel 304 density as the planning constant."
    - "A generic steel density would produce about 0.99 kg, so the stainless assumption changes the estimate only by a few percent."
  uncertainty_notes:
    - "STEP assembly material extraction for 1D3_part_3 returned only Generic with density 1000.0, so it was treated as placeholder metadata and not used for mass."
    - "If the actual hinge is aluminum or a multi-material purchased hinge, the mass could differ materially; no row-specific catalog weight was found."
material:
  primary_material: "stainless steel or corrosion-resistant steel hinge material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.pfeiffervacuum.com/za/en/knowledge/vacuum-technology/knowledge-book/3-mechanical-components-in-vacuum/3.2-materials.html; https://vacuum-shop.com/shop/en_US/category/2073323/product/820khh0600900/high-vacuum-chamber-horizontal-khh.html"
    cited_fact_or_basis: "BOM row 22 gives manufacturer Pfeiffer Vacuum and description 'door hinge' but no material. Local STEP material extraction for 1D3_part_3 returned Generic only. Pfeiffer's vacuum-materials guidance states stainless steel is the preferred chamber/component material family in vacuum technology, and a Pfeiffer KHH chamber product page describes a stainless steel door with hinges and states chamber body and door material as stainless steel 304 (1.4301). targeted_web_search: row-specific queries for 1D3_part_3/Pfeiffer door hinge material did not find an exact hinge material listing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For KB planning, model this hinge component as a stainless/corrosion-resistant steel mechanical part unless later vendor documentation identifies a different alloy."
  uncertainty_notes:
    - "The cited Pfeiffer chamber pages support the surrounding vacuum-chamber material context, not a row-specific hinge alloy."
    - "The exact grade is unresolved; do not encode this as a sourced 304 stainless part without better evidence."
how_to_make:
  summary: "Best near-term route is procurement as a Pfeiffer/vacuum-chamber hinge component. A local manufacturing fallback is to machine or fabricate the hinge leaf from corrosion-resistant steel stock, form/machine the two hinge knuckles, drill/ream the pin bores, deburr and passivate or clean for vacuum-compatible service, then assemble with the mating hinge leaves and pin."
  manufacturing_steps:
    - "Procure as a matched Pfeiffer Vacuum door-hinge component when vendor replacement parts are available."
    - "Fallback: cut stainless or corrosion-resistant steel bar/plate stock to the hinge-leaf blank and rough profile."
    - "Mill the tapered strap/leaf features and machine the two cylindrical knuckle barrels or fabricate them as welded/brazed-on barrels."
    - "Drill and ream coaxial pin bores through the barrels, then deburr bearing edges."
    - "Clean/passivate for vacuum-compatible use and assemble with the mating hinge components and hinge pin."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1D3_part_3.step; research/ream250_bom/ream250_bom_row_0022_1D3__views_2x2.png; https://www.pfeiffervacuum.com/global/en/service/genuine-parts/; https://www.pfeiffervacuum.com/za/en/knowledge/vacuum-technology/knowledge-book/3-mechanical-components-in-vacuum/3.2-materials.html"
    cited_fact_or_basis: "CAD and preview show the geometry to be a machined/fabricated hinge leaf with cylindrical knuckles and holes. Pfeiffer's genuine-parts page supports procurement as manufacturer-matched spare parts, while Pfeiffer vacuum-material guidance supports stainless steel as a vacuum-compatible component material family. targeted_web_search: no row-specific process sheet for 1D3_part_3 was found, so detailed machining/fabrication operations are inferred from geometry."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local fabrication fallback prioritizes geometry and vacuum-compatible material behavior over exact duplication of Pfeiffer's supplier process."
  uncertainty_notes:
    - "The actual vendor component may be cast, forged, welded, or machined differently; no row-specific manufacturing drawing was found."
kb_implications:
  - "item_granularity: simple_part - Treat 1D3 as a reusable hinge leaf/knuckle component rather than a full purchased module; the full door-hinge assembly can later be modeled from rows 1D1, 1D2, 1D3, pins/fasteners, and adapter row 1E if needed."
---

