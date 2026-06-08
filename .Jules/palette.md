## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2023-10-24 - Dynamic Toggles & Persistent End-States
**Learning:** Hard-stopping a simulation abruptly and displaying static text leads to poor visual context and cognitive friction.
**Action:** For simulation end-states, use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application, preserving the final visual context. Toggle labels should dynamically reflect the next available action (e.g., '(SPACE to Resume)' when paused) rather than displaying a static state.
