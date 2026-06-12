# Machine Review Decision Checklist Plan

## Purpose

Create a single source of truth for decisions that come out of the machine reality reviews in `research/machines/`.

The checklist is meant for human review first. A later agent should read checked decisions from the checklist and convert them into KB edit queue tasks without inferring intent from prose.

## Output file

Primary checklist:

- `research/machines_analysis/machine_review_decision_checklist.md`

The checklist is ordered alphabetically by machine ID.

## Review workflow

Build the checklist by reviewing one machine report at a time.

For each file:

1. Read one report from `research/machines/<machine_id>.md`.
2. Extract actionable recommendations, alternate recommendations, implied fixes, and explicit "do not do" guidance where it affects an action.
3. Immediately append or update that machine's checklist block in `machine_review_decision_checklist.md`.
4. Only then move to the next report.

Do not read a large batch of reports and update the checklist later from memory.

## Block structure

Each machine block should include:

- Source review path.
- KB item path when available.
- A short finding summary.
- Decision status, initially `unresolved`.
- One or more decision groups.
- A standard custom instruction checkbox.

Every actionable checkbox must have:

- A stable decision ID, using `<machine_id>.<action_slug>`.
- A concise action label.
- An action type.
- A proposed KB edit queue task description.
- Optional notes, constraints, and "do not do" guidance.
- A freeform instruction area for the user.

## Decision group rules

Use `Choose one` when options are mutually exclusive.

Use `Choose all that apply` when options can be combined.

If a future enqueue agent finds multiple checked options inside a `Choose one` group, it must stop and ask for clarification instead of enqueueing tasks.

If the recommendation is no action, include both:

- a `no_action` checkbox, and
- a `custom` / `user_choice` checkbox.

## Action types

Use these action type labels where applicable:

- `note_cleanup`
- `rename_or_alias`
- `reference_migration`
- `dedupe_or_consolidation`
- `split_item`
- `bom_or_recipe_update`
- `process_requirement_update`
- `consumable_or_tooling_modeling`
- `infrastructure_or_subsystem_modeling`
- `deferred_schema_or_modeling_decision`
- `research_or_design_followup`
- `no_action`
- `custom_user_instruction`

## Repo-specific terminology

In this repo, `machine` and `machine_id` are broad reusable process resource conventions. The checklist must not assume "machine" means only a literal standalone commercial machine.

When a review says "not a machine," translate that into actionable language such as:

- classify as tooling/resource/instrument/consumable conceptually;
- clarify notes so it is not treated as standalone equipment;
- keep as a reusable process resource if the simulator requires `machine_id`;
- avoid using it alone where a powered machine or process station is required.

## Enqueue-safety rules

A later agent converting checked items to queue tasks must:

1. Only enqueue checked decisions.
2. Ignore unchecked alternatives.
3. Treat checked `custom` instructions as authoritative for that machine.
4. Stop on conflicting checked options inside `Choose one` groups.
5. Preserve the source review path and decision ID in every queue task description.
6. Prefer one broad KB edit task per checked decision, but note when the implementation should split into smaller tasks if unrelated files or subsystems are affected.
7. Use KB edit tasks, not research tasks, unless the decision explicitly calls for `research_or_design_followup`.
8. Not infer additional work from the original research reports unless the checklist item directs it to do so.

## Checklist item template

```md
### Decision Group: Choose one

- [ ] `<machine_id>.action_slug`
  Action: Short imperative action.
  Action type: `note_cleanup`
  Queue task if checked: Concrete KB edit task description, including source review and expected files/areas to inspect.
  Notes: Constraints, alternatives, or do-not-do guidance.
  Freeform instructions:
  > 

- [ ] `<machine_id>.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for this machine from this review.
  Freeform instructions:
  > 
```

## Current agreed requirements

- The checklist must be actionable.
- "Do not do" guidance may be included when it is part of an actionable decision.
- Mutually compatible options should be in `Choose all that apply` sections.
- Mutually exclusive options should be in `Choose one` sections.
- Machine blocks should be ordered alphabetically by machine ID.
- Checked actions should become KB edit tasks.
- The checklist should include a standard freeform custom/user-choice checkbox.
