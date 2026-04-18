## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Simulation End State Graceful Degradation
**Learning:** Abruptly closing a visual simulation window when an end condition (like extinction) is met is jarring and destroys the visual context the user was just observing.
**Action:** For simulation end-states, always implement persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than immediately terminating the application loop.
