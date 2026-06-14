## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2024-05-20 - Dynamic Toggle Labels
**Learning:** Static instructions for toggleable states (e.g. "(SPACE to Pause)") cause cognitive friction when the user is already in that state.
**Action:** Toggle labels should dynamically reflect the next available action (e.g. "(SPACE to Resume)") rather than displaying a static state.

## 2024-05-20 - Graceful End-States
**Learning:** Abruptly terminating an application upon reaching an end-state (like simulation extinction) destroys the final visual context, leaving users confused.
**Action:** Use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application.
