---
row_identity:
  item: "3G"
  cad_file: "3G_flexible_pipe_ISO_K_DN63_320SFK063-130"
  source_row_number: 118
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130"
function:
  summary: "DN 63 ISO-K stainless spring bellows / flexible vacuum connector used to join ISO-K vacuum components while tolerating axial motion, vibration, or small alignment changes."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3G_flexible_pipe_ISO_K_DN63_320SFK063-130.step; https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "BOM row 118 identifies item 3G as Pfeiffer Vacuum product 320SFK063 with raw row text '63-130'; the manifest maps it to the matching STEP file. FreeCAD measured one solid with a 130.00 x 105.13 x 105.13 mm bounding box. The row-matched Pfeiffer Vacuum Online Shop page identifies 320SFK063-130 as a DN 63 ISO-K spring bellows with length 130 mm, axial stroke +/-16 mm, tightness 1e-11 Pa m3/s, and pressure range for elastomer or metal seals. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum product route for 320SFK063_130; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches product number 320SFK063-130, Global-No. 2000042744, and the DN 63 ISO-K spring-bellows family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM text '63-130' and CAD filename suffix '320SFK063-130' identify the 130 mm DN 63 variant of product 320SFK063."
  uncertainty_notes:
    - "The compact CAD contact-sheet render was attempted but interrupted after hanging during PNG save, so visual triage relies on CAD filename, FreeCAD geometry, and the row-matched official shop product imagery rather than a local preview image."
mass:
  value_kg: 0.929
  basis: "Per-unit mass for one physical spring bellows. FreeCAD measured CAD volume 116,108.868 mm^3, equal to 1.16108868e-4 m^3; using local generic stainless_steel density 8000 kg/m^3 for the mixed 304/316L stainless construction gives 0.92887 kg, rounded to 0.929 kg. BOM quantity is 1, so the row total is also about 0.929 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3G_flexible_pipe_ISO_K_DN63_320SFK063-130.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 116,108.868 mm^3 for 3G_flexible_pipe_ISO_K_DN63_320SFK063-130.step; the row-matched Pfeiffer Vacuum Online Shop page states flange 304 and bellows 316L stainless steel; kb/materials/properties.yaml lists generic stainless_steel density as 8000 kg/m^3. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum product route for 320SFK063_130; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches product number 320SFK063-130 and Global-No. 2000042744."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical material volume of one row item."
    - "The mixed 304 flange and 316L bellows construction maps to the local generic stainless_steel density constant because both stainless grades have similar density and no split-volume CAD material regions were available."
  uncertainty_notes:
    - "If the STEP export simplifies corrugation wall thickness, welds, or hidden end features, the actual catalog mass may differ from the CAD-density estimate."
material:
  primary_material: "Stainless steel: flange 304; bellows 316L."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The row-matched Pfeiffer Vacuum Online Shop page for 320SFK063-130 states the material as stainless steel, with flange 304 and bellows 316L. Local assembly STEP material extraction for 3G_flexible_pipe_ISO_K_DN63_320SFK063-130 returned only Generic material with density 1000.0, which does not resolve material. official_alternate_route_check: original BOM URL is the Pfeiffer Vacuum product route for 320SFK063_130; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches product number 320SFK063-130 and the same DN 63 ISO-K spring-bellows row."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local STEP package lacks a real material assignment for this part; the material value depends on the row-matched official shop/catalog route."
how_to_make:
  summary: "Best current route is procurement as Pfeiffer Vacuum 320SFK063-130 or an equivalent DN 63 ISO-K stainless spring bellows, followed by inspection and installation. A local manufacturing route would make thin-wall stainless bellows, stainless ISO-K end flanges, weld them into a vacuum-tight connector, clean/passivate, and leak-test the finished assembly."
  manufacturing_steps:
    - "Procure Pfeiffer Vacuum 320SFK063-130 or an equivalent DN 63 ISO-K stainless spring bellows."
    - "Inspect the DN 63 ISO-K interfaces, 130 mm installed length, bellows condition, sealing faces, cleanliness, and freedom of motion before installation."
    - "For local manufacture, form or hydroform thin-wall 316L stainless bellows convolutions, machine or form 304 stainless ISO-K end flanges, weld/braze the bellows to the flanges, passivate/clean the assembly, and helium leak-test it for vacuum service."
    - "Install between compatible ISO-K components using the appropriate centering ring/seal and clamp hardware while respecting the +/-16 mm axial stroke limit."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3G_flexible_pipe_ISO_K_DN63_320SFK063-130.step; https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130; https://vacuum-shop.com/shop/en_US/category/2073108/product/320sfk063130/bellows-stainless-steel-flange-304-bellows-316l.html"
    cited_fact_or_basis: "BOM row 118 gives Pfeiffer Vacuum product 320SFK063; the row-matched Pfeiffer Vacuum Online Shop page identifies a DN 63 ISO-K stainless spring bellows with 130 mm length, flange 304, bellows 316L, service life 10000 cycles, and +/-16 mm axial stroke. The bellows forming, flange fabrication, welding, passivation, and leak-test route is inferred from the product geometry and stainless vacuum bellows construction."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Procurement should remain the default KB route until a local vacuum-bellows forming, welding, and leak-test workflow is modeled."
    - "The local manufacturing steps are plausible operations for a stainless ISO-K spring bellows but are not directly specified by the cited product page."
  uncertainty_notes:
    - "targeted_web_search: searched 'Pfeiffer Vacuum 320SFK063 130 flexible pipe ISO-K DN 63 material weight', '320SFK063-130 weight kg', and '320SFK063-130 datasheet mass'; results resolved row-matched product identity, dimensions, material, stroke, and vacuum service data but did not provide a row-specific manufacturing process or catalog weight."
kb_implications:
  - "item_granularity: assembly - Model as a reusable standard DN63 ISO-K stainless spring-bellows connector with flange and bellows subcomponents, not as raw hose stock or a reAM250-specific custom part."
---
