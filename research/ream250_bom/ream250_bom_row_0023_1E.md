---
row_identity:
  item: 1E
  cad_file: 1E_adapter_hinge
  source_row_number: 23
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Custom hinge adapter block used with the nearby reAM250 door hinge hardware, providing a bolted offset/interface piece between the hinge assembly and the local frame or door geometry.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1E_adapter_hinge.step; research/ream250_bom/ream250_bom_row_0023_1E__views_2x2.png
    cited_fact_or_basis: "BOM row 23 names item 1E as 1E_adapter_hinge with quantity 2; adjacent rows 20-22 are Pfeiffer Vacuum door hinge parts. The supplied STEP is one matched part, and the rendered preview shows a rectangular wedge/block with two through holes suitable for bolted hinge adaptation."
    evidence_basis: bom_provided
  assumptions:
    - The adapter belongs to the same door hinge interface implied by adjacent BOM rows 1D1, 1D2, and 1D3.
  uncertainty_notes:
    - The BOM does not state the exact mating side or fastener specification, so the function is resolved at interface level rather than detailed installation geometry.
mass:
  value_kg: 0.443
  basis: "Per physical adapter, not row total. FreeCAD measured one solid with volume 56363.230 mm^3 and bounding box 78.00 x 44.00 x 27.00 mm; using generic steel density 7850 kg/m^3 from kb/materials/properties.yaml gives 0.4425 kg per adapter. BOM quantity is 2, so the row total would be about 0.885 kg."
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1E_adapter_hinge.step; kb/materials/properties.yaml
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 56363.229938 mm^3, area 14203.140498 mm^2, and bounding box 78 x 44 x 27 mm. Local material properties list generic steel density as 7850 kg/m^3. targeted_web_search: queries tried: \"1E_adapter_hinge\" reAM250; \"1E\" \"adapter hinge\" reAM250; \"reAM250\" \"adapter hinge\". Result: only reAM250 BOM listings were found for this row, with no row-specific material or catalog mass."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The CAD volume represents one physical adapter.
    - Generic steel is used as the planning density because the part is a compact structural hinge adapter and no sourced material grade was found.
  uncertainty_notes:
    - If the actual adapter is aluminum, the per-unit mass would be about 0.152 kg; if stainless steel, it would be about 0.451 kg.
material:
  primary_material: unknown metal/alloy
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1E_adapter_hinge.step
    cited_fact_or_basis: "Assembly STEP material extraction for 1E_adapter_hinge returned only material Generic with density 1000.0, which is placeholder metadata. The CAD geometry is a small structural bolted adapter block. targeted_web_search: queries tried: \"1E_adapter_hinge\" reAM250; \"1E\" \"adapter hinge\" reAM250; \"reAM250\" \"adapter hinge\" material. Result: no row-specific vendor, material grade, or drawing source was found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - Treat as a metal structural part for later planning because the geometry and hinge-load role are not consistent with a seal, adhesive, or electronic module.
  uncertainty_notes:
    - The exact alloy family and grade remain unresolved; steel, stainless steel, or aluminum would all be plausible depending on stiffness, corrosion, and matching hardware requirements.
how_to_make:
  summary: Machine as a small custom hinge adapter from rectangular metal stock, then deburr and install with the mating hinge fasteners.
  manufacturing_steps:
    - Cut rectangular metal bar or plate stock to the approximate blank size.
    - Mill the angled/recessed faces and outside profile shown in the CAD.
    - Drill the two through holes and deburr edges.
    - Inspect hole spacing and fit against the hinge and frame or door interface before installation.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1E_adapter_hinge.step; research/ream250_bom/ream250_bom_row_0023_1E__views_2x2.png
    cited_fact_or_basis: "The supplied CAD preview shows a compact custom block with planar faces, wedge/recess geometry, and two through holes. targeted_web_search: queries tried: \"1E_adapter_hinge\" reAM250 manufacturing; \"1E\" \"adapter hinge\" reAM250 drawing; \"reAM250\" \"adapter hinge\" material. Result: no row-specific manufacturing drawing or vendor route was found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - Conventional subtractive machining is the simplest plausible route for a two-piece-count custom adapter of this size and geometry.
  uncertainty_notes:
    - The route is inferred from geometry; the source package does not state whether the original part was milled, printed, cast, or modified from a standard bracket.
kb_implications:
  - "item_granularity: simple_part - Model as a reusable custom machined hinge adapter, not as raw stock or a purchased module; later KB work can parameterize material and hole pattern if more hinge-interface data is found."
---
