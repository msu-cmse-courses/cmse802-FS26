# Schedule Filename Convention

This template uses the filenames in the `Schedule` folder to define course pacing.

The goal is that an instructor can run `ls Schedule` and immediately see the instructional flow of the semester in order, without needing to manually maintain schedule dates in a separate file.

## Core Rule

The leading two-digit number is the course-day anchor.

- `01` means the first instructional meeting.
- `02` means the second instructional meeting.
- `03` means the third instructional meeting.

The actual calendar date for each numbered course day is computed from the selected `config/[semester]_calendar.yml` file.

The website should show real dates, not the course-day number.

## Instructor Setup Checklist

Use this checklist when starting a new course site from this template.

1. Update basic site identity in `/_config.yml`.
	- Set `title`, `description`, and `baseurl` for your repository.
	- Confirm the logo path points to your course or institution image.
2. Choose the semester calendar in `config/`.
	- Update `config/fall_calendar.yml` or `config/spring_calendar.yml`.
	- Verify first day, last day, meeting days, and breaks/cancelled classes.
3. Add schedule pages in `Schedule/` using the filename rules in this document.
	- Start with core `NN-class-*` pages.
	- Add due dates/checkpoints using `NN-same-*`, `NN-plus-*`, and `NN-next-*` as needed.
4. Add reference/policy pages under `Guide/` (and other top-level reference folders if needed).
	- Keep an entry page named `00-*.md` in each reference folder.
	- Use `layout: guide` for reference pages.
5. Generate schedule data.
	- Run the schedule generation command from the Makefile for your semester.
	- Confirm `_data/schedule.yml`, `_data/schedule_warnings.yml`, and `course_calendar.ics` update.
6. Review and clean warnings.
	- Fix filename mismatches or missing anchors reported in `_data/schedule_warnings.yml`.
7. Publish workflow check.
	- Verify local serve/build works.
	- Commit source files plus generated `_data/schedule.yml`, `_data/schedule_warnings.yml`, and `course_calendar.ics` before publishing.

## Example Content Replacement Policy

Pages in `Guide/`, `Schedule/`, and `index.md` that start with `**⚠️TODO:**` are placeholder examples.

- Instructors should either delete these files or replace their full content.
- Keep filename conventions in `Schedule/` if you want generated schedule links to keep working.
- For reference folders like `Guide/`, keep one `00-*.md` entry page per folder for menu routing.

Recommended replacement order:

1. Replace `index.md` with a real course landing page.
2. Replace `Guide/00-index.md` and `Guide/01-Syllabus.md`.
3. Replace all `Schedule/NN-class-*.md` files used this semester.
4. Re-run `make schedule-fall` or `make schedule-spring`.

## Calendar Subscription File

This template generates `course_calendar.ics` from `_data/schedule.yml`.

- The ICS includes schedule titles and dates for class and non-class events by default.
- Class events are exported as timed events (default 12:30-13:40).
- Non-class events are exported as all-day entries.
- When a schedule item has a URL, that link is included in the event.

Common commands:

- Regenerate both schedule data and ICS: `make schedule-fall` or `make schedule-spring`
- Regenerate only ICS from existing schedule data: `make calendar-ics`

## What Goes in `Schedule`

Use the `Schedule` folder for course content that should stay attached to the instructional pacing of the course.

Examples:

- class meeting pages
- homework due dates
- project checkpoints
- quizzes
- readings tied to a class day

## What Stays in `config/[semester]_calendar.yml`

Use the semester calendar file for dates that are about the institution or the semester itself rather than course content.

Examples:

- first and last day of the semester
- meeting days such as Tuesday and Thursday
- holidays
- fall break or spring break
- cancelled classes
- snow days
- manual date overrides

## Filename Grammar

Use lowercase, hyphen-separated filenames.

### 1. Class meetings

Pattern:

```text
NN-class-topic-slug.md
```

Examples:

```text
01-class-welcome.md
02-class-git-workflow.md
03-class-project-framing.md
```

Meaning:

- `NN` is the instructional meeting number.
- `class` means the item lands on that class meeting date.

### 2. Same-day items

Pattern:

```text
NN-same-topic-slug.md
```

Examples:

```text
05-same-reading-quiz.md
10-same-project-checkpoint.md
```

Meaning:

- The item happens on the same calendar date as class day `NN`.
- Use this when an event is tied to the same day but is not the main class page.

### 3. Calendar-day offsets

Pattern:

```text
NN-plus-D-topic-slug.md
```

Examples:

```text
06-plus-2-homework-1.md
12-plus-5-reflection.md
```

Meaning:

- Start from class day `NN`.
- Move forward `D` calendar days.
- Use this for due dates such as "two days after Day 06."

### 4. Next weekday after a class day

Pattern:

```text
NN-next-WDAY-topic-slug.md
```

Where `WDAY` is one of:

```text
mon tue wed thu fri sat sun
```

Examples:

```text
06-next-sun-homework-1.md
08-next-fri-lab-checkpoint.md
```

Meaning:

- Start from class day `NN`.
- Find the first named weekday strictly after that class date.
- Use this for patterns such as "the following Sunday after class day 06."

## Sorting Behavior

These filenames are designed to sort cleanly in directory listings.

Examples:

```text
01-class-welcome.md
01-same-syllabus-quiz.md
01-next-sun-homework-1.md
02-class-version-control.md
02-plus-2-reading-response.md
03-class-project-selection.md
```

This keeps all items associated with course day `01` together, then all items associated with course day `02`, and so on.

## Recommended Interpretation Rules

The schedule-generation script should interpret filenames as follows:

1. `NN-class-*` maps to the calendar date of course day `NN`.
2. `NN-same-*` maps to the same calendar date as course day `NN`.
3. `NN-plus-D-*` maps to `D` calendar days after course day `NN`.
4. `NN-next-WDAY-*` maps to the first matching weekday after course day `NN`.

The generated `_data/schedule.yml` file should then merge these items with non-class events defined in the semester calendar file.

## Missing Content and TBD Behavior

The schedule generator should always output all instructional class days computed from `config/[semester]_calendar.yml`, even when matching `Schedule` files do not exist yet.

If a class-day content file is missing:

- Include that date in `_data/schedule.yml`.
- Set a placeholder title such as `TBD`.
- Leave `url` empty or null.
- Keep the item visible on the website schedule.

When the instructor later adds the matching file and reruns the generator, the same schedule entry should automatically switch from `TBD` to the real title and link.

This supports a build-as-you-go workflow while preserving a complete semester calendar view for students.

## Mismatch Handling Rules

The generator should validate filename-to-calendar alignment and report warnings.

Recommended behavior:

1. Missing `NN-class-*` file for a computed class day:
	Generate a `TBD` class entry and warn.
2. Multiple `NN-class-*` files for the same anchor:
	Warn and use a deterministic tie-breaker (for example, lexical filename order) until resolved.
3. Anchor number larger than computed class-day count:
	Warn and skip, unless an explicit override is configured.
4. `NN-same-*`, `NN-plus-*`, or `NN-next-*` without a valid anchor day:
	Warn and skip.

Warnings should not fail the whole build by default; they should guide cleanup while still producing a usable website.

## Migration Workflow

The intended workflow for a new semester is:

1. Update `config/[semester]_calendar.yml`.
2. Reuse or adjust files in `Schedule`.
3. Run one schedule-generation command.
4. Regenerate `_data/schedule.yml` automatically.

This keeps instructional pacing in the `Schedule` folder while allowing semester dates to shift cleanly between terms.

## Repository and Publishing Structure Recommendation

For simplicity, keep a single source branch and publish from repository root:

1. Authoring source remains at repository root.
2. Generated schedule files remain in `_data/` and `course_calendar.ics`.
3. GitHub Pages is configured to publish from `main` branch, `root`.

Why this is the default recommendation:

- It keeps workflow simple for instructors using GitHub web edits.
- It avoids extra build-output folders and branch juggling.
- It aligns with this template's schedule-first generation flow.

## Notes

- Do not encode holidays or snow days as `Schedule` files unless they are actual course content items.
- Prefer filename-based pacing for instructor-authored content and calendar YAML for institutional constraints.