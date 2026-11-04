---
layout: schedule
published: true
date: '2026-11-17'
---

# JOSS Software Review Studio

Today you will examine a published research software project as a prospective user and reviewer. Choose a project from the [Journal of Open Source Software paper archive](https://joss.theoj.org/papers), read its paper, and use the repository to gather evidence about its software practices.

The goal is not to understand every part of the codebase or to become an expert user. The goal is to learn from a real research software project and identify one practice you can apply to your own release candidate.

## Agenda (80 minutes)

1. 10 min - Introduction, project selection, and review plan
2. 15 min - Read the JOSS paper and identify its software contribution
3. 35 min - Review the repository and attempt one bounded first-use workflow
4. 15 min - Complete the review card and prepare your Day 23 presentation
5. 5 min - Exit check: identify one practice to apply to your own project

### Learning Goals

By the end of this class, you should be able to:

- evaluate an unfamiliar research software project using observable evidence; and
- identify a documented software practice that could improve your own project's handoff readiness.

## Choose a JOSS Project

Use the [JOSS paper archive](https://joss.theoj.org/papers) to find a project that interests you. It does not need to be directly related to your research, but it should have a public repository and a paper you can read during class.

Record the paper citation, repository URL, and a release, tag, or commit you reviewed. Reviewing a fixed version makes your observations clear and repeatable.

## Review the Paper and Repository

First, read the JOSS paper. Identify the problem the software solves, its intended users, its contribution, and the evidence the authors use to show that it is useful.

Then examine the repository as a potential user. Follow the README and attempt one bounded first-use path:

- install the project;
- run a documented example, tutorial, or test;
- inspect a demonstration workflow; or
- reproduce one documented output.

You are not expected to understand the full codebase or successfully install every project. Record what you observe, including useful failures, rather than silently working around unclear instructions.

Complete the [JOSS Software Review Card](../Guide/22-JOSS-Software-Review-Card.md) as you work.

## Review Focus

Use the Safe, Portable, Reproducible, Robust, and Literate (SPRRL) framework:

- **Safe:** Are risks, assumptions, and data-handling expectations clear?
- **Portable:** Can a new user identify the setup and dependency requirements?
- **Reproducible:** Does the documentation provide a credible path from clone to a meaningful result?
- **Robust:** Are tests, validation checks, or understandable failure paths available?
- **Literate:** Can a future researcher understand the project purpose, workflow, outputs, and limitations?

## Prepare for Day 23

Prepare a two-minute presentation that names the project, explains what it does, shares one observed strength and one improvement opportunity, and identifies one practice you will apply to your own project.

## Before Next Class

- Complete your [JOSS Software Review Card](../Guide/22-JOSS-Software-Review-Card.md).
- Bring your two-minute presentation notes.
- Add the one practice you plan to adopt to your release-candidate fix plan.

## Daily Check-in and Reflection

[Daily Check-in Form](https://forms.cloud.microsoft/r/QkH6Mx8FUd)
