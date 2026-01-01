# Project Overview

## Purpose

This project makes self-replicating industrial systems analyzable, computable, and
comparable. The model turns narrative architectures into a dependency graph with
mass, energy, and time accounting, so tradeoffs and bottlenecks are explicit.

## Core Modeling Policy

Anything that cannot be manufactured locally is treated as an import. This is a
boundary condition, not a claim of feasibility. It keeps gaps visible and assigns
mass penalties to unknowns.

## Design Principles

- Structure before precision: coarse numbers are acceptable if they preserve
  dependency structure and conservation relationships.
- Processes before machines: unit operations are modeled first; machines are
  capacity providers and products of processes.
- Incompleteness is a feature: the system must run with missing data and surface
  gaps rather than hide them.
- Iteration is driven by bottlenecks: focus modeling effort on top contributors to
  imported mass, energy, and time.

## Scope and Non-Goals

In scope:
- A computable dependency graph across items, processes, and recipes.
- Mass, energy, and time accounting with explicit gaps.
- Incremental refinement over time.

Out of scope (for now):
- Full scheduling or Gantt-style planning.
- High-fidelity chemistry or precision manufacturing.
- Detailed supply-chain constraints beyond import mass penalties.

## Where to Go Next

- Schema and required fields: `docs/kb_schema_reference.md`
- Queue work approach: `docs/conservative_mode_guide.md`
- Parts and labor modeling: `docs/parts_and_labor_guidelines.md`
- Knowledge acquisition workflow: `docs/knowledge_acquisition_protocol.md`
