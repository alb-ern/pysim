## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Graceful End States
**Learning:** Abruptly closing a desktop/canvas application when a run/simulation naturally completes or fails feels jarring, frustrating users who want to see the final state or read metrics before acting.
**Action:** Always provide a graceful end-state (e.g., a clearly labeled end overlay that pauses execution, shows final metrics, and prompts the user to press a key like ESC to manually close the application).
