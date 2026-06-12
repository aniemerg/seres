# Electrolysis Cell Unit V0

## Machine identity

- KB ID: `electrolysis_cell_unit_v0`
- KB name: Electrolysis cell module v0
- KB file: `kb/items/machines/electrolysis_cell_unit_v0.yaml`
- Current KB type: `machine`
- Current KB mass: 25 kg
- Current KB description: modular electrolysis cell unit for chlor-alkali systems, with placeholder mass and capabilities.

## KB usage and needed function

The KB usage is broader than the item notes:

- `aluminum_smelting_hall_heroult_v0` uses it for Hall-Heroult aluminum smelting at about 960 C in molten cryolite.
- `cobalt_sulfate_extraction_v0` uses it for aqueous cobalt electrowinning from sulfate solution.
- Documentation also describes it as electrochemical reduction equipment in the minimal self-reproducing set.
- The item notes specifically mention chlor-alkali, while the current process references are aluminum smelting and cobalt electrowinning.

The local BOM is explicitly placeholder-like: nickel anode/vacuum-tube part, tungsten cathode blank, CaO-coated tungsten cathode, and tube electrode set. The recipe currently fabricates only a 25 kg steel shell. This is enough for provenance experiments, but not a realistic complete cell for all referenced chemistries.

## Reality classification

Classification: real practical machine category, but currently over-generic and internally inconsistent.

Electrolysis cells and electrolyzer cell stacks are real industrial equipment. However, chlor-alkali cells, water electrolyzer stacks, Hall-Heroult aluminum pots, molten-salt reduction cells, and aqueous electrowinning cells are materially and mechanically different. They use different temperatures, electrolytes, electrode materials, separators/membranes, current densities, containment, gas handling, and corrosion controls.

The KB item is realistic only as a coarse placeholder for "an electrochemical cell module." It is not realistic as one universal 25 kg machine that can cover chlor-alkali, Hall-Heroult, and cobalt electrowinning without chemistry-specific variants.

## Evidence links

- NIH/PMC, "The Aluminum Smelting Process": describes Hall-Heroult aluminum production as electrolytic reduction of alumina dissolved in molten fluoride electrolyte, with molten aluminum produced in electrolysis cells. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC4131936/
- SINTEF, "Could the chloride process replace the Hall-Heroult process": summarizes Hall-Heroult as alumina dissolved in molten cryolite and electrolytically reduced at around 960 C using consumable carbon anodes. Source: https://blog.sintef.com/energy/could-the-chloride-process-replace-the-hall-heroult-process-in-aluminium-production/
- COMSOL, "Current Distribution in a Chlor-Alkali Membrane Cell": describes a membrane unit cell with anode and cathode regions separated by a cation-selective membrane that prevents product mixing. Source: https://www.comsol.com/model/download/1063601/models.fce.chlor_alkali.pdf
- Nel Hydrogen, "A485 alkaline electrolyser stack and electrolyte system": describes an alkaline electrolyzer stack support system with gas separators, water seals, lye circulation, support frame, and stack service role. Source: https://nelhydrogen.com/resources/a485-series-alkaline-electrolyser-stack-and-electrolyte-system-module/
- OKON Recycling, "Electrowinning Process for Metal Recovery": describes electrowinning as an electrolytic process that deposits dissolved metal ions onto a cathode. Source: https://www.okonrecycling.com/industrial-scrap-metal-recycling/specialty-metals/electrowinning-process-metal-recovery/

## Commercial alternatives

- Chlor-alkali membrane cell elements and electrolyzer systems from industrial electrochemical equipment vendors.
- Water alkaline or PEM electrolyzer stacks from vendors such as Nel Hydrogen.
- Electrowinning cells for cobalt, copper, nickel, and other metal recovery operations.
- Aluminum smelting pots/cells for Hall-Heroult, which are much larger industrial assets than a 25 kg module.

Commercial analogues exist, but they are process-specific rather than universal.

## Build or open-source references

Small educational electrolysis cells are easy to build, but realistic industrial cells are not generic DIY equipment. The build requirements depend strongly on electrolyte, temperature, gas evolution, corrosion, current, and electrode life.

For low-temperature aqueous electrowinning or lab electrolysis, a small cell can be built from chemically compatible container materials, electrodes, bus bars, DC power supply, ventilation, and instrumentation. For Hall-Heroult or molten-salt reduction, build requirements escalate to refractory containment, high-current buswork, thermal insulation, high-temperature seals, fume capture, and consumable or inert electrodes.

No complete open-source build suitable for all KB uses was identified in this pass.

## Related machine research

Related KB items and processes:

- `water_electrolysis_system_v0`
- `electrolyzer_cell_stack`
- `electrolyzer_alkaline_v0`
- `electrolyzer_pem_v0`
- `mre_reactor_v0`
- `ffc_reactor_unit_v0`
- `aluminum_smelting_hall_heroult_v0`
- `cobalt_sulfate_extraction_v0`

These should not all collapse into one machine unless the KB deliberately uses `electrolysis_cell_unit_v0` as a temporary generic placeholder.

## Recommendation for KB realism

Keep as a temporary placeholder, but mark as needing chemistry-specific interpretation.

Recommended future cleanup:

- Rename or document the current item as `generic_electrolysis_cell_placeholder_v0` if it is intended only for early closure/provenance demos.
- Split real uses into at least three machine classes: `chloralkali_membrane_cell`, `aqueous_electrowinning_cell`, and `hall_heroult_reduction_cell`.
- For aluminum smelting, do not use a 25 kg generic cell as a realistic pot unless the process is explicitly scaled down as a laboratory/demo cell.
- For cobalt electrowinning, a smaller aqueous electrowinning cell is plausible, but it needs tank, cathode/anode plates, bus bars, electrolyte circulation, ventilation, and power supply assumptions.

Do not replace this with labor and tools. Electrochemical reaction hardware and high-current electrical interfaces are core machine functions.

## Confidence and open questions

Confidence: high that electrolysis cells are real equipment; low-to-medium that this specific KB item is realistic for all current uses.

Open questions:

- Is `electrolysis_cell_unit_v0` meant to be a chlor-alkali cell, an electrowinning cell, a Hall-Heroult cell, or a generic placeholder?
- Should `mre_reactor_v0` and `ffc_reactor_unit_v0` cover molten-salt/regolith electrolysis instead?
- Should the current BOM be replaced with chemistry-specific electrodes, membrane/separator, refractory/tank, bus bars, seals, gas handling, and power-interface components?
