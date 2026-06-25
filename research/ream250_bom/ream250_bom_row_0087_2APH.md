---
row_identity:
  item: 2APH
  cad_file: 2APH_felt_seal
  source_row_number: 87
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Thin square-frame seal or gasket used as a replaceable interface seal around a roughly 260 mm square opening.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APH_felt_seal.step; research/ream250_bom/ream250_bom_row_0087_2APH__views_2x2.png
    cited_fact_or_basis: "BOM row 87 names item 2APH with CAD file 2APH_felt_seal; FreeCAD measured one solid with 260.00 x 260.00 x 4.00 mm bounding box; rendered preview shows a flat square frame."
    evidence_basis: bom_provided
  assumptions:
    - The CAD filename suffix "felt_seal" and square-frame geometry are treated as the row identity's functional cue.
  uncertainty_notes:
    - No parent assembly placement was provided, so the exact mating surfaces and sealed medium are not identified.
mass:
  value_kg: 0.03
  basis: "Per-unit mass for quantity 1. CAD volume 32256.000 mm^3 = 0.000032256 m^3; assembly STEP material metadata density 930 kg/m^3; product is 0.000032256 * 930 = 0.029998 kg, rounded to 0.030 kg."
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APH_felt_seal.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: "FreeCAD measured one solid, volume 32256.000 mm^3, area 24192.000 mm^2, bounding box 260.00 x 260.00 x 4.00 mm; local STEP material extraction for 2APH_felt_seal returned material Rubber and density 930 kg/m^3."
    evidence_basis: bom_provided
  assumptions:
    - The CAD solid volume represents one physical BOM-row item.
    - The STEP density value is interpreted as kg/m^3, matching the reAM250 export convention noted by the extractor.
  uncertainty_notes:
    - CAD mass excludes any installation compression, adhesive backing, or trimming variation not represented in the STEP solid.
material:
  primary_material: rubber, grade unspecified
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: "Local assembly STEP material extraction for product 2APH_felt_seal returned material Rubber with density 930 kg/m^3."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - The BOM/CAD name says "felt_seal" while the assembly STEP metadata says Rubber; the material family is therefore rubber, but fiber content, elastomer grade, hardness, and reinforcement are not resolved.
how_to_make:
  summary: Procure as a replaceable rubber/felt-style seal when available; a local approximation would cut the square frame from thin rubber sheet or compatible seal stock, then inspect fit and edge quality.
  manufacturing_steps:
    - Select thin rubber sheet or compatible seal stock near 4 mm thickness.
    - Cut the outer square and inner opening by die cutting, knife cutting, laser/waterjet cutting, or a simple template-and-blade process.
    - Deburr or clean edges, check flatness, and trial-fit against the mating square opening.
  source:
    url_or_path: https://therubbercompany.com/gaskets-and-seals/die-cut-gaskets/; https://www.customgasketmfg.com/die-cut-gaskets-felt-washers/
    cited_fact_or_basis: "The Rubber Company describes die-cut gaskets as made with a die and cutting machine and suitable for varied materials; Custom Gasket Mfg. describes die-cut felt gaskets, seals, washers, and felt material thickness/style options."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The flat 260 x 260 x 4 mm frame geometry can be made from sheet stock rather than a molded 3D profile.
    - For KB planning, procurement and local sheet-cut fabrication are both plausible routes until the exact OEM seal specification is recovered.
  uncertainty_notes:
    - "targeted_web_search: tried 'agrolager 2APH felt seal', 'site:agrolager.de 2APH', '2APH rubber seal 260', and '2APH felt agrolager'; results did not provide a row-specific vendor page, drawing, or OEM manufacturing route."
    - Generic gasket/felt-seal fabrication sources support the route class, not this exact 2APH part specification.
kb_implications:
  - "item_granularity: simple_part - Model as a replaceable seal/gasket replaceable or applied part with per-unit mass about 0.030 kg unless later research identifies a reusable standard seal family."
---
