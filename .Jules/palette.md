## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-14 - Extinction Simulation Context
**Learning:** Abruptly closing the application upon a simulation end-state (like agent extinction) deprives the user of the context around why the failure happened.
**Action:** Use a persistent state overlay with a manual acknowledgment prompt (e.g. press ESC to Exit) for end states rather than immediately exiting, to allow the user to review the final simulation visual state.
