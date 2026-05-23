## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Simulation End States
**Learning:** Abruptly closing a simulation application when a termination condition is met (like population reaching 0) removes the final visual context from the user.
**Action:** For simulation end-states, use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application, preserving the final visual context. Ensure toggle labels dynamically reflect the next available action (e.g., "(ESC to Exit)", "(SPACE to Resume)") rather than displaying a static state to reduce cognitive friction.
