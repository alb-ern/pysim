## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Graceful End States
**Learning:** Closing an application abruptly on an end state (like extinction) prevents users from viewing final statistics, reading messages, or understanding what happened.
**Action:** Instead of terminating the program loop, apply a persistent visual overlay (like 'EXTINCT' and '(ESC to Exit)') and pause the simulation logic so users can explicitly dismiss the application.
