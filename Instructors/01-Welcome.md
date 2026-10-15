---
layout: guide
---

# Day 1 Instructor Notes - Welcome

## Goals for the Day

The first day is primarily about setting expectations for the course and ensuring students have the basic tools needed to participate.

Key messages to communicate:

- CMSE 802 is an elective course focused on research software and computational modeling.
- Much of the learning happens during class through activities, discussions, and hands-on exercises.
- Most work completed outside of class should directly support the student's own research project.
- Every student should have a research project they intend to use throughout the semester. If a student does not currently have a suitable project, they should contact the instructor immediately to identify one.

## Activity: Repository Setup

Students will clone a course repository provided by the instructor and begin configuring their development environment.

This activity is intentionally less about the repository itself and more about ensuring students have access to the fundamental tools used throughout the semester:

- Git
- Conda (Conda-Forge preferred)
- A terminal or command-line environment
- Basic software installation permissions on their computer

### Repository Hosting: GitHub vs. GitLab

This course introduces students to both GitHub and GitLab. Instructors may wish to briefly discuss when each platform is appropriate.

A useful guideline is:

- If a student's project can be publicly shared, GitHub is generally recommended.
- If a student's project contains unpublished research, sensitive data, proprietary code, or anything else that should remain private, GitLab (gitlab.msu.edu) is often the better choice.

Students should understand that:

- Git is the version control system.
- GitHub and GitLab are hosting platforms built around Git.
- The skills learned on one platform transfer almost directly to the other.

The goal is not to teach a particular hosting platform. The goal is to ensure students can use Git effectively as part of a professional research workflow.

This activity serves as an early diagnostic exercise to identify configuration problems before they become barriers later in the semester.

## What to Expect

This activity often takes longer than expected.

Students arrive with a wide variety of operating systems, security policies, institutional restrictions, and levels of technical experience. There is no single set of instructions that will work for everyone.

Common issues include:

- Git not installed
- Conda not installed
- PATH configuration problems
- Terminal unfamiliarity
- Permission issues
- Existing Python installations conflicting with Conda
- Authentication issues with GitHub or GitLab
- Students being uncertain how to navigate directories using the command line

The instructor should expect to spend a significant portion of class helping students troubleshoot individual machines.

## Teaching Philosophy

A common instinct is to try to provide the "correct" installation instructions. In practice, this is rarely possible.

The real learning objective is not successfully cloning a repository. The learning objective is teaching students how to solve computing environment problems independently.

Students should be encouraged to:

- Read error messages carefully.
- Consult documentation.
- Search for solutions.
- Ask questions.
- Experiment with possible solutions.
- Help one another troubleshoot.

This is often the first research software engineering lesson of the semester: every computer is different, and learning how to debug your own environment is a critical professional skill.

One useful framing is that the semester starts by treating students as researchers rather than consumers of software. Researchers routinely encounter installation, configuration, and compatibility problems. Learning to navigate these challenges is part of becoming an effective computational researcher.

## Suggested Strategy

Consider pairing students or forming small groups during setup.

Benefits include:

- Reducing the instructor's troubleshooting load.
- Encouraging peer learning.
- Helping students recognize that configuration problems are common.
- Building a collaborative classroom culture from the first day.

Students who successfully complete a step can often help nearby students who are encountering similar issues.

## Warning Signs

Follow up with students who:

- Cannot install or run Git.
- Cannot access a command line.
- Cannot install Conda or create environments.
- Do not have a research project.
- Appear unable to make progress without step-by-step instructions.

These issues are usually easier to address in the first few weeks than later in the semester.

## End of Class Checkpoint

By the end of Day 1, students should ideally:

- Have identified a research project for the semester.
- Successfully cloned the course repository.
- Have Git functioning on their machine.
- Have Conda installed and working.
- Be able to open a terminal and execute basic commands.

Not every student will reach all of these milestones during class, and that is okay. The primary goal is to identify obstacles early and begin building the problem-solving skills they will need throughout the semester.