## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-03-05 - Dynamic Toggle Labels and Graceful Exits
**Learning:** Hard-exiting a simulation on failure states removes context and feels jarring. Static toggle instructions (like "SPACE to Pause" when already paused) cause cognitive friction.
**Action:** Use persistent overlay states that require manual user acknowledgment (e.g., ESC to exit) for failure states. Update UI labels dynamically to reflect the *next available action* (e.g., "SPACE to Resume").
