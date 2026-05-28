## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Graceful End States and Dynamic Toggle Text
**Learning:** Abruptly closing the simulation on an end-state like extinction prevents the user from analyzing the final configuration. Using static text for a toggle action (e.g. `(SPACE to Pause)`) is confusing when the state changes.
**Action:** Use persistent semi-transparent overlays for end-states that require explicit manual exit (e.g., `(ESC to Exit)`). Always update toggle labels to reflect the next possible action (`(SPACE to Resume)` vs `(SPACE to Pause)`).
