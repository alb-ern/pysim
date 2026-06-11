## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-06-11 - Dynamic Toggle Labels & Graceful Exits
**Learning:** Users need accurate cues for current available actions, and abrupt closures destroy visual context.
**Action:** Use dynamic toggle labels (e.g., '(SPACE to Resume)' vs '(SPACE to Pause)') and require manual acknowledgment (ESC) for end-states.
