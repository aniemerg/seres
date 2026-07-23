---
row_identity:
  item: "2AD1"
  cad_file: "2AD1_part_1"
  source_row_number: 44
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Bearing insert/race subpart within the reAM250 top-axis SFA10 fixed bearing unit, locating the axis shaft and carrying radial and axial bearing loads."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0044_2AD1__views_2x2.png; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SFA/SFA10/p/18-000111"
    cited_fact_or_basis: "BOM row 44 identifies item 2AD1, quantity 1, CAD file 2AD1_part_1, description 'axis bearing top'. The full assembly STEP places 2AD1_part_1 under product 2AD0_top_axis_bearing_SFA10 and labels it PART-SFA10_FILE_11-DESC. HIWIN identifies SFA10 as an SFA fixed bearing, notes that the SFA fixed bearing is matched to SLA supported bearings, and lists SFA10 bearing type ZKLFA1050.2RS with axial dynamic and static load ratings. The rendered contact sheet shows a compact circular bearing-like part with a central bore and fastener/retainer features."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row-specific SFA10 parent assembly context is used to interpret the generic BOM description 'axis bearing top'."
    - "The part is treated as a bearing insert/race subpart rather than the complete SFA10 bearing unit because neighboring BOM rows list other SFA10 subparts separately."
  uncertainty_notes:
    - "The CAD export does not name the exact internal SFA10 component, so the function is resolved to bearing subpart level rather than a specific catalog subcomponent."
mass:
  value_kg: 0.154
  basis: "Per-unit estimate for quantity 1. FreeCAD measured volume 19578.005 mm^3, equivalent to 0.000019578 m^3. Using the local generic steel density 7850 kg/m^3 gives 0.000019578 m^3 * 7850 kg/m^3 = 0.1537 kg, rounded to 0.154 kg. The row total is also about 0.154 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD1_part_1.step; kb/materials/properties.yaml; https://www.albeco.com.pl/en/catalog/preview/podpory-lozyskowe-stale-sla-i-przesuwu-sfa.pdf"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 19578.005 mm^3, surface area 12515.448 mm^2, and bounding box about 35.29 x 28.00 x 50.00 mm. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. The SFA/SLA bearing-series catalog identifies SFA06/SFA10 component 1 as a steel pillow block housing and identifies the SFA10 bearing unit as including bearing type ZKLFA1050.2RS and lock nut HIR 10. targeted_web_search: searched '2AD1_part_1 axis bearing top material', 'SFA10 bearing material', 'SFA10 axis bearing', and 'SFA10 bearing block'; results found the row identity mirror plus HIWIN/SFA10 catalog data but no row-specific net mass."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The STEP solid is treated as the complete physical item represented by BOM row 44."
    - "Generic steel density is used as the planning density because SFA10 bearing-unit catalog data supports steel/bearing construction but does not give this subpart's exact grade or net mass."
  uncertainty_notes:
    - "The exact steel grade and any small non-steel inserts/coatings are unresolved, but they are unlikely to dominate mass at this scale."
material:
  primary_material: "steel bearing/housing material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.albeco.com.pl/en/catalog/preview/podpory-lozyskowe-stale-sla-i-przesuwu-sfa.pdf; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SFA/SFA10/p/18-000111"
    cited_fact_or_basis: "The full assembly STEP places 2AD1_part_1 inside 2AD0_top_axis_bearing_SFA10. The SFA/SLA catalog identifies SFA06/SFA10 component 1 as a steel pillow block housing and lists the SFA10 bearing and locknut elements; HIWIN identifies the SFA10 bearing type as ZKLFA1050.2RS. Local assembly STEP material extraction for 2AD1_part_1 returned only Generic with density 1000.0, which is placeholder metadata. targeted_web_search: searched '2AD1_part_1 material', 'SFA10 bearing material steel', and 'ZKLFA1050.2RS material'; no row-specific material grade was found."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row item uses steel-family bearing material because it is a subpart of an SFA10 bearing unit and the catalog identifies the relevant housing/bearing/locknut construction as steel/bearing hardware."
  uncertainty_notes:
    - "The exact bearing steel, heat treatment, and coating/plating are not identified by the BOM, STEP material metadata, or searched sources."
how_to_make:
  summary: "Machine and heat-treat steel bearing races or housing features, assemble with rolling elements/retainers, and inspect the bearing geometry"
  manufacturing_steps:
    - "Start from steel billet, tube, or forged blank sized for the bearing race/housing subpart."
    - "Turn and/or mill the central bore, outer bearing features, mounting/retainer geometry, and reference faces."
    - "Heat treat bearing-contact surfaces if this subpart is a race, then grind and finish critical bores and faces."
    - "Assemble with the remaining SFA10 bearing elements, rolling balls, locknut, and housing hardware."
    - "Inspect bore size, concentricity, face runout, fit to the SFA10 housing, and bearing rotation/load performance."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD1_part_1.step; research/ream250_bom/ream250_bom_row_0044_2AD1__views_2x2.png; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SFA/SFA10/p/18-000111"
    cited_fact_or_basis: "The STEP/contact sheet shows one compact bearing-like solid with a central bore and retainer/fastener features; HIWIN identifies SFA10 as a fixed bearing unit with bearing type ZKLFA1050.2RS and locknut HIR 10. targeted_web_search: searched 'SFA10 bearing manufacturing process', 'ZKLFA1050.2RS bearing manufacturing', and '2AD1_part_1 axis bearing top manufacturing'; no row-specific manufacturing route was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The detailed route is inferred from bearing race/housing geometry and SFA10 fixed-bearing function, not from a row-specific process drawing."
  uncertainty_notes:
    - "No source gives tolerances, bearing grade, hardness, preload, or factory assembly sequence for this subpart."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable steel bearing-unit subpart tied to an SFA10 fixed bearing assembly; defer a purchased-module split for the complete SFA10 unit and detailed bearing-race manufacturing until the surrounding bearing assembly is modeled."
---

Research result for reAM250 BOM row 44.
