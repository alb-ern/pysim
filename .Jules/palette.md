## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Simulation End-States & Dynamic Labels
**Learning:** Abruptly terminating an application upon reaching an end-state (like simulation extinction) causes loss of final visual context, confusing the user. Also, static toggle labels (e.g. "SPACE to Pause" when already paused) increase cognitive friction.
**Action:** Use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application. Also, toggle labels should dynamically reflect the next available action (e.g., "(SPACE to Resume)" when paused).
