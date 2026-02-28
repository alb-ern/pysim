# Palette's Journal - Critical Learnings

## 2024-05-24 - Pygame HUD visibility
**Learning:** Text overlays in Pygame simulations need proper contrast. Currently, the HUD might blend into the background (food/temperature grid).
**Action:** Adding a semi-transparent background behind text elements greatly improves readability and accessibility.

## 2024-05-24 - Pygame pause overlay
**Learning:** When pausing simulations, an overlay indicating the paused state is crucial for UX, but it shouldn't completely obscure the view.
**Action:** Use a semi-transparent screen overlay or a clear, centered text indicator for paused states.

## 2024-05-24 - Unhindered viewing and state indicators
**Learning:** Users often want to view complex visual simulations (like evolution sims) without HUD clutter, but still need clear visual indicators for global states like "Paused".
**Action:** Provide a toggle for the HUD (e.g., 'H' key) and use full-screen semi-transparent dark overlays for inactive states to ensure high contrast for state text without completely hiding the simulation underneath.
