---
layout: schedule
date: '2026-11-08'
---


# Milestone 5: Project Systems and Automation

## Due Date

This milestone is due on {{ page.date | date: "%B %d, %Y" }}.

## Purpose

This milestone should show that the project is not just a collection of scripts or notebooks, but a working system that can be run, checked, and reviewed by someone else. The emphasis here is on the operational infrastructure that makes a project reproducible and maintainable.

## Required Deliverables

Submit:

- a working project workflow that can be run from the repository root
- at least one reproducible automation entry point, such as a Makefile target or equivalent command sequence
- clear instructions for how to set up the environment and execute the main workflow
- evidence that the project can be evaluated without hidden setup steps or undocumented assumptions

## Project Progress Expectations

Your submission should include:

- a clean, repeatable way to initialize or configure the project
- a documented command or workflow for running the main analysis, build, or validation path
- a basic operational structure that another student or instructor can follow without extra explanation

## Software Engineering Expectations

The repository should demonstrate practical systems thinking, including:

- a usable `Makefile` or equivalent project command interface
- commands for environment setup, project checks, and local execution
- a reproducible path to run the project from a clean starting point
- enough structure that the repository looks and behaves like a real project rather than a loose collection of files

This is an opportunity to use the course tooling already in the repository. Good examples include:

- `make help`
- `make envs`
- `make serve`
- `make build-site`
- `make check`
- a documented `make init` or equivalent setup workflow

A project does not need to use exactly these targets, but it should have a comparable command interface that makes the workflow explicit and reviewable.

## Acceptable Alternatives

If the project uses a different stack or workflow, that is acceptable as long as it provides the same practical value: start-up instructions, reproducible execution, and a clear way to validate the project state. Students should explain the tool or workflow they selected and why it fits their project.

## Instructor Review Process

The instructor should be able to inspect the repository, understand the key workflow, and run the project with minimal friction. The project should feel operationally ready, not merely conceptually complete.

## Submission and Review Workflow

Each milestone is submitted by updating the student’s Git repository and making the current milestone work visible there. Students should commit the relevant changes and keep the repository in a reviewable state. No separate file or email submission is needed for this milestone. The instructor will pull the latest state of the repository after the due date and grade whatever is present at that time. There are no extensions.

These milestones are cumulative by design. Students are encouraged to work ahead whenever possible, and many later milestones can be completed early if the project is already progressing well.

## Baseline Make Commands

As a default reference workflow, students should be able to follow something like:

```bash
make help
make envs
make check
make serve
```

If the repository uses a different command structure, students should document it clearly and show that it provides a comparable path for evaluation, reproducibility, and handoff.

## Evidence of Completion

Submit a link to the repository and a short summary that explains:

- which project workflow was automated or standardized
- what command or tool was used to run the project
- how a reviewer should set up and execute the project
- what remains to be polished before the release-candidate stage