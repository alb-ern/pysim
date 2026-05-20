## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2023-10-25 - Dynamic Toggle Labels
**Learning:** Static toggle labels (like "(SPACE to Pause)") can cause cognitive friction when they do not reflect the current available action, especially in toggle states like Play/Pause.
**Action:** Always ensure toggle labels dynamically reflect the *next available action* (e.g., "(SPACE to Resume)" when paused) to make the interface more intuitive and reduce user confusion.
