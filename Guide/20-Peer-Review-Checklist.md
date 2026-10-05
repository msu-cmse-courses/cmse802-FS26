---
layout: guide
---

# Student Peer Review Checklist: Safe, Portable, Reproducible, Robust, and Literate (SPRRL)

## Purpose
This document provides a structured peer review process for research software projects. It is designed for course use, but it is also intended to support real handoff quality in research groups.

For live class sessions, use the companion one-page form in [Quick Peer Review Form](./21-Peer-Review-Quick-Form.md) and then expand notes in this full version if needed.

The core question is straightforward: can a future teammate get this project running, trust the workflow, understand the analysis, and continue the work without the original author in the room?

The review is organized around five quality dimensions: Safe, Portable, Reproducible, Robust, and Literate.

## Reviewer Mindset
Use this review as a professional collaboration exercise. Your role is to produce feedback that is concrete, testable, and useful to the project team. Report what you observed directly, separate facts from assumptions, and prioritize suggestions that improve runability and reproducibility. Strong reviews always include both strengths and improvements.

## Pre-Review Inputs
Before beginning, request the following from the project team: repository URL, target commit or tag, expected runtime for setup and demo, one key output to reproduce, and any data-access constraints. Always review a fixed commit or tag rather than a moving branch tip.

## Required Review Deliverables
Submit a completed checklist, a short review memo (one page maximum), and an evidence bundle containing terminal output and/or screenshots, notes on errors and recovery, and a final reproducibility status. Screen recordings are optional but strongly encouraged because they capture details that are difficult to communicate in writing.

## Step-by-Step Review Protocol

### Step 1: Pre-flight (about 5 to 10 minutes)
Start by confirming repository access and checking out the target commit/tag. Read the README fully before running commands, and identify the intended quickstart path.

Checkpoint: you can explain the intended setup path from documentation alone.

### Step 2: Setup and installation (about 10 to 20 minutes)
Begin with the project instructions, but use a clean and organized workflow. For example, it is acceptable to create a local conda environment inside the repository folder to avoid system clutter, even if the project describes an alternative setup path.

If your preferred workflow succeeds, note that as a portability/robustness strength. If it fails, revert to the project's documented setup path and record exactly where the difference mattered.

Capture what worked, what failed, what was unclear, and what required inference.

Checkpoint: install can be completed with no or only minor inference.

### Step 3: Smoke test (about 5 to 10 minutes)
Run the first validation path, such as tests, a demo script, or a notebook quick check.

Checkpoint: a basic workflow executes without editing project source code.

### Step 4: Reproduce one core result (about 15 to 30 minutes)
Follow the documented steps to reproduce one key result (figure, table, metric, or artifact). Record exact commands, runtime observations, and how closely the output matches the expected result description.

Checkpoint: at least one core project result is reproducible from project documentation.

### Step 5: Interpretability and handoff (about 10 minutes)
Evaluate whether a future teammate could interpret the output and continue the work. Confirm that assumptions, parameter choices, limitations, and next steps are clearly stated.

Checkpoint: you can explain what the output means and what the next teammate should do next.

## SPRRL Checklist (Pass / Partial / Fail)

### A. Safe
- [ ] No obvious secrets, credentials, or private keys are exposed.
- [ ] Risky operations are clearly labeled.
- [ ] Inputs and assumptions are validated or explicitly documented.
- [ ] Error behavior is understandable enough for debugging.
- [ ] Data handling is appropriate for sensitive contexts (IRB, NDA, or restricted data).
- [ ] If protected data cannot be shared, the project provides non-protected example data, synthetic data, or a mock workflow that still allows review.

Notes:

### B. Portable
- [ ] Setup instructions are complete and executable.
- [ ] Project avoids machine-specific absolute paths in core workflow.
- [ ] Dependency requirements are discoverable.
- [ ] A clean environment on another student machine can run the workflow with reasonable effort.
- [ ] Minor setup variations (for example local in-repo conda environment) are tolerated or can be recovered cleanly.

Notes:

### C. Reproducible
- [ ] README provides a clear path from clone to result.
- [ ] Commands are complete, ordered, and realistic.
- [ ] Parameters, seeds, and key configuration choices are recorded.
- [ ] One key result can be reproduced within expected tolerance.

Notes:

### D. Robust
- [ ] Tests exist for at least some core functionality.
- [ ] Test outcomes are clear and interpretable.
- [ ] Workflow fails gracefully when expected inputs are missing.
- [ ] Repository structure supports maintenance (modular code, not only ad hoc notebook cells).
- [ ] Recovery guidance exists for common failures.

Notes:

### E. Literate
- [ ] README explains project purpose and research context.
- [ ] Setup and run instructions are understandable to a course peer.
- [ ] Outputs are labeled and interpretable by a future teammate.
- [ ] Known limitations and next steps are documented.
- [ ] The project is documented so another student in the same lab could continue work with minimal verbal handoff.

Notes:

## Reproducibility Outcome Summary
Select one outcome and justify it briefly.

- [ ] PASS: a key result was reproduced exactly or within documented tolerance.
- [ ] PARTIAL: most of the workflow ran, but a key step was blocked or ambiguous.
- [ ] FAIL: workflow did not run far enough to evaluate a key result.

Blocking step (if PARTIAL or FAIL):

## High-Value Feedback Template
Provide three strengths and three ranked improvements.

### Strengths
1.
2.
3.

### Ranked Improvements
1. Most important fix:
2. Next fix:
3. Nice-to-have fix:

For each improvement, include observed issue, impact on usability/reproducibility, and a concrete fix recommendation.

## Reviewer Time Log
Record your approximate review time for calibration and process improvement.

- Pre-flight:
- Setup/install:
- Smoke test:
- Core result reproduction:
- Interpretability/handoff:
- Total:

## In-Class Two-Pass Peer Review Format (Recommended)
This format works well when the class can review live with immediate clarification.

In pass 1, Student A reviews Student B while Student B is present for questions. In pass 2, roles swap so Student B reviews Student A using the same protocol. This two-pass format is slower than asynchronous review, but it often produces higher-value feedback and faster correction cycles.

Suggested timing for one pair:
- 5 minutes: setup and handoff
- 20 to 25 minutes: pass 1 review
- 20 to 25 minutes: pass 2 review
- 5 to 10 minutes: mutual action items

If class size is odd, use one of the following structures:
- Form one triad and rotate reviewer roles.
- Pair one student with instructor/TA for one pass and with a peer for the second pass.
- Run one asynchronous second pass for the unpaired student.

## Optional Lightweight Scoring Rubric
If your instructor uses numeric scoring, apply this mapping: Pass = 2, Partial = 1, Fail = 0.

Category maximums:
- Safe: 12
- Portable: 10
- Reproducible: 8
- Robust: 10
- Literate: 10

Total maximum: 50

Suggested interpretation:
- 42 to 50: handoff-ready with minor refinements
- 34 to 41: usable with targeted fixes
- 24 to 33: substantial reproducibility gaps
- 0 to 23: not yet transferable

## Ethics and Professionalism
Treat all project materials as course-private unless explicit permission is granted. Do not redistribute peer code, logs, or recordings outside approved channels. Keep feedback focused on software and documentation quality rather than personal style.

## One-Sentence Goal
After this review, the project team should know exactly how to make their software easier for a future teammate to run, interpret, and extend.
