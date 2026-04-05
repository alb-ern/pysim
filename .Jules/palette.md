## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-04-05 - Preserve Visual Context for End-States
**Learning:** Abruptly closing the application upon a final end-state (like extinction) creates poor UX because the user loses the visual context of what happened right before the failure.
**Action:** Always pause simulations or preserve the final state upon failure, apply a transparent overlay, and require a manual exit (e.g. "ESC to Exit") so the user can digest the final state.
