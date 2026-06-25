---
row_identity:
  item: "6P"
  cad_file: "6P_belt_pulley_without_teeth"
  source_row_number: 194
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://youprintin3d.de/hardware/riemen-und-pulleys/gt2/580/gt2-pulley-20zaehne-8mm-bohrung.html"
function:
  summary: "Small GT2 timing-belt pulley for transmitting rotary motion to a GT2 belt in the reAM250 motion system; the row quantity is six identical pulleys."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6P_belt_pulley_without_teeth.step; research/ream250_bom/ream250_bom_row_0194_6P__views_2x2.png; https://youprintin3d.de/hardware/riemen-und-pulleys/gt2/580/gt2-pulley-20zaehne-8mm-bohrung.html"
    cited_fact_or_basis: "BOM row 194 lists item 6P, quantity 6, CAD file 6P_belt_pulley_without_teeth, manufacturer youprintin3d.de, and the GT2 pulley URL. FreeCAD measured one solid with an 18.00 x 18.00 x 14.20 mm bounding box; the preview shows a flanged pulley with central bore. The BOM URL product page identifies a GT2 Pulley 20 teeth, 8 mm bore, 7.5 mm gear width, 7 mm max belt width, and flanges on both edges."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM link route is treated as row-matched because it names the same GT2 pulley family and 8 mm bore represented by the small flanged pulley CAD."
  uncertainty_notes:
    - "The row does not identify the specific shaft or belt loop served by these six pulleys, so the functional location is motion-system level rather than axis-specific."
mass:
  value_kg: 0.0142
  basis: "FreeCAD volume 1772.480 mm^3 converted to 1.772480e-6 m^3 and multiplied by stainless steel density 8000 kg/m^3, giving 0.014180 kg per pulley. The row quantity of 6 implies about 0.0851 kg total for this BOM row."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6P_belt_pulley_without_teeth.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 1772.480 mm^3, area 1567.074 mm^2, and bounding box 18.00 x 18.00 x 14.20 mm. The assembly STEP material extractor matched 6P_belt_pulley_without_teeth to Stainless Steel with density 8000.0. The local density table lists stainless_steel density_kg_per_m3: 8000."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished physical volume of one pulley."
    - "The assembly STEP stainless steel density is used directly for mass conversion."
  uncertainty_notes: []
material:
  primary_material: "stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 6P_belt_pulley_without_teeth to material Stainless Steel with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local material metadata gives a stainless steel family but not a specific alloy grade."
how_to_make:
  summary: "Treat as a standard purchased GT2 pulley for current KB modeling; a local route would machine or hob a small stainless pulley blank, bore it to 8 mm, form flanges, finish/deburr, and verify belt fit."
  manufacturing_steps:
    - "Procure or make stainless cylindrical pulley stock/blank sized for an approximately 18 mm outer diameter and 14.2 mm overall length."
    - "Turn the pulley body and flanges on a lathe, then bore/ream the central 8 mm shaft hole."
    - "Cut or hob the GT2 belt tooth profile around the pulley circumference, keeping the belt-contact width compatible with a 7 mm belt."
    - "Deburr, clean, and inspect bore concentricity, flange edges, and belt engagement."
  source:
    url_or_path: "https://youprintin3d.de/hardware/riemen-und-pulleys/gt2/580/gt2-pulley-20zaehne-8mm-bohrung.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6P_belt_pulley_without_teeth.step; research/ream250_bom/ream250_bom_row_0194_6P__views_2x2.png"
    cited_fact_or_basis: "The BOM-provided vendor route identifies a GT2 20-tooth pulley with 8 mm bore, 7.5 mm gear width, 7 mm max belt width, and flanges on both edges. The STEP and preview show a single small flanged pulley body with central bore."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because the row is linked to a commercial GT2 pulley page, procurement of a standard pulley is the current preferred route; the machining route is included as a plausible later local-manufacturing route."
    - "The manufacturing route uses standard pulley-making operations inferred from the pulley geometry and GT2 belt interface."
  uncertainty_notes:
    - "The vendor page and CAD do not specify tooth manufacturing method, surface finish, or bore/set-screw details for a local replica."
kb_implications:
  - "item_granularity: simple_part - standard GT2 timing-belt pulley hardware; reuse or create a generic pulley/shaft hardware item rather than a reAM250-specific custom part unless later modeling needs tooth-profile manufacturing detail."
---

Research result for reAM250 BOM row 194.
