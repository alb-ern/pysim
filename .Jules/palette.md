## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Simulation End State Context
**Learning:** Abruptly terminating an application on end-states (like extinction) destroys visual context, and static toggle labels cause cognitive friction.
**Action:** Use persistent overlay states that require manual user acknowledgment (e.g., ESC to exit) and dynamically reflect the next available action in toggle labels.
