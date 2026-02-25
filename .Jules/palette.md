## 2025-02-23 - Visual Feedback for Game States
**Learning:** In graphical simulations (Pygame), simple text overlays for states like 'PAUSED' often lack sufficient contrast against dynamic backgrounds. Full-screen semi-transparent dimming provides immediate, unambiguous feedback that the world state is suspended.
**Action:** Default to using full-screen dimming layers (alpha ~100) for modal states (Pause, Game Over) to separate UI from the game world.
