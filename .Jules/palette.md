## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Graceful End States
**Learning:** Simulation environments that abruptly close on an end-state prevent users from analyzing the final conditions that led to the event.
**Action:** Implement a paused overlay with explicit exit instructions (e.g., "Press ESC to quit") when terminal states are reached.
