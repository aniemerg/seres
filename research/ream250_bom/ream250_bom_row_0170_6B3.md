---
row_identity:
  item: "6B3"
  cad_file: "6B3_glue"
  source_row_number: 170
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Long, narrow adhesive bead or glue strip used in the row-6 recoater belt/gliding-surface/ceramic-pole/blade area, plausibly to bond or retain the adjacent ceramic pole or gliding-surface elements."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B3_glue.step; research/ream250_bom/ream250_bom_row_0170_6B3__views_2x2.png; research/ream250_bom/ream250_bom_row_0168_6B1.md; research/ream250_bom/ream250_bom_row_0169_6B2.md"
    cited_fact_or_basis: "BOM row 170 names item 6B3 with quantity 1 and CAD file 6B3_glue; manifest row 170 maps it to one matched part STEP. Neighboring BOM rows are 6B1_gliding_surface, 6B2_ceramic_pole, and 6C1_blade. FreeCAD measured one solid with a 1.41 x 2.83 x 274.00 mm bounding box, and the rendered preview shows a very long thin bead-like strip."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM/CAD word 'glue' is interpreted as the functional role of an adhesive bead rather than as a rigid machined insert."
    - "The row-6 neighborhood is interpreted as the recoater belt/gliding-surface/ceramic-pole/blade subassembly."
  uncertainty_notes:
    - "The isolated part export does not show the exact bonded faces or whether the bead bonds 6B2 to 6B1, bonds another mating surface, or represents a modeled adhesive volume for several nearby contacts."
mass:
  value_kg: 0.000282
  basis: "Per-unit mass for quantity 1. FreeCAD volume is 235.204 mm^3 = 0.000000235204 m^3. Using an assumed cured adhesive density of 1200 kg/m^3 gives 0.000282245 kg, rounded to 0.000282 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B3_glue.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 235.204 mm^3 and bounding box 1.41 x 2.83 x 274.00 mm. Local assembly STEP material extraction for product 6B3_glue returned placeholder material 'Generic' with density 1000.0, which does not resolve material. targeted_web_search: queries tried '6B3_glue', 'reAM250 6B3 glue', 'reAM250 6B3_glue material', and 'reAM250 glue ceramic pole'; results found only public BOM repeats or non-row-specific pages, with no row-specific adhesive density or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The exported single-solid STEP volume represents one physical adhesive bead for the BOM row."
    - "A representative cured adhesive density of 1200 kg/m^3 is used because the row does not identify adhesive chemistry and the local density table has no adhesive entry."
  uncertainty_notes:
    - "A typical adhesive density range near 1000-1500 kg/m^3 would move the per-unit mass by roughly -17% to +25% from this estimate."
    - "If the BOM row represents multiple adhesive beads hidden behind the single exported part, total row adhesive mass would be higher than the isolated-part estimate."
material:
  primary_material: "unspecified adhesive/glue polymer"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B3_glue.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 170 and the CAD filename identify the item as 6B3_glue. The per-part STEP geometry is a long bead-like solid. Local assembly STEP material extraction returned only placeholder material 'Generic' with density 1000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because the row identity says glue, the material is kept at the broad adhesive/polymer family level rather than assigning an unsupported epoxy, silicone, acrylic, or cyanoacrylate grade."
  uncertainty_notes:
    - "No adhesive chemistry, cure method, service temperature, vacuum compatibility, or bonding-substrate compatibility is provided."
how_to_make:
  summary: "Plausible route: procure a compatible structural or retaining adhesive, clean and mask the mating surfaces, dispense a controlled 274 mm bead matching the CAD volume, assemble the mating recoater parts, cure, and inspect squeeze-out and bond continuity."
  manufacturing_steps:
    - "Select an adhesive compatible with the bonded substrates and the recoater operating environment."
    - "Clean and abrade or otherwise prepare the mating surfaces according to the adhesive process requirement."
    - "Dispense a narrow bead approximately matching the CAD envelope and volume."
    - "Position the adjacent recoater components and hold them in alignment during cure."
    - "Cure at the adhesive-specified temperature and time, then inspect bead continuity, squeeze-out, and bonded alignment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B3_glue.step; research/ream250_bom/ream250_bom_row_0170_6B3__views_2x2.png"
    cited_fact_or_basis: "BOM/CAD identify the item as glue, and CAD/preview show a simple long thin adhesive-like strip. targeted_web_search: queries tried 'reAM250 6B3 glue manufacturing', 'reAM250 glue ceramic pole', 'reAM250 6B3_glue adhesive', and 'adhesive bead ceramic pole gliding surface manufacturing'; results did not find a row-specific adhesive specification or process, so the route is inferred from the adhesive-bead geometry and BOM neighborhood."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row is modeled as an applied cured adhesive volume, not a reusable mechanical part or purchased calibrated module."
    - "Surface preparation, controlled dispensing, fixturing, and cure are included because they are normally required to turn an adhesive into the installed bonded feature represented by the CAD bead."
  uncertainty_notes:
    - "The actual adhesive may require a specific primer, mix ratio, cure schedule, vacuum bake-out, or cleanroom handling not stated by the BOM/CAD row."
kb_implications:
  - "item_granularity: simple_part - Model as a replaceable or applied part adhesive application or cured glue bead tied to an assembly step, not as a standalone reusable part or purchased module."
---
