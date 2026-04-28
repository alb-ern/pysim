## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2024-05-24 - Persistent Overlay End-States
**Learning:** Simulation end-states (like extinction) that abruptly close the application jar the user and remove context of the final simulation state.
**Action:** Use persistent overlays that pause execution and require explicit manual user acknowledgment (e.g., pressing ESC) to close, preserving the final visual state.
