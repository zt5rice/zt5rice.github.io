## Summary

- Added the approved Portfolio v2 plan, backup manifest, and rollback procedure.
- Captured the current live GitHub Pages repository at commit `97fdef9fbadd811947e92b586ca7427226537457`.
- Created and verified a Git bundle plus a full repository archive.
- Confirmed that restoring the bundle reproduces the baseline commit exactly.
- Created the `portfolio-v2` working branch while leaving `master` unchanged.

## Tracking

- Linear: `ZHA-185`
- Ticket: Back up the existing site and initialize the working workspace

## What changed

- `docs/PLAN.md`: approved scope, design direction, content rules, ticket map, and release gates.
- `docs/BACKUP.md`: baseline commit, backup artifacts, restore validation, and checksums.
- `docs/ROLLBACK.md`: protected baseline, preferred rollback flow, and emergency restore steps.

## Why

The existing GitHub Pages site must remain recoverable before any redesign work begins. This PR establishes the verified backup and written rollback procedure that every later ticket depends on.

## Validation

- `shasum -a 256 -c SHA256SUMS`: bundle and archive both passed.
- Restored the Git bundle into an isolated temporary directory.
- Compared original and restored `HEAD`: both resolved to `97fdef9fbadd811947e92b586ca7427226537457`.
- `git diff --check`: passed.
- No production branch or GitHub Pages setting was modified.

## Media evidence

No UI change in this ticket. No screenshot is required.

## Risk / rollback

- Risk: low. This PR adds documentation only and does not change runtime site files.
- `master` remains at the captured baseline.
- A separate 15 MB Git bundle and 30 MB archive are stored outside the website repository under `person_website/backups/`.
- Emergency restore commands are documented in `docs/ROLLBACK.md`.

## Merge gate

- Required approver: Zhao Tang.
- This PR is opened as a draft.
- Do not merge, squash-merge, auto-merge, or push directly to `master` before explicit manual approval.
