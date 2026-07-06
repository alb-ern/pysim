## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Preserve Visual Context on Simulation End
**Learning:** Abruptly terminating an application at a simulation end-state (like Extinction) removes the final visual context and can be confusing. Also, static toggle labels (like always saying "SPACE to Pause") increase cognitive friction.
**Action:** Use persistent overlay states for simulation end-states that require manual user acknowledgment (e.g., pressing ESC) to close. Ensure toggle labels dynamically reflect the next available action (e.g., "(SPACE to Resume)" when paused).
