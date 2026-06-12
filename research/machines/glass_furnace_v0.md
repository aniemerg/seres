# Glass furnace v0

## Machine identity

- Queue item: `machine_reality_glass_furnace_v0`
- KB ID: `glass_furnace_v0`
- KB file: `kb/items/machines/glass_furnace_v0.yaml`
- KB name: Glass furnace v0
- KB kind: `machine`
- KB modeled mass: 1400 kg

The KB models this as a batch or continuous glass melting furnace with a refractory shell, high-temperature heating elements, insulation, cooling loop, high-current power bus, optical pyrometer, temperature controller, sensor suite, control module, fasteners, and steel plate/sheet.

## KB usage and needed function

`glass_furnace_v0` is used by processes for:

- Glass melting and forming: `glass_melting_v0`, `glass_melting_and_forming_v0`, `glass_envelope_forming_v0`
- Glass refining and specialty glass production: `glass_refining_basic_v0`, `aluminosilicate_glass_production_v0`, `glass_envelope_quartz_fabrication_v0`
- Hot holding/pouring: `holding_and_pouring_basic_v0`
- Basalt melting: `basalt_melting_v0`

The needed function is a high-temperature refractory-lined furnace capable of melting silicate/glass batches, holding molten glass near working temperature, and supporting downstream forming or pouring. The KB item is a general capacity provider rather than a single exact industrial design.

## Reality classification

Classification: real practical machine family, modeled as a generic small glass melting furnace.

Glass melting furnaces are standard industrial and studio/research equipment. The KB item is not a placeholder. However, "glass furnace" is a broad category: pot furnaces, day tanks, tank furnaces, recuperative/regenerative melters, oxy-fuel melters, and all-electric melters differ greatly in mass, energy system, throughput, controls, and operating practice.

The KB mass of 1400 kg is plausible for a small studio, lab, or pilot-scale electric/pot furnace assembly. It is far too small for industrial continuous tank furnaces, which can contain large refractory structures and many tonnes of glass. The KB should therefore interpret this item as a small glass furnace unless future models split industrial-scale furnaces from small production furnaces.

## Evidence links

- IMI/NFG Course on Processing of Glass, "Basics of industrial glass melting furnaces": https://www.lehigh.edu/imi/teched/GlassProcess/Lectures/Lecture03_Hubert_industglassmeltfurnaces.pdf
  - Lists pot furnaces, day tanks, recuperative/unit melters, regenerative furnaces, oxygen-fired melters, special melters, and all-electric furnaces.
  - Describes discontinuous furnaces charging batch, heating it, melting, fining, homogenizing, and cooling to working temperature.
  - Describes continuous glass furnaces as refractory tanks used for container glass, flat glass, tableware, fibers, specialty glass, tubes, display glass, glass-ceramics, and lighting bulbs.

- Glassglobal overview of glass melting furnaces: https://www.glassglobal.com/consulting/reports/technology/
  - Divides glass melting furnaces into pot furnaces and tank furnaces.
  - Notes pot furnaces use refractory pots and batch cycles, while tank furnaces are for continuous flow to automatic forming machines.
  - Describes high-refractory baths, temperatures above 1500 C, recuperative/regenerative heat recovery, fuel firing, and electric melting.

- AXA XL risk consulting guideline for glass melting furnaces: https://axaxl.com/prc-guidelines/-/media/axaxl/files/pdfs/prc-guidelines/prc-17/prc17221glassmeltingfurnacesv1.pdf
  - Notes large regenerative tank furnaces, small pot furnaces for special glasses, and specialty electrically heated furnaces.
  - Highlights refractory selection, continuous operation, molten-glass containment, cooling systems, and high operating temperatures around 1500 C.

- Glass Service hand-made production furnaces: https://www.gsl.cz/services-products/products/special-furnaces/hand-made-production-furnaces/
  - Commercial examples include double pot electric furnaces and crucible electric furnaces for small-scale glass production and instruction.
  - Describes refractory construction, automatic controller or PLC control, resistance heating elements, and melting temperatures around 1420-1450 C.

## Commercial alternatives

- Small studio/research crucible or pot furnaces, such as Glass Service crucible/double-pot electric furnaces, are appropriate commercial analogs for the KB mass scale.
- Custom lab glass melting furnaces are sold by furnace manufacturers for research and industrial glass applications, often with refractory linings, precise temperature control, and corrosion-resistant designs.
- Large continuous tank furnaces, regenerative furnaces, and oxy-fuel/electric melters are commercial industrial equipment but should not be treated as equivalent to a 1400 kg small furnace.

## Build or open-source references

No credible open-source full build package for a production-quality glass melting furnace was found during this task. Practical small glass furnaces can be built by experienced kiln/furnace builders using refractory materials, insulation, heating elements or burners, controls, and safety systems, but molten glass containment and refractory compatibility are serious safety and durability issues.

For KB realism, local construction should be modeled as specialized refractory furnace fabrication rather than a casual assembly task. Critical subsystems include refractory lining/shell, element or burner system, temperature sensing/control, electrical power distribution, cooling where needed, and molten-glass spill containment.

## Related machine research

Related research files were not present in `research/machines` at the start of this task. Related queue items may include `casting_furnace_v0`, `blast_furnace_or_smelter`, `crucible_refractory`, `controlled_atmosphere_chamber`, and other high-temperature furnace or refractory equipment.

## Recommendation for KB realism

Keep `glass_furnace_v0`, but clarify its scope as "small glass melting furnace" or "small electric glass melting furnace" if future KB edits are allowed.

Recommended interpretation:

- Keep as a real machine.
- Treat the current 1400 kg item as small production/lab/studio-scale, not as an industrial continuous tank furnace.
- Avoid using it to imply full float-glass or container-glass industrial capacity without a separate large tank furnace/forehearth/forming-line model.
- Preserve the cooling loop and refractory shell in the BOM; those are realistic and important.
- Consider separating downstream forming equipment from the furnace if the KB later needs realism for sheets, envelopes, fibers, or precision glass parts.
- For basalt melting, keep this as a plausible high-temperature furnace only if temperature/refractory compatibility is documented; basalt/glass melts can be corrosive and may need different refractory details.

## Confidence and open questions

Confidence: high that glass furnaces are real and that the KB item is plausible as a small furnace; medium on the exact 1400 kg mass and process coverage.

Open questions:

- Is the intended machine electric, fuel-fired, or hybrid? The BOM suggests electric heating elements and high-current power.
- Does the KB need to distinguish melting from annealing, reheating, forming, and forehearth conditioning?
- Are quartz and aluminosilicate glass processes compatible with one generic refractory furnace, or do they need different furnace materials/temperatures?

