## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2024-05-24 - Dynamic Action Labels and Graceful End States
**Learning:** Static labels like "(SPACE to Pause)" cause cognitive friction when the simulation is already paused, and abrupt application termination upon an end-state like extinction prevents users from reviewing the final visual context.
**Action:** Toggle labels should dynamically reflect the next available action (e.g., "(SPACE to Resume)"), and simulation end-states should apply persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close.
