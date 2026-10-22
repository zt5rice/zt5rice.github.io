# Rollback Procedure

## Protected baseline
- Repository: `zt5rice/zt5rice.github.io`
- Baseline branch: `master`
- Baseline commit: `97fdef9fbadd811947e92b586ca7427226537457`
- Baseline tag: `pre-portfolio-redesign-2026-10-21`

## Backup artifacts
Stored outside the website repository in `/Users/zhaotang/projects/person_website/backups/`:

- `zt5rice.github.io-pre-redesign-2026-10-21.bundle`
- `zt5rice.github.io-pre-redesign-2026-10-21.tar.gz`
- `SHA256SUMS`

## Validation already completed
The bundle was cloned into an isolated temporary directory and its `HEAD` matched the baseline commit exactly.

## Preferred rollback after a bad merge
1. Stop deployment work and identify the bad merge commit.
2. Create a new revert commit; do not rewrite shared history.
3. Open a rollback PR referencing the affected ticket.
4. Require Zhao Tang's manual approval before merging the rollback PR.
5. Verify the production URL, resume, case-study pages, and social preview.

## Emergency restore from the backup bundle
```bash
git clone /Users/zhaotang/projects/person_website/backups/zt5rice.github.io-pre-redesign-2026-10-21.bundle /private/tmp/zt5rice-restore
cd /private/tmp/zt5rice-restore
git checkout 97fdef9fbadd811947e92b586ca7427226537457
```

Do not force-push `master` without explicit human approval. Preserve the Git history and record every rollback action in Linear.
