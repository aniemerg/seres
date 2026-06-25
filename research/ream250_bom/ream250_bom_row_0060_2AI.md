---
row_identity:
  item: "2AI"
  cad_file: "2AI_connection_axis"
  source_row_number: 60
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.karl-hipp.de/produkte/praezisionskugelgewindetriebe/nenndurchmesser-16mm/16-04/item/kgt-f1-16-04"
function:
  summary: "Precision connection-axis / flanged ball-screw-nut interface for the reAM250 z-axis drive: it couples the 16 mm lead-4 Karl Hipp ball-screw nut family into the local mount, with a central bore and six flange bolt holes visible in the row STEP."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.karl-hipp.de/en/products/precision-ball-screws/nominal-diameter-16mm/16-04/item/kgt-f1-16-04; research/ream250_bom/ream250_bom_row_0060_2AI__views_2x2.png"
    cited_fact_or_basis: "BOM row 60 identifies item 2AI as quantity 1, CAD file 2AI_connection_axis, manufacturer Karl Hipp GmbH, and description 'connection axis R16-05T3-DEB-401-490-'. The row-matched Karl Hipp page identifies the linked product family as Flange nut - F1 with nominal diameter 16 mm, lead 4 mm, ball diameter 2.5 mm, 4 circuits, wiper yes, Cdyn 8700 N, and Cstat 13100 N. The CAD preview shows a short flanged cylindrical part with a central bore and six bolt holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM Link URL is treated as the intended vendor-family route even though the original German path redirects to the English row-matched product page for inspection."
  uncertainty_notes:
    - "The BOM description says 'connection axis' while the vendor route is a flange-nut product family; the CAD geometry is consistent with a flanged nut/interface, so the function is locked to this row rather than generalized to the whole ball screw."
mass:
  value_kg: 0.198
  basis: "Per-unit estimate for quantity 1. FreeCAD measured one solid with volume 25229.522 mm^3, surface area 9826.902 mm^2, and bounding box about 40.00 x 40.47 x 48.00 mm. Using local generic steel density 7850 kg/m^3 from kb/materials/properties.yaml: 25229.522 mm^3 = 0.000025229522 m^3, so mass is about 0.198 kg. The BOM row quantity is 1, so the row total is also about 0.198 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AI_connection_axis.step; kb/materials/properties.yaml; https://www.schneeberger.com/fileadmin/documents/downloadcenter/01_product_catalogues_company_brochures/09_Others/Hipp_Product_catalog_EN.pdf"
    cited_fact_or_basis: "FreeCAD measured the row STEP as one solid with volume 25229.522 mm^3 and bounding box about 40.00 x 40.47 x 48.00 mm. The Hipp product catalog states standard ballscrew nut material as 100Cr6 hardened to 60 +/-2 HRC. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. bom_url_route_check: the BOM-provided Karl Hipp URL was checked first and resolved the row-matched F1 16-04 product family but did not expose material or catalog mass, so the Hipp product catalog hosted on Schneeberger was used for the material basis."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD solid volume is treated as the physical solid volume of one row item."
    - "100Cr6 bearing steel is approximated by the local generic steel density constant because the local density table has steel but no separate 100Cr6 entry."
  uncertainty_notes:
    - "No row-specific catalog mass was found; mass depends on CAD volume fidelity and the steel-density approximation."
material:
  primary_material: "100Cr6 hardened bearing steel for the ballscrew nut body; the row-matched F1 16-04 family also lists a wiper, whose material is not resolved."
  source:
    url_or_path: "https://www.schneeberger.com/fileadmin/documents/downloadcenter/01_product_catalogues_company_brochures/09_Others/Hipp_Product_catalog_EN.pdf; https://www.karl-hipp.de/en/products/precision-ball-screws/nominal-diameter-16mm/16-04/item/kgt-f1-16-04; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Hipp product catalog states standard ballscrew nut material as 100Cr6 hardened to 60 +/-2 HRC and stainless nut variant material as 1.4034 on request. The row-matched Karl Hipp F1 16-04 page lists wiper: yes. Local assembly STEP material extraction for 2AI_connection_axis returned only Generic material and density 1000.0, which does not resolve material. bom_url_route_check: the BOM-provided Karl Hipp URL matched the F1 16-04 product family but did not state material, so the product catalog was used for material. independent web search: searched 'Karl Hipp KGT-F1 16-04 material' and found the Hipp product catalog PDF with the standard nut material statement."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The standard 100Cr6 material is used because the BOM row does not indicate a stainless or special-order variant."
  uncertainty_notes:
    - "The catalog material resolves the ball-screw nut body, not detailed material splits for balls, return pieces, or wiper material."
how_to_make:
  summary: "Start from bearing-steel bar or forging, rough turn the cylindrical and flange features, drill the bolt circle and central bore, grind the ball track/thread geometry, heat treat to about 60 HRC, finish grind/lap bearing surfaces, install balls/return/wiper elements if part of the delivered nut, and inspect lead, preload/axial play, and flange interfaces"
  manufacturing_steps:
    - "For local manufacture, rough-machine 100Cr6 bearing-steel stock to the flanged cylindrical CAD envelope."
    - "Drill and finish the six flange mounting holes and central bore visible in the row STEP."
    - "Generate and grind the ball-screw nut race/thread geometry, then harden and finish-grind to precision ball-screw tolerances."
    - "Assemble recirculating balls, return path, and wiper elements if the row item represents the complete flange nut, then inspect against the screw-drive tolerance class."
  source:
    url_or_path: "https://www.karl-hipp.de/en/products/precision-ball-screws/nominal-diameter-16mm/16-04/item/kgt-f1-16-04; https://www.schneeberger.com/fileadmin/documents/downloadcenter/01_product_catalogues_company_brochures/09_Others/Hipp_Product_catalog_EN.pdf; research/ream250_bom/ream250_bom_row_0060_2AI__views_2x2.png"
    cited_fact_or_basis: "The row-matched Karl Hipp page identifies a precision F1 flange-nut family and lists F1 16-04 ordering parameters and performance data. The Hipp catalog states ball tracks are ground after heat treatment and that nut material is 100Cr6 hardened to 60 +/-2 HRC. The CAD preview shows the flanged cylindrical mounting form. targeted_web_search: searched 'Karl Hipp KGT-F1 16-04 material', 'R16-05T3-DEB-401-490 Karl Hipp', and 'Karl Hipp 100Cr6 ballscrew nut manufacturing'; results resolved product-family material and precision ball-screw catalog context but no row-specific manufacturing drawing for the custom connection axis."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route extrapolates common precision ball-screw-nut manufacturing steps from the sourced hardened, ground ball-track facts and visible flange geometry."
  uncertainty_notes:
    - "The exact custom operations for the R16-05T3-DEB-401-490 connection-axis variant are not published in the sources checked."
kb_implications:
  - "item_granularity: simple_part - model as one reusable precision ball-screw nut/connection-axis hardware item for now; keep procurement/manufacturing difficulty in the recipe/process layer rather than making it a separate machine subsystem."
---
