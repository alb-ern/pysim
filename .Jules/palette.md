## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Graceful Simulation End-States & Dynamic Action Labels
**Learning:** Abruptly closing the simulation on extinction removes the final visual context for the user, and static toggle labels (like always showing "(SPACE to Pause)") cause cognitive friction when the user is already paused or in an end state.
**Action:** For end-states, use persistent overlay states that require manual acknowledgment (e.g., "ESC to Exit") rather than force-quitting. Additionally, dynamically update toggle labels to reflect the *next available action* (e.g., "(SPACE to Resume)" when paused) to improve clarity.
