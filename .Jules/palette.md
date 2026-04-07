## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-04-07 - Simulation Extinction End-State
**Learning:** Abruptly terminating the application on end-states like extinction loses the final visual context, leading to a poor user experience.
**Action:** Use persistent overlay states that pause the simulation and require manual user acknowledgment (e.g., pressing ESC) to close rather than exiting immediately.
