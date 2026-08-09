---
layout: schedule
date: '2026-09-27'
---

# Milestone 2: Initial Prototype and Working Workflow

## Due Date

This milestone is due on {{ page.date | date: "%B %d, %Y" }}.

## Purpose

This milestone should demonstrate that the project has moved beyond planning and now has an early, meaningful implementation. It should also show that basic software-engineering practices are being used as part of the project workflow rather than as isolated exercises.

## Required Deliverables

Submit:

- a working prototype or early implementation of the core project capability
- evidence that the project can be run or exercised in a meaningful way
- a short note describing the current state of the work and the next planned improvements

## Project Progress Expectations

Your submission should include:

- a working implementation of the main feature, workflow, or analysis pipeline
- a clear example of the output or result the software produces
- enough functionality to make the project credible and worth continuing

## Software Engineering Expectations

The prototype should also demonstrate at least one practical software-engineering practice, such as:

- linting or equivalent code-quality checks
- environment or dependency setup instructions
- a documented workflow for running the prototype
- basic repository organization that supports future development
- a working Makefile or an equivalent documented entry point when appropriate

## Acceptable Alternatives

If the project uses a different language or toolchain, an equivalent practice is acceptable. For example, a student may use a comparable linting, formatting, or environment tool if it is appropriate for the project and clearly documented.

## Instructor Review Process

The instructor should be able to understand the prototype quickly, run or inspect the basic workflow, and see how the project is organized. The README and repository layout should support this process.

## Submission and Review Workflow

Each milestone is submitted by updating the student’s Git repository and making the current milestone work visible there. Students should commit the relevant changes and keep the repository in a reviewable state. No separate file or email submission is needed for this milestone. The instructor will pull the latest state of the repository after the due date and grade whatever is present at that time. There are no extensions.

These milestones are cumulative by design. Students are encouraged to work ahead whenever possible, and many later milestones can be completed early if the project is already progressing well.

## Baseline Make Commands

As a default reference workflow, students should be able to follow something like:

```bash
make help
make init
make lint
make test
make docs
```

This milestone should show that the project can be exercised and reviewed in a straightforward way. A workflow that follows the course-standard commands is usually easier for the instructor to assess than one that diverges significantly from the expected approach.

## Evidence of Completion

Submit a link to the repository and a brief summary that explains:

- what the prototype demonstrates
- what software-engineering tools or practices are already in place
- what remains to be improved
- how the current work may later contribute to the proposal and final report sections