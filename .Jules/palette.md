## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2023-10-27 - Graceful Exit on Extinction
**Learning:** Abruptly terminating a simulation when an end state is reached prevents the user from viewing the final state or understanding what happened.
**Action:** Always transition to a persistent "Game Over" or paused state with clear messaging (e.g., "EXTINCT", "ESC to Exit") and a dimming overlay to maintain visual context while indicating the simulation has ended.
