## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Simulation End States
**Learning:** Abruptly closing a visual simulation upon completion (or failure, like extinction) removes important context and prevents users from reviewing the final state of the environment.
**Action:** Always provide a static "End State" overlay (e.g., pausing the simulation and showing an "EXTINCTION" message) rather than abruptly terminating the program. Allow the user to explicitly dismiss or quit the application (e.g., via the ESC key).
