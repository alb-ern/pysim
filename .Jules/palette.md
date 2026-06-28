## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Simulation End States and Action Labels
**Learning:** Users experience friction when end states abruptly terminate an application or when action labels don't match the current state.
**Action:** Use persistent overlay states requiring manual dismissal (ESC) instead of abrupt exits, and ensure action labels dynamically update (e.g., "(SPACE to Resume)").
