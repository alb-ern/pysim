## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-06-13 - Simulation End-State Graceful Degradation
**Learning:** Users lose important visual context when a simulation abruptly terminates upon an 'extinct' end-state. Providing persistent visual overlays (e.g. 'EXTINCT' with a dimmed background) ensures the final state is preserved and understood. Action toggles (e.g. SPACE to pause, ESC to exit) must dynamically match the new constraints.
**Action:** Always maintain the final rendering frame and employ persistent overlay states requiring manual acknowledgment (like ESC) rather than abruptly closing applications or window interfaces.
