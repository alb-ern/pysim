## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-03-05 - Graceful Simulation End-States
**Learning:** Abruptly terminating an application upon failure states removes valuable final visual context for the user. Static toggle labels also cause cognitive friction when their actions change.
**Action:** For simulation end-states, use persistent overlay states requiring manual user acknowledgment to close. Ensure toggle labels dynamically reflect the next available action.
