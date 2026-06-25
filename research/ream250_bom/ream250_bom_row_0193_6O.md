---
row_identity:
  item: "6O"
  cad_file: "6O_belt_pulley_GT2_8mm_20_teeth"
  source_row_number: 193
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://youprintin3d.de/hardware/riemen-und-pulleys/gt2/580/gt2-pulley-20zaehne-8mm-bohrung.html"
function:
  summary: "GT2 timing-belt pulley for transmitting rotary motion to an 8 mm shaft in the reAM250 belt drive; the 20 teeth engage a GT2 belt and the flanges help keep the belt aligned."
  source:
    url_or_path: "https://youprintin3d.de/hardware/riemen-und-pulleys/gt2/580/gt2-pulley-20zaehne-8mm-bohrung.html; research/ream250_bom/ream250_bom_row_0193_6O__views_2x2.png"
    cited_fact_or_basis: "BOM-provided URL identifies the row as a GT2 pulley with 20 teeth, 8 mm bore, 7.5 mm gear width, 7 mm maximum belt width, and flanges on both edges; CAD preview shows a flanged toothed pulley with a central bore and set-screw boss."
    evidence_basis: "bom_provided"
  assumptions:
    - "The pulley is used with a matching GT2 timing belt in the machine motion system."
  uncertainty_notes: []
mass:
  value_kg: 0.004895
  basis: "FreeCAD measured one STEP solid with volume 1812.928 mm^3 and bounding box about 16.01 x 16.00 x 20.00 mm. Using the local aluminum density constant 2700 kg/m^3 gives 1812.927949846365 mm^3 * 1e-9 m^3/mm^3 * 2700 kg/m^3 = 0.004895 kg per pulley. BOM quantity is 6, so the row total is about 0.0294 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6O_belt_pulley_GT2_8mm_20_teeth.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured volume 1812.928 mm^3 for the row STEP; assembly STEP material extraction found Aluminum 6061 with density 2700.0; local material properties list aluminum density as 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP solid volume represents one physical pulley, including bore and visible flange/tooth geometry."
    - "The local aluminum density constant is close enough for Aluminum 6061 at this KB planning precision."
  uncertainty_notes:
    - "CAD export fidelity and any omitted fasteners, such as a grub screw, could shift the true purchased-unit mass slightly."
material:
  primary_material: "Aluminum 6061 pulley body"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material metadata for product 6O_belt_pulley_GT2_8mm_20_teeth reports material Aluminum 6061 and density 2700.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The vendor page confirms the pulley configuration but does not state material; the material value relies on the supplied assembly STEP metadata."
how_to_make:
  summary: "Prepare as a standard GT2 20-tooth, 8 mm bore flanged pulley, or locally make from Aluminum 6061 bar/blank by turning the bore and outside profile, cutting the GT2 tooth form, drilling/tapping the set-screw hole, and deburring/inspecting fit to the GT2 belt and 8 mm shaft"
  manufacturing_steps:
    - "Cut Aluminum 6061 round stock or near-net pulley blank."
    - "Turn the central bore and flange/body outside diameters to the CAD envelope."
    - "Cut the GT2 tooth profile around the pulley and form both belt-retaining flanges."
    - "Drill and tap the radial set-screw hole visible in the CAD preview."
    - "Deburr, clean, and inspect bore fit, tooth engagement, and flange clearance."
  source:
    url_or_path: "https://youprintin3d.de/hardware/riemen-und-pulleys/gt2/580/gt2-pulley-20zaehne-8mm-bohrung.html; research/ream250_bom/ream250_bom_row_0193_6O__views_2x2.png"
    cited_fact_or_basis: "BOM-provided vendor page identifies a standard GT2 20-tooth 8 mm bore pulley with two flanges; CAD preview shows a flanged toothed pulley and radial set-screw boss. targeted_web_search: not required for source-backed procurement route; detailed local machining route is inferred from geometry because the BOM route does not state manufacturing operations."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Manufacture can be modeled as a small precision machined aluminum part"
    - "The radial boss/hole is treated as a set-screw feature based on standard pulley geometry and the CAD preview."
  uncertainty_notes:
    - "The local manufacturing sequence is plausible but not vendor-sourced; exact tooth cutting method and tolerances are not specified by the BOM evidence."
kb_implications:
  - "item_granularity: simple_part - Model later as reusable standard GT2 aluminum pulley hardware rather than a machine-specific purchased module; quantity differences can reuse the same part entry."
---
