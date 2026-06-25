---
row_identity:
  item: "1A41"
  cad_file: "1A41_SM2A53-Step"
  source_row_number: 5
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.thorlabs.com/thorproduct.cfm?partnumber=SM2A53"
function:
  summary: "Thorlabs SM2A53 optical thread adapter ring, adapting external M52 x 0.75 threads to internal SM2 2.035-40 threads for mounting SM2-threaded optics or tube components into an M52 interface."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.thorlabs.com/item/SM2A53; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A41_SM2A53-Step.step; research/ream250_bom/ream250_bom_row_0005_1A41__views_2x2.png"
    cited_fact_or_basis: "BOM row 5 identifies item 1A41 as Thorlabs SM2A53 with description 'M52x0,75; Internal SM2 Threads' and the BOM link redirects to the Thorlabs SM2A53 item page. FreeCAD measured one ring-shaped solid with a 55.88 x 55.88 x 7.37 mm bounding box, and the rendered preview shows a thin threaded adapter ring."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents one physical SM2A53 adapter ring, consistent with BOM quantity 1 and one matched CAD solid."
  uncertainty_notes: []
mass:
  value_kg: 0.02
  basis: "Per unit. BOM quantity is 1, so the row total is also about 0.02 kg. The row-matched SM2A53 drawing lists approximate weight 0.02 kg. FreeCAD measured 1 solid, volume 2573.818 mm^3, area 3560.408 mm^2, and bounding box 55.88 x 55.88 x 7.37 mm; using local aluminum density 2700 kg/m^3 on that CAD volume would give about 0.00695 kg, so the drawing weight is retained as the better product-level mass estimate."
  source:
    url_or_path: "https://www.oxxius.ru/upload/iblock/dbe/j38qr4oay7zb9p73yap8tcsa50z0acsq/24386_E0W.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A41_SM2A53-Step.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "The SM2A53 drawing names the item 'SM2 to M52 x 0.75 adapter' and lists approximate weight 0.02 kg. FreeCAD measured the row STEP as one solid with volume 2573.818 mm^3 and a 55.88 x 55.88 x 7.37 mm bounding box. The local density table lists aluminum density 2700 kg/m^3. bom_url_route_check: the BOM-provided Thorlabs SM2A53 route was checked and resolves row identity and package-weight context, but the accessible page text did not expose the drawing material/approx-weight fields used for this mass value; the cited drawing is row-matched to SM2A53 and carries Thorlabs drawing/title text."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The drawing approximate weight is treated as the best product-level per-item mass despite the simplified local CAD volume yielding a lower aluminum-density estimate."
  uncertainty_notes:
    - "The Thorlabs item page search snippet reports package weight 0.01 kg each while the drawing reports approximate item weight 0.02 kg; downstream mass rollups should treat 0.02 kg as a rounded catalog/drawing value, not a weighed measurement."
material:
  primary_material: "anodized aluminum"
  source:
    url_or_path: "https://www.oxxius.ru/upload/iblock/dbe/j38qr4oay7zb9p73yap8tcsa50z0acsq/24386_E0W.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The row-matched SM2A53 drawing lists material as anodized aluminum. The local assembly STEP material extractor matched 1A41_SM2A53-Step but returned only Generic with density 1000.0, which is placeholder metadata under the task acceptance rules. bom_url_route_check: the BOM-provided Thorlabs SM2A53 route was checked and resolves product identity, but the accessible page text did not expose the material field; the cited drawing is row-matched to SM2A53 and carries Thorlabs drawing/title text."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "The source does not state the aluminum alloy grade or anodize type/thickness."
how_to_make:
  summary: "Machine an aluminum adapter ring, cut the external M52 x 0.75 and internal SM2 threads, knurl or texture the outside grip surface, anodize, and inspect thread fit and clear aperture"
  manufacturing_steps:
    - "Start from aluminum round bar or tube stock large enough for the 55.9 mm outside diameter."
    - "Turn the ring faces and bore on a lathe, leaving the approximately 7.4 mm axial thickness shown by the CAD and drawing."
    - "Cut the M52 x 0.75 external thread and internal SM2 2.035-40 thread; add the visible knurled or textured outer grip surface."
    - "Deburr and clean the optical-thread interfaces, anodize the aluminum, and inspect thread engagement, clear aperture, and overall thickness."
  source:
    url_or_path: "https://www.thorlabs.com/item/SM2A53; https://www.oxxius.ru/upload/iblock/dbe/j38qr4oay7zb9p73yap8tcsa50z0acsq/24386_E0W.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A41_SM2A53-Step.step; research/ream250_bom/ream250_bom_row_0005_1A41__views_2x2.png"
    cited_fact_or_basis: "The BOM-linked Thorlabs route identifies SM2A53 as the row product. The SM2A53 drawing and CAD/preview show a thin adapter ring with external M52 x 0.75 threads, internal SM2 threads, anodized aluminum material, 55.9 mm outside diameter, 48.3 mm clear aperture, and about 7.4 mm thickness. targeted_web_search: searched 'SM2A53 Thorlabs material weight', 'SM2A53 M52x0.75 internal SM2 threads material', and 'Thorlabs SM2A53 drawing anodized aluminum'; results found row-matched product/drawing facts but no row-specific manufacturing-process specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the ring geometry, aluminum material, standard optical thread forms, and visible textured grip surface."
    - "Anodizing is included because the row-matched drawing states anodized aluminum."
  uncertainty_notes:
    - "The sources do not state Thorlabs' actual production route, tooling, alloy, anodize class, thread tolerances, or inspection procedure."
kb_implications:
  - "item_granularity: simple_part - Model as one standard anodized aluminum optical thread adapter ring; reuse a generic threaded adapter or optomechanical ring part if later KB entries need similar SM2/M52 adapters."
---

# reAM250 BOM Row 5 - 1A41

Research result for the leased reAM250 BOM row.
