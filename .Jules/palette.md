## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-03-05 - Simulation End-States
**Learning:** Abruptly closing a visual simulation upon reaching an end-state (like extinction) destroys the final visual context, confusing users about what happened.
**Action:** Always provide a persistent overlay state that requires manual user acknowledgment (e.g., pressing ESC to exit) rather than abruptly terminating the application.
