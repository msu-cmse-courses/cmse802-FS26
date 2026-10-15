---
layout: guide
---

# Days 11-12 - Code Review and Repository Cleanup Days

## Goals for the Week

This week provides an opportunity to pause the normal repository exercises and focus directly on student projects.

By this point in the semester, students have begun developing their own software and have received their first round of instructor feedback. The goal of these two class meetings is to help students improve the quality, usability, and organization of their project repositories.

Key messages:

- Good software is not only about writing code.
- Repository organization matters.
- Documentation matters.
- Reproducibility matters.
- Fresh eyes often reveal problems that the original author never notices.

## Day 1: Live Code Review and Repository Cleanup

### Live Code Review

I begin class by conducting a live code review of a student project (with the student's permission).

The goal is not to criticize the project or evaluate the student. The goal is to model the thought process of someone trying to understand and use unfamiliar software.

The review typically includes:

- Examining the repository structure.
- Reading the README.
- Looking at installation instructions.
- Exploring notebooks and source files.
- Identifying strengths.
- Identifying opportunities for improvement.

I intentionally think out loud during the process and encourage questions from the class.

Students often learn as much from watching the review as they do from receiving their own individual feedback.

### Repository Cleanup

After the review, students spend the remainder of class cleaning and organizing their repositories.

Common cleanup tasks include:

- Removing unused files.
- Removing outdated notebooks.
- Updating README files.
- Improving documentation.
- Reorganizing directories.
- Removing large or unnecessary data files.
- Cleaning up experimental code.

One lesson learned from previous offerings of the course is that repository templates can unintentionally encourage students to keep files they do not actually need.

I originally encouraged students to begin with a fairly complete repository template. In practice, many students left large portions of the template untouched, resulting in cluttered repositories and confusion about which files mattered.

In future offerings, I would recommend treating templates as examples and references rather than starting points. It is often easier for students to begin with a minimal repository and add components as they become necessary.

### Teaching Philosophy

Students frequently believe that software development consists primarily of writing code.

This class period helps reinforce the idea that maintaining, organizing, documenting, and simplifying software are equally important skills.

Removing unnecessary complexity is often one of the most valuable improvements a student can make.

## Day 2: Peer Code Reviews

### Activity Overview

Students conduct peer code reviews in pairs or small groups.

I ask students to imagine the following scenario:

> You are a new undergraduate researcher joining this lab. The repository belongs to a graduate student or senior researcher. Your goal is to get the software running, understand how it works, and perform some useful work with it.

The repository author becomes the "lab mentor" while the reviewer plays the role of the new student.

This framing works well because it reflects a common academic research experience.

### Suggested Process

Ask students to:

1. Meet with their partner.
2. Introduce the project.
3. Explain the research goals at a high level.
4. Walk through setup and installation.
5. Help the reviewer run the software.
6. Demonstrate a workflow or experiment.
7. Gather feedback.

Encourage reviewers to ask questions whenever something is unclear.

Typical questions include:

- Where should I start?
- Which file am I supposed to run?
- What does this notebook do?
- How do I install the dependencies?
- What input data do I need?
- How do I know if everything is working?

These are exactly the types of questions future lab members will ask.

### What to Expect

Students are often surprised by how difficult it can be to explain their own software.

Repositories that seem obvious to their authors may be confusing to someone seeing them for the first time.

Common discoveries include:

- Missing instructions.
- Assumptions about prior knowledge.
- Confusing file names.
- Poor documentation.
- Hidden dependencies.
- Inconsistent workflows.

These discoveries should be viewed as successes rather than failures. The purpose of the exercise is to uncover issues while there is still time to improve them.

### Teaching Philosophy

The goal of peer review is not to judge code quality.

The goal is to evaluate usability.

Students often focus on whether code works. Future users care about whether they can understand and use the software.

This activity helps students practice:

- Communication.
- Documentation.
- Software onboarding.
- Collaborative development.
- User-centered design.

More importantly, it gives students an opportunity to experience both sides of the relationship: the developer and the new user.

## End of Week Checkpoint

By the end of the week, students should ideally:

- Have received feedback from both the instructor and peers.
- Have cleaned and organized their repositories.
- Have improved documentation and project structure.
- Better understand how others experience their software.
- Be thinking about their projects from the perspective of future users and collaborators.

The most important outcome is that students begin viewing their software as something that must be understandable by others, not just something that works on their own computer.
