# EBF3 Source Registry Layout

This folder stores source locations and basic source metadata only. Do not put
extracted claims, interpretation, adopted/rejected components, or modeling
decisions here.

Use:

- `level_0_machine/`: whole-machine source registries plus colocated `raw/`
  files where the raw source primarily supports the machine-level model.
- `level_1_subsystems/`: source registries for the seven EBF3 subsystem BOMs
  plus colocated `raw/` files where the raw source primarily supports a
  subsystem.
- `level_2_parts/`: source registries for specific part-family or
  component-level reviews, such as electromagnetic lenses or cathodes, plus
  colocated `raw/` files when applicable.

If multiple registries use one raw source, keep one physical copy in its primary
level folder and link to that path from other registries. Do not duplicate raw
PDF/TXT files across levels.

Allowed registry metadata:

- Source ID
- Title
- Publisher/site
- Date, when known
- URL or local file path
- Authority class, such as `primary`, `external`, or `user_derived`. Authority
  is scope-sensitive: the same source can be primary for a machine-level claim
  and only external for a component-level claim.
- Short scope note, such as "machine-level" or "part-family reference"

Do not include extracted claims, quotes, adopt/defer/reject decisions, or
modeling interpretation in source registry files.

Put actual reading notes, extracted claims, comparison matrices, and
adopt/defer/reject decisions in `research/ebf3_bom_sources/organized/`.

A registry entry means only "this source is available for review." It does not
mean that every claim in the source has been accepted, or that a KB item can be
created from it without an organized planning file.
