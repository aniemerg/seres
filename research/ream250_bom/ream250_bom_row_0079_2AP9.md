---
row_identity:
  item: 2AP9
  cad_file: 2AP9_spring_block_front
  source_row_number: 79
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Front spring block in the 2AP build-platform/spring stack, likely providing a long edge support, spacer, or spring reaction surface for the adjacent spring plate and platform hardware.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP9_spring_block_front.step; research/ream250_bom/ream250_bom_row_0079_2AP9__views_2x2.png
    cited_fact_or_basis: "BOM row 79 names item 2AP9 as 2AP9_spring_block_front with quantity 1; neighboring rows include spring_plate, assembly_plate, heating_plate, lifting_platform, right/back/left spring blocks, spacer sleeves, shim disks, pressing_plate, and build_platform. FreeCAD measured one solid with bbox about 22.00 x 205.00 x 15.00 mm, and the rendered preview shows a long grooved block/rail form."
    evidence_basis: bom_provided
  assumptions:
    - The word "front" is interpreted as the side-specific member among the four spring block rows.
    - The block's function is inferred from row naming, neighboring BOM context, and CAD geometry rather than from an assembly drawing with explicit load paths.
  uncertainty_notes:
    - Exact contact faces, spring preload role, and mating parts remain uncertain without a fully interpreted assembly constraint model.
mass:
  value_kg: 0.422
  basis: "Per-unit estimate for quantity 1. FreeCAD volume is about 53766.281 mm^3, or 5.376628e-5 m^3. Using generic steel density from kb/materials/properties.yaml, 7850 kg/m^3, gives about 0.422 kg per block; an aluminum-family block of the same CAD volume would be about 0.145 kg, so the chosen value is a conservative ferrous-metal planning estimate."
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP9_spring_block_front.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: "FreeCAD measured one solid, volume 53766.281 mm^3, area about 16102.915 mm^2, and bbox about 22.00 x 205.00 x 15.00 mm. Local properties table gives generic steel density as 7850 kg/m^3. Assembly STEP material extractor matched this product only to Generic with density 1000.0, which does not identify a usable material. targeted_web_search: queries tried: \"2AP9_spring_block_front\", \"reAM250 spring_block_front\", \"spring block front reAM250\", and \"2AP9 spring_block_front\"; results found duplicated BOM listings or unrelated vehicle spring-block pages, with no row-specific material or catalog mass."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The STEP solid volume is treated as the physical per-unit part volume.
    - Generic steel density is used as a conservative effective density for a likely machined metal block because no row-specific material or mass source was found.
  uncertainty_notes:
    - The mass could be much lower if the part is aluminum or another light alloy; material uncertainty is the dominant mass uncertainty.
material:
  primary_material: unknown metal/alloy
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0079_2AP9__views_2x2.png
    cited_fact_or_basis: "BOM row 79 provides no material, manufacturer, product ID, or link URL. Assembly STEP material extraction for 2AP9_spring_block_front returns only Generic with density 1000.0. CAD preview shows a long grooved block compatible with a machined metal component. targeted_web_search: queries tried: \"2AP9_spring_block_front\", \"reAM250 spring_block_front\", \"spring block front reAM250\", and \"2AP9 spring_block_front\"; no row-specific material source was found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - A metal/alloy family is chosen because the row is a structural block in a heated build-platform area and the CAD form resembles a machined rail/block rather than a polymer seal or consumable.
  uncertainty_notes:
    - Specific grade, heat treatment, surface finish, and whether the block is steel or aluminum remain unresolved.
how_to_make:
  summary: "Plausible route is local fabrication from rectangular metal bar stock by sawing to length, milling the external profile and longitudinal grooves, drilling or machining any end features, deburring, and inspecting fit against the spring/platform stack"
  manufacturing_steps:
    - Cut rectangular metal bar stock to a blank slightly longer than the approximately 205 mm finished length.
    - Mill the long faces, grooves, and side-specific front geometry to match the STEP model.
    - Drill, slot, or finish end features visible in the CAD model as required by the mating hardware.
    - Deburr, clean, and inspect dimensions and flatness before assembly into the spring block set.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP9_spring_block_front.step; research/ream250_bom/ream250_bom_row_0079_2AP9__views_2x2.png
    cited_fact_or_basis: "CAD measurement and preview show a single long, narrow, grooved solid with bbox about 22.00 x 205.00 x 15.00 mm. The BOM names it as a side-specific spring block rather than a purchased vendor component. targeted_web_search: queries tried: \"2AP9_spring_block_front\", \"reAM250 spring_block_front\", \"spring block front reAM250\", and \"2AP9 spring_block_front\" no source stated a manufacturing process for this row."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The block is treated as a simple machined metal part rather than a calibrated module or casting.
    - Milling from bar stock is selected because the CAD shape is prismatic and low-volume custom fabrication is plausible for this machine.
  uncertainty_notes:
    - The route may change if the true material is a heat-treated steel, aluminum alloy, or surface-coated part with special thermal or wear requirements.
kb_implications:
  - "item_granularity: simple_part - Model later as one reusable side-specific machined spring/block rail or as a variant within a spring-block family, not as a purchased module."
---

Research result for reAM250 BOM row 79.
