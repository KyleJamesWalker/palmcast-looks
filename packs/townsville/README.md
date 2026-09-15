# townsville

Five themes and six transitions inspired by The Powerpuff Girls.

Every file is plain CSS and carries no artwork. The skyline, hearts, bubbles and
lightning are inline SVG data URIs. The type is whatever rounded face the reader
already has.

```bash
palmcast --theme-dir packs/townsville/themes \
         --transition-dir packs/townsville/transitions
```

## Themes

| Name | Look |
|---|---|
| `townsville-powerpuff` | Townsville at sunset. Starburst sky, lit skyline, hearts drifting up, headings outlined like a cartoon cel in all three girls' colors. |
| `townsville-blossom` | Raspberry dark, a ribbon across the rule, hearts over a rose starburst. |
| `townsville-bubbles` | The one daylight theme. Soft sky, clouds on the horizon, bubbles floating up. |
| `townsville-buttercup` | Near black under a lime charge, diagonal stripes, headings in uppercase. |
| `townsville-mojo` | Lab purple lit from below by Chemical X, with a green readout glow. |

## Transitions

| Name | Motion |
|---|---|
| `townsville-heart` | The next slide opens out of an 18-point heart. The lobes overshoot the viewport so the corners fill. |
| `townsville-pow` | A punch landing. The next slide overshoots, then settles. |
| `townsville-chemical-x` | The last slide boils green and dissolves upward. |
| `townsville-sugar-spice` | The pair turns through the middle, hue running round the wheel. |
| `townsville-flyover` | The camera banks across the rooftops. |
| `townsville-hotline` | A hot pink flare, one shake, and the next slide is there. |

## Notes

Every theme paints its backdrop on `.viewer` and `.stage` and keeps them opaque.
Palmcast requires that. A surface the page shows through puts two slides of text
on screen at once during a transition.

The drifting sprites sit on `::before` and `::after` at `z-index: -1`, under a
forced `isolation: isolate`. Without the isolation the browser may paint them
behind the surface background, where nobody sees them.

A reader who asks for less motion gets a still backdrop. Palmcast already swaps
any transition for a cross fade.
