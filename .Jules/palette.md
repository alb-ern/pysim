## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2024-06-17 - Dynamic Action Labels and Graceful End States
**Learning:** Static toggle labels (like "(SPACE to Pause)") and abrupt application termination on end states create cognitive friction and lose visual context.
**Action:** Use dynamic labels that reflect the next available action (e.g., "(SPACE to Resume)") and implement persistent overlays for end states requiring manual acknowledgment (e.g., ESC to Exit) to preserve the final visual state.
