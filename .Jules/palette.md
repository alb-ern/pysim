## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-26 - Graceful End-States
**Learning:** Abruptly terminating an application on an end-state (like simulation extinction) creates a jarring user experience and removes final visual context that users might want to examine.
**Action:** For simulation end-states, use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application.
