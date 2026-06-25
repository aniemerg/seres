---
row_identity:
  item: "3N1"
  cad_file: "3N1_curvature_320SWN063"
  source_row_number: 125
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130"
function:
  summary: "Curved/flexible bellows body for a Pfeiffer 320SFK063-130 DN 63 ISO-K spring bellows, providing a compliant leak-tight vacuum path between ISO-K end connections."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "BOM row 125 identifies item 3N1 as 320SFK063: curvature from Pfeiffer Vacuum. Manifest row 125 maps it to 3N1_curvature_320SWN063.step. The official Pfeiffer Vacuum Online Shop page identifies 320SFK063-130 as a DN 63 ISO-K spring bellows with length 130 mm, axial stroke +/- 16 mm, tightness 1e-11 Pa m3/s, and pressure range down to 1e-8 hPa. official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; the accessible official alternate route was vacuum-shop.com for the same order number 320SFK063-130 / Global-No. 2000042744, with Pfeiffer Vacuum Components & Solutions contact/copyright and matching product data."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM subname 'curvature' denotes the bellows/curved compliant body rather than the two separate end-piece rows."
  uncertainty_notes:
    - "The CAD contact-sheet renderer timed out, so visible shape triage is based on the STEP filename, BOM row, FreeCAD geometry, and official product family rather than an inspected preview image."
mass:
  value_kg: 0.59
  basis: "Per unit for quantity 1. FreeCAD measured one solid with volume 73775.057 mm3 and bounding box 459.42 x 88.49 x 120.67 mm. Using stainless steel density 8000 kg/m3 from kb/materials/properties.yaml gives 73775.057e-9 m3 * 8000 kg/m3 = 0.590 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3N1_curvature_320SWN063.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 73775.05654310233 mm3, area 743254.7143541607 mm2, and bounding box 459.41688342161996 x 88.49322384838703 x 120.67291873706048 mm. The official product page states stainless steel construction with 304 flange and 316L bellows for DN 63. Local properties table gives stainless_steel density 8000 kg/m3. official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; vacuum-shop.com official alternate matched order number 320SFK063-130 / Global-No. 2000042744 and supplied the product material family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific CAD solid volume represents the one physical curvature/bellows body counted by this BOM row."
    - "The generic stainless_steel density is an adequate calculation constant for the 316L bellows body at this planning precision."
  uncertainty_notes:
    - "If the STEP export represents a deformed or path-expanded bellows subshape instead of true manufactured metal volume, the mass may be biased; no catalog mass for the subpart was found in BOM-side evidence."
material:
  primary_material: "Stainless steel; official full product material split is 316L bellows with 304 stainless flanges."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The official product page states material as stainless steel with flange 304 and bellows 316L for DN 63 to DN 100 and DN 320. Local STEP material extraction for product 3N1_curvature_320SWN063 returned only Generic with density 1000.0, which is a placeholder and was not used to resolve material. official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; the accessible official alternate route was the Pfeiffer Vacuum Online Shop page for the same order number 320SFK063-130 / Global-No. 2000042744."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because this row is named 'curvature' and companion rows cover end pieces, the row material follows the official bellows material rather than the flange material."
  uncertainty_notes:
    - "The row-specific STEP material metadata is placeholder-only, so the material assignment depends on matching the BOM product family and subpart name to the official product material split."
how_to_make:
  summary: "Thin-wall stainless bellows forming followed by trimming, end preparation, welding to end pieces, and helium leak/pressure testing"
  manufacturing_steps:
    - "Start from thin 316L stainless tube or sheet formed into tube stock."
    - "Form corrugations by hydroforming, roll forming, or equivalent bellows-forming tooling to the DN 63 geometry."
    - "Trim and prepare ends for welding or joining to the separate ISO-K end-piece rows."
    - "Clean for vacuum service, weld/assemble with end pieces in the full spring-bellows assembly, then leak test and inspect stroke/compliance."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3N1_curvature_320SWN063.step"
    cited_fact_or_basis: "The official product page identifies a purchasable stainless DN 63 ISO-K spring bellows with tightness, pressure range, axial stroke, dimensions, and downloadable CAD. The STEP geometry measured by FreeCAD gives the row-specific solid volume and bounding box. targeted_web_search: searched '320SFK063-130 Pfeiffer Spring bellows', '320SFK063-130 material', and '320SFK063-130 weight'; results found official product/material/dimension data but no source stating the detailed factory manufacturing route for the bellows subpart."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route follows common stainless vacuum bellows production practice inferred from the official product type and CAD geometry."
  uncertainty_notes:
    - "Detailed process parameters such as wall thickness, forming pressure, heat treatment, weld procedure, and acceptance-test limits are not provided by the sources checked."
kb_implications:
  - "item_granularity: simple_part - Model this row as the bellows/curved body subpart of a standard DN 63 ISO-K spring bellows; the full 320SFK063-130 product may later be represented as an assembly with two end-piece rows."
---
