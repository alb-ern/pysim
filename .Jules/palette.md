## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Graceful End States and Dynamic Labels
**Learning:** Abruptly terminating simulations on end states prevents users from reviewing the final context, and static toggle labels create cognitive friction.
**Action:** Use persistent overlays that require manual acknowledgment (e.g., ESC to exit) for critical end-states, and ensure UI action labels dynamically reflect the *next available action* (e.g., "(SPACE to Resume)") rather than the static state.
