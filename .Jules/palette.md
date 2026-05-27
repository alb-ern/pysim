## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-05-27 - Graceful Termination & Dynamic Labels
**Learning:** Abruptly closing the simulation window on the "extinct" state is jarring and removes the final context from the user. Static toggle labels like "(SPACE to Pause)" when the game is already paused or ended cause cognitive friction.
**Action:** Use persistent overlay states (like "EXTINCT") requiring manual acknowledgment (e.g., ESC) to exit, preserving visual context. Ensure toggle labels dynamically reflect the *next available action* (e.g., "(SPACE to Resume)", "(ESC to Exit)").
