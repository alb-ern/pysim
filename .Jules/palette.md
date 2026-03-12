## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Graceful End States
**Learning:** Abruptly closing a simulation window when an end condition (like extinction) is met prevents users from observing the final state.
**Action:** Implement persistent overlay states (like EXTINCTION) that pause the simulation and require manual user acknowledgment to close, preserving the final visual context.
