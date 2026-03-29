## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-29 - Simulation End-State UX
**Learning:** Abruptly exiting a simulation when the population reaches zero (extinction) removes the visual context of what caused the failure.
**Action:** For simulation end-states, use persistent overlay states (like a paused screen showing EXTINCT) that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application.
