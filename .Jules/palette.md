## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2025-03-05 - Persistent End-States and Dynamic Action Labels
**Learning:** Abruptly closing the application upon a terminal state (like extinction) prevents users from reviewing the final visual context, and static toggle labels (like "SPACE to Pause" when already paused) cause cognitive friction.
**Action:** For simulation end-states, use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close. Also, ensure toggle labels dynamically reflect the next available action (e.g., "SPACE to Resume" when paused) rather than displaying a static state.
