## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-17 - Persistent Extinction Overlay
**Learning:** The simulation abruptly closing when agents reach 0 provides no final visual context to the user.
**Action:** Use persistent overlays that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application.
