---
layout: schedule
published: true
date: '2026-11-10'
---



# Data Driven Modeling - Day 3

Repository: <https://github.com/colbrydi/data_driven_modeling>

## Agenda (80 minutes)

1. 10 min - Check-in and share your dataset descriptions
2. 20 min - Introduce AutoML, TPOT, and combined algorithm selection and hyperparameter optimization (CASH)
3. 35 min - Guided work in `Assignment_Instructions_Part_3.ipynb`
4. 15 min - Discuss what makes an AutoML recommendation trustworthy

### Learning Goals

By the end of this class, you should be able to:

- Run a bounded AutoML search without leaking the final test data into its decisions.
- Explain why a high AutoML score does not settle a scientific question.

## In-Class Focus

Part 2 had you make model choices by hand. Today a tool makes them for you. We run a deliberately small TPOT search, compare its recommendation with the Part 2 baseline, and inspect the pipeline it chose before deciding whether to trust it. This is the main software activity of the unit.

Use the repository as the primary working reference:

- Repository: <https://github.com/colbrydi/data_driven_modeling>
- Notebook: `Assignment_Instructions_Part_3.ipynb`

As you work, consider which choices TPOT made, which choices it could not responsibly make for you, and how cross-validation evidence differs from held-out test evidence.

## Before Next Class

- Finish any remaining work in `Assignment_Instructions_Part_3.ipynb`, including the planning exercise for your own data.
- Confirm that you can log in to the HPCC and have the partition and Conda instructions from the instructor. Part 4 assumes the Part 3 workflow already runs for you.
- Preview `Assignment_Instructions_Part_4.ipynb`.

## Daily Check-in and Reflection

[Daily Check-in Form](https://forms.cloud.microsoft/r/QkH6Mx8FUd)