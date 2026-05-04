## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Persistent End-States and Dynamic Labels
**Learning:** Abruptly closing the simulation application upon reaching an end-state (like Extinction) abruptly removes the visual context the user may want to observe. Also, static toggle labels like "(SPACE to Pause)" are misleading when the simulation is already paused.
**Action:** Use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application. Also, toggle labels should dynamically reflect the next available action (e.g., "(SPACE to Resume)") rather than displaying a static state to reduce cognitive friction.
