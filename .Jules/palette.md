## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-06-25 - Dynamic Action Labels & Graceful Exits
**Learning:** Static labels like "(SPACE to Pause)" cause cognitive friction when the app is already paused. Also, abruptly terminating an application on an end-state (like extinction) forces the user out of the context.
**Action:** Use dynamic toggle labels that reflect the *next* action (e.g., "(SPACE to Resume)" when paused). For end-states, present a persistent overlay that requires explicit user dismissal (e.g., "Press ESC to Exit") rather than auto-closing.
