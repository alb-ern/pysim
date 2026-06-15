## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-03-05 - Simulation End-States
**Learning:** Abruptly closing the simulation on end-states (like Extinction) removes context and causes a frustrating, sudden exit.
**Action:** Always provide persistent overlays that require manual user acknowledgment (e.g., pressing ESC) instead of terminating the application automatically.
