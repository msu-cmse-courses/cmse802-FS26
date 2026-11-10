---
layout: schedule
published: true
date: '2026-12-01'
---


# LangChain and LangGraph - Day 2

Repository: <https://github.com/maryambrj/langchain-langgraph-tutorials>

Today we complete the [LangChain + LangGraph tutorial](https://github.com/maryambrj/langchain-langgraph-tutorials) and evaluate what makes an LLM workflow useful, reviewable, and appropriate for research support. The TA will guide the advanced examples and help distinguish a compelling demonstration from evidence that a workflow is reliable.

## Agenda (80 minutes)

1. 10 min - Check-in and recap: model behavior, chains, and routing
2. 20 min - Guided work: tools and reflection/revision workflows
3. 20 min - Guided work: retrieval-augmented generation and source-aware answers
4. 15 min - Guided work: human-in-the-loop interruption and approval
5. 5 min - Complete graph visualization and remaining tutorial examples
6. 10 min - Workflow reflection and project connection

## Learning Goals

By the end of this class, you should be able to:

- explain how tools, retrieval, reflection, and human approval change an LLM workflow; and
- identify the evidence, validation, and documentation needed before adapting an LLM workflow for research.

## In-Class Focus

Continue in the same Google Colab copy and complete the remaining tutorial sections:

- Tool use with weather and Wikipedia examples
- Reflection and revision
- Retrieval-augmented generation (RAG)
- Human-in-the-loop control
- Graph visualization

As you work, separate model-generated text from retrieved context and tool output. A tool call or retrieved document can provide useful information, but it does not automatically establish that an answer is correct, complete, or appropriate for a research claim.

Do not enter API keys, restricted research data, participant information, or other sensitive material into the notebook. If an external service, package, or model does not behave as expected, record what happened and use that observation in the reflection rather than silently skipping it.

## Workflow Reflection

In your project repository, add a short dated entry to your reflection notes. Address all three prompts:

1. Which tutorial component would be most useful for working with unstructured information in your research, and what would it not be reliable enough to decide?
2. What evidence, test, source check, or human approval step would you require before using its output?
3. Which of Safe, Portable, Reproducible, Robust, or Literate would be hardest to achieve in a workflow you might adapt, and what concrete improvement would you make?

## Before Next Class

- Finish any remaining tutorial cells and preserve your Colab copy or an exported notebook.
- Commit and push the reflection entry with your current project work.
- Bring your project in a reviewable state for the final code-review day.

## Daily Check-in and Reflection

[Daily Check-in Form](https://forms.cloud.microsoft/r/QkH6Mx8FUd)