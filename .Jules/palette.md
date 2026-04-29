## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-04-29 - Prevent Abrupt Exit on Simulation End-states
**Learning:** Abruptly exiting an application when reaching a terminal state (like extinction) drops all visual context, making it hard for users to understand what happened.
**Action:** Use persistent overlay states (e.g., dimming the background, drawing an overlay text) that require manual user acknowledgment (like pressing ESC to Exit) to preserve visual context and improve UX clarity.
