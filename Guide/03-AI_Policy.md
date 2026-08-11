---
layout: guide
---

# Artificial Intelligence Policy

Artificial intelligence is an increasingly important part of modern research and software development.

In this course, we will discuss many forms of AI, including machine learning, data-driven modeling, and generative AI systems such as GitHub Copilot, ChatGPT, Claude, Gemini, and similar large language models (LLMs).

These technologies are powerful tools, but they should not be confused with expertise.

The goal of this course is not to avoid AI. The goal is to learn how to use AI responsibly while remaining the scientist, engineer, and researcher in the loop.

## Trust But Verify

One of the most important ideas in this course is:

> Do not use AI if you do not know what the output should look like.

AI is often most useful when it helps you work faster in an area where you already have some understanding.

Examples include:

- explaining unfamiliar code
- improving documentation
- suggesting software designs
- generating test cases
- brainstorming approaches
- helping debug errors

Treat AI output as a draft, a suggestion, or a hypothesis. Review it, test it, question it, and make sure you can explain it yourself.

If you cannot explain a result, you should not submit it.

## Keep It Simple

One common difficulty with AI-assisted software development is the production of unnecessary complexity.

Over the past few years I have seen many examples of AI-generated code that technically works but is far more complicated than the problem requires. This often results in:

- duplicated code
- unused functions
- unnecessary abstractions
- unused dependencies
- features that were never requested

In software engineering this is sometimes called "slop"—extra code that adds complexity without adding value.

Throughout this course, remember the principle:

    Keep It Simple, Silly (KISS)

Simple code is often:

- easier to understand
- easier to test
- easier to debug
- easier to document
- easier to maintain

When using AI tools, do not assume that longer solutions are better solutions.

If an AI generates fifty lines of code for a problem that should require five, consider simplifying the design before accepting the result.

One of the goals of this course is to learn how to recognize unnecessary complexity and how to build software that remains understandable to future users, collaborators, and your future self.

## Hidden Risks

Generative AI systems inherit many of the strengths, weaknesses, and biases found in human-generated data.

One of the biggest risks is overconfidence.

Students, researchers, and AI systems can all become more confident than they should be, especially when working in a new area. Beginners often overestimate their understanding because they do not yet know what they do not know, a phenomenon commonly associated with the Dunning-Kruger effect.

Generative AI can amplify this problem by producing answers that sound authoritative regardless of their accuracy. Convincing answers are not necessarily correct answers.

This is why skepticism, validation, testing, and peer review remain essential.

When possible:

- discuss ideas with classmates
- compare multiple sources
- test assumptions
- look for evidence that might prove you wrong

Good science often begins by questioning answers that appear obvious.

## AI and Scientific Software Engineering

Throughout this course we will evaluate software using five principles:

- Safe
- Portable
- Reproducible
- Robust
- Literate

AI should support these goals rather than undermine them.

A useful question to ask is:

> Does this AI-generated output improve the quality of the software?

If the answer is unclear, additional validation is probably needed.

## AI-Enabled Repository Templates

Many of the repositories used in this course include an experimental AI support framework.

The primary template can be found here:

https://github.com/colbrydi/Research_Software_Project_Template

The template includes guidance files that provide context to both humans and AI systems.

These files describe:

- project philosophy
- software engineering practices
- repository conventions
- documentation expectations

Some AI tools automatically read this information when generating code or documentation.

## A Course Experiment

One of the questions we are exploring in CMSE 802 is:

> Can repository-level guidance help students use AI tools more effectively?

Rather than repeatedly explaining project expectations to an AI assistant, we place that information directly into the repository.

In this sense, the repository itself becomes part of the prompt.

The goal is not to control AI behavior. The goal is to provide context that encourages both students and AI systems to follow the same software engineering practices.

Students are encouraged to explore these files and observe how additional context influences AI-generated responses.

## Student Responsibility

The use of AI tools is permitted unless a specific activity states otherwise.

However, you remain responsible for all submitted work.

You should be able to:

- explain your code
- explain your design decisions
- explain your results
- justify why you trust a particular solution

AI can assist your work. Responsibility for that work remains yours.