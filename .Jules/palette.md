## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Graceful Simulation Termination
**Learning:** Abruptly closing the application upon a final state (like extinction) deprives users of the visual context that led to the event.
**Action:** For end-states, use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than immediately terminating the application.
