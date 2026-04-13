## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2024-04-13 - Preserve End-State Context
**Learning:** Abruptly closing the application on simulation end-states prevents users from analyzing the final state of the world.
**Action:** Use persistent overlay states (like an EXTINCT overlay) that require manual user acknowledgment (e.g., pressing ESC) to close, preserving the final visual context.
