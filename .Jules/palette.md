## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2024-03-10 - Simulation End-State Preservation
**Learning:** Abruptly closing the application when a simulation ends (like reaching an extinct state) prevents users from analyzing the final state, creating a jarring experience.
**Action:** For simulation end-states, use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application, preserving the final visual context.

## 2024-03-10 - Dynamic Toggle Labels
**Learning:** Displaying a static toggle label (like "(SPACE to Pause)") while the application is already paused causes cognitive friction, as the label doesn't reflect the action the user can actually take next.
**Action:** Toggle labels should dynamically reflect the next available action (e.g., "(SPACE to Resume)" when paused) rather than displaying a static state to reduce cognitive friction.
