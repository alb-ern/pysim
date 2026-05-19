## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-05-19 - Persistent End States & Dynamic Toggles
**Learning:** Abruptly quitting on simulation extinction prevents the user from viewing the final visual context. Static toggle instructions (like '(SPACE to Pause)') cause cognitive friction when they do not reflect the current state.
**Action:** Use persistent overlay states requiring manual user acknowledgment (e.g. ESC) for end-states, and dynamically update toggle labels to reflect the next available action.
