## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-06-05 - Dynamic Toggle Labels and End-States
**Learning:** Abrupt simulation termination on extinction causes a loss of context. Static HUD toggle labels cause cognitive friction.
**Action:** Use persistent end-states with clear dynamic HUD instructions (e.g. SPACE to Resume / ESC to Exit).
