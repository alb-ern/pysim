## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Graceful Failure States
**Learning:** Abruptly closing the application upon a failure state (like extinction) leaves users confused about whether the app crashed or finished by design.
**Action:** Instead of immediate termination, provide a distinct visual end-state (e.g., a dark overlay with red text) and require explicit user action (like pressing ESC) to exit, making the state clear and intentional.
