## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Dynamic Toggle Labels
**Learning:** Static toggle labels (like always showing "(SPACE to Pause)" even when already paused) cause cognitive friction by not reflecting the current state.
**Action:** Always ensure toggle labels dynamically reflect the *next* available action to provide clear context to the user.
