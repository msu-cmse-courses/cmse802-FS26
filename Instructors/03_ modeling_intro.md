---
layout: guide
---

# Day 3 Start Modeling Intro

## Goals for the Day

Day 3 begins the first major in-class coding exercise. Students start with working code in a Jupyter notebook and gradually transform it into reusable software.

Key messages:

- Working code is often just the beginning.
- Software can be improved through organization, reuse, and documentation.
- Students are expected to make progress, ask questions, and learn.
- Grades are based on engagement with the notebooks, not on finishing them.

## Activity: Multi-Day Git Repository Exercise

Students work through a Git repository designed to span approximately four class periods.

The exercise introduces:

- Functions
- Code reuse
- Software organization
- Packaging
- Version control
- Development workflows

The first notebook asks students to convert code that generates a figure into reusable functions. For some students, this may be their first time writing functions. Meet students where they are and focus on helping them make steady progress.

## Pair Programming and Collaboration

Students should work in pairs whenever possible.

Encourage students who move quickly to:

- Continue to later notebooks.
- Help their partner.
- Assist nearby groups.

The class is intentionally designed so students can move at different speeds.

## What to Expect

Many of the same setup issues from Day 1 will reappear:

- Missing Conda installations
- Missing Git installations
- Command-line unfamiliarity
- PATH configuration issues
- Environment conflicts
- Operating-system-specific problems

Every student's computer is different. There is no single installation procedure that works for everyone.

Instructors should spend much of the class circulating, troubleshooting, and helping students learn how to debug their own systems.

One setup approach that often works well is:

1. Install Conda from Conda-Forge.
2. Install Git using:

   ```bash
   conda install git
   ```

3. Use a Conda terminal for all development work.

However, this should be presented as a useful starting point rather than the only correct solution.

## A Common Challenge: Mapping Weights to a Triangle

One of the more difficult parts of the notebook involves converting three weights and three triangle corner points into a Cartesian coordinate within the triangle.

Most students will not reach this section on the first day, but some will.

The mathematics is straightforward once understood, but many students find it challenging because they are simultaneously learning programming, debugging, and software organization.

A useful lesson is that students do not need to memorize every mathematical technique. Instead, they need to learn how to identify what they know, what they need, and how to find the missing information.

One useful approach is to ask an LLM:

> I have three corner points of a triangle in Cartesian coordinates and three weights. How do I calculate the Cartesian coordinates of the point represented by those weights?

The resulting solution is surprisingly simple. The important skill is not knowing the formula from memory. The important skill is knowing how to find, evaluate, and apply the solution.

## Optional Live Demonstration

If the instructor is comfortable doing so, consider spending 5-10 minutes demonstrating the entire assignment from start to finish.

The goal is not to produce the perfect solution. In fact, it can be beneficial if mistakes occur.

Students rarely get to watch an experienced developer solve a new problem in real time. During the demonstration, consider:

- Thinking out loud.
- Looking up documentation.
- Using Google.
- Using an LLM.
- Testing ideas.
- Making mistakes.
- Recovering from mistakes.

This models authentic software development and helps students understand that successful programmers spend much of their time learning, debugging, and refining solutions rather than simply typing correct code.

## Teaching Philosophy

This exercise is intentionally designed to meet students where they are.

Students will arrive with very different levels of programming experience. Focus on progress rather than completion.

Encourage:

- Learning by doing.
- Experimentation.
- Problem solving.
- Peer learning.
- Asking questions.

The project notebooks create a low-risk environment where students can develop confidence while gradually adopting research software engineering practices.

## Warning Signs

Follow up with students who:

- Cannot navigate the command line.
- Cannot activate environments or run basic commands.
- Remain stuck on setup issues.
- Wait passively for answers instead of trying solutions.
- Become isolated from their partner.
- Worry that they are "behind" because they have not finished the notebook.

## End of Class Checkpoint

By the end of Day 3, students should ideally:

- Have downloaded and opened the exercise repository.
- Be working in a functional development environment.
- Understand the purpose of functions and code reuse.
- Have started modifying notebook code.
- Be collaborating with classmates and asking questions when needed.

Students do not need to finish the notebook. The most important outcome is that they begin viewing software as something they can actively modify, improve, debug, and learn from.