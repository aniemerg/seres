---
row_identity:
  item: "6H1"
  cad_file: "6H1_powder_chute"
  source_row_number: 182
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Powder chute for guiding metal powder through the reAM250 powder-handling path; the CAD shows a long tapered chute or funnel-like duct with flanged lips."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6H1_powder_chute.step; research/ream250_bom/ream250_bom_row_0182_6H1__views_2x2.png"
    cited_fact_or_basis: "BOM row 182 lists item 6H1, quantity 1, and CAD file 6H1_powder_chute. FreeCAD measured one solid with volume 190359.520 mm^3 and a 352.00 x 85.75 x 202.00 mm bounding box; the rendered preview shows a long tapered chute with flanged lips."
    evidence_basis: "bom_provided"
  assumptions:
    - "The filename's 'powder_chute' wording is interpreted as the component's functional role in powder handling."
  uncertainty_notes:
    - "The row does not show the surrounding assembly, so the exact inlet/outlet orientation and mating interfaces are inferred from the chute form rather than locked by an assembly drawing."
mass:
  value_kg: 1.52
  basis: "FreeCAD volume 190359.520 mm^3 converts to 1.903595e-4 m^3. Using the local stainless_steel density table value of 8000 kg/m^3 gives about 1.52 kg per part."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6H1_powder_chute.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 190359.520 mm^3, area 298946.812 mm^2, and bounding box 352.00 x 85.75 x 202.00 mm. The local density table lists stainless_steel density as 8000 kg/m^3. targeted_web_search: searched \"6H1_powder_chute material\", \"6H1 powder chute reAM250 material\", \"reAM250 powder chute material\", and \"reAM250 6H1_powder_chute\"; found duplicate BOM/public reAM250 context but no row-specific material or mass source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid is treated as the complete per-unit geometry for one BOM row 6H1 part."
    - "A stainless/steel sheet-metal density scenario is used because the part is a rigid powder-contact chute in a metal PBF-LB/M machine and no resolved row-specific material source was found."
  uncertainty_notes:
    - "Mass depends on the unresolved material. If the part is aluminum rather than steel or stainless steel, the same CAD volume would imply about 0.51 kg using the local aluminum density of 2700 kg/m^3."
material:
  primary_material: "metal sheet/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0182_6H1__views_2x2.png; web targeted search"
    cited_fact_or_basis: "BOM row 182 names a powder chute but provides no material or manufacturer. Local assembly STEP material extraction for 6H1_powder_chute returned only placeholder material 'Generic' with density 1000.0. The rendered preview shows a rigid tapered chute body with flanged lips. targeted_web_search: searched \"6H1_powder_chute material\", \"6H1 powder chute reAM250 material\", \"reAM250 powder chute material\", and \"reAM250 6H1_powder_chute\"; found duplicate BOM/public reAM250 context but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A broad metal sheet/alloy family is inferred from the rigid chute geometry and powder-contact role in a metal powder bed fusion machine."
  uncertainty_notes:
    - "No row-specific source resolves the alloy or grade; stainless steel is plausible for powder contact and wear, but aluminum or another metal cannot be excluded from the current evidence."
how_to_make:
  summary: "Fabricate as a formed sheet-metal chute: cut blanks, bend or brake-form the tapered walls and flange lips, join seams as needed, then deburr and clean for powder handling."
  manufacturing_steps:
    - "Cut sheet-metal blanks for the tapered chute body and flange or lip features."
    - "Bend or brake-form the long tapered channel to the 352.00 x 85.75 x 202.00 mm CAD envelope."
    - "Join seams or corner details by welding, brazing, riveting, or folded seams depending on powder containment and cleanability requirements."
    - "Deburr, radius powder-contact edges, clean, and inspect the chute opening geometry and mating lips against the STEP model."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6H1_powder_chute.step; research/ream250_bom/ream250_bom_row_0182_6H1__views_2x2.png"
    cited_fact_or_basis: "FreeCAD measured one solid with a 352.00 x 85.75 x 202.00 mm bounding box; the contact-sheet preview shows a long tapered chute with thin-wall faces and flanged lips. targeted_web_search: searched \"6H1_powder_chute manufacturing\", \"6H1 powder chute reAM250 material\", \"reAM250 powder chute material\", and \"powder chute sheet metal fabrication\"; found duplicate BOM/public reAM250 context and generic fabrication context, but no row-specific manufacturing drawing or process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Sheet cutting and forming are chosen because the visible shape is a thin-wall tapered chute rather than a solid machined block."
    - "Seam-joining method remains a process choice because neither the BOM row nor CAD metadata specifies whether the chute must be welded, folded, or assembled from multiple pieces."
  uncertainty_notes:
    - "The CAD preview does not provide wall-thickness callouts, bend radii, tolerances, surface finish, or powder-cleanability requirements, so this is a plausible fabrication route rather than a complete process plan."
kb_implications:
  - "item_granularity: simple_part - one fabricated powder-contact chute that can be modeled as a simple formed sheet-metal part; defer exact alloy and seam details until a row-specific drawing or material source is found."
---

Research result for reAM250 BOM row 182.
