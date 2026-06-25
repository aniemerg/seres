---
row_identity:
  item: "25"
  cad_file: "25_frame_z_axis"
  source_row_number: 248
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Tall square structural frame for the reAM250 Z-axis assembly; it provides the vertical support envelope for Z-axis motion hardware or build/lift-axis structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/25_frame_z_axis.step; research/ream250_bom/ream250_bom_row_0248_25__views_2x2.png"
    cited_fact_or_basis: "BOM row 248 states item 25, quantity 1, CAD file 25_frame_z_axis. Manifest row 248 maps the same row to matched part STEP gold_export/parts/25_frame_z_axis.step. FreeCAD measured one solid with bounding box about 400.00 x 400.00 x 962.00 mm, and the rendered contact sheet shows a tall square open frame."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD filename's z_axis wording is interpreted as the location/function of the frame in the Z-axis subsystem."
  uncertainty_notes:
    - "The row does not identify the exact attached rails, screw, build plate, or lift mechanism, so the function is limited to structural support for the Z-axis assembly rather than a complete motion module."
mass:
  value_kg: 46.224
  basis: "FreeCAD volume 5,777,974.343 mm^3 equals 0.005777974343 m^3. Assembly STEP material metadata for 25_frame_z_axis reports Stainless Steel with density 8000 kg/m^3. Per-unit mass is 0.005777974343 m^3 * 8000 kg/m^3 = 46.2238 kg. BOM quantity is 1, so the row total is also about 46.224 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/25_frame_z_axis.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid with volume about 5,777,974.343 mm^3, area about 1,038,048.988 mm^2, and bounding box about 400.00 x 400.00 x 962.00 mm. Local assembly STEP material extraction matched 25_frame_z_axis to material Stainless Steel with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The matched STEP solid volume is used as the physical-volume proxy for one BOM row item."
    - "The assembly STEP density is treated as kg/m^3-like metadata, consistent with the reAM250 extractor note."
  uncertainty_notes:
    - "The STEP export represents the frame as one solid, so it does not expose separate tube, weld, fastener, or machining allowance masses."
material:
  primary_material: "stainless steel structural frame material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 25_frame_z_axis matched material Stainless Steel with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "No more specific stainless alloy grade is inferred beyond the STEP material family."
  uncertainty_notes:
    - "The CAD metadata does not state a stainless grade, heat treatment, surface finish, or passivation requirement."
how_to_make:
  summary: "Fabricate as a stainless structural frame by cutting tube or bar members to length, fixturing them square, welding or otherwise joining the corners and braces, then cleaning, straightening, and inspecting the frame against the STEP dimensions."
  manufacturing_steps:
    - "Cut stainless tube or bar stock for the four vertical members and square top/bottom perimeter members implied by the contact sheet."
    - "Fixture the members to the 400 x 400 mm square footprint and 962 mm height so the frame stays straight and square during joining."
    - "Weld, braze, or mechanically join the frame members; use welding as the nominal local-manufacturing route for a stiff stainless machine frame."
    - "Clean and passivate or otherwise finish the stainless surfaces as required for the AM machine environment."
    - "Inspect overall height, squareness, mounting faces, and any rail/interface locations against the STEP model before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/25_frame_z_axis.step; research/ream250_bom/ream250_bom_row_0248_25__views_2x2.png"
    cited_fact_or_basis: "CAD geometry and preview show one tall open square stainless frame about 400.00 x 400.00 x 962.00 mm. targeted_web_search: searched \"25_frame_z_axis\", \"reAM250 frame_z_axis\", \"Renishaw AM250 z axis frame material\", and \"Renishaw AM250 25_frame_z_axis\"; results found duplicate BOM listings and general AM250/Z-axis references, but no row-specific manufacturing drawing or fabrication procedure."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The open-frame geometry is better modeled as fabricated from cut structural members than as a single casting or additive-manufactured block."
    - "Welding is selected as the nominal route because it is the common low-volume route for stainless machine frames of this scale."
  uncertainty_notes:
    - "The exact member cross-sections, weld details, tolerances, and post-weld machining requirements are not available from the BOM row or STEP metadata."
kb_implications:
  - "item_granularity: complex_module - Model this as a stainless Z-axis structural frame assembly made from repeated cut frame members, with later decomposition into tube/bar stock and welding steps if detailed local fabrication is needed."
---

Research result for reAM250 BOM row 248.
