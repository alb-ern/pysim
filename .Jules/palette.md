## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-05-17 - Graceful Simulation Extinction End State
**Learning:** Abruptly closing the simulation on extinction (0 agents) causes a jarring experience and prevents users from reviewing the final world state (temperature/food distribution).
**Action:** Apply a persistent, semi-transparent overlay indicating the 'EXTINCT' state and dynamically update action labels (e.g. 'ESC to Exit') rather than forcefully quitting the application.
