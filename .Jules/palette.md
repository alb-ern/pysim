## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Dynamic Action Labels
**Learning:** Static labels (e.g., "SPACE to Pause") cause cognitive friction when the user has already performed the action.
**Action:** Toggle labels should dynamically reflect the next available action (e.g., "(SPACE to Resume)") rather than displaying a static state.
