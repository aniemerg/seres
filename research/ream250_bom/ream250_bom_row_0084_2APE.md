---
row_identity:
  item: "2APE"
  cad_file: "2APE_spacer_sleeve"
  source_row_number: 84
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small cylindrical spacer sleeve used four times in the reAM250 build-platform/heating-plate hardware stack, likely spacing or locating a bolted connection through the adjacent shim, pressing plate, and platform parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APE_spacer_sleeve.step; research/ream250_bom/ream250_bom_row_0084_2APE__views_2x2.png"
    cited_fact_or_basis: "BOM row 84 lists item 2APE, quantity 4, CAD file 2APE_spacer_sleeve. Manifest row 84 maps the row to a matched part STEP. FreeCAD measured one solid with bounding box 13.00 x 9.00 x 13.00 mm, and the rendered preview shows a short cylindrical sleeve with a central through bore. Neighboring BOM rows include shim disk, pressing plate, build platform, heating plate, spring blocks, and bolts."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name and through-bore cylinder geometry are interpreted as a mechanical spacer/sleeve rather than a fluid fitting or bearing."
    - "The four row instances are assumed to be identical copies of the same physical spacer sleeve."
  uncertainty_notes:
    - "The BOM and CAD do not expose mating constraints, so the exact interface being spaced or located is inferred from neighboring build-platform hardware rows."
mass:
  value_kg: 0.0067
  basis: "Per-unit planning estimate for one spacer sleeve; BOM quantity is 4, so the row total is about 0.0266 kg. FreeCAD volume is 848.230 mm^3, equal to 8.48230e-7 m^3. Using the local generic steel density constant of 7850 kg/m^3 gives 0.00666 kg per sleeve, rounded to 0.0067 kg. If the same CAD volume were aluminum at 2700 kg/m^3, it would be about 0.0023 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APE_spacer_sleeve.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 848.230 mm^3, surface area 753.982 mm^2, and bounding box 13.00 x 9.00 x 13.00 mm. kb/materials/properties.yaml lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. targeted_web_search: tried '\"2APE\" \"spacer sleeve\"', '\"2APE_spacer_sleeve\"', and '\"reAM250\" \"2APE\"'; results found duplicate reAM250 BOM listings but no row-specific catalog weight, material, or drawing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the physical volume of one sleeve."
    - "A steel-like density is used as the nominal estimate because this is a small compression/spacing sleeve near bolts and build-platform hardware, and no row-specific material is provided."
  uncertainty_notes:
    - "Actual mass depends directly on unresolved material; aluminum construction would be about one third of the stated steel-like estimate."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APE_spacer_sleeve.step"
    cited_fact_or_basis: "BOM row 84 gives no manufacturer, product ID, link URL, material family, or grade. Assembly STEP material extraction for product 2APE_spacer_sleeve returned material 'Generic' with density 1000.0, which is placeholder metadata. CAD geometry is a rigid sleeve rather than a seal, cable, or consumable. targeted_web_search: tried '\"2APE\" \"spacer sleeve\"', '\"2APE_spacer_sleeve\"', and '\"reAM250\" \"2APE\"'; no row-specific usable material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The small spacer sleeve is treated as metallic because the CAD is a rigid through-bore cylinder used near bolted build-platform hardware."
  uncertainty_notes:
    - "Material family is broad only; downstream KB modeling should not choose steel, stainless steel, or aluminum specifically without a drawing, full assembly note, or designer-provided material field."
how_to_make:
  summary: "Make as a simple turned spacer sleeve from metal tube or round bar: cut stock, drill or bore the through hole if needed, turn the outer diameter and length, deburr, and inspect the bore and spacer length."
  manufacturing_steps:
    - "Select metal tube or round bar stock large enough for the 13 mm outside diameter envelope."
    - "Cut a blank slightly over the finished spacer length."
    - "Turn the outside diameter and face both ends to the finished length on a lathe."
    - "Drill, ream, or bore the central through hole to the required fastener or locating diameter if using solid bar stock."
    - "Deburr inner and outer edges, clean, and inspect length, outside diameter, bore diameter, and squareness."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APE_spacer_sleeve.step; research/ream250_bom/ream250_bom_row_0084_2APE__views_2x2.png"
    cited_fact_or_basis: "The STEP and rendered contact sheet show a one-piece cylindrical sleeve with a central through bore and a 13.00 x 9.00 x 13.00 mm envelope. targeted_web_search: tried '\"2APE\" \"spacer sleeve\"', '\"2APE_spacer_sleeve\"', and '\"reAM250\" \"2APE\"'; results found duplicate BOM text but no row-specific manufacturing drawing or process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Lathe turning and drilling/boring are the most plausible local manufacturing route for a small cylindrical through-bore spacer."
    - "No heat treatment or coating is included because neither the BOM nor CAD evidence states a requirement."
  uncertainty_notes:
    - "The CAD preview is sufficient for route triage but does not provide tolerances, bore fit class, surface finish, coating, or exact stock material."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable one-piece metal spacer sleeve/bushing rather than as a purchased module or assembly."
---

Research result for reAM250 BOM row 84.
