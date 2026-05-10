## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2024-05-10 - Simulation End-States and Dynamic Labels
**Learning:** Abruptly terminating an application upon reaching an end-state (like agent extinction) removes visual context, confusing users. Static HUD hints ("SPACE to Pause" while already paused) also cause cognitive friction.
**Action:** For simulation end-states, use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close. Toggle labels should dynamically reflect the next available action (e.g., "SPACE to Resume" when paused) to reduce friction.
