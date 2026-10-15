# Day 6 Instructor Notes

## Goals for the Day

Day 6 concludes the introductory modeling repository and provides students with their first experience sharing software with other users.

At this point, students should have:

- Created reusable functions.
- Moved those functions into a Python file.
- Added basic documentation.
- Developed a simple API for creating ternary plots using barycentric coordinates.

The primary goal for this class is to test whether their software can actually be used by someone else.

Key message:

> Software is not truly reusable until another person successfully uses it.

## Activity: Repository Exchange

Students exchange repositories and attempt to use another student's software on their own computer.

This can be done by:

- Sharing repository URLs.
- Cloning a partner's repository.
- Following the provided instructions.
- Running the code.
- Generating figures.

Students should be encouraged to avoid explaining their code immediately.

Instead, ask their partner to use the repository as if they were a new lab member discovering it for the first time.

## Learning Objectives

Students should begin to realize that good software is more than code.

Success depends on:

- Clear organization.
- Meaningful function names.
- Documentation.
- Reasonable defaults.
- Reproducible setup instructions.

Many students believe their software is easy to use because they understand it. This exercise helps them discover what assumptions they may have made without realizing it.

## What to Expect

This exercise usually works better than students expect.

Most repositories will successfully run on another machine, but the process often reveals many small issues.

Common discoveries include:

- Missing instructions.
- Hard-coded paths.
- Unclear function names.
- Ambiguous argument requirements.
- Assumptions about installed packages.
- Missing documentation.
- Environment differences.

These are exactly the kinds of issues this activity is designed to reveal.

## Discussion Topics

After students have tried each other's repositories, consider discussing questions such as:

- What was easy to understand?
- What was confusing?
- What documentation helped the most?
- What assumptions did the original developer make?
- What would make the software easier to use?

Students often discover that different groups made different design decisions even though they were solving the same problem.

This frequently leads to productive conversations about software design and tradeoffs.

## Teaching Philosophy

The purpose of this exercise is not to determine whose solution is "best."

The purpose is to demonstrate that software development involves communication.

Students naturally make design decisions based on their own understanding of a problem. Seeing alternative solutions helps them recognize that there are often multiple reasonable approaches.

This is also one of the first opportunities for students to receive feedback from an actual user.

The goal is to help students transition from thinking:

> "Does my code work?"

to

> "Can someone else use my code?"

That shift is an important step toward becoming a research software engineer.

## Possible Mini Lecture: The Real User Test

Many students assume software is finished once it runs correctly on their machine.

This activity provides an opportunity to discuss why testing with real users is important.

A useful question is:

> Could a new graduate student joining your lab next semester successfully use your repository without your help?

If not, what would need to change?

This conversation naturally motivates future topics such as:

- Documentation
- Packaging
- Testing
- Reproducibility
- Continuous integration

## Warning Signs

Follow up with students whose repositories:

- Only run on their own computer.
- Require extensive verbal explanation.
- Contain hard-coded paths or assumptions.
- Lack documentation.
- Are difficult for another student to understand.

These are common issues and should be viewed as learning opportunities rather than failures.



## Repository Reflection Assignment

At the conclusion of each repository exercise, students should write a short reflection (typically one or two paragraphs) describing how the topics explored in the repository relate to their own research.

Students should place these reflections in the `paper/` directory of their semester project repository.

These reflections are not intended to be formal papers. Instead, they serve as a running record of how course concepts connect to the student's research interests and software development practices.

At the end of the semester, students will use these notes to help write a final reflection describing what they learned and how they applied course concepts to their work.

## Reflection Goals

Students often focus on completing notebook exercises without taking time to consider why the material matters.

The reflection assignment encourages students to step back and answer questions such as:

- How does this topic connect to my research?
- How might I use these ideas in my current project?
- What software engineering practices could improve my work?
- What new questions did this repository raise?

The emphasis is on thoughtful reflection rather than technical correctness.

## Teaching Philosophy

Students will sometimes claim that a repository is unrelated to their research.

Rather than accepting this immediately, encourage them to think more broadly.

For example, a student may say:

> My research does not use analytical modeling.

A useful follow-up question is:

> Where might analytical modeling appear in your field, even if it is not part of your current project?

The goal is not to force an artificial connection. The goal is to encourage students to explore how computational methods, software engineering practices, and modeling techniques might apply within their discipline.

Often the most valuable reflections come from students who initially believed there was no connection.

Encourage students to push themselves slightly beyond their immediate project and think about how the ideas could be applied to their research area, future work, collaborators, or broader scientific community.

## Grading Note

In-class repositories are not graded based on completion, sophistication, or correctness.

Students enter the course with very different backgrounds and progress at different rates.

Instead, grading is primarily based on participation, engagement, and daily check-ins.

The reflection provides evidence that the student has considered the material and can connect course concepts to their own research and professional development.

The objective is growth, not competition.

## End of Class Checkpoint

By the end of Day 6, students should ideally:

- Have successfully shared their repository with another student.
- Have attempted to use software written by someone else.
- Have identified strengths and weaknesses in their own design.
- Better understand the importance of documentation and reproducibility.
- Realize that software development is fundamentally a communication exercise as much as a technical one.

The most important outcome is that students experience what it feels like to be both the developer and the user of research software. This perspective helps motivate many of the software engineering practices that will be introduced throughout the remainder of the course.