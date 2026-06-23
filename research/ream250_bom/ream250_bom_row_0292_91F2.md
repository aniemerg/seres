---
row_identity:
  item: "91F2"
  cad_file: "91F2_plate_80x80x10_M12"
  source_row_number: 292
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Square mild-steel 80 x 80 x 10 mm plate with a central M12-sized through hole and chamfered/countersunk relief features; likely a spacer, clamp plate, mounting pad, or load-spreading plate for a bolted joint in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91F2_plate_80x80x10_M12.step; research/ream250_bom/ream250_bom_row_0292_91F2__views_2x2.png"
    cited_fact_or_basis: "BOM row 292 and manifest row 292 identify item 91F2 with quantity 3 and CAD file 91F2_plate_80x80x10_M12. FreeCAD measured one solid with bounding box 80.00 x 80.00 x 10.00 mm. The rendered top view shows a square plate with a central round hole and diagonal relief/chamfer features."
    evidence_basis: "bom_provided"
  assumptions:
    - "The central feature is treated as M12-sized because the row CAD name includes M12 and the preview shows a central circular through feature."
    - "The exact installation location is not named in the BOM row, so the functional role is inferred from plate geometry and bolt-hole form."
  uncertainty_notes:
    - "The BOM row does not state the parent assembly or mating parts, so spacer versus clamp versus mounting-pad usage remains uncertain."
mass:
  value_kg: 0.496
  basis: "Per-unit mass from FreeCAD volume 63161.452 mm^3 = 0.000063161452 m^3 multiplied by local assembly STEP material density 7850 kg/m^3 for Steel, Mild, giving 0.495817 kg per plate. BOM quantity is 3, so row total is about 1.49 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91F2_plate_80x80x10_M12.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 63161.452 mm^3, area 16132.875 mm^2, and bounding box 80.00 x 80.00 x 10.00 mm. Local STEP material extraction from 00_assembly.step for product 91F2_plate_80x80x10_M12 reports material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP-export density is interpreted as kg/m^3, consistent with the extractor note for the reAM250 export."
    - "The CAD solid volume already accounts for the central hole and chamfered/recessed features."
  uncertainty_notes:
    - "Mass excludes paint, coating, burrs, and any separate fasteners or inserts not represented in this single CAD solid."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 91F2_plate_80x80x10_M12 reports material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata gives mild steel but no specific alloy grade, heat treatment, coating, or surface finish."
how_to_make:
  summary: "Procure or locally fabricate as a simple mild-steel plate: cut an 80 x 80 x 10 mm blank from mild-steel plate stock, drill or machine the central M12 clearance/tapped feature as required by the mating fastener, add the visible chamfer/countersink or diagonal relief geometry, deburr, and apply any required corrosion-protection finish."
  manufacturing_steps:
    - "Cut square blank from 10 mm mild-steel plate stock."
    - "Drill, bore, or tap the central M12-sized feature according to the mating bolt requirement."
    - "Mill or countersink the visible relief/chamfer geometry around the central feature."
    - "Deburr edges and inspect hole location, plate thickness, and flatness."
    - "Apply finish or coating if required by the surrounding assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91F2_plate_80x80x10_M12.step; research/ream250_bom/ream250_bom_row_0292_91F2__views_2x2.png"
    cited_fact_or_basis: "CAD geometry shows a one-piece square plate, 80.00 x 80.00 x 10.00 mm, with a central round M12-named feature and visible chamfer/relief faces. targeted_web_search: searched \"91F2 plate_80x80x10_M12\", \"91F2 80x80x10 M12 plate\", and \"91F2_plate_80x80x10_M12 material\"; results did not provide a row-specific vendor drawing, process sheet, or catalog route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because no row-specific manufacturing document was found, standard plate-cutting and drilling/milling operations are assumed from the simple steel-plate geometry."
    - "Whether the central M12 feature is a clearance hole, tapped hole, or countersunk/counterbored feature should be checked against mating hardware before final fabrication."
  uncertainty_notes:
    - "No source states tolerances, flatness, surface finish, edge-break size, coating, or whether the M12 feature is threaded."
kb_implications:
  - "item_granularity: simple_part - Model as one reusable custom mild-steel plate/spacer/mounting block, not as an assembly or purchased module; consolidate with similar steel plates if later KB work finds equivalent dimensions within the 5x approximation rule."
---
