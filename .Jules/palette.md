## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - Simulation End-State UX
**Learning:** Abruptly quitting an application when a simulation ends (like an extinction state) leaves the user confused about what happened and prevents them from seeing the final state of the simulation.
**Action:** Use persistent overlay states (like "EXTINCT") with dynamic toggle labels (like "(ESC to Exit)") to require manual user acknowledgment and preserve the final visual context.
