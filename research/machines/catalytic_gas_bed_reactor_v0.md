# Catalytic gas-bed reactor v0

## Machine identity

- KB ID: `catalytic_gas_bed_reactor_v0`
- Proposed KB file: `kb/items/machines/catalytic_gas_bed_reactor_v0.yaml`
- Role: heated gas-solid catalytic reactor for fixed-bed, gauze-bed, packed-bed, or coarse fluidized/contact-bed service.

## Research summary

The target processes are not ordinary stirred liquid reactions or simple gas recirculation. They require gas contacting with a hot catalyst bed, controlled residence time, temperature control, pressure relief, and offgas routing.

Reference summaries:

- Ostwald ammonia oxidation uses platinum-rhodium gauze catalysts for ammonia oxidation to NO; a recent open review describes the Pt-Rh catalyst gauze role in the industrial process: https://pmc.ncbi.nlm.nih.gov/articles/PMC8821626/
- EPA sulfur recovery documentation describes catalytic Claus plants and notes activated alumina or titanium dioxide catalysts in catalytic stages: https://www.epa.gov/sites/default/files/2020-09/documents/8.13_sulfur_recovery.pdf
- Catalytic oxidation equipment for CO/VOC cleanup is commonly modeled as plug-flow packed-bed catalytic oxidation service, with catalyst beds or monoliths in a metal housing.
- The Rochow/Mueller direct process reacts methyl chloride with silicon over copper catalyst/promoters in a fluidized/contact bed; Wacker describes methyl chloride flowing through a bed of contact mass particles: https://reports.wacker.com/2011/ar/pathstoinnovation/processinnovation.html

## KB modeling decision

Create `catalytic_gas_bed_reactor_v0` as the reactor resource for high- or moderate-temperature gas-solid catalytic conversion. It contains the reactor body, catalyst bed support, heater/jacket, gas manifolds, temperature sensing/control, relief, and offgas interface.

Scope boundaries:

- `gas_handling_loop_v0`: gas recirculation, flow control, and offgas plumbing; it does not provide catalyst bed residence time or hot reactor internals by itself.
- `furnace_basic`: generic heat source; it does not provide gas distribution through catalyst, pressure relief, or product/offgas containment.
- `packed_bed_distillation_v0`: vapor-liquid packed column for separation/absorption/stripping; not a reactive catalyst bed.
- `generic_chemical_reactor_v0` and `chemical_reactor_basic`: stirred/jacketed reactor abstractions for moderate liquid/gas-liquid chemistry, not gas-solid packed-bed catalytic service.

Use this resource for Ostwald ammonia oxidation, catalytic Claus sulfur recovery stages, CO oxidation cleanup, and Rochow gas-solid chloride service where a dedicated gas-bed reactor is now modeled.

