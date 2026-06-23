## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-06-23 - Simulation State UX Improvements
**Learning:** Abruptly closing the simulation on end-states like extinction jarringly removes visual context, and static toggle labels cause cognitive friction.
**Action:** Use persistent overlay states that require manual dismissal for end-states, and dynamically update toggle labels to reflect the next available action (e.g., '(SPACE to Resume)').
