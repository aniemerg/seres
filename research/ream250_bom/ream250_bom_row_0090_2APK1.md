---
row_identity:
  item: 2APK1
  cad_file: 2APK1_bottom
  source_row_number: 90
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Bottom plate of the 2APK0 heating-plate-cover group, closing the underside of a small cover around the build-platform heating-plate area and providing perimeter fastener points plus two central circular clearances.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APK1_bottom.step; research/ream250_bom/ream250_bom_row_0090_2APK1__views_2x2.png
    cited_fact_or_basis: BOM row 90 lists item 2APK1 quantity 1 as 2APK1_bottom; the full assembly names the parent product 2APK0_heating_plate_cover; FreeCAD measured one solid with about 77.00 x 4.00 x 76.30 mm bounding box, and the rendered views show a thin square plate with perimeter holes and two central circular cutouts.
    evidence_basis: bom_provided
  assumptions:
    - The name 2APK1_bottom is interpreted relative to the adjacent 2APK0_heating_plate_cover and sibling rows 2APK2_front_back and 2APK3_left_right.
  uncertainty_notes:
    - CAD identifies the cover geometry but does not state what the two central clearances pass around.
mass:
  value_kg: 0.058
  basis: Per-unit estimate for quantity 1. FreeCAD volume is 21477.399 mm^3, or 0.0000214774 m^3; using the local aluminum density constant of 2700 kg/m^3 gives about 0.05799 kg. If the same volume were generic steel at 7850 kg/m^3, mass would be about 0.169 kg.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APK1_bottom.step; kb/materials/properties.yaml
    cited_fact_or_basis: FreeCAD measured one solid, volume 21477.398680519793 mm^3, surface area 12699.856357074465 mm^2, and bounding box 77.00 x 4.00 x 76.30 mm; kb/materials/properties.yaml lists aluminum density 2700 kg/m^3 and generic steel density 7850 kg/m^3.
    evidence_basis: engineering_hypothesis
  assumptions:
    - The CAD solid is treated as one physical row item with no hidden inserts or omitted fasteners.
    - Aluminum is used as the planning density because the row is a thin local cover plate rather than the main heated mass.
  uncertainty_notes:
    - "targeted_web_search: queries tried were \"2APK1 2APK1_bottom material\", \"2APK1_bottom\", \"2APK1 bottom CAD\", and \"2APK1 plate bracket material\"; the only relevant public result found was a mirrored BOM listing that repeated the row name but did not provide material or mass."
    - The assembly STEP material extractor returned only Generic with density 1000.0, so package metadata does not resolve material; if this part is stainless or mild steel, downstream mass should use the steel-side value in the basis instead.
material:
  primary_material: unknown metal/alloy
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APK1_bottom.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: CAD and manifest identify the row as a single thin plate in the heating-plate-cover group; local assembly STEP material extraction for 2APK1_bottom returned material Generic and density 1000.0, which is placeholder metadata rather than a material.
    evidence_basis: engineering_hypothesis
  assumptions:
    - A metallic plate is assumed because the CAD is a thin structural cover near the build-platform heater and shows machined or cut plate features.
  uncertainty_notes:
    - "targeted_web_search: queries tried were \"2APK1 2APK1_bottom material\", \"2APK1_bottom\", \"2APK1 bottom CAD\", and \"2APK1 plate bracket material\"; no row-specific vendor, drawing, or material source was found beyond a BOM mirror."
    - The exact alloy or grade remains unknown, so later KB modeling should keep this broad unless a source drawing or native CAD material table is recovered.
how_to_make:
  summary: Make as a simple thin metal cover plate from sheet or flat stock, with the perimeter profile, central circular cutouts, corner/perimeter holes, and shallow rib-like pocket geometry produced by CNC machining or waterjet/laser cutting followed by machining as needed.
  manufacturing_steps:
    - Start with metal sheet or flat plate stock near 4 mm thickness.
    - Cut the outside square profile and the two central circular openings.
    - Drill or machine the small perimeter fastener holes.
    - Machine shallow ribs, pockets, or chamfers visible in the CAD if they are functional rather than CAD display artifacts.
    - Deburr, clean, and inspect hole locations before assembly into the heating-plate-cover group.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APK1_bottom.step; research/ream250_bom/ream250_bom_row_0090_2APK1__views_2x2.png
    cited_fact_or_basis: CAD preview shows a 4 mm thick plate-like part with perimeter holes, two circular cutouts, and shallow triangular/ribbed features; no source file states the manufacturing route.
    evidence_basis: engineering_hypothesis
  assumptions:
    - Conventional sheet/plate cutting plus drilling or light CNC machining is a plausible route for this geometry.
  uncertainty_notes:
    - "Targeted_web_search: queries tried were \"2APK1 2APK1_bottom material\", \"2APK1_bottom\", \"2APK1 bottom CAD\", and \"2APK1 plate bracket material\" no row-specific process drawing or supplier page was found."
    - The CAD preview is sufficient for route triage but not for deciding whether the triangular features are machined ribs, relief pockets, or export/tessellation artifacts.
kb_implications:
  - "item_granularity: simple_part - Model as one reusable thin metal cover plate, not a purchased module; material should remain broad until a drawing or native CAD material source resolves the alloy."
---
