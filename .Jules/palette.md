## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Simulation End States and Dynamic Toggle Labels
**Learning:** Abruptly terminating an application upon a failure state (like simulation extinction) removes the visual context the user needs to understand what happened. Furthermore, static toggle labels (e.g. "(SPACE to Pause)") become confusing when the app state changes (e.g., when it is already paused).
**Action:** For simulation end-states, use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application, preserving the final visual context. Toggle labels should dynamically reflect the next available action (e.g., "(SPACE to Resume)") rather than displaying a static state to reduce cognitive friction.
