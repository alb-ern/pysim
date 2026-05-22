## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-05-22 - Graceful End States and Dynamic Action Hints
**Learning:** Abruptly closing a simulation upon end-state (extinction) denies the user the ability to view the final application state. Additionally, static toggle action hints (e.g., "(SPACE to Pause)" when the game is already paused) create cognitive friction. Central visual overlays on visually busy backgrounds need localized darker backing frames to guarantee high contrast and readability.
**Action:** Transition applications into a graceful paused overlay state upon finish conditions that require manual exit (e.g. ESC). Implement state-dependent dynamic action labels for toggles, and use semi-transparent backing layers specifically behind text overlays.
