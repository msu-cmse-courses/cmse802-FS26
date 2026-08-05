# Copilot Instructions for CMSE 802 (FS26)

## Purpose
Use this repository to run and improve a cohesive graduate course on research software engineering for mixed-background students. Prioritize decisions that keep the learning goals clear, the weekly workflow manageable, and the course arc coherent across instructors and semesters.

## Always Start Here (Required Context)
Before proposing major edits, read these files to restore project context:
- scratch/CMSE802_Course_Vision_and_Implementation_Plan.md
- scratch/Student_Peer_Review_Checklist_SPRRL.md
- scratch/Student_Peer_Review_Quick_Form_SPRRL.md
- README.md
- schedule.md
- course_schedule/Calendar_Logistics.md

If the task is about schedule content or dates, also read:
- config/topics_per_day.yml
- config/fall_calendar.yml
- scripts/update_schedule.py

## Core Course Identity
Preserve and reinforce this software quality mantra across all student-facing materials:
- Safe
- Portable
- Reproducible
- Robust
- Literate

Any new assignment, rubric, checklist, or policy should map visibly to one or more of these dimensions.

## Teaching and Product Goals
Prioritize:
1. Reuse and adapt strong existing materials before creating new content.
2. Keep weekly deliverables clear, low-friction, and directly tied to course learning goals.
3. Evidence-based AI use: students must test and validate AI-generated code.
4. Reproducibility and handoff readiness for future teammates.
5. Sustainable instructor workload and low student overwhelm.

## User Style Preferences
Follow these writing and structure preferences for generated course documents:
- Use professional prose as the default style.
- Use bullet points as supporting structure, not the dominant format.
- Keep student-facing documents consistent in tone and template.
- Prefer concise, operational language over abstract or verbose framing.
- Include practical implementation details (timing, evidence, workflow steps).

For student-facing class-day schedule pages and course descriptions:
- Keep pages short, simple, and reference-like rather than essay-like.
- Prefer a consistent structure: H1 title, timed agenda, 1 to 2 learning goals, short section blocks, and a brief "Before Next Class" list when needed.
- Keep daily learning goals minimal. Do not expand them into long competency lists unless the user explicitly asks.
- Focus on what students will do, discuss, or prepare, not on internal course design rationale.
- Match the tone and formatting of nearby day pages unless the user asks for a new pattern.
- Leave room for instructor flexibility when a class may pivot based on student projects, background, or shared tool needs.

## Curriculum Guardrails
Keep scope controlled. Avoid overbuilding.

Default planning constraints:
- Approximately 13 instructional weeks in a 26-meeting semester.
- About 5 core projects, with optional tracks for advanced topics.
- Maximum of one in-class software project per week.
- Major projects often span two weeks.
- Keep grading artifacts short and sustainable.
- Prefer cohesive progression over adding isolated "interesting" activities.

## Cohesion and Thread Preservation
Treat the course as a connected system, not a set of independent assignments.

Each assignment usually serves multiple goals at once, often across these threads:
- modeling fluency (physical, analytical, data-driven)
- software engineering practices (testing, modularity, version control, documentation)
- responsible AI workflow (generation, validation, trust calibration)
- reproducibility and handoff quality

When proposing changes, do not optimize for only one thread. Explicitly document how a change affects at least two to three threads and whether it weakens the semester narrative.

For any significant assignment revision, include a short "design intent" note:
- primary learning goal(s)
- secondary hidden/support goals
- prerequisites it assumes
- downstream assignments it prepares students for
- what breaks if this piece is removed or heavily changed

## Future Instructor Handoff
Write and revise materials so a future instructor can understand why each component exists, not just what students do.

Default expectation:
- preserve rationale next to assignment specs
- explain tradeoffs and alternatives briefly
- call out dependencies between activities
- avoid creating a patchwork of disconnected artifacts

Historical caution:
- The archive in scratch/archive_daily includes examples of materials that look strong in isolation but are difficult to run as one cohesive course.
- Use archive material selectively and always re-anchor it to the current thread structure.

## Assignment and Review Design Defaults
When drafting or revising assignments:
- Separate required vs optional work clearly.
- Include explicit submission evidence expectations.
- Require tests and reproducibility notes at baseline.
- Keep reflection prompts short and cumulative.

When drafting or revising code review materials:
- Prefer a scalable three-layer model:
  - peer reproducibility review
  - self screen-recorded run-through
  - limited instructor deep dives
- Include protected-data pathways (synthetic/example/mock workflows).
- Support in-class two-pass review logistics.

## Repository-Specific Operational Notes
- The schedule system is configuration-driven.
- Prefer editing schedule source files rather than hand-editing generated outputs.
- Preserve local-safe build workflow and explicit publish boundaries.
- The Research_Software_Project_Template directory is a separate repository reference; do not assume it should be committed into this repo.

## Copilot Behavior Expectations
When assisting in this repository:
1. Anchor recommendations to the implementation plan and existing course architecture.
2. Explain tradeoffs briefly and choose the lowest-friction viable path.
3. Prefer edits that preserve cross-week cohesion over isolated optimization.
4. Flag when a request increases instructor/student cognitive load or breaks thread continuity.
5. When useful, propose companion artifacts that preserve design intent for future instructors.

## Definition Check for Environment Strategy
Maintain this distinction in student-facing guidance:
- Reproducible environment: exact pins for verification consistency.
- Robust environment: compatibility-oriented constraints for broader install success.
