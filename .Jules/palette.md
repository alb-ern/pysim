## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-05-30 - Persistent Simulation End-States
**Learning:** Abruptly terminating an application at a simulation end-state (like Extinction) destroys the visual context, leaving the user without a clear understanding of the final state.
**Action:** For simulation end-states, use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application, preserving the final visual context.
