# Calculation Verification (Task 6)

## Process 1: regolith_mining_highlands_v0 (continuous, linear_rate, per_unit energy)
- time_model: rate 12.5 kg/hr, scaling_basis = regolith_lunar_highlands (output)
- energy_model: per_unit 0.5 kWh/kg, scaling_basis = regolith_lunar_highlands
- expected duration (100 kg output): 100 / 12.5 = 8.00 hr
- observed duration: 8.00 hr (provided)
- expected energy: 100 kg * 0.5 kWh/kg = 50.00 kWh
- observed energy: 50.00 kWh
- output observed: regolith_lunar_highlands 100.00 kg

## Process 2: metal_forming_basic_v0 (batch, fixed_per_batch energy)
- time_model: hr_per_batch = 1.5 hr
- energy_model: fixed_per_batch 1.5 kWh
- expected duration: 1.50 hr
- observed duration: 1.50 hr (provided)
- expected energy: 1.50 kWh per batch
- observed energy: 1.50 kWh
- output observed: formed_metal_part 0.95 kg

## Process 3: crushing_basic_v0 (continuous, linear_rate, per_unit energy)
- time_model: rate 3.3333 kg/hr, scaling_basis = anorthite_ore (input)
- energy_model: per_unit 1.5 kWh/kg, scaling_basis = anorthite_ore
- expected duration (1 kg input): 1 / 3.3333 = 0.30 hr
- observed duration: 0.30 hr (provided)
- expected energy: 1 kg * 1.5 kWh/kg = 1.50 kWh
- observed energy: 1.50 kWh
- output observed: regolith_crushed 1.00 kg
