## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Graceful Extinction End-State
**Learning:** Abruptly terminating the application when the simulation ends discards the final visual context.
**Action:** Use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close, preserving the final state.
