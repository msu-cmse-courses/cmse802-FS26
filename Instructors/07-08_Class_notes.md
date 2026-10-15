---
layout: guide
---

# Days 7-8 Start Analytical Modeling

## Goals for the Day

Days 7 and 8 continue the Analytical Modeling repository.

Students typically work through:

- Part 1: Symbolic Python
- Part 2: Synthetic Data Generation

Most students find these notebooks substantially easier than the previous repository. As a result, many students progress more quickly and may already be starting Part 3 by the end of Day 8.

This is generally desirable. Part 4 introduces StackGP and is intentionally much more open-ended. Additional time spent exploring Part 4 often leads to richer discussions and experimentation.

## Learning Objectives

Students should begin to understand:

- The difference between analytical and data-driven approaches.
- How symbolic mathematics can be used to represent and manipulate models.
- How synthetic data can be generated from known relationships.
- The strengths and limitations of modeling using generated data.

The technical details are important, but the larger goal is helping students understand how different modeling techniques relate to one another.

## Teaching Philosophy

Encourage students to move forward when they are ready.

The goal is not for the entire class to be on exactly the same notebook page at the same time. Students learn at different rates and arrive with different backgrounds.

Students who finish early can:

- Continue to later notebooks.
- Help nearby students.
- Experiment beyond the notebook requirements.
- Explore alternative modeling approaches.

The open-ended nature of the later exercises is intentional.

## What to Expect

Compared to the first repository:

- Fewer installation issues.
- More conceptual questions.
- More discussions about modeling.
- More opportunities for experimentation.

Students may become less concerned with software mechanics and more interested in the meaning of the models they are creating.

This is a good sign.

## Possible Mini Lecture: Symbolic Modeling

A useful discussion topic is the distinction between:

- Analytical models
- Physical models
- Data models

Ask students:

> What information do we know before collecting data?

and

> What information can only be learned from data?

Symbolic Python provides a useful bridge between mathematical models and software implementation.

## Possible Mini Lecture: Makefiles

Many students have never encountered Makefiles.

A short demonstration can introduce:

- Automating repetitive commands.
- Capturing project workflows.
- Reproducibility.
- Reducing mistakes.

The goal is not to teach advanced Makefile development. The goal is to show students how simple automation can save time and improve consistency.

## Possible Mini Lecture: Dirk's Three Steps of Debugging

This framework frequently helps students who feel overwhelmed when debugging.

### Step 1: Where is the bug?

Identify the specific location where something is failing.

Students often skip this step and immediately start changing code.

Instead:

- Narrow the problem.
- Determine which function is failing.
- Determine which line is failing.
- Determine which input triggers the failure.

### Step 2: What is causing the bug?

Once the bug has been isolated, determine why it occurs.

Useful tools include:

- Error messages
- Print statements
- Small test cases
- Reading documentation
- Searching online resources
- Using an LLM

Many error messages directly suggest likely causes.

However, students should also understand that error messages can occasionally be misleading. They are clues, not proof.

### Step 3: Fix the bug

Only after understanding both the location and cause of the problem should students begin modifying code.

Many new programmers spend most of their time at Step 3 and very little time at Steps 1 and 2.

The purpose of this framework is to encourage disciplined debugging.

## Example Debugging Story

One example frequently encountered in class involves code that appears to hang or stall.

Students often assume a specific function is broken.

Instead, demonstrate how to:

- Break large functions into smaller parts.
- Run pieces independently.
- Add diagnostic print statements.
- Use `flush=True` when needed.
- Determine exactly where execution stops.

In one recent example, the root cause was ultimately an environment issue rather than a coding mistake.

The important lesson was not the specific solution. The important lesson was learning how to systematically isolate the source of the problem.

## Guidance for Future Instructors

The mini lectures are not intended to be formal lectures.

Most emerged naturally from helping students solve real problems.

When possible:

- Demonstrate your thinking process.
- Debug in front of students.
- Admit uncertainty.
- Look things up.
- Test ideas.
- Make mistakes and recover from them.

Students rarely get to observe how experienced researchers actually solve problems. Seeing that process is often more valuable than seeing a polished solution.

The objective is not to demonstrate expertise.

The objective is to model effective habits.

## End of Class Checkpoint

By the end of Day 8, students should ideally:

- Understand the purpose of symbolic modeling.
- Have generated and analyzed synthetic data.
- Be making progress toward Part 3.
- Be increasingly comfortable debugging independently.
- Be learning how to use software tools to explore models rather than simply execute code.

If students are moving into Part 3 or beyond, they are generally on pace for the remainder of the repository.