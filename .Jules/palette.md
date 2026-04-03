## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2023-10-24 - Extinction End-State UX
**Learning:** Simulation end-states should preserve the final visual context by requiring manual user acknowledgment instead of abruptly terminating.
**Action:** Implement persistent overlay states for end-conditions that pause the simulation and wait for a specific input (like ESC) to exit.
