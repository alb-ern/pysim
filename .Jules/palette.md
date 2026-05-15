## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.
## 2026-03-05 - Persistent Simulation End-States
**Learning:** Automatically closing an application when a final condition is met (like extinction) jarringly removes all visual context, leaving users confused about what just happened. Additionally, static labels (like "(SPACE to Pause)") during end-states or paused states cause cognitive friction.
**Action:** Use persistent overlay states (like EXTINCT) that require manual dismissal (e.g., ESC to Exit) to preserve visual context. Always use dynamic toggle labels (e.g., "(SPACE to Resume)" when paused) that reflect the *next* available action.
