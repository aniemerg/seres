# Multimeter set

## Machine identity

- KB ID: `multimeter_set`
- KB file: `kb/items/machines/multimeter_set.yaml`
- KB name: Multimeter set
- KB mass: 2 kg per unit
- Current KB role: reusable electrical diagnostic/test tool set for voltage, current, resistance, and continuity checks.

## KB usage and needed function

Local usage shows `multimeter_set` is a diagnostic tool bundle:

- It is listed in the minimal/self-reproducing machine set.
- It is required by `electrical_testing_v0`, `electrical_testing_basic_v0`, and `testing_and_calibration_circuit_v0`.
- It is included in the `measurement_equipment` recipe.
- Some related BOMs and recipes still reference `multimeter_digital` from `kb/imports`, while other recipes note a prior change from `multimeter_digital` to `multimeter_set`.
- `test_equipment_basic`, `test_equipment_electronics`, and `measurement_equipment` also include broader instrumentation bundles.

The needed function is low-power electrical troubleshooting and verification during assembly: measuring voltages, currents, resistances, continuity, and basic component behavior. It should be modeled as reusable test equipment, not a consumable input.

## Reality classification

Classification: real practical tool set / instrument bundle.

Digital multimeters are standard electronics and electrical maintenance instruments. A "set" of multimeters is not one canonical machine, but it is a practical kit of reusable diagnostic tools. The 2 kg mass is plausible for a few handheld meters with probes, leads, fuses, small case, and accessories.

## Evidence links

- Fluke's digital multimeter product category describes professional DMMs for electrical testing: https://www.fluke.com/en-us/products/electrical-testing/digital-multimeters
- Fluke's usage guide covers measuring AC/DC voltage, continuity, capacitance, frequency, and diodes with a multimeter: https://www.fluke.com/en-us/learn/blog/maintenance-monitoring/how-to-use-a-multimeter-guide
- National Instruments describes a DMM as a test instrument for measuring voltage, current, and resistance for DC and AC signals: https://www.ni.com/en/shop/electronic-test-instrumentation/digital-multimeters/dmm-measurement-fundamentals.html
- Harbor Freight's digital multimeter manual documents practical safety/use cases including resistance, diode, and continuity testing: https://manuals.harborfreight.com/manuals/59000-59999/59434-193175470935.pdf
- Yokogawa lists voltage/current standards used for calibrating multimeters and related electrical instruments: https://tmi.yokogawa.com/us/solutions/products/generators-sources/standard/

## Commercial alternatives

Commercial alternatives include:

- Handheld digital multimeters from Fluke, Keysight, Klein, Extech, Brymen, Uni-T, Hioki, and many low-cost suppliers.
- Bench digital multimeters for fixed electronics labs.
- Clamp meters for higher-current electrical work.
- Broader electronics test equipment bundles that include multimeters, oscilloscopes, power supplies, and signal generators.

For KB realism, `multimeter_set` is appropriate for field/assembly testing. Use broader test-equipment items when a process requires oscilloscopes, signal generators, power supplies, or calibrated lab instrumentation.

## Build or open-source references

- HYDRAmeter is an open-source digital multimeter project under the CERN Open Hardware Licence: https://github.com/jduffy105/HydraMeter_0.4
- STM32 Open Source Multimeter documents an open design using an STM32F373 to measure voltage, current, and power: https://hackaday.io/project/165857-stm32-open-source-multimeter

These references support buildability of a multimeter in principle, but accurate, safe DMMs require input protection, fusing, isolation, calibration references, PCB layout discipline, and enclosure design. For high-voltage or safety-critical work, commercial/imported meters remain more realistic than local first-generation fabrication.

## Related machine research

Related local report:

- `research/machines/oscilloscope_basic.md`

Related KB items:

- `multimeter_digital` under `kb/imports`
- `multimeter_analog_v0`
- `test_equipment_basic`
- `test_equipment_electronics`
- `measurement_equipment`
- `hand_tools_electrical`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep `multimeter_set` as a real reusable tool/instrument bundle.

Recommended cleanup when KB edits are allowed:

- Consolidate lingering `multimeter_digital` references into `multimeter_set` unless a single imported DMM is specifically needed.
- Keep this item distinct from `test_equipment_electronics` only when a process needs basic DMM functions and not a full bench-instrument suite.
- Consider modeling high-accuracy calibration standards separately from ordinary multimeters. Calibration sources, voltage references, resistance standards, and current sources are not the same as the field meters.
- Keep mass at 2 kg unless the set is explicitly expanded to many meters, bench DMMs, or calibration fixtures.

## Confidence and open questions

Confidence: high that the tool set is real and useful.

Open questions:

- Should the self-reproducing set import safety-rated digital multimeters indefinitely, or model only analog/basic locally buildable meters?
- Which processes need calibrated measurements versus simple continuity/voltage checks?
- Should `multimeter_set` be `kind: machine`, `part`, or a broader tool category? It behaves as reusable equipment in the current simulator model, so `machine` is acceptable for now.
