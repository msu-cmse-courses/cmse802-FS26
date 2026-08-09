---
layout: schedule
date: '2026-11-08'
---

# Milestone 5: Release Candidate and Handoff Package

## Due Date

This milestone is due on {{ page.date | date: "%B %d, %Y" }}.

## Purpose

This milestone should show that the project is approaching a stable and presentable state. It should also demonstrate that the software-engineering practices introduced earlier in the course are now integrated into a nearly complete project workflow.

## Required Deliverables

Submit:

- a release-candidate version of the project
- a repository that is organized and understandable for review
- a short handoff note describing what is ready and what remains optional

## Project Progress Expectations

Your submission should include:

- a near-final version of the main workflow or software artifact
- a clear presentation of the project’s current capabilities
- evidence that the work is close to the final intended outcome

## Software Engineering Expectations

The release candidate should demonstrate a mature and reviewable software workflow, including:

- a clean repository structure and consistent organization
- passing or otherwise documented tests or validation checks
- updated documentation and usage instructions
- a working Makefile or equivalent documented workflow if relevant
- evidence that the project can be evaluated by someone else without special setup knowledge

## Acceptable Alternatives

If the project uses a different tooling stack, the student should explain the equivalent approach and provide instructions for how it should be run or reviewed.

## Instructor Review Process

The instructor should be able to inspect the repository, understand the current state of the project, and evaluate quality with minimal friction. The README and project structure should support this review.

## Submission and Review Workflow

Each milestone is submitted by updating the student’s Git repository and making the current milestone work visible there. Students should commit the relevant changes and keep the repository in a reviewable state. No separate file or email submission is needed for this milestone. The instructor will pull the latest state of the repository after the due date and grade whatever is present at that time. There are no extensions.

These milestones are cumulative by design. Students are encouraged to work ahead whenever possible, and many later milestones can be completed early if the project is already progressing well.

## Baseline Make Commands

As a default reference workflow, students should be able to follow something like:

```bash
make help
make init
make check
make docs
```

This milestone should show that the project is close to a polished, review-ready state. The more closely the workflow aligns with the course-standard commands, the easier it will be for the instructor to evaluate the repository.

## Evidence of Completion

Submit a link to the repository and a short summary that explains:

- the project state at release-candidate stage
- the software-engineering practices that are now in place
- the most important remaining improvement areas