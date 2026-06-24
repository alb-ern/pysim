## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Persistent Extinction Overlay
**Learning:** Abruptly closing the simulation on extinction prevents users from seeing the final state.
**Action:** Implemented a persistent 'EXTINCT' overlay requiring manual dismissal (ESC) to preserve context.

## 2026-03-05 - Dynamic Toggle Labels
**Learning:** Static labels for toggles can be confusing and increase cognitive friction.
**Action:** Updated toggle labels to dynamically reflect the next available action (e.g., '(SPACE to Resume)' when paused).
