## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2023-10-27 - Graceful End-States and Dynamic Labels
**Learning:** Abruptly closing the simulation (application exit) upon extinction strips the user of the final visual context and causes confusion. Static toggle labels (like "(SPACE to Pause)" when the game is already paused) add cognitive friction. Furthermore, high-contrast text overlays (via dark, semi-transparent rectangles) are critical for readability when rendering text over busy canvas/game backgrounds.
**Action:** Always implement graceful end-states (e.g., transition to a PAUSED/EXTINCT overlay requiring manual EXIT) rather than abrupt termination. Use dynamic labels that reflect the *next available action* (e.g., "(SPACE to Resume)"). Always add semi-transparent contrast backdrops for centered HUD elements in simulation environments.
