## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-06-18 - Graceful simulation end-state & dynamic action labels
**Learning:** Abruptly quitting an application upon reaching an end-state (like simulation extinction) causes users to lose visual context. Furthermore, using static labels for controls (like "(SPACE to Pause)" even when paused) increases cognitive friction.
**Action:** Use persistent end states with manual acknowledgment (e.g. "EXTINCT" overlay, requiring ESC to exit) and dynamically reflect the *next available action* in toggle labels (e.g. "(SPACE to Resume)").
