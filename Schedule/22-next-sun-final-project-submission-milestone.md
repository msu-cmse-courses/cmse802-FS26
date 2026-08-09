---
layout: schedule
date: '2026-11-22'
---

# Milestone 6: Final Project Submission and Presentation Materials

## Due Date

This milestone is due on {{ page.date | date: "%B %d, %Y" }}.

## Purpose

This milestone marks the completion of the course project. It should show that the project is not only finished, but also documented, reviewable, and supported by software-engineering practices that make the work understandable and reusable.

## Required Deliverables

Submit:

- the final repository for the project
- a polished and complete version of the main workflow or software artifact
- supporting documentation, examples, and usage instructions
- a JOSS-style manuscript written as a Markdown file in the repository, using the scaffold in `paper/paper.md` from the project template repository at https://github.com/colbrydi/Research_Software_Project_Template
- presentation materials or a short demonstration plan for sharing the work

## Project Progress Expectations

Your submission should include:

- a complete project that addresses the original research question, modeling goal, or software problem
- evidence of the main technical contributions and results
- a clear summary of limitations, next steps, or lessons learned

## Software Engineering Expectations

The final project should demonstrate that software engineering practices are integrated into the work, including:

- a usable repository structure
- clear installation, running, and evaluation instructions
- testing, validation, or quality checks where appropriate
- documentation that supports reuse and review
- a working Makefile or equivalent documented workflow when relevant
- a final manuscript that follows a JOSS-style structure and can be adapted for submission or future publication

## Acceptable Alternatives

Students may use alternative tools or workflows when appropriate. If they do, they should explain the tool, how to run it, and why it is suitable for the project.

## Instructor Review Process

The instructor should be able to review the final project by reading the repository, following the documented workflow, and understanding how the work was evaluated. The project should be understandable without special assistance.

## Submission and Review Workflow

Each milestone is submitted by updating the student’s Git repository and making the current milestone work visible there. Students should commit the relevant changes and keep the repository in a reviewable state. No separate file or email submission is needed for this milestone. The instructor will pull the latest state of the repository after the due date and grade whatever is present at that time. There are no extensions.

These milestones are cumulative by design. Students are encouraged to work ahead whenever possible, and many later milestones can be completed early if the project is already progressing well.

The final manuscript should be prepared with the JOSS submission guidance in mind. Students should consult the JOSS website at https://joss.readthedocs.io/ while preparing the final paper.

## Baseline Make Commands

As a default reference workflow, students should be able to follow something like:

```bash
make help
make init
make check
make docs
```

The final project should be easy to review, easy to run, and easy to evaluate. A workflow that follows the course-standard commands is more portable and more likely to receive a strong evaluation than one that departs sharply from the expected structure.

## Evidence of Completion

Submit a link to the repository and a short summary that explains:

- the project goal and final outcome
- the main software-engineering practices used
- the location of the JOSS-style manuscript and its relation to the final repository
- any presentation or demonstration materials that support the submission