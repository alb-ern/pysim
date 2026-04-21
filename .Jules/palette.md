## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2024-05-18 - Extinction Overlay
**Learning:** For simulation end-states, abrupt window termination removes the final visual context the user may want to inspect.
**Action:** Implemented a persistent "EXTINCT" overlay that requires manual acknowledgment (pressing ESC) to exit, ensuring the user can view the final simulation state.
