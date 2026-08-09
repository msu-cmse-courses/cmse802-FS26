---
layout: schedule
date: '2026-10-25'
---

# Milestone 4: Documentation and Reproducibility Pass

## Due Date

This milestone is due on {{ page.date | date: "%B %d, %Y" }}.

## Purpose

This milestone should make the project easier to understand, run, and evaluate. It should also demonstrate that documentation and reproducibility are part of the project itself, not extra work added later.

## Required Deliverables

Submit:

- improved documentation for the project workflow and outputs
- clear instructions for installation, setup, or execution
- a reproducible path for someone else to evaluate the work

## Project Progress Expectations

Your submission should include:

- a clearer explanation of the project purpose and current state
- examples of expected input, output, or workflow behavior
- enough information for a new reader to understand what the project does and how it fits together

## Software Engineering Expectations

The repository should demonstrate structured documentation and reproducibility practice, such as:

- a stronger README or project overview
- environment or dependency instructions
- generated or structured documentation when appropriate, such as pdoc or an equivalent system
- comments, docstrings, or other explanatory material for core components
- a working Makefile or documented equivalent workflow for running the project

## Acceptable Alternatives

If the project uses alternative documentation or publishing tools, those are acceptable when they provide equivalent clarity and reproducibility. Students should identify the tool used and explain how it should be run.

## Instructor Review Process

The instructor should be able to understand the project quickly, install or access the required dependencies, and follow the documented path to evaluate the work. The repository should not rely on hidden assumptions.

## Submission and Review Workflow

Each milestone is submitted by updating the student’s Git repository and making the current milestone work visible there. Students should commit the relevant changes and keep the repository in a reviewable state. No separate file or email submission is needed for this milestone. The instructor will pull the latest state of the repository after the due date and grade whatever is present at that time. There are no extensions.

These milestones are cumulative by design. Students are encouraged to work ahead whenever possible, and many later milestones can be completed early if the project is already progressing well.

## Baseline Make Commands

As a default reference workflow, students should be able to follow something like:

```bash
make help
make init
make docs
make check
```

This milestone should demonstrate that the project is understandable and reproducible enough for another person to evaluate. A repository that follows the course-standard workflow is generally more portable and easier to review.

## Evidence of Completion

Submit a link to the repository and a short summary that explains:

- what documentation or reproducibility improvements were added
- which tool or workflow was used
- how a reviewer should run or evaluate the project
- how these materials will support the final JOSS-style manuscript and project handoff