# Pyrolysis Chamber v0 Machine Reality Research

## Machine identity

- KB machine id: `pyrolysis_chamber_v0`
- KB name: Pyrolysis chamber v0
- KB file: `kb/items/machines/pyrolysis_chamber_v0.yaml`
- Current KB mass: 120 kg
- Current BOM: `bom_pyrolysis_chamber_v0`
- Current recipe: `recipe_pyrolysis_chamber_v0`

## KB usage and needed function

The item is used directly by `methane_pyrolysis_v0` to decompose methane into hydrogen and solid carbon/carbon black. The KB note defines the temperature range as 800-1200 C and says the chamber includes refractory lining, heating elements, temperature control, and gas handling fittings.

The needed function is not just a hot chamber. Methane pyrolysis needs controlled high-temperature residence time, methane feed, inert or controlled atmosphere, hydrogen/carbon product handling, carbon removal, seals, thermal insulation, off-gas handling, and likely process-specific reactor geometry.

## Reality classification

Real practical reactor category, but specialized and not yet a commodity generic machine.

Methane pyrolysis reactors are real and actively developed, including thermal, catalytic, plasma, and molten-metal approaches. The KB item is realistic as a simplified bench/pilot reactor chamber, but the exact design is underspecified. Carbon deposition/clogging, carbon product separation, heat transfer, gas purity, catalyst or molten media selection, and reactor material compatibility are central design issues.

## Evidence links

- A 2025 RSC review describes methane pyrolysis as a technology family with thermal, catalytic, plasma, and molten-media reactor designs, and discusses scale-up challenges: <https://pubs.rsc.org/en/content/articlehtml/2025/ee/d4ee06191h>
- PARC/ARPA-E describes a high-throughput methane pyrolysis liquid mist reactor concept using molten metal catalyst to convert natural gas to hydrogen and solid carbon: <https://arpa-e.energy.gov/programs-and-initiatives/search-all-projects/high-throughput-methane-pyrolysis-low-cost-emissions-free-hydrogen>
- A KIT liquid-metal bubble column study reports methane pyrolysis experiments at 1100 C and discusses avoiding carbon deposition on hot reactor walls: <https://publikationen.bibliothek.kit.edu/1000056467/3940752>
- A 2026 NIH/PMC paper on Joule-heated methane pyrolysis describes carbon particles in a fluidized bed absorbing energy and creating a hot medium above 1200 C: <https://pmc.ncbi.nlm.nih.gov/articles/PMC12513321/>

## Commercial alternatives

- Thermal methane pyrolysis reactor with resistive or furnace heating.
- Catalytic methane pyrolysis reactor using metal or carbon catalysts at lower temperatures.
- Molten-metal bubble column or mist reactor to improve heat transfer and carbon management.
- Plasma methane pyrolysis reactor.
- Conventional carbon black furnace process or steam methane reforming, if the goal is industrial carbon/hydrogen production rather than low-carbon pyrolysis.

## Build or open-source references

A small experimental chamber can be built from refractory-lined high-temperature vessel components, electrical heating, thermocouples, gas fittings, seals, insulation, and a downstream condenser/filter/trap. The current KB recipe is directionally plausible for a chamber shell.

However, safe and useful methane pyrolysis also needs flammable gas handling, leak control, hydrogen handling, carbon removal, purge/inerting, exhaust treatment, over-temperature protection, and reactor-specific carbon management. Open, general-purpose DIY instructions are not a safe or sufficient basis for a production reactor.

## Related machine research

Related local reports:

- `research/machines/chemical_reactor_basic.md`
- `research/machines/chemical_reactor_vessel_v0.md`
- `research/machines/generic_chemical_reactor_v0.md`
- `research/machines/mre_reactor_v0.md`
- `research/machines/heating_furnace.md`

## Recommendation for KB realism

Keep the item as a methane-pyrolysis-specific reactor, not a generic high-temperature chemical reactor.

Recommended options:

- Rename or document as `methane_pyrolysis_reactor_v0` if that is its only current use.
- Keep separate from `chemical_reactor_basic`; methane pyrolysis has distinct high-temperature gas/carbon-handling requirements.
- Add downstream equipment assumptions when needed: gas separator/filter, hydrogen handling, carbon collection, purge gas, and safety controls.
- Do not use this item for mineral vacuum pyrolysis or generic polymer/ceramic pyrolysis without checking temperature, gas atmosphere, and product handling.
- Treat 120 kg as a small experimental/pilot chamber mass, not a full commercial pyrolysis plant.

## Confidence and open questions

Confidence: high that methane pyrolysis reactors are real; medium that a simple 120 kg chamber adequately models the KB process without additional gas/carbon handling equipment.

Open questions:

- Is the KB intended to produce carbon black, graphite-like carbon, or generic solid carbon?
- Does the reactor use thermal, catalytic, plasma, molten-metal, or fluidized-bed pyrolysis?
- Should `methane_pyrolysis_v0` require separate carbon collection and hydrogen purification equipment?
