## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Persistent Simulation End-States
**Learning:** Abruptly terminating the application at the end of a simulation (like "Extinction") removes context, confusing the user and preventing post-simulation analysis.
**Action:** Use persistent overlay states (with a semi-transparent dark background for contrast) that require manual user acknowledgment (e.g., pressing ESC) to close.

## 2026-03-05 - Dynamic Toggle Labels
**Learning:** Displaying static status labels for toggles requires cognitive effort to infer the next available action.
**Action:** Make toggle labels dynamically reflect the next action (e.g., '(SPACE to Resume)' when paused) to reduce cognitive friction.
