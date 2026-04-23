## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-03-05 - Extinction Overlay
**Learning:** Abruptly terminating simulations when end-states (like extinction) are reached creates a jarring user experience, depriving them of the final visual context.
**Action:** Use persistent overlays that require manual user acknowledgment (e.g., pressing ESC) to exit the application rather than quitting automatically.
