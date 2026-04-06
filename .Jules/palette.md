## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Simulation Termination States
**Learning:** Abruptly closing an application upon reaching an end state (like extinction) prevents users from reviewing the final visual context, leading to a jarring experience.
**Action:** Use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to exit, preserving the final visual state.
