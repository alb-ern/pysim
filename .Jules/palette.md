## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Dynamic Action Toggles and Persistent End States
**Learning:** Hard-coded HUD toggles like `(SPACE to Pause)` create confusion when the app is already paused. Further, ending a simulation by immediately closing it removes valuable context from the final state.
**Action:** Update toggle labels dynamically based on state (`(SPACE to Resume)` when paused) and create persistent end-states (like `EXTINCT`) that require user interaction to exit (`(ESC to Exit)`), preserving visual context.
