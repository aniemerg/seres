1. `System boundary`
   Electrostatic beneficiation “module” that takes **dry, crushed/sieved highlands-like regolith** and outputs **2–4 solid product streams** (electrostatically split, optionally preceded by magnetic split), suitable as:

* **ore-enriched feed** for oxygen/metal extraction (e.g., Fe/Ti-bearing phases, glassy agglutinates),
* **anorthite/plagioclase-rich** fraction for construction/ceramics or Al/Ca/Si-rich downstream routes,
* **tailings** for backfill/berms/sinter feed.

Boundary includes: **dry handling + PSD conditioning + tribocharging + electrostatic separation + product collection + dust control** inside a vacuum-compatible enclosure. Excludes excavation/haulage upstream and final chemical reactors downstream (but includes their interface specs).

---

2. `Functional decomposition`
   **F1. Feed conditioning**

* Crush (if needed), deagglomerate, sieve/classify to electrostatic-friendly PSD.
* Remove oversize and ultra-fines that destabilize charging/flow.

**F2. Preconditioning**

* Ensure *very low volatiles/moisture* (vacuum bake / thermal conditioning).
* Thermal stabilization to reduce tribo drift and sticking.

**F3. Optional magnetic pre-separation**

* Remove **strongly magnetic/ferromagnetic fraction** (np-Fe-bearing agglutinates, metal grains) to reduce “electrical noise” and widen electrostatic selectivity.

**F4. Tribocharging**

* Impart controlled charge distribution (sign + magnitude) using a selected charger material and mixing geometry.

**F5. Electrostatic separation**

* Split particles by **q/m** in a controlled E-field (parallel plate or free-fall geometry), collecting multiple bins/cuts.

**F6. Product handling & QA**

* Mass metering, sample ports, periodic composition checks (e.g., LIBS/XRF on bulk, or sentinel XPS/SEM in lab).
* Route streams to downstream chemistry or construction feedstock.

---

3. `Candidate architecture options (A/B/C)`
   **A) “First-gen” tribocharging + parallel-plate multi-bin separator (baseline)**

* Proven lab approach in lunar-vacuum experiments; uses **plates at about ±15 kV** and multiple collection bins. ([NASA Technical Reports Server][1])
* Best for: simple, modular, low moving parts.

**B) Magnetic → size classification → tribo + parallel-plate (multi-stage flowsheet)**

* Explicitly staged approach (size separation then magnetic then electrostatic) has been explored as a *sequential beneficiation* strategy. ([Frontiers][2])
* Best for: higher selectivity and throughput robustness across variable feed.

**C) Advanced/optional: induction or corona-assisted electrostatic separation**

* Review literature identifies multiple electrostatic-force approaches (tribo, induction, etc.) and discusses tradeoffs for SRU. ([ScienceDirect][3])
* Best for: future optimization if tribo-only selectivity is insufficient; added HV complexity.

---

4. `Recommended architecture`
   **Recommend B for an SRU “process recipe”:**

1) **PSD conditioning** (narrow band) → 2) **optional magnetic pre-sep** → 3) **tribocharger** → 4) **parallel-plate multi-bin electrostatic separator**.

Why:

* Tribo + plates at **±15 kV** has demonstrated meaningful elemental/mineral fractionation in vacuum tests. ([NASA Technical Reports Server][1])
* Magnetic pre-removal of ferromagnetic agglutinates/soil metal was used historically as a pretreatment in lunar sample work (reported in a modern compilation).
* Multi-stage sequential beneficiation is repeatedly advocated in recent experimental/testbed work to improve grade/recovery. ([Frontiers][2])

---

5. `BOM draft` (process-module oriented)
   *(Quantities are for a **~10–50 kg/hr pilot**; scale linearly for higher throughput.)*

* Vacuum-tight beneficiation enclosure (Al alloy frame + SS panels), 1 set — contains dust, maintains low pressure; manufacturable early with imported sheet/fasteners.
* Feed hopper + metering feeder (SS/Al, auger or vibratory), 1 — stable mass flow to charger; auger is straightforward but needs dust-sealed bearings.
* Sieve stack / airless classifier (SS mesh screens, vibration drive), 1 — target PSD window; replaceable meshes.
* **Magnetic separator module** (NdFeB magnets imported; SS housing), 1 (optional) — removes magnetic fraction upstream; simple/repairable.
* Tribocharger “static mixer” cartridges (PTFE / Al / Cu / SS liners), 3–6 — swappable charger materials to tune polarity/charge magnitude (tribo depends strongly on material pairing).
* Electrostatic separator: parallel plates (Cu plates, ceramic standoffs), 1 set — E-field region; compatible with **±15 kV** operation demonstrated in tests. ([NASA Technical Reports Server][1])
* HV power supply (±0–20 kV, low mA, current-limited), 1 — must be current-limited for safety and arc resilience.
* Charge/field instrumentation: HV dividers, picoammeter/electrometer taps, 1 set — monitor leakage/charge drift.
* Multi-bin collector (7-bin or 3-bin), 1 — tests used multiple bins and also simplified 3-bin collection (pos/neg/middle). ([NASA Technical Reports Server][1])
* Dust filtration / cyclone (vac-rated), 1 — capture fines and prevent contamination of HV surfaces.
* Control electronics (PLC/MCU), 1 — closed-loop feed rate, vibration, HV setpoint, bin-change logic.
* Sensors: pressure, temperature, humidity proxy (residual gas), vibration, mass flow, 1 set — process control + diagnostics.

---

6. `Manufacturing route draft` (stepwise process flow with candidate I/O streams)
   Below is a **workable first-gen recipe** with *plausible* splits for a **highlands-like feed** (plagioclase-rich, lower mafic fraction than mare). Where literature provides only enrichment factors rather than full mass balances, I give conservative pilot-plant numbers and call them out as tunable.

### Step 0 — Inputs and nominal feed

* **Input solid:** crushed regolith, nominal **45–250 µm** after milling/sieving.
* **Highlands-like mineralogy expectation:** plagioclase/anorthite dominant, with pyroxene/olivine + glass/agglutinates; ilmenite can be low in some sites/samples (e.g., Apollo 14 ~1.3 vol.% reported in a vacuum-beneficiation paper). ([NASA Technical Reports Server][1])
  *(Site mineralogy varies a lot; treat “highlands-like” as plagioclase-rich, Ti-bearing phases minority.)*

### Step 1 — Drying / volatile conditioning (preconditioning)

* **Operation:** vacuum bake (e.g., 100–200 °C, hours) or continuous heated screw under vacuum.
* **Goal:** minimize adsorbed volatiles; lunar environment is naturally dry, and low moisture improves tribo and prevents sticking (a key advantage highlighted in tribo-electrostatic work).
* **Outputs:** conditioned solids + trace volatiles to pump line (trap as needed).

### Step 2 — PSD windowing (critical sensitivity control)

* **Sieve/classify to a narrow band**. A commonly used test band is around **50–75 µm**, near the cited dominant regolith range **~45–100 µm**, because charging/separation is more repeatable in a narrow PSD. ([NASA Technical Reports Server][1])
* **Recommended pilot cuts:**

  * **Cut A:** 25–45 µm (optional “fines” stream; often problematic for flow/adhesion)
  * **Cut B:** 45–100 µm (primary electrostatic feed; first-gen)
  * **Cut C:** 100–250 µm (secondary feed; may need different HV/geometry)
  * **>250 µm:** recycle to mill
* **Output streams:** sized feed streams + oversize recycle.

### Step 3 — Optional magnetic separation (integration point #1)

* **Purpose:** remove ferromagnetic agglutinates/metal grains that can dominate charging behavior; magnetic pretreatment is documented in lunar beneficiation context.
* **Suggested setting:** low-gradient permanent magnet drum or belt.
* **Plausible split (highlands-like, 45–100 µm cut):**

  * **Magnetic fraction (M):** ~3–10 wt% (np-Fe/agglutinate-rich; site dependent)
  * **Non-magnetic fraction (NM):** ~90–97 wt% → electrostatic feed
* **Routing:**

  * M → metallurgy feed (Fe-rich) or shielding aggregate trials
  * NM → tribocharging + electrostatic separation

### Step 4 — Tribocharging (charge prep)

* **Method:** pass NM powder through a static mixer/charger made of selectable materials (Al/Cu/SS/PTFE are commonly evaluated charger materials in tribo-electrostatic work).
* **Control knobs:** mixer length, flow rate, wall material, internal baffles, residence time, temperature.
* **Quality checks:** measure net charge / charge distribution proxy via Faraday cup sampling (periodic).

### Step 5 — Electrostatic separation (parallel plates, multi-bin)

* **Separator:** parallel plates with multiple collection bins; tests report operation with plates at **±15 kV**. ([NASA Technical Reports Server][1])
* **Operation:** feed enters field region, trajectories diverge by q/m; collect:

  * **POS plate fraction (P+)**
  * **NEG plate fraction (P−)**
  * **MID / bottom tray (P0)** (weakly charged / mixed)

#### Plausible product splits (highlands-like NM feed, 45–100 µm)

A conservative *starting* mass split for tuning:

* **P+ (plagioclase/anorthite-enriched):** 55–75 wt%
* **P0 (mixed middlings):** 15–30 wt%
* **P− (mafic/glass/Ti/Fe-enriched):** 5–20 wt%

Why these directions are plausible:

* Vacuum tribo-electrostatic work reports **elemental concentration shifts** across collected fractions and “mineral enrichment up to a few hundred percent.” ([NASA Technical Reports Server][1])
* Expect highlands regolith to yield a large “light silicate” stream (plagioclase-rich) simply because it is the dominant phase; electrostatic separation mainly *upgrades* the minority mafic/Ti fraction rather than flipping the bulk composition.

### Step 6 — Recleaning / staged separation (integration point #2)

To improve grade without huge losses:

* Re-run **P0** (middlings) through tribo+plates (possibly with different charger material) to split into **P0→P+** and **P0→P−**.
* Optionally re-run **P−** at a tighter PSD (e.g., 50–75 µm only) for stronger upgrading.

This “multi-stage sequential” concept is consistent with recent beneficiation testbed approaches emphasizing staged size + magnetic + electrostatic. ([Frontiers][2])

### Step 7 — Downstream chemistry interfaces (integration point #3)

* **Ti/Fe-enriched (P−, and/or M):**

  * Route to **hydrogen reduction** (ilmenite-bearing) or other oxygen extraction; ilmenite enrichment is often cited as desirable because it is energetically favorable for oxygen production. ([USRA Houston][4])
* **Plagioclase/anorthite-enriched (P+):**

  * Route to **construction ceramics/sinter feed**, glass-ceramic production, or as a “clean silicate” input to future chemical schemes (Al/Ca/Si extraction pathways).
* **Tailings management:**

  * Blend low-value streams for berms, radiation shielding, landing pad sinter feed, or backfill.

---

7. `Test/verification steps`
   **Bench acceptance tests (per PSD cut):**

1) **Flowability & deagglomeration:** verify no bridging in hopper; stable feeder mass flow.
2) **Charging characterization:** Faraday cup tests on charger output (net charge vs time/temperature; repeatability across charger materials).
3) **Separation characterization:** run fixed mass (e.g., 1–5 kg) at **±15 kV baseline**, measure:

   * mass yield of P+, P0, P− bins,
   * bulk chemistry via XRF/LIBS (Fe, Ti, Al, Ca proxies),
   * magnetic susceptibility per fraction to validate upstream magnet effectiveness.
4) **Stage-recovery curves:** re-run middlings; build grade–recovery map for target metric (e.g., TiO₂ wt% proxy).
5) **HV stability:** log leakage current, arc events, plate contamination rate.

**Go/no-go metrics (first-gen):**

* Stable operation without arcing for N hours at target throughput.
* Repeatable mass splits (±10% relative) and measurable Fe/Ti enrichment in P− vs feed (even if modest).

---

8. `Failure modes and maintenance plan`
   **Likely failure modes**

* **Plate fouling / dust coating** → field distortion, leakage current rise, arcing risk.
* **Charge drift** from temperature swings, charger wear, or feed mineralogy changes.
* **PSD creep** (screen wear, crusher setting drift) → reduced selectivity.
* **Magnet clogging** (if used) → reduced capture, throughput loss.
* **Electronics/HV insulation degradation** under dust + thermal cycling.

**Maintenance plan**

* Modular, quick-swap: charger liners, sieve meshes, bin inserts, plate shields.
* Scheduled “HV hygiene” cycle: vacuum-compatible brushing/airless vibration cleaning; bake-out to drive off volatiles.
* Continuous monitoring of leakage current as early warning; auto-derate HV on excursions.
* Periodic recalibration runs with a reference simulant batch.

---

9. `Assumptions and uncertainties`

* **Mass split numbers are starting points**, not guaranteed: literature often reports enrichment factors and elemental changes, not full industrial mass balances.
* “Highlands-like” is **site dependent**; even within Apollo samples, ilmenite abundance varies and reported values differ by locality/sample class. A cited value for Apollo 14 (~1.3 vol.% ilmenite) illustrates low-Ti cases. ([NASA Technical Reports Server][1])
* Electrostatic response depends strongly on:

  * **PSD** (narrower is better),
  * **surface state** (space weathering, glass/agglutinate content),
  * **charger material pairing** and residence time,
  * **electric field strength and geometry** (plates vs free-fall).
* Lunar operations help (dry vacuum), but dust adhesion and thermal cycling still create practical challenges.

---

10. `Sources and confidence`
    **High confidence**

* Electrostatic beneficiation in vacuum with tribocharging and parallel plates is a well-studied approach for lunar simulants/samples, with **operation at about ±15 kV** reported and meaningful fractionation/enrichment observed. ([NASA Technical Reports Server][1])
* Narrow PSD operation around the dominant lunar regolith size range (order **~45–100 µm**) is a common and defensible design choice for repeatability. ([NASA Technical Reports Server][1])
* Multi-stage beneficiation (size + magnetic + electrostatic) is an active and documented testbed strategy to improve grade/recovery robustness. ([Frontiers][2])

**Medium confidence**

* The specific **plausible mass splits** (e.g., P+ 55–75%, P− 5–20% for highlands-like NM feed) are engineering priors consistent with “bulk plagioclase dominance + minority mafic upgrading,” but should be calibrated experimentally for your chosen simulant/site.
* Magnetic pre-sep fraction yield (3–10 wt%) varies widely with maturity/np-Fe content.

**Low confidence (needs your target site/simulant data)**

* Exact achievable **ilmenite grade/recovery** for a given highlands deposit without site-specific mineralogy + PSD + space-weathering state characterization.

If you want, I can also express the recipe as a **machine-readable flowsheet** (streams with names, PSD bands, and tunable split parameters) suitable to drop into your YAML KB simulator.

[1]: https://ntrs.nasa.gov/api/citations/20110016173/downloads/20110016173.pdf "02"
[2]: https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2023.1328341/full?utm_source=chatgpt.com "Optimizing lunar regolith beneficiation for ilmenite enrichment"
[3]: https://www.sciencedirect.com/science/article/pii/S0032063319301266?utm_source=chatgpt.com "The beneficiation of lunar regolith for space resource ..."
[4]: https://www.hou.usra.edu/meetings/lunarisru2019/pdf/5074.pdf "5074.PDF"
