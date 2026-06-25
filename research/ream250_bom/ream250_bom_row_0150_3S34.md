---
row_identity:
  item: 3S34
  cad_file: 3S34_part_4
  source_row_number: 150
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Fabricated outlet duct segment in the reAM250 process-gas path, carrying gas through part of the gas outlet pipe assembly.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S34_part_4.step; research/ream250_bom/ream250_bom_row_0150_3S34__views_2x2.png
    cited_fact_or_basis: >-
      BOM row 150 names item 3S34 as "gas outlet pipe: part 4"; the manifest
      maps the same row to 3S34_part_4.step; FreeCAD measured one solid with a
      60.00 x 60.00 x 270.00 mm bounding box; the rendered views show a hollow
      square-section duct segment with a sloped or offset end.
    evidence_basis: bom_provided
  assumptions:
    - The numbered "part 4" label means this row is one segment of a larger gas outlet pipe assembly rather than a standalone gas-handling subsystem.
  uncertainty_notes: []
mass:
  value_kg: 0.765
  basis: Per-unit estimate for quantity 1. FreeCAD measured material volume as 97440.000 mm^3, equal to 0.00009744 m^3. Using the local generic steel density of 7850 kg/m^3 gives 0.764904 kg, rounded to 0.765 kg.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S34_part_4.step; kb/materials/properties.yaml
    cited_fact_or_basis: >-
      FreeCAD measured one solid, volume 97440.000 mm^3, area 98752.390 mm^2,
      and bounding box 60.00 x 60.00 x 270.00 mm; kb/materials/properties.yaml
      lists generic steel density as 7850 kg/m^3.
    evidence_basis: engineering_hypothesis
  assumptions:
    - The CAD solid volume is treated as the physical material volume of one BOM-row item.
    - Generic steel density is used as a planning constant for a rigid metal outlet pipe because no row-specific material was provided.
  uncertainty_notes:
    - 'targeted_web_search: queries tried "reAM250 3S34 gas outlet pipe part 4 material", "reAM250 gas outlet pipe additive manufacturing machine material", "Renishaw AM250 gas outlet pipe material", and "Renishaw AM250 gas outlet pipe"; results gave general reAM250/AM250 gas-flow context but no row-specific material or catalog mass.'
    - The mass is material-sensitive; the same CAD volume would be about 0.263 kg in aluminum at 2700 kg/m^3 or about 0.780 kg in stainless steel at 8000 kg/m^3.
material:
  primary_material: unknown metal/alloy duct material
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S34_part_4.step
    cited_fact_or_basis: >-
      BOM row 150 has blank Material family and Specific material / grade
      fields; assembly STEP material extraction for 3S34_part_4 returned
      material "Generic" and density 1000.0, which is placeholder metadata; the
      part STEP and preview show a rigid hollow pipe form.
    evidence_basis: engineering_hypothesis
  assumptions:
    - Treat the row as a metallic duct component for later planning because the CAD geometry is a thin-wall rigid pipe in a process-gas outlet assembly.
  uncertainty_notes:
    - 'targeted_web_search: queries tried "reAM250 3S34 gas outlet pipe part 4 material", "reAM250 gas outlet pipe additive manufacturing machine material", "Renishaw AM250 gas outlet pipe material", and "Renishaw AM250 gas outlet pipe"; no row-matched material specification was found.'
    - The exact alloy or grade remains unspecified, so corrosion, heat, and fabrication assumptions should be checked before detailed KB manufacturing work.
how_to_make:
  summary: Plausible route is to fabricate a short square-section metal duct segment from tube or sheet stock, cut the angled/offset end geometry, weld or form as needed, deburr, leak-check, and assemble into the gas outlet pipe run.
  manufacturing_steps:
    - Select square metal tube or folded sheet stock close to the 60 mm outer section.
    - Cut to the 270 mm envelope and create the angled transition faces shown in the CAD.
    - Weld, braze, or seam-close any formed-sheet edges if tube stock is not used.
    - Deburr internal edges and inspect for fit and gas-path obstructions.
    - Leak-check and install as one segment of the outlet pipe assembly.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S34_part_4.step; research/ream250_bom/ream250_bom_row_0150_3S34__views_2x2.png
    cited_fact_or_basis: >-
      CAD measurement and rendered views show one hollow, square-section,
      Thin-wall pipe segment with a 60.00 x 60.00 x 270.00 mm bounding box and
      Angled transition geometry.
    evidence_basis: engineering_hypothesis
  assumptions:
    - "Fabrication from metal tube or sheet is more plausible for KB planning than treating this as a calibrated module"
    - Normal workshop cutting, forming, welding or brazing, deburring, and leak-check operations are sufficient at this level of model fidelity.
  uncertainty_notes:
    - 'targeted_web_search: queries tried "reAM250 3S34 gas outlet pipe part 4 material", "reAM250 gas outlet pipe additive manufacturing machine material", "Renishaw AM250 gas outlet pipe material", and "Renishaw AM250 gas outlet pipe" no row-specific manufacturing drawing or vendor process route was found.'
    - The exact joining method depends on the unresolved alloy and how this segment interfaces with adjacent gas outlet pipe parts.
kb_implications:
  - 'item_granularity: simple_part - Model as a reusable fabricated duct or pipe segment, not as a purchased module or multi-part assembly, unless later source data shows an integrated subassembly.'
---
