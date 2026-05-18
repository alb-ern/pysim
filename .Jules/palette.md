## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Simulation End-State UX
**Learning:** Abruptly closing the simulation (or application) upon an end-state like "Extinction" removes context and leaves the user confused about what happened.
**Action:** Always transition into a persistent "end-state" overlay that pauses the system, displays the result clearly, and requires an explicit user action (like pressing ESC) to exit.

## 2026-03-05 - Dynamic Toggle Labels
**Learning:** Static instructions for toggles like "(SPACE to Pause)" are misleading when the state is already paused.
**Action:** Always make toggle labels dynamic (e.g., "(SPACE to Resume)" when paused, "(SPACE to Pause)" when running) to accurately reflect the action that will happen when the key is pressed.
