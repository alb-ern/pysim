## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## $(date +%Y-%m-%d) - Graceful Extinction End-State
**Learning:** Abruptly closing a visual application or simulation (e.g., when an end condition like `agents == 0` is met) creates a jarring user experience. Users lose the final visual context and may wonder if the program crashed.
**Action:** Always implement a persistent end-state overlay (e.g., "EXTINCT") that requires explicit user acknowledgment (like pressing ESC) to exit, preserving the final visual state. Additionally, ensure contextual toggle labels (like "(SPACE to Resume)") dynamically update to reflect the current state and available actions to reduce cognitive friction.
