---
layout: schedule
date: '2026-10-11'
---

# Milestone 3: Testing and Validation Baseline

## Due Date

This milestone is due on {{ page.date | date: "%B %d, %Y" }}.

## Purpose

This milestone should show that the project has begun to mature from a prototype into something that can be checked, evaluated, and trusted with greater confidence. It should also demonstrate that testing or validation is treated as part of the project workflow.

## Required Deliverables

Submit:

- a core test, validation step, or quality check for the project
- evidence that the main workflow behaves as expected for at least one meaningful use case
- a short explanation of assumptions, limitations, or known edge cases

## Project Progress Expectations

Your submission should include:

- a clearly demonstrated core capability or workflow
- evidence that the project behaves correctly for an important use case
- enough validation to show that the implementation is not only present but also meaningful

## Software Engineering Expectations

The repository should include practical evidence of testing or validation, such as:

- pytest or an equivalent testing framework
- a validation script, notebook, or reproducible check
- documented expectations for success and failure
- a workflow that allows another person to repeat the validation process
- a working Makefile or equivalent entry point if the project uses one

## Acceptable Alternatives

If a project uses a different language or ecosystem, an equivalent validation approach is acceptable. Students should clearly document the tool used, how to run it, and what results should be expected.

## Instructor Review Process

The instructor should be able to run or inspect the validation workflow without needing extra explanation. The repository should make it clear how the tests or checks are supposed to work.

## Submission and Review Workflow

Each milestone is submitted by updating the student’s Git repository and making the current milestone work visible there. Students should commit the relevant changes and keep the repository in a reviewable state. No separate file or email submission is needed for this milestone. The instructor will pull the latest state of the repository after the due date and grade whatever is present at that time. There are no extensions.

These milestones are cumulative by design. Students are encouraged to work ahead whenever possible, and many later milestones can be completed early if the project is already progressing well.

## Baseline Make Commands

As a default reference workflow, students should be able to follow something like:

```bash
make help
make init
make test
make check
```

This milestone should show that the project has a repeatable validation workflow. If the repository uses a different approach, the student should explain it clearly and show that it provides equivalent functionality.

## Evidence of Completion

Submit a link to the repository and a short summary that explains:

- what was tested or validated
- which tool or workflow was used
- what remains untested or still needs attention
- how the validation results could later support the final report and software quality discussion