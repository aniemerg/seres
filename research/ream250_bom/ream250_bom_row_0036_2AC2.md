---
row_identity:
  item: 2AC2
  cad_file: 2AC2_part_2
  source_row_number: 36
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Bottom-axis supported bearing block for the reAM250 lower axis bearing assembly; it radially supports the lower ballscrew or shaft end and provides the mounting/alignment envelope for that bearing point.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0036_2AC2__views_2x2.png; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127; https://po-center.ru/HIWIN/hiwin_compact.pdf"
    cited_fact_or_basis: "BOM row 36 lists item 2AC2, quantity 1, CAD file 2AC2_part_2, description 'axis bearing bottom'. The manifest maps the row to assembly context 2AC0_bottom_axis_bearing_SLA10 and notes that 2AC2_part_2 imports with zero solids. FreeCAD measured the retained context bbox as 86.00 x 24.00 x 58.00 mm, and the rendered preview shows a pillow-block-like support with a central bearing bore, mounting feet, and through holes. HIWIN identifies SLA10 as a supported bearing for 16 mm shaft nominal diameter; the HIWIN compact catalog lists SLA-10 dimensions L 86, B 24, H 58 mm and 6200.2RS bearing."
    evidence_basis: independent_vendor_spec
  assumptions:
    - The row label 2AC2_part_2 is interpreted through the matched 2AC0_bottom_axis_bearing_SLA10 assembly context because the row-specific product imports with no solids.
    - The SLA10 string in the CAD parent assembly identifies the same supported-bearing family as the HIWIN SLA10 product data.
  uncertainty_notes:
    - The exact 2AC2 subpart cannot be isolated from the supplied CAD; it may represent one occurrence or subcomponent within the bottom-axis bearing assembly rather than the whole commercial bearing block.
mass:
  value_kg: 0.53
  basis: "Per-unit mass for BOM quantity 1. FreeCAD measured the retained SLA10 assembly context volume as 67013.783 mm3. Using a steel-family effective density from kb/materials/properties.yaml gives 67013.783 mm3 x 1e-9 m3/mm3 x 7850 kg/m3 = 0.526 kg, rounded to 0.53 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/2AC0_bottom_axis_bearing_SLA10.step; kb/materials/properties.yaml; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127; https://po-center.ru/HIWIN/hiwin_compact.pdf"
    cited_fact_or_basis: "FreeCAD measured 6 solids, volume 67013.783 mm3, area 20516.186 mm2, and bbox 86.00 x 24.00 x 58.00 mm for the retained assembly context. The local density table gives generic steel density as 7850 kg/m3. HIWIN's SLA10 product page and compact catalog match the context dimensions and identify the unit as a supported bearing using 6200.2RS. No row-specific catalog weight was found. targeted_web_search: tried 'SLA10 bearing weight', 'HIWIN SLA10 mass weight', 'HIWIN SLA10 supported bearing material weight', and '2AC2_part_2 axis bearing bottom mass'; results matched the SLA10 identity and dimensions but did not provide a row-specific mass."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The available parent assembly volume is used as the row-level mass proxy because the manifest says 2AC2_part_2 has zero imported solids.
    - A steel-family effective density is used for the full context, even though the bearing unit can include bearing steel, seals, lubricant, and retaining hardware.
  uncertainty_notes:
    - If the isolated 2AC2 product is only a housing half, retainer, bearing insert, or other subcomponent, its actual per-unit mass may be substantially lower than 0.53 kg.
    - The all-steel-density estimate does not resolve mixed-material fractions or voids beyond what is represented by the CAD volume.
material:
  primary_material: steel-family supported bearing unit; catalog-level stack is steel pillow block housing, deep-groove ball bearing 62...2RS, and DIN 471 circlip
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://po-center.ru/HIWIN/hiwin_compact.pdf; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "Local STEP material extraction for 2AC2_part_2 returned only Generic with density 1000.0, which is placeholder metadata. The HIWIN compact catalog describes the SLA supported bearing as a floating bearing consisting of steel pillow block housing, deep-groove ball bearing DIN 625 62...2RS, and circlip DIN 471; the SLA10 line identifies 6200.2RS. HIWIN's SLA10 product page independently matches the row context as type SLA10. targeted_web_search: tried 'HIWIN SLA supported bearing steel pillow block housing', 'HIWIN SLA10 material housing', 'HIWIN SLA10 6200.2RS circlip material', and '2AC2_part_2 material'; results found catalog-level component material for the SLA family but no row-specific material grade."
    evidence_basis: independent_vendor_spec
  assumptions:
    - The catalog's SLA supported-bearing material stack is applied to the row because the CAD parent assembly name and dimensions match SLA10.
    - Bearing/seal details are retained as a component material set rather than collapsed into a single alloy grade.
  uncertainty_notes:
    - Exact housing alloy/grade, bearing steel grade, seal elastomer, lubricant, and heat treatment are not resolved for 2AC2.
    - The CAD metadata itself does not confirm material; it only provides placeholder Generic material.
how_to_make:
  summary: "Precision fabrication of the steel pillow-block housing, installation of a 6200.2RS bearing and DIN 471 circlip, then alignment and fit inspection"
  manufacturing_steps:
    - "Machine as assembled from precision motion components"
    - Machine or cast the pillow-block housing to the 86 mm x 24 mm x 58 mm envelope with the bearing seat, mounting holes, and alignment stop features.
    - Install or locally manufacture a 6200.2RS deep-groove bearing, fit the circlip/retainer, lubricate as required, and inspect bore alignment and radial support function in the bottom-axis assembly.
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0036_2AC2__views_2x2.png; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127; https://po-center.ru/HIWIN/hiwin_compact.pdf"
    cited_fact_or_basis: "HIWIN identifies SLA10 as a ready supported bearing, and the compact catalog states the SLA supported-bearing stack as steel pillow block housing, deep-groove ball bearing 62...2RS, and DIN 471 circlip. The rendered CAD context shows a compact bearing block with a central bore, mounting feet, and through holes. The detailed machining/casting, bearing manufacture, assembly, and inspection route is inferred from the geometry and catalog component stack rather than directly stated as a manufacturing process. targeted_web_search: tried 'HIWIN SLA10 manufacturing housing material', 'SLA10 supported bearing manufacturing process', 'bearing pillow block manufacturing process', and '2AC2_part_2 manufacturing'; results did not provide a row-specific manufacturing route."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The manufacturing route assumes conventional bearing-block construction with a precision bearing seat, standard rolling bearing insertion, and retainer hardware.
  uncertainty_notes:
    - Local manufacturing details such as fits, tolerances, surface finish, heat treatment, seal specification, and quality checks require a manufacturer drawing or teardown before process modeling.
kb_implications:
  - "item_granularity: complex_module - Model this row as a functional SLA10-class supported bearing complex module for this pass; split into housing, 6200.2RS bearing, circlip/seal, lubricant, and assembly operations only if later KB work needs bearing-unit closure."
---
