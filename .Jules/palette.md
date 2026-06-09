## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2023-10-27 - End-state UI preservation
**Learning:** Abruptly terminating an application at the end-state jarringly removes context, frustrating users who want to review the final simulation state. Additionally, static toggle labels cause friction; labels should display the next available action (e.g., '(SPACE to Resume)' when paused, '(ESC to Exit)' when extinct).
**Action:** Always maintain the final visual context by applying an overlay and requiring manual user acknowledgment (like pressing ESC) to close, while dynamically updating action hints to reflect available interactions.
