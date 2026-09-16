# gotham

Five themes and six transitions for a deck given after dark.

Every file is plain CSS and carries no artwork. The skyline, the cards and the
halftone are inline SVG and gradients. The type is whatever condensed face the
reader already has.

```bash
palmcast --theme-dir packs/gotham/themes \
         --transition-dir packs/gotham/transitions
```

## Themes

| Name | Look |
|---|---|
| `gotham-knight` | Rain on the diagonal over a deco skyline, one beam in the cloud, slab caps. |
| `gotham-signal` | Charcoal, and a single hard cone thrown up from the bottom edge with dust in it. |
| `gotham-arkham` | Institutional green, tile to the ceiling, a fluorescent that gives up every few seconds. |
| `gotham-joker` | Acid green over lab violet, cards and diamonds drifting past. |
| `gotham-gazette` | **The light one.** Newsprint, halftone, a fold down the middle and a masthead rule. |

## Transitions

| Name | Motion |
|---|---|
| `gotham-batarang` | Spins in from the top corner and lands flat. |
| `gotham-grapple` | The line goes taut and the slide leaves upward, uncovering the next. |
| `gotham-blackout` | Full black for a beat, so nothing crosses in the dark. |
| `gotham-searchlight` | A cone sweeps from the foot of the screen and leaves the next slide behind it. |
| `gotham-smoke` | Both slides blur grey through a pellet. |
| `gotham-gargoyle` | A step off the ledge; the next rises to meet the camera. |

## Knobs

```markdown
<!-- theme: gotham-knight hour=storm rain=heavy -->
```

| Theme | Knob | Choices |
|---|---|---|
| `gotham-knight` | `hour` | `night` · `storm` · `dawn` |
| | `rain` | `heavy` 6s, `steady` 12s, `light` 24s, `dry` 0s |
| `gotham-signal` | `beam` | `amber` · `white` · `crimson` |
| `gotham-arkham` | `ward` | `green` · `bone` · `rust` |
| | `flicker` | `restless` 3s, `uneasy` 7s, `steady` 14s, `still` 0s |
| `gotham-joker` | `rogue` | `joker` · `riddler` · `ivy` |
| | `drift` | `calm` 60s, `normal` 30s, `brisk` 16s, `still` 0s |
| `gotham-gazette` | `stock` | `newsprint` · `bright` · `aged` |

The first choice in each row is what the file ships, and it has no
`@container style()` block of its own.

## Notes

`gotham-gazette` is the only theme here for a room with the lights on, and the
only one that sets the seven `--code-*` variables: the defaults in `base.css`
are written for a dark ground and are unreadable on paper.

`gotham-searchlight` hangs a `mask-image` on
`::view-transition-new(palmcast-surface)`, so it writes its own name twice. That
is allowed; every occurrence has to name this same file.

Nothing here moves for a reader who asked for less motion: the rain, the dust
and the fluorescent all stop, and Palmcast already swaps any transition for a
cross fade.

## Licence

MIT, matching Palmcast. DC Comics and Warner Bros. own Batman, Gotham City and
its characters. This pack is unofficial fan work: it ships colours, shapes and
keyframes, and carries no artwork, logo, font or audio from anything.
