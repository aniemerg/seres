## A. Recommended battery chemistry for lunar manufacturing

### Recommendation: **Nickel–Iron (Ni–Fe) aqueous rechargeable**

**Why this is the best “bootstrap” choice (not best energy density):**

* **Vacuum-manufacturing compatibility:** aqueous electrolyte is *not* vacuum-compatible *while open*, but the cell is sealed—so you can manufacture in a **pressurized workshop** (habitat / pressure vessel) without needing an ultra-dry room. This directly resolves your current “dry room vs lunar vacuum” contradiction by choosing a chemistry that doesn’t require anhydrous processing.
* **Manufacturing simplicity:** no SEI formation complexity, no organic solvent handling, no polymer separators that must be micron-perfect like Li-ion (you can use robust separators).
* **Materials plausibility:** Fe is easy; Ni is the main pain point (likely partial import early). Electrolyte is **KOH**: needs K + O + H. (H may be sourced from lunar volatiles/ice; K availability from regolith is location-dependent and likely low, so plan for K import early.)
* **Operational robustness:** tolerates abuse, long cycle life; lower Wh/kg is acceptable for 500 kg packs on lunar haulers (your model explicitly prefers closure over performance).

### Secondary variant to keep in the KB as “later upgrade”

**Li-ion (LiFePO₄) or solid-state Li-metal** for higher Wh/kg *after* the factory can make/import polymers, dry processing, high-purity salts/solvents, and tight QC. (This is a “growth-stage” branch, not seed-stage.)

---

## B. Process flow with quantitative, YAML-shaped data (Ni–Fe)

These are **best-guess engineering placeholders** intended to be computationally usable immediately. Treat all numbers as “educated_guess / low–medium confidence” until you replace them with sourced values.

### 1) Electrode fabrication (Ni hydroxide cathode + Fe anode)

```yaml
step_name: electrode_fabrication_nife
inputs:
  - item: iron_powder_or_sheet
    qty: 1.0   # kg
  - item: nickel_compound_active_material   # e.g., Ni(OH)2 precursor
    qty: 0.6   # kg
  - item: conductive_additive              # carbon black / graphite
    qty: 0.05  # kg
  - item: binder_simple                    # PTFE or similar (import early)
    qty: 0.02  # kg
  - item: current_collector_nickel_or_steel_mesh
    qty: 0.15  # kg
outputs:
  - item: electrodes_nife_set
    qty: 1.6
    waste_fraction: 0.05
energy_kwh: 2.0
time_hr: 3.0
atmosphere_required: pressurized_air
temperature_C: 20
equipment_type: powder_mill_press_sinter_oven
provenance:
  source: educated_guess
  confidence: low
notes: "Avoids moisture-sensitive steps; can be done in pressurized shop."
```

### 2) Electrolyte preparation (KOH aqueous)

```yaml
step_name: electrolyte_prep_koh
inputs:
  - item: potassium_hydroxide
    qty: 0.25
  - item: deionized_water
    qty: 0.75
outputs:
  - item: electrolyte_koh_solution
    qty: 1.0
    waste_fraction: 0.01
energy_kwh: 0.2
time_hr: 0.5
atmosphere_required: pressurized_air
temperature_C: 20
equipment_type: chemical_mixer_tank
provenance:
  source: educated_guess
  confidence: medium
notes: "Water is the gating resource; treat as imported until lunar volatiles processing exists."
```

### 3) Cell assembly + sealing (no dry room; but must be pressurized)

```yaml
step_name: cell_assembly_and_seal_nife
inputs:
  - item: electrodes_nife_set
    qty: 1.6
  - item: separator_robust                 # e.g., cellulose / ceramic / simple polymer
    qty: 0.08
  - item: electrolyte_koh_solution
    qty: 0.5
  - item: battery_cell_casing_metal
    qty: 0.3
outputs:
  - item: battery_cell_nife
    qty: 2.4
    waste_fraction: 0.03
energy_kwh: 1.0
time_hr: 2.0
atmosphere_required: pressurized_air
temperature_C: 20
equipment_type: assembly_station_sealer
provenance:
  source: educated_guess
  confidence: low
notes: "You can delete 'glove_box_or_dry_room' requirement for this variant."
```

### 4) Formation / conditioning (simplified vs Li-ion)

```yaml
step_name: formation_cycle_nife
inputs:
  - item: battery_cell_nife
    qty: 2.4
outputs:
  - item: battery_cell_nife_formed
    qty: 2.4
energy_kwh: 1.5          # per kg cell (placeholder)
time_hr: 6.0             # per batch-equivalent (placeholder)
atmosphere_required: pressurized_air
temperature_C: 20
equipment_type: formation_rack_power_electronics
provenance:
  source: educated_guess
  confidence: low
notes: "Ni-Fe conditioning is real but less finicky than SEI-dependent Li-ion."
```

---

## C. Material sourcing analysis (what can be lunar vs import)

A pragmatic “seed factory” plan is: **Fe local early**, everything else “explicit imports,” then “substitute/localize” over generations.

* **Iron (Fe):** *Lunar-extractable* (ilmenite/other oxides → reduction).
* **Nickel (Ni):** likely **must import early** (trace in regolith, but not a great first-extraction target).
* **Potassium hydroxide (KOH):** **must import early** unless you explicitly model K extraction + water supply.
* **Water:** **must import** unless you already have a lunar volatiles chain.
* **Separator:**

  * bootstrap: **import** (polymer/cellulose), or try **ceramic separator** later (requires ceramics control).
* **Casing (steel/aluminum):** *Lunar-extractable* in principle, but steel quality/alloying may be “import assist” at first.

---

## D. Equipment list with rough mass estimates

These are deliberately coarse so you can add them as KB “machines” and start computing bottlenecks.

```yaml
- equipment_name: powder_mill_and_mixer
  mass_kg: 200
  function: "prepare electrode powders and mixes"
  capacity: "5 kg/hr"
  power_kW: 2.0
  provenance: {source: educated_guess, confidence: low}

- equipment_name: hydraulic_press
  mass_kg: 500
  function: "press electrodes / plaques"
  capacity: "50 electrodes/hr"
  power_kW: 3.0
  provenance: {source: educated_guess, confidence: low}

- equipment_name: low_temp_oven
  mass_kg: 300
  function: "dry/cure/sinter mild processes"
  capacity: "10 kg/batch"
  power_kW: 5.0
  provenance: {source: educated_guess, confidence: low}

- equipment_name: chemical_mixer_tank
  mass_kg: 150
  function: "mix KOH electrolyte"
  capacity: "20 L/hr"
  power_kW: 1.0
  provenance: {source: educated_guess, confidence: medium}

- equipment_name: cell_sealer_station
  mass_kg: 250
  function: "seal metal casings leak-tight"
  capacity: "30 cells/hr"
  power_kW: 2.0
  provenance: {source: educated_guess, confidence: low}

- equipment_name: formation_rack
  mass_kg: 400
  function: "charge/discharge conditioning and QA"
  capacity: "2 kW continuous, 20 cells simultaneously"
  power_kW: 2.0
  provenance: {source: educated_guess, confidence: low}
```

---

## E. Concrete KB edits to resolve your current contradictions

Your current KB has generic battery parts + a Li-ion-ish assembly assumption and explicitly requires `glove_box_or_dry_room`.

Here’s the cleanest structural fix:

1. **Split `battery_cell.yaml` into variants**

   * `battery_cell_nife.yaml`
   * `battery_cell_lion_lfp.yaml` (later)
2. **Split `battery_cell_assembly_v0.yaml` into variant processes**

   * `battery_cell_assembly_nife_v0.yaml` **(no glove box; requires pressurized shop)**
   * `battery_cell_assembly_lion_v0.yaml` (keeps dry room / inert atmosphere)
3. **Add an explicit facility/environment constraint**

   * `pressurized_workshop` vs `vacuum_workshop`
   * Then make “electrolyte handling” steps require pressurized.
4. **Update `battery_pack_large` recipe**

   * Keep the pack assembly structure, but swap the cell process ID based on variant; treat thermal management as **radiator-first** in vacuum (fans/pumps only if you have a fluid loop).
