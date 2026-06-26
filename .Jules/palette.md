## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-06-26 - Simulation End-state UX
**Learning:** Abruptly closing the application upon a terminal end-state (like EXTINCTION) forces the user to lose the final visual context, creating a jarring experience. Static label texts (e.g., '(SPACE to Pause)') also create friction when the action is no longer viable depending on the current state.
**Action:** Use persistent overlay states for simulation end-conditions requiring manual acknowledgment (e.g., pressing ESC) rather than terminating, and ensure action labels dynamically update based on state (e.g. '(SPACE to Resume)' when paused).
