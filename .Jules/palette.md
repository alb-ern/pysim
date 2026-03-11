## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Graceful Simulation Termination
**Learning:** Abruptly closing a window on simulation end-states (like extinction) provides poor feedback, leaving users wondering if the app crashed.
**Action:** Always transition terminal states into a paused visual overlay that clearly communicates the outcome and provides explicit instructions to exit (e.g., "Press ESC to Exit").
