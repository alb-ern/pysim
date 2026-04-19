## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-04-19 - Persistent End States
**Learning:** When simulations or dynamic interactions reach a terminal state (like extinction), abruptly closing the window removes visual context and feels jarring.
**Action:** Use persistent overlay states (like a dim overlay with clear status text) that require manual user acknowledgment (e.g., pressing ESC) to close, preserving the final visual context.
