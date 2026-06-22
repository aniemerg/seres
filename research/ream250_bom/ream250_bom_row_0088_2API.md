---
row_identity:
  item: 2API
  cad_file: 2API_build_platform
  source_row_number: 88
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Large square build platform in the reAM250 z-axis/build-platform mount group, providing the main flat build surface or support block that sits near the pressing plate, felt seal, inner seal guide, and heating-plate-cover parts.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2API_build_platform.step; research/ream250_bom/ream250_bom_row_0088_2API__views_2x2.png
    cited_fact_or_basis: "BOM row 88 lists item 2API, quantity 1, CAD file 2API_build_platform. Manifest row 88 maps the row to one matched part STEP. FreeCAD measured one solid with about 252.00 x 252.00 x 50.00 mm bounding box, and the rendered contact sheet shows a square block/platform with a broad flat top face and side relief features. Nearby BOM rows include 2APG_pressing_plate, 2APH_felt_seal, 2APJ_inner_seal_guide, and 2APK heating-plate-cover parts."
    evidence_basis: bom_provided
  assumptions:
    - The filename "build_platform" is interpreted literally as the platform/support surface in the build-platform mount stack.
  uncertainty_notes:
    - The BOM and CAD identify the row and geometry but do not specify the exact thermal, vacuum, or powder-contact interface requirements of this platform.
mass:
  value_kg: 24.7
  basis: "Per-unit planning estimate for one 2API build platform; BOM quantity is 1. FreeCAD volume is 3149770.302 mm^3 = 0.003149770302 m^3. Using the local generic steel density constant of 7850 kg/m^3 gives 24.7257 kg, rounded to 24.7 kg. If the same CAD volume were aluminum at 2700 kg/m^3, one platform would be about 8.50 kg."
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2API_build_platform.step; kb/materials/properties.yaml
    cited_fact_or_basis: "FreeCAD measured one solid with volume 3149770.302 mm^3, area 181714.747 mm^2, and bounding box 252.00 x 252.00 x 50.00 mm. kb/materials/properties.yaml lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. targeted_web_search: tried \"2API_build_platform\", \"2API build platform reAM250\", \"reAM250 build platform material\", and \"2API reAM250\"; results found the public reAM250 project page and duplicate BOM text but no row-specific mass or material."
    evidence_basis: engineering_hypothesis
  assumptions:
    - Generic steel is used as the planning density because the part is a large structural build-platform block in a metal PBF machine, while the local STEP material metadata is only Generic.
  uncertainty_notes:
    - The true material is unresolved, so the mass could plausibly be much lower if the platform is aluminum or higher if it is stainless/tool steel; downstream planning should treat 24.7 kg as a steel-equivalent estimate, not a sourced weight.
material:
  primary_material: unknown structural metal/alloy
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0088_2API__views_2x2.png
    cited_fact_or_basis: "BOM row 88 and the manifest identify 2API_build_platform but provide no manufacturer, product ID, material hint, or link URL. Assembly STEP material extraction for product 2API_build_platform returned material Generic with density 1000.0, which is placeholder metadata rather than a real material. The CAD preview shows a rigid square platform/block. targeted_web_search: tried \"2API_build_platform\", \"2API build platform reAM250\", \"reAM250 build platform material\", and \"2API reAM250\"; no row-specific usable material source was found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The platform is treated as a broad structural metal/alloy because it is a thick, load-bearing build-platform component in a metal powder-bed-fusion machine.
  uncertainty_notes:
    - No source distinguishes steel, stainless steel, tool steel, or aluminum for this row; avoid assigning a specific grade until a drawing, material list, or fabrication note is found.
how_to_make:
  summary: Make as a custom machined metal platform from thick plate or billet stock, with sawing or rough cutting, face milling/grinding of the broad build surface, machining of side relief and interface features, deburring, cleaning, and dimensional inspection; procure as a custom-fabricated machine plate if local precision machining is unavailable.
  manufacturing_steps:
    - Cut a roughly 252 mm square, 50 mm thick blank from structural metal plate or billet stock.
    - Face mill or grind the top and bottom datum surfaces to the required flatness and parallelism.
    - Machine the side relief features and any mating ledges visible in the CAD model.
    - Deburr edges, clean the platform, and inspect dimensions against the surrounding pressing plate, seal, and guide parts.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2API_build_platform.step; research/ream250_bom/ream250_bom_row_0088_2API__views_2x2.png
    cited_fact_or_basis: "CAD and rendered views show one large square block/platform with broad flat faces, 252.00 x 252.00 x 50.00 mm bounding box, and side relief/interface geometry. targeted_web_search: tried \"2API_build_platform manufacturing\", \"2API build platform reAM250\", \"reAM250 build platform material\", and \"reAM250 build platform drawing\"; results did not provide a row-specific manufacturing drawing, vendor route, or fabrication note."
    evidence_basis: engineering_hypothesis
  assumptions:
    - Thick-plate or billet machining is selected as the simplest plausible route for the observed one-piece block/platform geometry.
  uncertainty_notes:
    - The CAD does not state tolerances, flatness, surface finish, heat treatment, coating, or whether the platform requires a material matched to the powder processed on the machine.
kb_implications:
  - "item_granularity: simple_part - Model as one custom machined metal platform/block with a later material-grade decision; it does not need a sub-BOM unless future evidence shows inserts, sensors, or bonded features."
---
