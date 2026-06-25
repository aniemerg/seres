---
row_identity:
  item: 3S47
  cad_file: 3S47_part_7
  source_row_number: 158
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: >
    Thin formed panel for the gas outlet subassembly, likely acting as one
    segment of an outlet duct, guide vane, or baffle surface that helps shape
    inert-gas flow leaving the outlet region.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S47_part_7.step; research/ream250_bom/ream250_bom_row_0158_3S47__views_2x2.png
    cited_fact_or_basis: >
      BOM row 158 identifies item 3S47, quantity 1, as "gas outlet: part 7";
      the manifest maps it to 3S47_part_7.step. FreeCAD measured one solid with
      bounding box about 8.00 x 50.00 x 90.71 mm, and the rendered preview shows
      a thin folded sheet-like panel with lips/creases.
    evidence_basis: bom_provided
  assumptions:
    - The row belongs to the multi-part gas outlet group represented by adjacent BOM rows 3S41 through 3S48.
  uncertainty_notes:
    - The exact installed orientation and flow-interface role are not stated in the BOM or STEP metadata.
mass:
  value_kg: 0.0359
  basis: >
    Per-unit estimate for quantity 1. FreeCAD volume is 4487.058 mm^3, equal to
    4.487058e-6 m^3. Using an 8000 kg/m^3 stainless-steel-density proxy from
    kb/materials/properties.yaml gives 0.035896 kg, rounded to 0.0359 kg.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S47_part_7.step; kb/materials/properties.yaml
    cited_fact_or_basis: >
      FreeCAD measured one solid, volume 4487.058 mm^3, surface area
      9264.743 mm^2, and bounding box about 8.00 x 50.00 x 90.71 mm.
      kb/materials/properties.yaml lists stainless_steel density as
      8000 kg/m^3. targeted_web_search: queries tried "reAM250 gas outlet part
      3S47 material", "Renishaw reAM250 gas outlet material", and "reAM250
      additive manufacturing machine gas outlet stainless steel"; results
      confirmed the reAM250/AM250 context as metal powder-bed-fusion equipment
      but did not provide a row-specific material or mass.
    evidence_basis: engineering_hypothesis
  assumptions:
    - The CAD solid volume is a usable proxy for one physical item in this BOM row.
    - Stainless-steel density is used as a conservative proxy for a thin metal gas-flow panel in a powder-bed-fusion machine.
  uncertainty_notes:
    - If the actual part is aluminum or another lighter alloy, mass could be roughly 3x lower.
    - The STEP assembly material extractor returned only Generic with density 1000.0, so it does not resolve physical material.
material:
  primary_material: unknown corrosion-resistant sheet metal/alloy
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S47_part_7.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://davidwenzler.github.io/reAM250/
    cited_fact_or_basis: >
      CAD geometry shows a thin folded panel in the gas outlet group. The local
      assembly STEP material extractor matched 3S47_part_7 but reported only
      Generic and density 1000.0, which is placeholder metadata. The reAM250
      project page describes the machine as a powder bed fusion of metals
      research platform. targeted_web_search: queries tried "reAM250 gas outlet
      part 3S47 material", "Renishaw reAM250 gas outlet material", and
      "reAM250 additive manufacturing machine gas outlet stainless steel";
      no row-specific usable material source was found.
    evidence_basis: engineering_hypothesis
  assumptions:
    - A gas outlet panel inside or near an inert-gas flow path is more likely to be metal sheet than polymer because of heat, spatter, powder, and cleaning exposure.
  uncertainty_notes:
    - No source identified a specific grade, so later KB modeling should keep this broad unless the original CAD or drawings provide material callouts.
how_to_make:
  summary: >
    Plausible route is sheet-metal fabrication: cut a flat blank from
    Corrosion-resistant metal sheet, form the lips/creases with a press brake or
    Simple forming fixture, deburr, clean, and inspect fit in the gas outlet
    Assembly.
  manufacturing_steps:
    - Cut the blank profile from thin corrosion-resistant sheet stock by laser, waterjet, shear, or CNC routing.
    - Form the long lip and angled crease features with a press brake or matched fixture.
    - Deburr edges and clean surfaces for powder-bed-fusion machine service.
    - Inspect envelope and fit against the neighboring gas outlet parts.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S47_part_7.step; research/ream250_bom/ream250_bom_row_0158_3S47__views_2x2.png; https://github.com/DavidWenzler/reAM250
    cited_fact_or_basis: >
      CAD and preview show a thin folded panel with simple planar faces and no
      Complex machined pockets. The reAM250 repository identifies the platform
      As a metal laser powder-bed-fusion research machine. targeted_web_search:
      Queries tried "reAM250 gas outlet part 3S47 material", "Renishaw reAM250
      Gas outlet material", and "reAM250 additive manufacturing machine gas
      Outlet stainless steel" no row-specific manufacturing drawing or vendor
      Process note was found.
    evidence_basis: engineering_hypothesis
  assumptions:
    - The visible folds are intentional formed sheet features rather than a thick machined solid.
    - Prioritize common sheet-metal operations over machining from billet.
  uncertainty_notes:
    - Without an assembly drawing, bend sequence, bend radii, and tolerances are unknown.
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable formed sheet-metal baffle/panel for gas-flow ducting rather than as a purchased calibrated module."
---
