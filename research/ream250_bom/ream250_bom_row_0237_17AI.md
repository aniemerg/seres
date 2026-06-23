---
row_identity:
  item: "17AI"
  cad_file: "17AI_hinge"
  source_row_number: 237
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small hinge or hinge-block component used in the reAM250 17A0_hood assembly, likely providing a pivot or mounting interface for the hood cover/sheet structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AI_hinge.step; research/ream250_bom/ream250_bom_row_0237_17AI__views_2x2.png"
    cited_fact_or_basis: "BOM row 237 identifies item 17AI, quantity 2, CAD file 17AI_hinge; the manifest maps it to gold_export/parts/17AI_hinge.step as matched_existing part; 00_assembly.step places two 17AI_hinge occurrences under product definition 17A0_hood; nearby 17A0_hood children include strut profiles, handle, front/top/side/back sheets, and cover_sheet_hood_top; FreeCAD measured one solid with a 20.00 x 26.00 x 26.00 mm bounding box; the rendered preview shows a compact wedge/block-like solid with no visible pin, knuckle, or fastener holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The word hinge in the CAD/BOM name is interpreted as the functional role even though the exported per-row solid looks like one hinge block or leaf element rather than a complete multi-piece hinge assembly."
  uncertainty_notes:
    - "The CAD preview does not show the mating pin, barrel, or fastener features, so the exact hinge mechanism and mating components are not resolved from this row alone."
mass:
  value_kg: 0.0346
  basis: "FreeCAD volume 12800.000 mm^3 equals 1.28e-5 m^3. Using the local aluminum density constant 2700 kg/m^3 gives 0.0346 kg per 17AI hinge; BOM quantity is 2, so the row total would be about 0.069 kg. A generic steel density alternative would be about 0.100 kg per unit."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AI_hinge.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 12800.000 mm^3, area 3360.000 mm^2, and bounding box 20.00 x 26.00 x 26.00 mm; local STEP material extraction for 17AI_hinge reports only Generic with density 1000.0; kb/materials/properties.yaml lists aluminum density 2700 kg/m^3 and steel density 7850 kg/m^3; the BOM/assembly context places the part in 17A0_hood with Bosch Rexroth strut profiles and hood sheets. targeted_web_search: searched \"17AI_hinge reAM250\", \"reAM250 17AI hinge\", \"17AI_hinge CAD\", and \"20 x 26 x 26 hinge block aluminum profile\"; found duplicate BOM listings but no row-specific material, density, or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The measured STEP solid is treated as one complete physical 17AI hinge item."
    - "Aluminum density is used as the planning estimate because the row sits in an aluminum-profile hood/frame context and the geometry is a small custom block; the steel alternative is recorded for sensitivity."
  uncertainty_notes:
    - "Mass depends directly on the unresolved material. If the part is steel rather than aluminum, the per-unit estimate increases by roughly 3x."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AI_hinge.step; research/ream250_bom/ream250_bom_row_0237_17AI__views_2x2.png"
    cited_fact_or_basis: "BOM row 237 names 17AI_hinge but has no manufacturer, product ID, material family, or grade; local STEP material extraction for 17AI_hinge reports only Generic with density 1000.0; the CAD preview shows a compact solid hinge block/leaf form in a 17A0_hood subassembly that also contains frame profiles and sheet parts. targeted_web_search: searched \"17AI_hinge reAM250\", \"reAM250 17AI hinge\", \"17AI_hinge CAD\", and \"20 x 26 x 26 hinge block aluminum profile\"; found duplicate BOM listings but no usable row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal family is used because the item is a hinge/load-transfer part in a machine hood and the CAD is a solid machined-looking block."
  uncertainty_notes:
    - "The exact alloy or grade is not resolved; aluminum is plausible from the surrounding hood/frame context, while steel remains plausible for hinge wear or load capacity."
how_to_make:
  summary: "Model as a simple machined hinge block or leaf: cut a small metal blank, mill the wedge/block profile, add any mating hinge or mounting features required by the higher-level hood assembly, deburr, finish, and inspect fit."
  manufacturing_steps:
    - "Start from aluminum or steel bar/block stock sized above the 20 x 26 x 26 mm bounding box."
    - "Saw or cut the blank to rough size."
    - "Mill the rectangular and angled/wedge faces visible in the CAD export."
    - "Machine any missing assembly-interface details required by the mating hood hinge, such as pin bores, slots, or threaded mounting holes, if those are represented outside this row's simplified export."
    - "Deburr edges, clean, apply corrosion protection or anodize/passivate as appropriate for the final alloy, and inspect the fit in the 17A0_hood assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AI_hinge.step; research/ream250_bom/ream250_bom_row_0237_17AI__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The STEP/contact sheet shows one compact solid with a 20.00 x 26.00 x 26.00 mm bounding box and wedge/block-like faces; 00_assembly.step places two instances in 17A0_hood. targeted_web_search: searched \"17AI_hinge reAM250\", \"reAM250 17AI hinge\", \"17AI_hinge CAD\", and \"20 x 26 x 26 hinge block aluminum profile\"; found duplicate BOM listings but no row-specific manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The route is inferred from the simple solid geometry and small-machine hinge function, not from a vendor process sheet."
    - "If later CAD context exposes bores or pin features hidden outside this row, those operations should be added to the machining route."
  uncertainty_notes:
    - "The CAD export lacks tolerances, surface finish, heat treatment, exact material, and visible hinge-pin geometry, so process details remain approximate."
kb_implications:
  - "item_granularity: simple_part - treat as one reusable small machined hinge block/leaf in the hood assembly rather than a purchased calibrated module or a complete hinge subassembly."
---

Research result for reAM250 BOM row 237.
