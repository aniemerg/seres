# High-temperature power supply v0

## Machine identity

- KB ID: `high_temperature_power_supply_v0`
- KB name: High-temperature power supply v0
- KB file: `kb/items/machines/high_temperature_power_supply_v0.yaml`
- KB kind: `machine`
- Current KB mass: 320 kg
- Current KB scope: high-current electrical power supply for molten regolith electrolysis, furnaces, steel refining, stainless refining, molten CaCl2 electrolyte production, getter activation, porous receiver fabrication, and related high-temperature processes.

## KB usage and needed function

The KB uses `high_temperature_power_supply_v0` as a resource for energy-intensive or electrochemical thermal processes, including:

- `kb/processes/oxygen_extraction_molten_regolith_electrolysis_v0.yaml`
- `kb/processes/molten_cacl2_electrolyte_production_v0.yaml`
- `kb/processes/steel_refining_basic_v0.yaml`
- `kb/processes/stainless_refining_basic_v0.yaml`
- `kb/processes/getter_deposition_activation_v0.yaml`
- `kb/processes/porous_receiver_fabrication_v0.yaml`

The intended function is not ordinary electronics bench power. It is a robust high-current power conversion system, likely a transformer/rectifier or controlled DC supply, for electrolysis, resistive heating, or furnace/electrode operation.

## Reality classification

Classification: real practical machine category, with naming ambiguity.

High-current DC power supplies, industrial rectifiers, furnace power supplies, and electrolysis power supplies are real commercial equipment. The KB item is realistic as an aggregated industrial high-current supply.

The name "high-temperature power supply" is imprecise because the power supply itself does not necessarily operate at high temperature; it supplies current to high-temperature processes. A clearer name would be `high_current_process_power_supply_v0` or `industrial_electrolysis_power_supply_v0`.

## Evidence links

- Tektronix describes electrolysis power supplies as devices that provide precise DC voltage and current for electrolysis, with voltage/current control as a key feature. Source: https://www.tek.com/en/blog/reliable-scalable-turnkey-programmable-dc-power-supplies-for-hydrogen-electrolysis
- Volteq lists high-current DC supplies and rectifiers for electroplating, anodizing, electrolysis, electrocoagulation, resistive heating, DC motors, and battery charging; it notes currents from 50 A to 1000 A and custom rectifiers up to 30,000 A. Source: https://www.volteq.com/high-power-high-current-power-supplies.html
- GE Vernova describes direct-feed power systems for AC or DC electric arc furnaces, including converter system, EAF transformer, and arc-current control/regulation. Source: https://www.gevernova.com/power-conversion/product-solutions/Direct-Feed
- Friem describes rectifiers in electrolysis as converting AC to DC because electrochemical decomposition requires DC. Source: https://friem.com/en/blog/rectifiers-role-industrial-chemistry/

## Commercial alternatives

Commercial alternatives include:

- Industrial DC rectifier for electrolysis or electroplating.
- Programmable high-current DC power supply.
- SCR/thyristor rectifier.
- Transformer plus diode/thyristor rectifier and control electronics.
- Furnace transformer and converter system for arc or resistance furnaces.
- Specialized FFC/MRE controlled DC power supply if the electrochemical process needs low-voltage, high-current regulation.

For the KB's molten regolith and molten salt processes, a controlled high-current DC rectifier is the best interpretation. Furnace-only heating may need a separate furnace transformer or AC power controller.

## Build or open-source references

At small scale, high-current supplies can be built from transformers, rectifiers, contactors, cooling, and controls, but high-power systems are safety-critical:

- Low-voltage, high-current electrolysis and plating supplies often use transformer/rectifier or switching topologies.
- Welding power supplies are sometimes adapted for high-current experiments, but this is not a good production model for controlled industrial electrolysis.

Local manufacture is plausible only if the KB can produce transformers, rectifier diodes/SCRs, busbars, cooling, insulation, controls, safety interlocks, and enclosures. Semiconductor power devices and control electronics may remain import-limited.

## Related machine research

Related KB entries include:

- `ffc_power_supply_controlled_v0`
- `high_temp_power_supply_unit`
- `power_supply_dc_high_current`
- `power_supply_high_voltage`
- `welding_power_supply_v0`
- `power_conditioning_equipment`
- `mre_reactor_v0`
- `electrolysis_cell_unit_v0`

There is likely overlap between `high_temperature_power_supply_v0`, `high_temp_power_supply_unit`, `power_supply_dc_high_current`, and `ffc_power_supply_controlled_v0`. Future cleanup should preserve process-specific requirements: current, voltage, waveform, regulation accuracy, duty cycle, and safety.

## Recommendation for KB realism

Keep the item, but clarify the name and scope.

Recommended interpretation: an industrial high-current process power supply for high-temperature electrolysis and furnace-like processes.

Recommended future cleanup:

- Rename or note it as `high_current_process_power_supply_v0`.
- Split process-specific supplies only if voltage/current/regulation requirements matter.
- Avoid using this item for ordinary lab electronics; use `power_supply_benchtop` or `power_supply_bench` there.
- Consider consolidating with `power_supply_dc_high_current` or `ffc_power_supply_controlled_v0` if their requirements are within the same coarse range.

## Confidence and open questions

Confidence: high that this is a real practical equipment category; medium that one generic supply can cover every KB process currently referencing it.

Open questions:

- What voltage and current are required for MRE, FFC, steel refining, and furnace heating cases?
- Should furnace heating use AC/transformer control while electrolysis uses DC rectification?
- Are power semiconductors, transformers, busbars, cooling, insulation, and interlocks separately modeled?
- Does the 320 kg mass include cooling and safety enclosure, or only the electrical converter?
