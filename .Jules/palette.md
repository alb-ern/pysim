## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-03-05 - End-State Persistence
**Learning:** Abruptly terminating applications or simulations upon reaching an end-state frustrates users by destroying visual context.
**Action:** Use persistent overlay states (like EXTINCT or GAME OVER) that require explicit manual acknowledgment (e.g., pressing ESC) to close, preserving the final visual context.
