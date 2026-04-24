## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-04-24 - Simulation End State Experience
**Learning:** Abruptly terminating visual simulations on extinction loses critical context and final state, leading to a confusing user experience where the screen just disappears.
**Action:** For simulation end-states, use persistent overlay states (like the EXTINCT dim overlay) that require manual user acknowledgment (e.g., pressing ESC) to close, preserving the final visual context for review.
