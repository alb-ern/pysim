## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-05-02 - Dynamic Toggle Labels and Persistent Overlays
**Learning:** Users experience cognitive friction when toggle hints display static text instead of actionable outcomes, and abrupt visual closures upon simulation end prevent users from digesting the final state.
**Action:** Use dynamic toggle labels (e.g., '(SPACE to Resume)' when paused) and apply persistent overlays (like 'EXTINCT') that require manual exit to preserve context.
