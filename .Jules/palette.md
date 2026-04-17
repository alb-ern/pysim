## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2023-10-27 - Graceful Degradation for Extinction
**Learning:** Abruptly exiting an application when reaching an end state (like all agents dying) removes context and is jarring for users.
**Action:** Use an overlay state (e.g., EXTINCT) that pauses the simulation and waits for user interaction (ESC to Exit) to allow reflection and preserve visual context.
