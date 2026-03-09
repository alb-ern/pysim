## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-09 - Graceful Terminal Application States
**Learning:** Abruptly quitting an application upon reaching an end-state prevents users from inspecting the final visual state.
**Action:** Always maintain the final visual state and require explicit user action (like pressing an EXIT key) to terminate the application.