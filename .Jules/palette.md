## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2025-03-08 - Simulation End-States
**Learning:** Abruptly terminating an application when a simulation reaches an end-state (like extinction) creates a jarring user experience, preventing them from viewing the final state.
**Action:** Use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application, preserving the final visual context.
