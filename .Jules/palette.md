## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Persistent Overlays for End-States
**Learning:** Abruptly terminating a simulation or application when it reaches a terminal end-state (like extinction) is jarring and prevents users from observing the final state context.
**Action:** Use persistent overlay states for simulation end-states that pause execution and require explicit user action (e.g., ESC to exit) rather than immediately closing the application.
