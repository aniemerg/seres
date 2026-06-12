# Power supply benchtop

## Machine identity

- KB ID: `power_supply_benchtop`
- KB file: `kb/items/parts/power_supply_benchtop.yaml`
- KB name: Bench-top power supply
- KB kind in file: `machine`
- KB mass: 2 kg per unit
- Current KB role: regulated DC bench supply for electronics testing, calibration, and small experimental rigs.

## KB usage and needed function

Local usage shows this is a reusable electronics-lab instrument:

- It is listed in the minimal/self-reproducing imported-machine set, although the path is under `kb/items/parts`.
- It is required by `testing_and_calibration_circuit_v0` and `electrical_testing_basic_v0`.
- It has capabilities `regulated_dc_power` and `bench_power_supply`.
- It is distinct from `high_temperature_power_supply_v0`, `ffc_power_supply_controlled_v0`, `welding_power_supply_v0`, and high-current electrolysis/furnace power systems.
- `research/machines/high_temperature_power_supply_v0.md` explicitly recommends using `power_supply_benchtop` or `power_supply_bench` for ordinary lab electronics.

The needed function is adjustable, current-limited low-voltage DC power for circuit bring-up, testing, and calibration.

## Reality classification

Classification: real practical instrument.

Benchtop DC power supplies are standard electronics test instruments. The KB item is realistic as a low-power lab supply. The 2 kg mass is plausible for a small single-output or compact programmable bench supply, but not for large multi-output, high-current, rack, welding, electrolysis, or furnace supplies.

## Evidence links

- Keysight's bench power supply guide describes adjustable voltage/current, constant-voltage and constant-current operation, and line/load regulation: https://www.keysight.com/blogs/en/tech/educ/2023/bench-power-supply
- Rohde & Schwarz explains CV and CC operation for DC benchtop power supplies and current limiting: https://www.rohde-schwarz.com/us/products/test-and-measurement/essentials-test-equipment/dc-power-supplies/understanding-constant-voltage-current_256008.html
- B&K Precision describes constant voltage and constant current modes in regulated power supplies: https://www.bkprecision.com/knowledge/technical-notes/163/understanding-constant-voltage-cv-and-constant-current-cc-modes-in-regulated-power-supplies
- NI documents CV/CC indicators for its DC power supply instrument: https://www.ni.com/docs/en-US/bundle/virtual-bench-help/page/powersupply_ts_cv_cc.html
- AMETEK/Sorensen lists programmable DC bench power supplies from 75 W to 840 W with defined voltage and current ranges: https://www.programmablepower.com/products/dc-bench-power

## Commercial alternatives

Commercial alternatives include:

- Single-output adjustable lab bench supplies.
- Multi-output bench supplies for analog/digital electronics.
- Programmable bench supplies with remote control.
- Low-noise linear supplies for sensitive circuits.
- Switching supplies for higher power density.
- Rack-mounted programmable DC supplies for larger rigs.

For process equipment, use dedicated high-current or high-voltage supplies rather than this item.

## Build or open-source references

- Analog Devices provides a high-performance portable DC bench supply design with 0-24 V and 0-3 A CV/CC control: https://www.analog.com/en/resources/technical-articles/high-performance-portable-dc-bench-power-supply.html
- Instructables documents variable lab bench supply builds with adjustable voltage and current limit: https://www.instructables.com/Build-a-Variable-Lab-Bench-Power-Supply/
- Electronics-Lab documents a 0-24 V / 3 A lab power supply with current limiting: https://www.electronics-lab.com/project/build-0-24v-3a-lab-power-supply-current-limit/

These support local buildability for basic bench supplies, assuming access to transformers or DC converters, regulators, protection circuits, meters/displays, enclosure, connectors, and calibration.

## Related machine research

Related local reports:

- `research/machines/high_temperature_power_supply_v0.md`
- `research/machines/power_conditioning_equipment.md`
- `research/machines/welding_tig_unit_v0.md`

Related KB items:

- `power_supply_bench`
- `power_supply_components_basic`
- `power_supply_low_voltage`
- `power_supply_dc_high_current`
- `high_temperature_power_supply_v0`
- `ffc_power_supply_controlled_v0`
- `welding_power_supply_v0`
- `test_equipment_basic`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep `power_supply_benchtop` as a real low-power test instrument.

Recommended cleanup when KB edits are allowed:

- Consider moving path/classification consistency: the file is under `parts` but declares `kind: machine`.
- Keep it distinct from high-current electrolysis, welding, hot-wire, and furnace power supplies.
- Add nominal output range if known, such as 0-30 V and 0-3 A, or specify that it is a representative small bench supply.
- Consolidate with `power_supply_bench` if both represent the same instrument.
- Keep the 2 kg mass for a small bench supply.

## Confidence and open questions

Confidence: high that the item is real and useful.

Open questions:

- Should `power_supply_benchtop` and `power_supply_bench` be merged?
- What output range and ripple/noise requirements do current test processes need?
- Should calibration standards be modeled separately from the power supply?
