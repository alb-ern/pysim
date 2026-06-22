## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-06-22 - Dynamic Pause Toggle Label
**Learning:** Toggle labels should dynamically reflect the next available action (e.g., '(SPACE to Resume)' when paused) rather than displaying a static state to reduce cognitive friction.
**Action:** Use dynamic string formatting based on current state variables for toggle labels.
