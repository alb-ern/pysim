## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Persistent Extinction Overlay and Dynamic Action Labels
**Learning:** Abrupt program termination on simulation end-states breaks the user's visual context. Showing a static toggle label during different interaction states increases cognitive friction.
**Action:** For simulation end-states, use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close. Ensure toggle labels (like SPACE to pause/resume) dynamically reflect the *next available action* rather than displaying a static state.
