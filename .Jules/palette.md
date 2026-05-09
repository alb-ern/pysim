## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-05-09 - Dynamic Action Hints and Persistent End-States
**Learning:** Persistent overlay states require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating the application, preserving final visual context.
**Action:** Use dynamic toggle labels reflecting the next available action (e.g., (SPACE to Resume)) rather than displaying a static state to reduce cognitive friction.
