## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Dynamic Toggle Labels
**Learning:** Static toggle labels (e.g., "SPACE to Pause") can cause cognitive friction when the application is already in the paused state, as the label suggests an action that cannot be taken.
**Action:** Always ensure toggle labels dynamically reflect the *next available action* (e.g., "(SPACE to Resume)" when paused) to reduce cognitive load and improve clarity.
