---
row_identity:
  item: "91C"
  cad_file: "91C_angle_profile_DIN_59370_50x5_200"
  source_row_number: 288
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Short 200 mm length of sharp-edged equal steel L-angle profile, likely used as a small structural bracket, spacer, stiffener, or mounting rail in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91C_angle_profile_DIN_59370_50x5_200.step; research/ream250_bom/ream250_bom_row_0288_91C__views_2x2.png"
    cited_fact_or_basis: "BOM row 288 names item 91C as quantity 3, cad file 91C_angle_profile_DIN_59370_50x5_200, description sharp-edged L-profile. CAD geometry is one solid with 50.00 x 50.00 x 200.00 mm bounding box; preview shows an L-shaped angle section."
    evidence_basis: "bom_provided"
  assumptions:
    - "Function is inferred from the row name and angle-section geometry because the BOM row does not name the parent mounting location."
  uncertainty_notes:
    - "Exact installation location and load case are not identified from this row alone."
mass:
  value_kg: 0.746
  basis: "Per-unit mass for one 200 mm angle profile: FreeCAD volume 95042.920 mm^3 = 9.504292e-5 m^3, multiplied by row-specific STEP density 7850 kg/m^3 gives 0.746 kg. BOM quantity is 3, so row total is about 2.24 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91C_angle_profile_DIN_59370_50x5_200.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 95042.920 mm^3, surface area 40864.588 mm^2, and 50.00 x 50.00 x 200.00 mm bounding box. Assembly STEP material extraction for this product returned Steel, Mild with density 7850.0; local material properties list generic steel density as 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single exported CAD solid represents one physical BOM-row item."
    - "The STEP density is interpreted as kg/m^3, consistent with the extractor note for this reAM250 export."
  uncertainty_notes:
    - "CAD volume is used directly; any unmodeled small chamfers, burrs, or cut-end finish are below the precision needed for this BOM estimate."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Assembly STEP material extraction matched product 91C_angle_profile_DIN_59370_50x5_200 to material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The export does not specify a more exact steel grade such as S235JR, so the material should remain mild steel unless later vendor or drawing evidence narrows it."
how_to_make:
  summary: "Locally make as a DIN 59370-style bright square-edge equal steel angle, 50 x 50 x 5 mm nominal section, then cut to 200 mm length and deburr the cut ends"
  manufacturing_steps:
    - "Start from mild-steel flat/strip or commercial bright square-edge equal angle stock."
    - "Form the sharp-edged L profile by rolling, press-brake forming, or equivalent profile-forming operation suitable for 5 mm steel."
    - "Cut the profile to 200 mm length."
    - "Deburr and inspect length, leg dimensions, and squareness before assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://webstore.ansi.org/standards/din/din593701978"
    cited_fact_or_basis: "BOM row identifies a sharp-edged L-profile with CAD filename DIN_59370_50x5_200. ANSI's DIN 59370 listing identifies the standard as steel sections, bright square-edge equal angles, covering dimensions, permissible deviations, and weights. targeted_web_search: searched 'DIN 59370 sharp edged L profile angle steel 50x5 material manufacturing hot rolled' and 'DIN 59370 L profile sharp-edged angle profile steel'; results confirmed standard/profile identity but did not provide a row-specific manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The 50x5_200 filename is interpreted as 50 x 50 x 5 mm equal angle cut to 200 mm, consistent with the CAD bounding box and measured volume."
    - "The inferred from common steel angle/profile production and cut-to-length practice, not from a row-specific process drawing."
  uncertainty_notes:
    - "The exact original supply route, surface finish, and forming process are not specified by the BOM row."
kb_implications:
  - "item_granularity: simple_part - Treat this as reusable cut-to-length steel angle stock/profile rather than a machine-specific assembly; later KB modeling can represent standard angle stock plus a cutting operation."
---

