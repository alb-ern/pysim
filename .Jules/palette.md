## 2026-03-05 - Pygame Pause Readability
**Learning:** Rendering white text directly over a busy simulation background reduces contrast and makes text hard to read.
**Action:** Always provide a semi-transparent dark overlay behind critical centered HUD elements (like a PAUSED state) to ensure sufficient contrast and visual hierarchy.

## 2026-07-07 - Enhance End-State Lifecycle Visibility
**Learning:** Automatically terminating the application immediately upon reaching an end state (like extinction) creates a poor user experience by deleting the final visual context.
**Action:** Use an explicit terminal overlay state that pauses updates and requires a manual user acknowledgment to close, preserving the final context. Also update HUD indicators dynamically (e.g., Space to Resume instead of Space to Pause when paused) to reduce friction.
