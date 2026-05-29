## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2023-10-25 - Dynamic Toggle Labels and Graceful End-States
**Learning:** For simulation end-states, abruptly terminating the application destroys the final visual context, while static toggle labels (e.g., "(SPACE to Pause)" when already paused) create cognitive friction.
**Action:** Use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close for end-states. Ensure toggle labels dynamically reflect the next available action.
