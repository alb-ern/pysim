## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-03-05 - Dynamic Action Labels & Graceful Exits
**Learning:** Hardcoding static action labels (like "SPACE to Pause") when the action context changes (e.g. paused vs running) creates cognitive friction. Terminating simulations abruptly on end-states hides the final context from users.
**Action:** Use dynamic toggle labels that reflect the *next available* action (e.g., "(SPACE to Resume)" when paused). For simulation end-states, use persistent overlay states that require manual user acknowledgment (e.g., pressing ESC) to close rather than abruptly terminating.
