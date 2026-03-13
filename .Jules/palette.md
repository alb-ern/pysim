## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-13 - Extinction UX
**Learning:** Abruptly closing the simulation on extinction removes the final visual context and leaves the user wondering what happened.
**Action:** Use a persistent overlay state that requires manual user acknowledgment (e.g., pressing ESC) to close simulation end-states, preserving the final visual context.
