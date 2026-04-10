## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Preserving visual context on end-state
**Learning:** Abruptly closing a simulation application on an end-state like extinction removes the visual context the user needs to understand what just happened.
**Action:** Instead of abruptly terminating, preserve the visual state and overlay a persistent state message (e.g. "EXTINCT") requiring explicit manual acknowledgment (e.g. ESC to Exit) to close the application.
