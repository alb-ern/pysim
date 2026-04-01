## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2025-05-15 - End-state Visual Context
**Learning:** Abruptly quitting an application when a simulation reaches an end-state (like extinction) removes the final visual context, which leaves users confused about what just happened.
**Action:** Always provide a persistent overlay state (e.g., "EXTINCTION") that pauses the application and requires manual user acknowledgement (like pressing ESC) to close.
