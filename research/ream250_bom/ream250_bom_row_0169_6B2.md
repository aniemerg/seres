---
row_identity:
  item: "6B2"
  cad_file: "6B2_ceramic_pole"
  source_row_number: 169
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Long, small-section pole used as a wear-resistant guide, spacer, or contact member in the row-6 belt/gliding-surface/blade area of the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B2_ceramic_pole.step; research/ream250_bom/ream250_bom_row_0169_6B2__views_2x2.png"
    cited_fact_or_basis: "BOM row 169 names item 6B2 as CAD file 6B2_ceramic_pole with quantity 1. Manifest row 169 maps it to one matched part STEP. Neighboring BOM rows include 6A_conveyor_belt, 6B1_gliding_surface, 6B3_glue, and 6C1_blade. FreeCAD measured one solid with a 4.00 x 4.00 x 274.00 mm bounding box, and the rendered preview shows a long straight square-section rod."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-6 neighborhood in the BOM is interpreted as a belt/gliding-surface/blade mechanism, so the pole is treated as a local guide, spacer, or wear/contact element rather than an electrical insulator."
  uncertainty_notes:
    - "The isolated part export does not show exact mating faces, load direction, or whether the pole is bonded to the gliding surface or mounted separately."
mass:
  value_kg: 0.00826
  basis: "Per-unit mass for quantity 1. FreeCAD volume is 3443.186 mm^3 = 0.00000344319 m^3. Using the local generic ceramic density of 2400 kg/m^3 gives 0.00826365 kg, rounded to 0.00826 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B2_ceramic_pole.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 3443.186 mm^3 and bounding box 4.00 x 4.00 x 274.00 mm. The BOM/CAD name includes 'ceramic_pole'. The local material properties table lists generic ceramic density as 2400 kg/m^3. Local assembly STEP material extraction for product 6B2_ceramic_pole instead returned material 'Stainless Steel' with density 8000.0. targeted_web_search: queries tried '6B2_ceramic_pole', 'reAM250 ceramic pole', and 'reAM250 6B2 ceramic'; results found only public BOM repeats and no row-specific material or mass source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The exported single-solid STEP volume represents one physical 6B2 item."
    - "The word 'ceramic' in the row/CAD name is treated as the intended material family, while the stainless assembly metadata is treated as conflicting export metadata for this row."
    - "Generic dense ceramic density from the local properties table is used because no ceramic grade is supplied."
  uncertainty_notes:
    - "If the assembly STEP stainless metadata is correct, the same CAD volume would imply about 0.0275 kg per unit instead of 0.00826 kg."
    - "If the part is a denser technical ceramic such as alumina, the mass could be closer to 0.0136 kg per unit."
material:
  primary_material: "technical ceramic material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B2_ceramic_pole.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 169 and the CAD filename identify the part as 6B2_ceramic_pole. The per-part STEP geometry is a long 4 x 4 x 274 mm pole. Local assembly STEP material extraction for the same product returned 'Stainless Steel' with density 8000.0, which conflicts with the row/CAD name. targeted_web_search: queries tried '6B2_ceramic_pole material', 'reAM250 ceramic pole material', and 'reAM250 6B2 ceramic pole'; results found BOM repeats but no row-specific drawing, grade, or vendor page."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because 'ceramic' is embedded in the row identity, the broad ceramic family is preferred over the conflicting stainless metadata for planning."
  uncertainty_notes:
    - "No ceramic grade, composition, surface finish, or procurement standard is provided."
    - "The conflicting stainless material metadata should be rechecked against the native CAD assembly before final KB modeling."
how_to_make:
  summary: "Plausible route: make or procure a small technical-ceramic square rod, cut it to the 274 mm length, grind or lap the sides/ends as needed, then bond or install it with the neighboring gliding-surface and glue components."
  manufacturing_steps:
    - "Select a dense technical ceramic rod or green ceramic preform sized near the 4 x 4 mm square section."
    - "If made locally, press, extrude, or machine a green ceramic blank from ceramic powder plus binder, then debind and sinter it."
    - "Cut the sintered rod to approximately 274 mm length."
    - "Grind or lap the sides and ends to final straightness, fit, and surface finish."
    - "Install or bond the pole in the belt/gliding-surface/blade subassembly, using the neighboring 6B3_glue row if that is the mating adhesive."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B2_ceramic_pole.step; research/ream250_bom/ream250_bom_row_0169_6B2__views_2x2.png"
    cited_fact_or_basis: "BOM/CAD identify a ceramic pole, neighboring row 6B3 is glue, and CAD/preview show a simple straight 4 x 4 x 274 mm rod. targeted_web_search: queries tried 'reAM250 6B2 ceramic pole manufacturing', 'ceramic square rod 4mm manufacturing grind cut sintered', and 'ceramic pole wear guide rod manufacturing'; results did not find a row-specific process, so the route is inferred from the simple ceramic-rod geometry and BOM neighborhood."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is a monolithic ceramic rod rather than a vendor-calibrated module."
    - "Final grinding or lapping is included because sintered ceramic rods normally need finishing when used as long contact or guide members."
    - "The adjacent glue row indicates bonding is a plausible installation route, but the exact joint design is not visible in the isolated CAD."
  uncertainty_notes:
    - "Actual production may use an off-the-shelf ceramic rod cut to length rather than local green-forming and sintering."
    - "Tolerances, straightness, surface roughness, and adhesive compatibility are not specified by the BOM row."
kb_implications:
  - "item_granularity: simple_part - Model as a simple ceramic rod/contact pole with unresolved grade, not as a purchased module or assembly; the stainless metadata conflict should be preserved as a modeling caveat."
---
