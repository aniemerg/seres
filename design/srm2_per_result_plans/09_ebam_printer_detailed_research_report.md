# EBAM Printer Detailed Research Report

Date: 2026-03-04
Scope: `design/srm2_bom_research_results/09_ebam_printer.md`
Purpose: align wire-feed electron-beam AM findings with existing KB machine chain and add missing process coverage.

## 1) Source extraction summary
Report 09 recommends a wire-feed EBAM/EBF3-style architecture with:
- electron beam + HV chain
- wire feed and controlled vacuum cell
- closed-loop process control and safety boundaries

## 2) Existing KB mapping
Strong existing coverage already present:
- `ebf3_wire_feed_machine_v0` (wire-feed electron beam machine)
- `ebm_machine_lunar_v0` (powder-focused EBM machine variant)

Gap:
- no explicit `electron_beam_additive_manufacturing_v0` process for simulation use
- no explicit output artifact representing EBAM near-net deposited metal

## 3) Recommended KB updates
- add process: `electron_beam_additive_manufacturing_v0`
- add output material: `ebam_deposited_metal_blank_v0`
- keep `ebf3_wire_feed_machine_v0` as primary machine dependency

