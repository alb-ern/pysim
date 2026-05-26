## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-05-26 - Graceful Extinction & Dynamic Toggle
**Learning:** Abruptly closing the application upon a failure state (extinction) removes visual context, and static toggle labels (e.g. '(SPACE to Pause)' while already paused) increase cognitive friction.
**Action:** Use persistent overlay states that require manual user acknowledgment to close, and dynamically update toggle labels to reflect the *next* available action.
