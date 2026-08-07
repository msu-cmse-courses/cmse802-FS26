# Course Website Template

This repository is a semester-portable, schedule-first course website template.

## First-Time Instructor Checklist

1. Update site settings in `_config.yml`.
	- Set `title`, `description`, and `baseurl`.
	- Confirm logo path.
2. Replace example content pages.
	- Update `index.md`.
	- Replace pages in `Guide/`.
	- Replace pages in `Schedule/`.
	- Any page marked with `**⚠️TODO:**` is intended to be replaced.
3. Update semester dates.
	- Edit `config/fall_calendar.yml` or `config/spring_calendar.yml`.
4. Generate schedule + calendar data.
	- Run `make schedule-fall` or `make schedule-spring`.
5. Review generated files before publishing.
	- `_data/schedule.yml`
	- `_data/schedule_warnings.yml`
	- `course_calendar.ics`

Core design goals:

- Calendar-driven class timeline from `config/[semester]_calendar.yml`
- Instructor-friendly schedule authoring from files in `Schedule/`
- Automatic `_data/schedule.yml` generation (no manual schedule YAML editing)
- Build-as-you-go publishing with `TBD` placeholders for missing class content

## Quick Start

1. Update the semester calendar file:
	- `config/fall_calendar.yml` or `config/spring_calendar.yml`
2. Add or rename files in `Schedule/` using the naming convention in:
	- `Instructors/Schedule_Filename_Convention.md`
3. Generate schedule data for the semester:

```bash
make schedule-fall
```

or

```bash
make schedule-spring
```

## What The Generator Produces

Running `make schedule-...` executes `scripts/update_schedule.py` and writes:

- `_data/schedule.yml`
- `_data/schedule_warnings.yml`
- `course_calendar.ics`

Behavior:

- All class days computed from the semester calendar are always included.
- If a matching class file is missing, the class appears as `TBD` with no link.
- Relative schedule items (same day, plus offset, next weekday) are added from filename parsing.
- Non-class calendar events (holidays, breaks, closures) are merged into the same schedule timeline.
- The generated `course_calendar.ics` includes schedule dates and links for calendar subscription.

## Local Development

Create or update the conda environment first:

```bash
make envs
```

Install/update local Ruby gems (inside the conda environment):

```bash
make bundle-install
```

Serve locally:

```bash
make serve
```

If you are testing before a GitHub remote is configured, use the local-safe serve target from the Makefile.

```bash
make serve-local
```

Build static site output into `_site/`:

```bash
make build-site
```

## Optional: Automatic Reminder Before Push

If you want an automated reminder, you can enable a local Git pre-push hook that checks schedule artifacts before every push.

Install it once:

```bash
./scripts/install_git_hooks.sh
```

What it does on `git push`:

- runs `make schedule-fall` (or another target you set)
- checks whether generated files changed
- blocks push if updates are needed so you can commit them first

Generated files checked:

- `_data/schedule.yml`
- `_data/schedule_warnings.yml`
- `course_calendar.ics`

If you need spring generation for a specific push:

```bash
SCHEDULE_MAKE_TARGET=schedule-spring git push
```

## GitHub Pages Recommendation

Use `main` as source branch and publish from the repository root.

Recommended flow:

1. Run `make schedule-fall` or `make schedule-spring` when calendar/schedule content changes.
2. Commit source files plus generated `_data/schedule.yml`, `_data/schedule_warnings.yml`, and `course_calendar.ics`.
3. In GitHub Pages settings, set source to `main` / `root`.
4. Let GitHub Pages render Jekyll automatically.

This keeps editing simple (including GitHub web edits) and avoids a local pre-build publish step.

## Two Supported Workflows

1. GitHub-first workflow (quick edits in web UI)
	- Edit markdown/config files in GitHub.
	- Ensure `_data/schedule.yml` is current when schedule/calendar changes.
	- Let GitHub Pages render from `main` / `root`.

2. Local preview workflow (quick validation before push)
	- `make envs`
	- `make bundle-install`
	- `make serve`
	- Preview locally, then push source files.

## GitHub Rendering Compatibility Notes

- GitHub Pages native rendering has a restricted plugin set.
- This template is designed to work without requiring custom plugin execution in GitHub.
- Schedule generation is handled by `scripts/update_schedule.py`, which writes `_data/schedule.yml` before commit.

## Dependencies

- Python 3
- Conda (environment is defined in `environment.yml`)
- `pyyaml` and `jupyterlab` are installed through the conda environment
- Ruby and Bundler are installed through the conda environment
- Jekyll is installed via `bundle install` using the `github-pages` gem stack in `Gemfile`

## Notes for Template Authors

- Manual `<!-- TOC_START -->` blocks are no longer required.
- The right-side TOC is generated automatically from page headings.
- You can still keep manual TOC sections if desired, but the default workflow is automatic.

