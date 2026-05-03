## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-05-03 - Graceful End-States & Dynamic Toggles
**Learning:** Abruptly quitting the simulation on extinction ruins visual context, and static toggle hints cause cognitive friction.
**Action:** Use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC), and dynamically update toggle labels based on context.
