## 2025-02-23 - Dynamic Background Contrast
**Learning:** Pygame text overlays ("PAUSED") directly on dynamic simulation backgrounds suffer from variable contrast.
**Action:** Always use a semi-transparent scrim (e.g., `pg.Surface.fill((0,0,0,100))`) behind modal text to ensure readability.
