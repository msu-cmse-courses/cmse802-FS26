---
layout: guide
---

# Days 13-16 - Physical Modeling Repository Instructor Notes

## Overview

This repository introduces physical modeling through a series of increasingly complex examples. Most students move through the first two notebooks fairly quickly, while the third notebook is intentionally much more challenging. We schedule four class periods for the repository even though there are only three notebook sections. This gives students additional time to explore the final material without feeling rushed.

## Days 1-2: Modeling and Performance

The first two notebooks generally proceed smoothly.

Topics include:

- SIR modeling
- The wave equation
- Performance optimization

The wave equation notebook also introduces several software engineering concepts related to performance. Students start with a pure Python implementation and then progressively improve performance using:

- NumPy
- Numba/JIT compilation

One useful lesson is that performance optimization is often more complicated than expected.

For example, some students may discover that their Numba implementation is not significantly faster, or may even be slower than expected. In many cases this is because Numba was installed without parallel support or because the problem size is too small to benefit from compilation overhead.

This is completely acceptable and often leads to productive discussions about:

- Measuring performance
- Profiling code
- Computational tradeoffs
- Why optimization should be driven by evidence

The notebook naturally sets up later discussions about larger computational resources and HPC systems.

## Day 3: MFEM and HPC

Many students reach Day 3 earlier than expected.

This notebook is significantly more difficult than the previous material and often becomes the primary focus for the remainder of the repository.

Students are asked to install and run:

- MFEM
- BESFEM

The objective is not necessarily to master these libraries. Instead, the goal is to expose students to a realistic scientific software stack and the challenges involved in getting complex software running.

Students should have the remainder of the repository period to work through this process.

## Recommended HPC Introduction

I strongly recommend dedicating some class time to introducing the HPCC before students begin the MFEM exercises.

If HPC is outside the instructor's area of expertise, this may be a good opportunity to invite an ICER consultant or other campus expert for a guest presentation.

Topics I typically cover include:

1. Logging into OnDemand.
2. Using the Files menu to move files between systems.
3. Launching a development shell.
4. Running simple commands such as:
   - `git clone`
   - `ls`
   - `cd`
5. Starting interactive jobs such as:
   - JupyterLab
   - Interactive Desktop
6. Discovering and loading software using the `module` command.

The goal is not to produce expert HPCC users in a single lecture. The goal is to make the environment feel approachable enough for students to begin experimenting on their own.

## Installation Philosophy

The MFEM installation instructions are intentionally nontrivial.

Many students will spend considerable time trying to follow installation instructions and resolve dependencies.

Let them struggle with this process a bit.

Learning how to navigate installation challenges is an important research software engineering skill.

Interestingly, some observant students eventually realize that MFEM is already available on the HPCC through the module system and discover solutions such as:

```bash
module load MFEM
```

I generally do not advertise this shortcut immediately.

The students who discover it often feel a sense of accomplishment, and the students who continue with the installation process still gain valuable experience working with scientific software.

Both paths provide useful learning opportunities.

## Teaching Philosophy

The primary lesson of this repository is not the SIR model, the wave equation, Numba, or MFEM.

The broader lesson is that every computational model exists within physical constraints.

Scientists and engineers constantly make decisions about:

- Runtime
- Memory
- Storage
- Accuracy
- Resolution
- Computational resources

These engineering decisions are often just as important as the mathematics underlying the model.

Students do not need to finish every notebook. The goal is to understand the tradeoffs involved in computational modeling and gain confidence working with increasingly realistic scientific software environments.