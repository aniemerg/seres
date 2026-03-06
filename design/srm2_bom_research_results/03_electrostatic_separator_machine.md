1. `System boundary`
   A modular **electrostatic_separator** stage for **dry, vacuum-dominant regolith beneficiation**, positioned **after comminution + sizing + magnetic and/or gravity separation**. It accepts a **non-magnetic (or weakly magnetic) mineral fraction** and splits it into **two (or more) product cuts** based on **charge-to-mass ratio (q/m)** and/or **electrical conductivity/dielectrophoresis response** in a controlled electric field.
   Interfaces:

* **Upstream:** comminution + sieve/classifier; optional magnetic removal (drum/roll).
* **Downstream:** product bins feeding (a) oxygen feedstock (e.g., ilmenite-enriched), (b) silicate-rich tailings, (c) middlings recycle.
* **Utilities:** electrical power, control/data, dust-tight enclosure (vacuum compatible), maintainable wear parts.

---

2. `Functional decomposition`

* **F1 Feed conditioning**

  * F1.1 Metered dosing (vibratory feeder / screw micro-feeder).
  * F1.2 Deagglomeration (vibration + baffles; optional mild heating).
  * F1.3 Size control (target narrow PSD; reject oversize/ultrafines).
* **F2 Particle charging**

  * F2.1 Tribocharging via controlled contacts (static mixer / baffle chute / helical channel) using selected materials (Al/Cu/PTFE). NASA work repeatedly uses Al/Cu/PTFE chargers and shows lunar vacuum is favorable for this approach. ([NASA Technical Reports Server][1])
* **F3 Field separation**

  * F3.1 Homogeneous E-field region (parallel plates) with controlled plate gap and voltage.
  * F3.2 Free-fall trajectory separation into multiple bins (center + deflected streams). The “vertical free-fall + parallel plate” concept is explicitly used and recommended in lunar-focused studies.
* **F4 Collection & recirculation**

  * F4.1 Sealed bin carousel or removable bin drawers.
  * F4.2 Middlings recycle loop (optional).
* **F5 Controls & safety**

  * F5.1 HV enable chain (interlocks, door switches, discharge resistors).
  * F5.2 Field/arc monitoring (leakage current, fast trip).
  * F5.3 Process telemetry (mass flow estimate, voltage, current, temperature).

---

3. `Candidate architecture options (A/B/C)`

**A) Tribocharger + Parallel-plate free-fall separator (baseline, first-generation)**

* **How it works:** particles are tribocharged, then pass through a **vertical plate field**; positive/negative (and high/low q/m) trajectories diverge into bins (classic KSC-style testbeds).
* **Pros:** simplest mechanics (few moving parts), vacuum-friendly, scalable by widening plate area or paralleling modules.
* **Cons:** sensitive to PSD spread, feed rate, and dust deposition; requires careful HV insulation design.

**B) Corona/roll electrostatic separator (conductivity-based induction; more “mineral sands industry” style)**

* **How it works:** charged corona electrode + grounded roll; conductive vs non-conductive grains follow different paths as they discharge/adhere on the roll.
* **Pros:** high throughput on Earth; strong for conductive/non-conductive splits.
* **Cons:** moving roll in abrasive dust + vacuum lubrication challenges; corona geometry in vacuum needs careful breakdown control; more complex. (General industrial principle references exist, but lunar-specific validation is thinner than A.) ([ScienceDirect][2])

**C) Electrostatic Travelling Wave (ETW) convey-and-sort (advanced/optional)**

* **How it works:** phased electrodes create travelling-wave fields to move/segregate particles (also used in dust transport/dust mitigation literature).
* **Pros:** can combine conveyance + sorting; potentially precise.
* **Cons:** electrode fabrication complexity, multiphase drive electronics, less “first-gen ISRU” friendly. ([ScienceDirect][3])

---

4. `Recommended architecture`
   **Recommend Option A (Tribocharger + parallel-plate free-fall), implemented as a modular “separator cassette.”**

Baseline parameterization consistent with published lunar beneficiation testbeds:

* **Voltage:** design for **±25–30 kV** capability (adjustable), consistent with prior lunar-focused plate-separator studies and a DLR testbed design selection.
* **Plate size:** ~**28.3 cm × 28.3 cm** aluminum plates (demonstrated as a workable lab module size).
* **Plate gap:** start around **d ≈ 0.10 m** (gives strong fields without excessive collision risk; used in DLR sizing math and is a practical mechanical spacing).
* **Feed size:** target **~20–200 µm**, with best separation typically at **narrow bands** (many lunar regolith grains of interest fall ~45–100 µm, and multiple studies sieve to bands like 50–75 µm / 75–100 µm).
* **Throughput assumption (module):** **0.1–0.5 kg/min** (6–30 kg/hr) per cassette as a realistic first-gen target for a compact system; scale by parallel cassettes. (DLR lab hardware discusses feeder ranges on the order of grams/min up to ~kg/hr scale depending on subsystem; treat as a sizing starting point, not a proven lunar field rate.)
* **Power:** HV supplies are generally low-current; the dominant loads are feeder/vibrator and controls. (DLR plate-capacitor energy is small; practical power budget dominated by auxiliaries.)

Integration with magnetic/gravity chain:

* Put electrostatics **after magnetic separation** so the feed is already stripped of strongly magnetic grains; electrostatics then refines non-magnetic mineral fractions (e.g., silicates vs ilmenite-bearing grains depending on charging behavior). Multi-stage chains of sizing → magnetic → electrostatic are explicitly used in modern regolith beneficiation experiments/reviews. ([DLR eLib][4])

---

5. `BOM draft` (component, material, qty, unit, rationale, manufacturability)

**Separator cassette (one module, ~30 cm class):**

| Component                                                     |                                           Material |       Qty | Unit | Rationale                                                                     | Manufacturability (1st-gen vs 2nd-gen)                                                                    |
| ------------------------------------------------------------- | -------------------------------------------------: | --------: | ---- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Parallel plates (~283×283×4 mm)                               |                                           Aluminum |         2 | ea   | Homogeneous field; proven lab scale                                           | 1st: imported Al plate; 2nd: lunar Al possible later                                                      |
| Plate standoffs/insulating stems (~190 mm)                    |       Ceramic / glass-ceramic / high-grade polymer |       2–4 | ea   | Maintain gap; prevent leakage paths                                           | 1st: imported ceramic; 2nd: cast/sintered regolith glass/ceramic (advanced)                               |
| HV DC power supply ±25–30 kV (adjustable)                     |                                     COTS HV supply |         1 | ea   | Enables field tuning; prior designs select ±25 kV capability                  | 1st: imported COTS; 2nd: partial in-house later                                                           |
| HV cables/connectors rated ≥30 kV                             |                          Silicone / PTFE insulated |       2–4 | ea   | Vacuum-compatible HV routing                                                  | 1st: imported                                                                                             |
| Bleeder/discharge resistors + HV divider                      |                            Thick-film HV resistors |         1 | set  | Safe discharge; monitoring                                                    | 1st: imported                                                                                             |
| Arc/leakage current trip (fast)                               |                                        Electronics |         1 | set  | Prevent sustained arcing                                                      | 1st: imported                                                                                             |
| Charger: static mixer / helical chute                         |                                    Aluminum (body) |         1 | ea   | Many controlled contacts for tribocharging; used in lunar testbeds            | 1st: CNC mill/lathe from Al; 2nd: later cast/machine                                                      |
| Charger liners / swap-in contact inserts                      |                                         Al/Cu/PTFE |         3 | sets | Tune polarity/magnitude; Al/Cu/PTFE are common in lunar tribocharging studies | 1st: imported Cu/PTFE; 2nd: Cu later, PTFE likely imported long-term ([NASA Technical Reports Server][1]) |
| Feed metering: vibratory feeder or micro-screw                |                                              SS/Al |         1 | ea   | Stable mass flow into charger                                                 | 1st: imported motor/controller; 2nd: structure local later                                                |
| Deagglomeration baffle box                                    |                                           Aluminum |         1 | ea   | Break soft clumps; stabilize flow                                             | 1st: sheet metal fab                                                                                      |
| Mild pre-heat band (optional)                                 |                                 Kapton/film heater |         1 | ea   | Adjust surface conductivity / reduce adhesion (lab practice)                  | 1st: imported; optional                                                                                   |
| Separator enclosure (dust-tight)                              | Al frame + acrylic/PC panels (lab) / metal (lunar) |         1 | ea   | Containment; protect HV; serviceable                                          | 1st: Al extrusion + panels; 2nd: all-metal, regolith shielding                                            |
| Collection bin set (multi-slot)                               |                                       Stainless/Al |         1 | set  | Split products (pos/neg/mid)                                                  | 1st: simple sheet metal                                                                                   |
| Vacuum-compatible bearings/actuators (if any moving shutters) |                                Dry-lube compatible | as needed | set  | Only if adding bin shutters/valves                                            | Minimize moving parts in baseline                                                                         |
| Sensors: plate voltage, current, temp, door interlock         |                                              Mixed |         1 | set  | Commissioning + safety                                                        | 1st: imported                                                                                             |

**Cross-check against an existing detailed lab BOM:**
A DLR lunar-beneficiation testbed BOM for the electrostatic separator includes (among other items) a **static mixer, outer tube, heat tape, HV supply, parallel plates, HV cables, stands/retainers**.

---

6. `Manufacturing route draft` (ordered process steps with inputs/outputs)

**A. Fabricate mechanical subassemblies**

1. **Plate set fabrication**

* Input: Al plate stock (or machined plate kit).
* Process: waterjet/CNC cut → deburr → radius edges (reduce field enhancement) → clean (solvent) → optional anodize (note: anodize can charge; test).
* Output: 2 matched electrodes.

2. **Insulator + retainer build**

* Input: ceramic rods/standoffs, stainless fasteners, insulating washers.
* Process: assemble into rigid spacing frame; include creepage path features (grooves, shields).
* Output: plate-gap fixture.

3. **Tribocharger module**

* Input: Al billet/tube; optional Cu/PTFE liners/inserts.
* Process: CNC mill helical channel or static-mixer baffles; add quick-release access for cleaning; add replaceable wear liners.
* Output: charger cartridge.

4. **Feed metering + interface chute**

* Input: feeder (vibratory/screw), hopper, flexible vacuum-compatible boot.
* Process: mount; add flow restrictor; add anti-bridging geometry.
* Output: stable feed subsystem.

5. **Enclosure + bin pack**

* Input: Al frame, panels, gaskets, bin drawers.
* Process: assemble dust-tight housing; add service door interlocks; align fall-line through field into bins.
* Output: contained separator cassette.

**B. Electrical integration**
6) Mount HV supply, route HV cables with strain relief; install bleeder resistors, HV divider, current sensing, fast-trip.
7) Add grounding plan: single-point ground reference, shielded HV, guarded measurement nodes.
8) Add optional heater tape control and feeder controller.

**C. Commissioning**
9) Dry clean, vacuum bake (if applicable), then HV ramp tests (below).

---

7. `Test/verification steps`

**Electrical / HV**

* **Insulation resistance + leakage current** at low voltage, then stepped to operating range.
* **HV ramp & hold test:** step to ±5 kV increments up to ±25–30 kV, hold at each step; log leakage current and trip events. (Prior lunar plate-separator experiments operate at kV–tens of kV settings. ([NASA Technical Reports Server][5]))
* **Arc immunity test:** introduce worst-case dust conditions (coating test coupons) and verify fast-trip.

**Process / separation**

* **Baseline simulant runs** on a narrow PSD (e.g., 50–75 µm) and then broader PSD; measure product composition (XRF/XPS/SEM-EDS depending on lab). Lunar beneficiation studies commonly sieve into size fractions and evaluate pre/post composition.
* **Voltage sweep:** map grade vs recovery across multiple field settings (e.g., ±8/±10/±12 kV were used in reduced-gravity flight experiments; lab designs consider up to ±30 kV). ([NASA Technical Reports Server][5])
* **Flow-rate sweep:** increase feed until separation quality degrades; establish nominal throughput.
* **Repeatability:** 10+ runs at nominal settings to measure drift due to fouling or tribocharger wear.

**Mechanical / contamination**

* **Dust containment leak test** (pressure decay or tracer).
* **Wear inspection** schedule validation: charger liners, chute edges, bin lip buildup.

---

8. `Failure modes and maintenance plan`

**FM1 Dust fouling / coating of insulators and electrodes**

* Mechanism: regolith fines deposit on insulators → creepage paths → leakage → arc.
* Mitigations:

  * Long creepage paths, shield rings, sacrificial dust skirts; “easy-open” cleaning access.
  * Keep plate edges radiused; avoid sharp fasteners near HV.
  * Periodic dry brushing / CO₂ puff (if available) / electrostatic “shake-off” (optional).
* Maintenance: wipe/brush insulators each shift; replace skirts monthly.

**FM2 Arcing / partial discharge**

* Mechanism: local field enhancement + dust bridges; in vacuum, different breakdown behavior and higher usable voltages are noted for lunar environments, but arcing risk remains if geometry is poor. ([LPI][6])
* Mitigations:

  * Field grading (rounded edges, guard electrodes), fast-trip, controlled ramp.
  * Humidity is absent on Moon (good for sticking), but also changes charging dynamics; design for conservative margins.
* Maintenance: inspect arc marks; polish/replace plates if pitting occurs.

**FM3 Tribocharger wear / drift in charging behavior**

* Mechanism: abrasive grains polish surfaces, alter work-function/contact behavior; liners change.
* Mitigations: replaceable inserts (Al/Cu/PTFE sets); standardize surface finish (Ra spec).
* Maintenance: weigh/measure inserts; swap when charging performance shifts.

**FM4 Feed instability (bridging, surging, clumping)**

* Mechanism: PSD too broad, ultrafines agglomerate electrostatically, hopper bridging.
* Mitigations: upstream sizing; vibratory conditioning; anti-bridge hopper geometry; controlled vibration.
* Maintenance: daily hopper cleanout; screen check.

**FM5 Electrode collision / product loss**

* Mechanism: too-small gap or too-high flow → particle trajectories strike plates.
* Mitigations: maintain ~10 cm class gap for 30 cm plates initially; tune flow and alignment.
* Maintenance: check plate alignment weekly.

---

9. `Assumptions and uncertainties`

**Assumptions (baseline sizing)**

* Feed PSD after sizing: **20–200 µm**, preferably narrow bands (e.g., 50–75 µm).
* Field module: **~28–30 cm plates**, **~10 cm gap**, **±25–30 kV** adjustable.
* Throughput per cassette: **0.1–0.5 kg/min** as a practical first target (not a demonstrated lunar operational number).

**Key uncertainties**

* Actual regolith variability (glass/agglutinates vs discrete minerals) and how stable tribocharging signatures are across sites.
* Long-duration fouling rates in true lunar dust environment (electrostatic adhesion + abrasion).
* Best charging material set depends on target mineralogy; Al/Cu/PTFE are common test materials but not universally optimal. ([NASA Technical Reports Server][1])

---

10. `Sources and confidence`

**High confidence (directly supported by lunar beneficiation literature / detailed designs)**

* Tribocharging + parallel-plate separation is a well-studied lunar regolith beneficiation method; lunar vacuum and low moisture are favorable.
* Plate separator concept geometry (vertical free-fall between plates) and voltage ranges in the **kV–tens of kV** regime (including ±8 to ±12 kV flights; up to ±30 kV referenced; ±25 kV selected in a detailed testbed design). ([NASA Technical Reports Server][5])
* Existence of a concrete electrostatic-separator BOM (plates, HV supply, cables, charger, stands/retainers) and specific plate size (~283 mm).

**Medium confidence (engineering extrapolation from lab systems to fieldable lunar hardware)**

* Suggested module throughput (0.1–0.5 kg/min) and power breakdown (auxiliaries dominate) as first-gen design targets—reasonable but site- and hardware-dependent.
* Maintenance intervals (shift/week/month) need empirical validation.

**Lower confidence / advanced options**

* Corona-roll separator and ETW sorting as lunar-first-gen: technically plausible but less directly validated for long-life, maintainable lunar hardware compared to the plate free-fall approach. ([ScienceDirect][7])

[1]: https://ntrs.nasa.gov/api/citations/20110016173/downloads/20110016173.pdf "02"
[2]: https://www.sciencedirect.com/science/article/abs/pii/S0304389407014148?utm_source=chatgpt.com "Optimization of key factors of the electrostatic separation for ..."
[3]: https://www.sciencedirect.com/science/article/pii/S0304388622000638?utm_source=chatgpt.com "A review of particle transport and separation by ..."
[4]: https://elib.dlr.de/202743/1/frspt-04-1328341.pdf?utm_source=chatgpt.com "Optimizing lunar regolith beneficiation for ilmenite enrichment"
[5]: https://ntrs.nasa.gov/api/citations/20110016172/downloads/20110016172.pdf "02"
[6]: https://www.lpi.usra.edu/meetings/roundtable2006/pdf/1026.pdf?utm_source=chatgpt.com "the use of tribocharging in the electrostatic beneficiation ..."
[7]: https://www.sciencedirect.com/science/article/abs/pii/S0304389408004615?utm_source=chatgpt.com "A new two-roll electrostatic separator for recycling of metals ..."
