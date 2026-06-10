## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2025-06-10 - Persistent End-States
**Learning:** End states like "Extinct" abruptly closed the app rather than keeping the visual context intact, losing valuable visual information for users wanting to examine the final frame.
**Action:** Created persistent end-states (e.g. paused logic inside EXTINCT condition) and explicitly prompted users with "(ESC to Exit)" to maintain closure and context.
