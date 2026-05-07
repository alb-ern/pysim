## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - End-State Overlays and Dynamic Toggles
**Learning:** Abruptly terminating an application at a simulation end-state destroys visual context, and static toggle labels cause cognitive friction.
**Action:** Use persistent overlay states (like EXTINCT) that require manual acknowledgment (ESC) to close. Ensure toggle labels dynamically reflect the next available action (e.g., '(SPACE to Resume)' when paused).
