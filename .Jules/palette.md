## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-03-05 - Persistent Overlay for Simulation End-States
**Learning:** Abruptly terminating an application at a simulation end-state (like extinction) loses the final visual context, which frustrates users trying to analyze the final state.
**Action:** Use persistent overlay states that pause the simulation and require manual user acknowledgment (e.g., pressing ESC) to exit, preserving the final visual context.
