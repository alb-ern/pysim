## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2023-10-27 - Simulation End States
**Learning:** Abruptly closing application windows when termination conditions are met (e.g. extinction) creates poor user experience and removes context.
**Action:** Use persistent overlay states (like "EXTINCT") that require manual user acknowledgment (e.g., pressing ESC) to exit rather than abruptly terminating the application, preserving the final visual context.
