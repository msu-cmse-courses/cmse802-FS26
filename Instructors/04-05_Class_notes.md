# Days 4-5 Instructor Notes

## Goals for the Day

Days 4 and 5 focus on moving code from a notebook into a reusable Python module. This is often the first time students have experienced the difference between writing code for themselves and writing code that can be reused by others.

Key messages:

- Functions are more useful when they live outside the notebook.
- Notebooks should focus on analysis, visualization, and experimentation.
- Reusable code should be placed in Python files.
- Good software is easier to understand, maintain, and reuse.

## Activity: Moving Functions into a Python File

Students should migrate the functions they developed earlier into a Python file located in the same directory as their notebook.

This is intentionally the simplest possible example of a software package or API.

The goal is for students to separate:

- Code that performs work (Python file)
- Code that uses the functionality (Notebook)

By the end of the exercise, the notebook should primarily:

1. Import the functions.
2. Provide inputs.
3. Generate and display results.

This helps students see how software can be organized into reusable components.

## Interface Design

Once the functions have been moved into a Python file, encourage students to improve the usability of their code.

Topics worth discussing include:

- Function names
- Input arguments
- Default values
- Return values
- Error messages
- Readability

Students should begin thinking about what makes a function easy for another researcher to use.

A useful question is:

> If a new student joined your lab next week, could they figure out how to use this function?

## Jupyter Development Challenges

Moving code into a Python file often reveals one of the frustrations of notebook development.

Students may update a Python file but find that the notebook continues using the old version.

This provides a good opportunity to discuss:

- Importing modules
- Kernel state
- Restarting the kernel
- Reloading code during development

Many students will need to either:

- Restart the kernel after making changes, or
- Use notebook tools that automatically reload imported modules

This is a common source of confusion, so expect questions.

## Documentation and Docstrings

As students move code into a Python file, introduce the idea that code should explain itself.

Topics to discuss:

- Function documentation
- Docstrings
- Input descriptions
- Return value descriptions
- Usage examples

Students often assume documentation is something added at the end of a project. Encourage them to treat documentation as part of the development process.

Even a simple docstring can dramatically improve usability.

## Optional Live Demonstration

If you are comfortable doing so, spend 5-10 minutes demonstrating the migration process yourself.

Consider showing:

- Copying a function from a notebook into a Python file.
- Importing the function back into the notebook.
- Adding a docstring.
- Improving function arguments.
- Fixing mistakes as they occur.

As with Day 3, the value comes from students seeing an experienced developer think through a problem in real time.

Use documentation, search engines, LLMs, or trial-and-error when appropriate. The goal is to model an authentic software development workflow rather than present a polished solution.

## Teaching Philosophy

Many students arrive believing software development is about writing code.

These lessons begin to demonstrate that software development is really about organization, maintainability, communication, and reuse.

The objective is not to create a perfect package. The objective is to help students develop habits they can apply to their own research software throughout the semester.

Encourage:

- Iterative improvement.
- Experimentation.
- Refactoring.
- Documentation.
- Peer learning.

## Day 5 Extension: Using Someone Else's Code

If time permits near the end of Day 5, consider having students share their Python files with another group.

Ask students to:

- Exchange code.
- Read another group's docstrings.
- Import and use another group's functions.
- Provide feedback on usability.

This frequently leads to valuable discussions.

Students quickly discover that code which seems obvious to the author can be confusing to everyone else.

The exercise reinforces why:

- Clear interfaces matter.
- Good names matter.
- Documentation matters.
- Testing with real users matters.

## Warning Signs

Follow up with students who:

- Keep all functionality inside the notebook.
- Struggle to distinguish between reusable code and analysis code.
- Do not document their functions.
- Become frustrated by module reloading and kernel issues.
- Have difficulty explaining how someone else would use their code.

## End of Class Checkpoint

By the end of Day 5, students should ideally:

- Have moved one or more functions into a Python file.
- Be importing those functions into a notebook.
- Understand the benefits of separating code from analysis.
- Have written basic docstrings.
- Have improved the usability of their functions.
- Have seen examples of how other students approached the same problem.

The most important outcome is that students begin viewing software as something that can be reused and shared. This shift from notebook scripting toward reusable software is one of the foundational ideas that the remainder of the course will continue to build upon.