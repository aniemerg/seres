---
row_identity:
  item: 2ADC
  cad_file: 2ADC_part_C
  source_row_number: 55
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: >
    Top bearing support/bracket for the reAM250 K+C S5/0500 glass-scale axis
    installation, providing a rigid bearing bore and bolted mounting flanges
    for locating the encoder/bearing hardware near the top of the axis.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADC_part_C.step; research/ream250_bom/ream250_bom_row_0055_2ADC__views_2x2.png; https://www.top-maschinen.de/k-c-glasmassstab-s5-500-mm-5-m-verfahrweg-520-mm-812251.html"
    cited_fact_or_basis: >
      BOM row 55 identifies item 2ADC as "axis bearing top S5/0500 K+C glass
      scale S5"; FreeCAD measured one solid with 86.00 x 37.00 x 58.00 mm
      bounding box; the rendered contact sheet shows a bracket-like body with a
      large circular bore and bolt-hole flanges; the K+C S5/0500 page identifies
      the S5/0500 as a 500 mm glass scale for linear measuring systems with
      compact construction.
    evidence_basis: independent_vendor_spec
  assumptions:
    - The CAD part is one physical bearing-support bracket represented by BOM quantity 1.
  uncertainty_notes:
    - The row does not identify the exact bearing or encoder interface carried by the bore.
mass:
  value_kg: 0.173
  basis: >
    Per-unit estimate for quantity 1. FreeCAD volume is 64019.959 mm^3
    (0.000064020 m^3). Modeled as an aluminum-family machined bracket at
    2700 kg/m^3 from kb/materials/properties.yaml: 0.000064020 m^3 * 2700
    kg/m^3 = 0.1729 kg. If the part is steel instead, the same CAD volume would
    be about 0.503 kg using the local 7850 kg/m^3 steel density.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADC_part_C.step; kb/materials/properties.yaml"
    cited_fact_or_basis: >
      FreeCAD measured CAD volume 64019.959 mm^3 and bounding box 86.00 x
      37.00 x 58.00 mm for 2ADC_part_C. Local density table gives aluminum
      density 2700 kg/m^3 and generic steel density 7850 kg/m^3. targeted_web_search:
      queries tried were "2ADC_part_C material weight", "axis bearing top
      S5/0500 material", and "K+C S5/0500 bracket material weight"; results
      found the K+C glass scale product context but no row-specific bracket mass
      or material.
    evidence_basis: engineering_hypothesis
  assumptions:
    - The CAD solid volume is a usable net-volume proxy for the physical part.
    - Aluminum-family density is used as the planning estimate for this compact machined bracket.
  uncertainty_notes:
    - Mass is material-sensitive; a steel version would be roughly three times heavier.
material:
  primary_material: unknown metal/alloy
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0055_2ADC__views_2x2.png"
    cited_fact_or_basis: >
      Local assembly STEP material extraction for product 2ADC_part_C returned
      material "Generic" with density 1000.0, which is placeholder metadata and
      does not identify a real material. The CAD preview shows a rigid bracket
      geometry with bearing bore and bolted flanges. targeted_web_search:
      queries tried were "2ADC_part_C material", "axis bearing top S5/0500
      material", and "K+C glass scale S5 bearing bracket material"; no
      row-specific material source was found.
    evidence_basis: engineering_hypothesis
  assumptions:
    - The part is treated as metallic because the geometry and function are those of a bearing/encoder support bracket.
  uncertainty_notes:
    - The exact alloy or steel/aluminum choice is unresolved and should be checked against the original CAD model or build notes before detailed manufacturing planning.
how_to_make:
  summary: >
    Manufacture as a small machined metal bracket, then install bearing or
    encoder-interface hardware during the axis/glass-scale assembly.
  manufacturing_steps:
    - Cut rectangular metal stock to a blank slightly larger than the CAD envelope.
    - CNC mill the outer profile, mounting feet, central bearing pocket/bore, and side reliefs.
    - Drill or mill the flange mounting holes and deburr all edges.
    - Inspect bore position and mounting-hole spacing, then fasten into the glass-scale axis assembly.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADC_part_C.step; research/ream250_bom/ream250_bom_row_0055_2ADC__views_2x2.png"
    cited_fact_or_basis: >
      CAD evidence shows one compact bracket-like solid with a large circular
      bore, stepped body, and multiple mounting holes. targeted_web_search:
      queries tried were "axis bearing top S5/0500 manufacturing", "2ADC_part_C
      machining", and "K+C S5/0500 bearing bracket"; no source stated the
      row-specific manufacturing route.
    evidence_basis: engineering_hypothesis
  assumptions:
    - Subtractive machining is the simplest route for the observed bore, flanges, and small-batch bracket geometry.
  uncertainty_notes:
    - Heat treatment, surface finish, and tolerance class are not specified by the BOM or STEP metadata.
kb_implications:
  - "item_granularity: simple_part - Model as a reusable machined bearing-support bracket rather than a purchased calibrated module; material/alloy can be refined later if source data appears."
---

Research result for reAM250 BOM row 55.
