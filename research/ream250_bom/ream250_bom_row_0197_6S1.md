---
row_identity:
  item: 6S1
  cad_file: 6S1_support_1
  source_row_number: 197
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Small steel support/mounting rib used as part of the motor mount structure.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6S1_support_1.step; research/ream250_bom/ream250_bom_row_0197_6S1__views_2x2.png
    cited_fact_or_basis: >-
      BOM row 197 identifies item 6S1, quantity 1, CAD file 6S1_support_1,
      description "motor mount"; the rendered CAD preview shows a small
      triangular wedge/rib support with bounding box about 26.33 mm x 3.17 mm x
      16.67 mm.
    evidence_basis: bom_provided
  assumptions:
    - The single CAD solid represents one physical 6S1 item because the manifest maps row 197 to one matched-existing part instance.
  uncertainty_notes:
    - The CAD and BOM identify this as part of a motor mount, but they do not show the surrounding motor interface in this per-part result.
mass:
  value_kg: 0.00549
  basis: Per-unit mass for one 6S1 support. FreeCAD measured volume 699.825 mm^3; assembly STEP material metadata gives density 7850 kg/m^3, so 699.825e-9 m^3 * 7850 kg/m^3 = 0.00549 kg. BOM quantity is 1, so the row total is also about 0.00549 kg.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6S1_support_1.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: >-
      FreeCAD read one solid with volume 699.825 mm^3 and bounding box about
      26.33 mm x 3.17 mm x 16.67 mm; local STEP material extraction matched
      product 6S1_support_1 to material "Stahl-1" with density 7850 kg/m^3.
    evidence_basis: bom_provided
  assumptions:
    - The exported STEP volume is treated as the finished solid volume for one item.
  uncertainty_notes:
    - Mass excludes any separate fasteners or mating motor-mount parts because this row is only 6S1_support_1.
material:
  primary_material: Steel, STEP material name "Stahl-1".
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: >-
      Local assembly STEP material extraction for product 6S1_support_1 returned
      material "Stahl-1" and density 7850 kg/m^3.
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - The material is resolved to steel family, but no alloy grade, heat treatment, or coating is provided by the local metadata.
how_to_make:
  summary: Make as a small steel support from CAD geometry, most plausibly by cutting or milling the triangular profile from steel stock and deburring/finishing before motor-mount assembly.
  manufacturing_steps:
    - Cut a steel blank or near-net triangular profile sized to the CAD bounding box.
    - Mill, grind, or file the wedge faces to match the CAD profile and thickness.
    - Deburr edges, apply any required corrosion-protection finish, and inspect fit against the mating motor-mount parts.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6S1_support_1.step; https://www.xometry.com/sheet-metal-fabrication/custom-metal-bracket-fabrication/; https://www.approvedmachining.com/custom-machined-motor-mounts
    cited_fact_or_basis: >-
      The CAD preview shows a simple steel wedge/rib support without visible
      purchased-module features. Xometry describes custom metal brackets as
      manufacturable by CNC machining, sheet metal fabrication, or 3D printing;
      Approved Machining describes custom machined motor mounts made to
      submitted 3D CAD data in aluminum or carbon steel. targeted_web_search:
      queries tried were "motor mount triangular steel support bracket
      manufacturing laser cut machined wedge bracket" and "steel motor mount
      support bracket fabrication plate machined laser cut"; results supported
      generic bracket/motor-mount fabrication routes but did not identify a
      row-specific 6S1 vendor process.
    evidence_basis: engineering_hypothesis
  assumptions:
    - Because the local package gives geometry and steel material but not process history, the route is selected as a plausible low-complexity fabrication path for a small steel support.
  uncertainty_notes:
    - The exact original manufacturing method could have been machining, cutting from plate, additive manufacturing, or another workshop process; the result only needs a plausible KB planning route.
kb_implications:
  - "item_granularity: simple_part - Model 6S1 as a reusable small steel support/bracket part rather than a purchased module; it has one CAD solid, one material family, and no sub-BOM evidence."
---
