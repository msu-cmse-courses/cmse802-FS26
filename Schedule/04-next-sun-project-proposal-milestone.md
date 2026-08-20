---
layout: schedule
date: '2026-09-13'
---
# Milestone 1: Project Proposal and Initial Git Repository

## Due Date

This milestone is due on {{ page.date | date: "%B %d, %Y" }}.

## Purpose

This milestone establishes the project direction and the initial software foundation for the semester. It should show that the project is meaningful, feasible, and organized well enough to support later milestones.

## Required Deliverables

Submit:

- an initial repository with a visible project structure
- the URL to the repository’s main GitHub or GitLab page submitted through the course online form
- a short project proposal written as a Markdown file in the repository
- a standard proposal file named `paper/proposal.md` or an equivalent clearly documented name, using the scaffold in the project template repository at https://github.com/colbrydi/Research_Software_Project_Template
- a README that explains the purpose and basic workflow
- a brief note describing the next planned step

## Project Progress Expectations

Your proposal should include:

- a clear research question or software problem
- the main model components involved, such as analytical, physical, or data-driven elements
- a realistic software goal for the semester
- a first-phase plan with a timeline
- a basic plan for how the work will be tested or validated
- a concrete metric for success
- a short summary section that can later be adapted into a JOSS-style manuscript

## Software Engineering Expectations

The repository should demonstrate early software-engineering practice, including:

- Git and GitHub use, with at least one visible commit and instructor access
- a basic README with purpose, workflow, and project orientation
- initial environment or dependency instructions where appropriate
- a simple project structure that can grow over the semester
- a working Makefile or an equivalent documented workflow if one is included
- a proposal document that is written in a clear, reviewable Markdown format suitable for later expansion

## Acceptable Alternatives

Students are not expected to use the exact same tools in every project. If a project uses an alternative workflow, the student should clearly document:

- the alternative tool or workflow
- why it is appropriate for the project
- how to run it
- what output or behavior should be expected

## Instructor Review Process

The instructor should be able to review the repository quickly by reading the README, inspecting the structure, and understanding the proposed workflow. The repository should not require guesswork to interpret.

## Submission and Review Workflow

Each milestone is submitted by updating the student’s Git repository and making the current milestone work visible there. Students should commit the relevant changes and keep the repository in a reviewable state. For the first milestone, students should also submit the URL to their repository through the course online form: [CMSE Project Registration – Fill out form](https://forms.cloud.microsoft/r/KR51WhT02B). The link should open the repository’s main landing page on GitHub or GitLab so the instructor can access the project directly.

For milestones after the first one, no separate file or email submission is needed. The instructor will pull the latest state of the repository after the due date and grade whatever is present at that time. There are no extensions.

These milestones are cumulative by design. Students are encouraged to work ahead whenever possible, and many later milestones can be completed early if the project is already progressing well.

The proposal should also be written with the eventual JOSS paper in mind. Students may consult the JOSS paper guidance at https://joss.readthedocs.io/en/latest/paper.html while preparing this milestone.

## Baseline Make Commands

As a default reference workflow, students should be able to follow something like:

```bash
make help
make init
make check
make docs
```

These commands are intended as a baseline example based on the course template. A repository that follows this workflow is generally easier for the instructor to review and evaluate. The easier it is for the instructor to grade the project, the better the evaluation experience will be for everyone.

## Evidence of Completion

Submit a link to the repository and a short summary that explains:

- the project goal
- the current repository state
- the first planned next step

