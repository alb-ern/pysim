## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - End-State App Termination
**Learning:** Abruptly closing the simulation by terminating the process when the population dies out feels like a crash and ruins visual context.
**Action:** Use persistent overlay states (like a paused EXTINCT screen) for simulation end-states that require manual user acknowledgment (e.g., pressing ESC) to exit, preserving the final visual context.
