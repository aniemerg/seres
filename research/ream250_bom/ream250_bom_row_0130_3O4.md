---
row_identity:
  item: "3O4"
  cad_file: "3O4_end_piece_320SWN063"
  source_row_number: 130
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130"
function:
  summary: "DN 63 ISO-K stainless end piece or flange-end connector for the Pfeiffer spring-bellows/flexible vacuum line, providing the rigid sealing and clamp interface at one end of the bellows assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O4_end_piece_320SWN063.step; research/ream250_bom/ream250_bom_row_0130_3O4__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "BOM row 130 identifies item 3O4 as 3O4_end_piece_320SWN063, product description 320SFK063: end piece, manufacturer Pfeiffer Vacuum, quantity 1. The manifest maps row 130 to one matched_existing vendor_component STEP file. FreeCAD measured one solid, and the rendered contact sheet shows a ring/flange-like end connector with a through bore and stepped outer profile. The Pfeiffer product route identifies 320SFK063-130 as a DN 63 ISO-K spring bellows with 130 mm length and flange connection length 30 mm. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; alternate URL https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html is the Pfeiffer Vacuum online shop route for the same product ID 320SFK063-130 and lists Pfeiffer Vacuum Components & Solutions contact details, so it is treated as row-matched BOM-side vendor evidence."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific CAD end piece is treated as one rigid end/flange component from the Pfeiffer 320SFK063/320SWN063 vacuum bellows family, not as the complete bellows assembly."
  uncertainty_notes:
    - "The BOM row and local STEP do not state which end of the larger flexible line this part occupies or whether it is welded, pressed, or otherwise attached to the bellows in the supplier assembly."
mass:
  value_kg: 0.412
  basis: "FreeCAD volume 51352.068 mm^3 = 0.0000513521 m^3. Using local kb/materials/properties.yaml density for stainless_steel_304, 8030 kg/m^3, gives 0.4123 kg, rounded to 0.412 kg per unit. BOM quantity is 1, so the row total is also about 0.412 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O4_end_piece_320SWN063.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "FreeCAD measured the row STEP as one solid with volume 51352.06790278328 mm^3. Pfeiffer's product route states the product material as stainless steel with flange 304 and bellows 316L. The local density table lists stainless_steel_304 at 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; alternate URL https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html is the Pfeiffer Vacuum online shop route for the same product ID 320SFK063-130 and lists Pfeiffer Vacuum Components & Solutions contact details, so it is treated as row-matched BOM-side vendor evidence."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row CAD volume represents one physical end piece, and the end piece corresponds to the flange/end-connector material rather than the thin 316L bellows material."
    - "Small CAD tessellation or export simplifications are ignored because the estimate only needs planning-scale mass."
  uncertainty_notes:
    - "If the CAD body includes weld lips, hidden sleeve geometry, or non-solid simplifications differently than the real supplier part, the actual mass could shift, but the stainless flange-density estimate should remain within planning tolerance."
material:
  primary_material: "stainless steel 304 / EN 1.4301 flange or end-piece material"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Pfeiffer product route for 320SFK063-130 states stainless steel construction with flange 304 and bellows 316L. Local assembly STEP material extraction for 3O4_end_piece_320SWN063 returned only Generic with density 1000.0, which is placeholder material metadata. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; alternate URL https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html is the Pfeiffer Vacuum online shop route for the same product ID 320SFK063-130 and lists Pfeiffer Vacuum Components & Solutions contact details, so it is treated as row-matched BOM-side vendor evidence."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because this row is named and shaped as an end piece rather than the corrugated bellows span, the flange 304 material applies to the row item."
  uncertainty_notes:
    - "The supplier page specifies material at the parent spring-bellows product level, not a separate standalone 3O4 end-piece line item."
how_to_make:
  summary: "Machine or form the 304 stainless ISO-K end ring/flange, finish the sealing/clamp surfaces, and weld or join it to the stainless bellows body during the larger bellows assembly"
  manufacturing_steps:
    - "Start from 304 stainless round bar, tube, or near-net ring stock sized for a DN 63 ISO-K end connector."
    - "Turn the bore, outside diameter, stepped faces, and sealing or clamp-interface features; deburr and clean for vacuum service."
    - "Join the end piece to the bellows or adjacent stainless connector body using a vacuum-compatible weld or supplier-equivalent joining process."
    - "Inspect concentricity, sealing faces, leak tightness, and compatibility with the DN 63 ISO-K clamp and centering-ring interface."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O4_end_piece_320SWN063.step; research/ream250_bom/ream250_bom_row_0130_3O4__views_2x2.png"
    cited_fact_or_basis: "Pfeiffer's product route identifies the parent item as a stainless DN 63 ISO-K spring bellows, material flange 304 and bellows 316L, with tightness 1e-11 Pa m3/s and axial stroke. CAD/rendered row evidence shows a one-piece annular end connector geometry. targeted_web_search: queries tried: '320SFK063 Pfeiffer end piece manufacturing', '320SWN063 end piece material', and 'ISO-K stainless bellows flange 304 welded end piece'; result: found row-matched product/material/interface facts but no supplier statement for the standalone end-piece manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Model this as a vacuum-clean machined or formed stainless end piece plus assembly joining to the bellows, because the standalone row is not exposed as a separately documented part"
  uncertainty_notes:
    - "The actual supplier process may use proprietary forming, spinning, or external subcomponents rather than the generic machining/forming route listed here"
kb_implications:
  - "item_granularity: simple_part - Model as one reusable stainless ISO-K bellows end/flange piece; keep the full spring bellows as an assembly or purchased module if later KB work models the complete 320SFK063 connector."
---
