# dcla

Four themes and three transitions in the Data Con LA palette, for a talk given
at the conference or about it.

```bash
palmcast --theme-dir packs/dcla/themes \
         --transition-dir packs/dcla/transitions
```

## Themes

| Name | Look |
|---|---|
| `dcla-keynote` | **The default.** Light stock, condensed headings, the three-colour rule along the foot. |
| `dcla-stage` | The same deck inverted onto near black, for a screen the whole hall reads at once. |
| `dcla-sunset` | Los Angeles at golden hour: violet down into amber, city and palms in silhouette. |
| `dcla-grid` | A plot grid, a scatter and a trend line, kept faint enough to read a table through. |

## Transitions

| Name | Motion |
|---|---|
| `dcla-wipe` | The three colours cross as one bar and leave the next slide behind. |
| `dcla-plot` | The next slide settles up out of the bottom-left origin. |
| `dcla-freeway` | A lane change at speed, both slides leaning into it. |

## Knobs

```markdown
<!-- theme: dcla-keynote accent=amber -->
```

| Theme | Knob | Choices |
|---|---|---|
| `dcla-keynote` | `accent` | `azure` #169fff · `amber` #ffa800 · `violet` #a452ff |
| `dcla-stage` | `accent` | the same three |
| `dcla-sunset` | `hour` | `golden` · `dusk` · `night` |
| `dcla-grid` | `density` | `sparse` · `normal` · `dense` |

The picker offers these by name and writes the value, so a deck says
`accent=amber` and gets `#ffa800`. Any colour the grammar allows still works,
so a deck can ask for one the pack never thought of.

## Notes

`dcla-keynote` and `dcla-grid` are the light themes and the only ones that set
the seven `--code-*` variables; the defaults in `base.css` are written for a
dark ground.

On a light ground a heading is never painted in the raw accent. Amber on paper
is around 1.9:1, which is unreadable, so the heading is mixed toward the ink
until all three clear the bar for large type. `dcla-stage` paints the raw colour
because near black gives it the room.

Both fonts are asked for by name and never fetched. `Barlow` is the
conference's own face and appears first in the stack; a reader without it gets
whatever condensed grotesque they already have. A theme is served to every
phone in the room, and none of them should be made to hit a font CDN.

## Licence

MIT, matching Palmcast. This pack is unofficial and not endorsed by Data Con LA.
It uses the palette published in their
[media kit](https://www.dataconla.com/doc/media-kit/) and ships **no logo or
mark of any kind**: the kit asks that the logo not be altered or recoloured, and
the surest way to honour that is not to carry it.
