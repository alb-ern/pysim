## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-06-19 - Avoid abrupt simulation termination
**Learning:** Terminating the simulation abruptly on extinction loses visual context.
**Action:** Use an 'EXTINCT' overlay and wait for explicit user action (ESC) to close the application.
