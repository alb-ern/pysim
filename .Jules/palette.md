## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Persistent Overlay End States
**Learning:** Abruptly closing a simulation window when an end-state is reached deprives the user of the final context.
**Action:** Use persistent overlay states (like EXTINCT or PAUSED) that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application. This preserves the final visual context.
