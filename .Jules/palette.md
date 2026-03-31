## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2024-05-24 - Graceful Application Extinction Overlays
**Learning:** Sudden application termination removes necessary visual context for the end state.
**Action:** Implement persistent overlay states requiring explicit manual acknowledgment to close.
