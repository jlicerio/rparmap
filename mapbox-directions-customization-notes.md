# Mapbox Directions Customization Notes

## Customizations Attempted

- Overrode panel background, border, and font to match site theme (light gray, purple, Cormorant Garamond font).
- Made the panel more compact and increased width on desktop for readability.
- Restyled the route summary header to use a solid purple background with white text.
- Changed step backgrounds and text for clarity and visual hierarchy.
- Added word-break and white-space rules to prevent text overlap and wrapping issues.
- Moved maneuver icons (arrows) to the far right, then removed them entirely for a text-only look.
- Hid all SVG icons and maneuver symbols using CSS.
- Limited the visible directions steps to 3 at a time, with a "Show More" button to reveal all steps.
- Ensured only the first 3 steps are shown by default using JavaScript after panel render.
- Enabled the walking/driving profile switcher and hid input fields for a cleaner UI.
- Fixed the "Show More" button styling to match the theme.
- Addressed issues with direction text being hidden by only targeting icon elements in CSS.

## Revert Request

- Requested to revert to the original Mapbox Directions plugin (for Mapbox GL JS) appearance and behavior for comparison.
- The original plugin displays all steps, includes maneuver icons, and uses the default Mapbox styling.

---

This document tracks all changes and experiments made to the Mapbox Directions panel for future reference and comparison. 