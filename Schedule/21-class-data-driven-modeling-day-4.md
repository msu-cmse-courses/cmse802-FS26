---
layout: schedule
published: false
date: '2026-11-12'
---



# Data Driven Modeling - Day 4

Repository: <https://github.com/colbrydi/data_driven_modeling>

## Agenda (80 minutes)

1. 10 min - Check-in and confirm HPCC access
2. 15 min - Discuss search-seed variability, the resource contract, and selection versus final evaluation
3. 30 min - Guided work in `Assignment_Instructions_Part_4.ipynb`
4. 25 min - Write your data-driven modeling reflection for your project and share it with a partner

### Learning Goals

By the end of this class, you should be able to:

- Run a bounded TPOT search as a Slurm job array and keep a record of each run.
- Select a candidate from training-only results and evaluate it once on the held-out test set.
- Describe how data-driven components could, or could not, contribute to your own project.

## In-Class Focus

Repeating an AutoML search does not make its recommendation automatically trustworthy. Today we ask how sensitive a search is to its random seed by running the same problem several times on the HPCC, comparing the recommendations, and separating the choice of a candidate from its final evaluation.

Use the repository as the primary working reference:

- Repository: <https://github.com/colbrydi/data_driven_modeling>
- Notebook: `Assignment_Instructions_Part_4.ipynb`

Submit the array early because jobs may wait in the queue; use that time to review the resource settings and software versions you will need to document. As you work, consider what varied across tasks, what stayed fixed, and whether the top candidate is clearly better or just search noise.

## Data-Driven Modeling Reflection

This class closes the data-driven modeling unit. In your project repository, add a short dated entry to `paper/reflections.md`, alongside the entries from the earlier modeling modules. Address all three prompts:

1. Which data-driven component from this unit (summary statistics, classical machine learning, or AutoML) could contribute to your project, and what question would it answer that your analytical or physical components cannot? If none is appropriate, explain why.
2. Do you have enough data to trust it? Describe your observations and features, how you would split the data to avoid leakage, and what baseline a model would have to beat.
3. What evidence would you need before trusting its output, and what would a teammate need to repeat it? Which of Safe, Portable, Reproducible, Robust, or Literate would be hardest to achieve, and what concrete step would you take?

Keep each answer short and specific to your project. Share your entry with a partner and note one question they asked that you could not yet answer.

## Before Next Class

- Finish the array summary, the candidate selection, and the single final held-out evaluation.
- Add the evidence listed in the notebook (Slurm script, per-seed `run.json` records, summary, and its reflection) to your project repository.
- Commit and push your `paper/reflections.md` entry with your current project work.
- Milestone 5 (Project Systems and Automation) is due this weekend; connect today's reproducible workflow to your own project's command interface.

## Daily Check-in and Reflection

[Daily Check-in Form](https://forms.cloud.microsoft/r/QkH6Mx8FUd)