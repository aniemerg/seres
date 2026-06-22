---
row_identity:
  item: 2APJ
  cad_file: 2APJ_inner_seal_guide
  source_row_number: 89
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Thin square inner seal guide plate in the build-platform seal stack, likely locating or constraining the adjacent felt seal around a square opening.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APJ_inner_seal_guide.step; research/ream250_bom/ream250_bom_row_0089_2APJ__views_2x2.png
    cited_fact_or_basis: BOM row 89 lists item 2APJ quantity 1 as 2APJ_inner_seal_guide; manifest row 89 maps it to one matched part STEP; FreeCAD measured one solid with 200.00 x 200.00 x 4.00 mm bounding box; the rendered contact sheet shows a thin square frame/guide plate with a large central square opening, corner holes, and local corner features. Neighboring BOM rows identify 2APH_felt_seal, 2API_build_platform, and 2APK heating-plate-cover parts.
    evidence_basis: bom_provided
  assumptions:
    - The filename suffix "inner_seal_guide" is interpreted literally as a guide or retainer for the adjacent inner seal interface.
    - The nearby felt seal and build-platform rows are used only as assembly context, not as proof of the exact mating surfaces.
  uncertainty_notes:
    - The CAD package does not provide parent assembly placement for this row, so the exact sealed medium, compression direction, and mating parts remain unresolved.
mass:
  value_kg: 0.212
  basis: Per-unit planning estimate for quantity 1. FreeCAD volume is 78355.497 mm^3, or 0.000078355497 m^3; using the local aluminum density constant of 2700 kg/m^3 gives 0.21156 kg, rounded to 0.212 kg. If the same CAD volume were generic steel at 7850 kg/m^3, one guide would be about 0.615 kg.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APJ_inner_seal_guide.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: >-
      FreeCAD measured one solid, volume 78355.497 mm^3, surface area
      45726.450 mm^2, and bounding box 200.00 x 200.00 x 4.00 mm.
      kb/materials/properties.yaml lists aluminum density 2700 kg/m^3 and
      generic steel density 7850 kg/m^3. Assembly STEP material extraction for
      2APJ_inner_seal_guide returned material Generic with density 1000.0,
      which is placeholder metadata. targeted_web_search: tried
      "2APJ_inner_seal_guide", "2APJ inner seal guide reAM250", "reAM250 inner
      seal guide material", and "2APJ_inner_seal_guide.step"; results found
      only duplicate BOM text and unrelated seal pages, with no row-specific
      mass or material source.
    evidence_basis: engineering_hypothesis
  assumptions:
    - The CAD solid volume represents one physical BOM-row item with no hidden inserts or omitted fasteners.
    - Aluminum is used as the planning density because this is a thin guide/retainer plate near the seal/build-platform stack; the steel-equivalent mass is retained in the basis for downstream sensitivity.
  uncertainty_notes:
    - The true alloy is not sourced; downstream mass should be revised if a drawing, native CAD material table, or physical weigh-in identifies steel, stainless steel, or another material.
material:
  primary_material: unknown metal/alloy
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APJ_inner_seal_guide.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0089_2APJ__views_2x2.png
    cited_fact_or_basis: >-
      BOM row 89 and the manifest identify a custom row named
      2APJ_inner_seal_guide but provide no manufacturer, product ID, material
      hint, or link URL. The rendered CAD preview shows a rigid 4 mm thick
      square frame/guide plate with machined or cut features. Local assembly
      STEP material extraction returned only Generic with density 1000.0, which
      is placeholder metadata rather than a material. targeted_web_search: tried
      "2APJ_inner_seal_guide", "2APJ inner seal guide reAM250", "reAM250 inner
      seal guide material", and "2APJ_inner_seal_guide.step"; no row-specific
      usable material source was found.
    evidence_basis: engineering_hypothesis
  assumptions:
    - A metallic material family is assumed from the thin rigid plate geometry, corner holes, and role as a seal guide/retainer rather than as the compliant seal itself.
  uncertainty_notes:
    - No evidence distinguishes aluminum, steel, stainless steel, or another alloy, so later KB modeling should keep the material broad until a drawing or native CAD material source is recovered.
how_to_make:
  summary: Make as a simple custom guide/retainer plate from 4 mm sheet or flat plate stock; cut the outside square, central opening, corner holes, and local relief features, then deburr, clean, and inspect fit against the seal and build-platform stack.
  manufacturing_steps:
    - Select metal sheet or flat plate stock near 4 mm thickness.
    - Cut the 200 mm square outer profile and large central square opening by laser, waterjet, router, mill, or equivalent sheet/plate cutting process.
    - Drill or machine the corner holes and local corner relief/retainer features shown in the CAD model.
    - Deburr and break sharp edges to avoid damaging the adjacent seal.
    - Clean and inspect flatness, hole locations, and fit against the felt seal and build-platform interface.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APJ_inner_seal_guide.step; research/ream250_bom/ream250_bom_row_0089_2APJ__views_2x2.png
    cited_fact_or_basis: >-
      CAD and rendered views show one 4 mm thick square frame/plate with a large
      central opening, corner holes, and local corner relief features; no source
      file states the manufacturing route. targeted_web_search: tried
      "2APJ_inner_seal_guide manufacturing", "2APJ inner seal guide reAM250",
      "reAM250 inner seal guide drawing", and "inner seal guide plate material";
      no row-specific fabrication drawing, vendor page, or process note was
      found.
    evidence_basis: engineering_hypothesis
  assumptions:
    - Conventional sheet/plate cutting plus drilling or light CNC machining is the simplest plausible route for the observed one-piece geometry.
    - Edge finishing is included because the part interfaces with a seal and should not abrade or cut the compliant seal material.
  uncertainty_notes:
    - The CAD preview supports route triage but does not specify tolerances, surface finish, coating, or whether the plate requires a particular hardness or corrosion resistance.
kb_implications:
  - "item_granularity: simple_part - Model as one custom thin metal guide/retainer plate with broad metal/alloy material until later evidence resolves the exact alloy; it does not need a sub-BOM."
---
