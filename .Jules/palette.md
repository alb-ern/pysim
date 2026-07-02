## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Dynamic Toggle Labels
**Learning:** Static labels for toggleable states (like pausing/resuming) cause cognitive friction by not reflecting the next available action.
**Action:** Ensure toggle labels dynamically reflect the next available action (e.g., '(SPACE to Resume)' when paused) to reduce cognitive friction.
