## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2024-05-15 - Persistent End-States
**Learning:** Abruptly terminating the application when a simulation reaches an end-state (like extinction) creates a jarring user experience and prevents the user from analyzing the final visual context of the world.
**Action:** Implement persistent overlay states for simulation end-states that pause the simulation and require manual user acknowledgment (e.g., pressing ESC) to close, preserving the final visual state.
