# Machine identity

- Queue item: `machine_reality_precision_levels`
- KB item: `precision_levels`
- KB name: Precision levels
- KB file: `kb/items/machines/precision_levels.yaml`
- Current KB kind: `machine`
- Current mass: 3 kg
- Current BOM: `bom_precision_levels_v0`
- Current recipe: `recipe_precision_levels_v0`
- Current note: precision spirit levels and electronic levels for machine-tool leveling and alignment, 0.02 mm/m or better.

# KB usage and needed function

`precision_levels` is used by `precision_alignment_and_leveling_v0` along with `alignment_tools` and `labor_bot_general_v0`. The needed function is to measure small angular deviations during machine-frame leveling, machine-tool installation, way alignment, shimming, and iterative verification.

The KB's 3 kg mass is plausible for a cased precision machinist level or compact electronic level. The main issue is classification: this is calibrated metrology tooling, not a powered production machine.

# Reality classification

Real practical metrology tool set.

Precision machinist levels and electronic levels are standard industrial tools. The KB accuracy target of 0.02 mm/m matches commercial products. Treating the item as a "machine" is acceptable only if the KB uses `machine` broadly for required equipment; semantically it is better described as a precision metrology instrument or tool kit.

# Evidence links

- Digi-Pas lists the DWL-3500XY 2-axis precision digital machinist level with 0.001 degree resolution, equivalent to 0.02 mm/m, for leveling, angle, alignment, vibration measurement, and data logging: https://www.digipas.com/product/precision-measurement/2-axis-precision-digital-machinist-level/
- WYLER sells high-precision spirit levels and circular spirit levels to DIN877 and DIN2276/1, including horizontal, magnetic, frame, adjustable, micrometer, and crankpin spirit levels: https://www.wylerag.com/en/products/high-precision-spirit-levels/
- Level Developments sells precision machinist levels with 0.02 mm/m sensitivity and 200 mm bases: https://www.leveldevelopments.com/products/engineers-level/machinists-levels/pel-0-02-200-precision-machinists-level-0-02mm-m-200mm-base/
- Level Developments also sells electronic engineer's levels as high-precision digital machinist levels, with versions specified in arcseconds: https://www.leveldevelopments.com/products/engineers-level/precision-digital-levels/
- ALPA Metrology describes WYLER inclination/alignment products for geometric inspection, machine alignment, flatness checks, and high-precision industrial and metrological measurements: https://www.alpametrology.com/en/wyler-spirit-levels-and-inclination-measuring-instruments/
- Haas Tooling/YouTube product material describes precision digital levels used for CNC machinery and machine accuracy setup: https://www.youtube.com/watch?v=FlNYzIjYBtc

# Commercial alternatives

Commercial alternatives include:

- Precision machinist spirit level with ground base.
- Frame level or square level for horizontal and vertical alignment.
- Electronic/digital precision level or inclinometer.
- Laser alignment system for larger machine installations.
- Autocollimator or optical metrology setup for higher precision angular alignment.
- Granite surface plate plus dial indicators, straightedges, and shims for complementary leveling and geometry checks.

# Build or open-source references

Locally building the body is much easier than locally making a trustworthy precision level. A credible build requires:

- stable, stress-relieved and precisely machined body,
- accurately ground/scraped reference base,
- precision vial or electronic tilt sensor,
- adjustment screws and locking hardware,
- thermal stability and repeatability checks,
- calibration against a known reference, reversal procedure, surface plate, or traceable angular standard.

The KB recipe correctly notes calibration against a known reference. However, the current BOM is too coarse: it only lists aluminum stock. A realistic BOM should include the vial or electronic sensor module, adjustment hardware, case/protection, calibration/reference needs, and possibly a steel/cast iron base for some variants. The recipe also outputs `machined_steel_part_precision` from aluminum inputs, which looks like a data consistency issue.

# Related machine research

Related local reports:

- `inspection_tools_basic.md`
- `measurement_equipment.md`
- `precision_tooling_set.md`
- `precision_lathe.md`
- `surface_grinder.md`
- `fixturing_workbench.md`

Related KB items include `alignment_tools`, `inspection_tools_basic`, `measurement_equipment`, `optical_metrology_tools`, `granite_surface_plate_large`, and `straightedge_precision`.

# Recommendation for KB realism

Keep `precision_levels`, but classify or describe it as calibrated metrology tooling rather than a machine.

Recommended refinements:

- Rename or alias conceptually to `precision_level_set` or `precision_machinist_levels`.
- Keep the 0.02 mm/m target; it is commercially realistic.
- Add explicit components for precision vial/electronic level sensor, adjustment hardware, protective case, and calibration/reference procedure.
- Fix the recipe material mismatch: aluminum inputs should not produce `machined_steel_part_precision`.
- Keep it separate from broad `inspection_tools_basic`; precision levels are specifically for leveling/alignment, not general dimensional inspection.
- Use `optical_metrology_tools` or laser alignment systems for larger or higher-precision alignment tasks where a level alone is insufficient.

# Confidence and open questions

Confidence: high that the item is real and commercially available; high that the KB mass and accuracy are plausible; medium on whether local manufacture is realistic without importing the vial/sensor and calibration reference.

Open questions:

- Should the KB treat precision levels as a subtype of `measurement_equipment` or keep them separate because machine-tool alignment is a core process?
- Is the intended variant a spirit level, an electronic inclinometer, or a kit containing both?
- What calibration standard is available in the self-reproduction chain?
