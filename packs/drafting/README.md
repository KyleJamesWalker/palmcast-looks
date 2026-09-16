# drafting

Four themes and two transitions on paper. The counterweight to the rest of this
repository, which is mostly dark: three of these four are for a room with the
lights on, and the fourth prints on white if you ask it to.

```bash
palmcast --theme-dir packs/drafting/themes \
         --transition-dir packs/drafting/transitions
```

## Themes

| Name | Look |
|---|---|
| `drafting-blueprint` | Cyan on navy, a grid at two pitches, a plotter border and title block. |
| `drafting-graph` | Fine graph paper and a pencil-grey hand. The quietest theme in the repository. |
| `drafting-legal` | A yellow pad: blue rules, a red margin, punch holes, blue-black ink. |
| `drafting-typewriter` | Off-white stock, monospace end to end, one ribbon colour for the whole page. |

## Transitions

| Name | Motion |
|---|---|
| `drafting-pageturn` | The sheet lifts at the corner and goes over, uncovering the next. |
| `drafting-erase` | Rubbed out from the left with a soft edge, the next already underneath. |

## Knobs

```markdown
<!-- theme: drafting-blueprint stock=whiteprint -->
```

| Theme | Knob | Choices |
|---|---|---|
| `drafting-blueprint` | `stock` | `blueprint` · `whiteprint` · `sepia` |
| `drafting-graph` | `grid` | `fine` · `normal` · `coarse` |
| `drafting-typewriter` | `ribbon` | `black` · `blue` · `red` |

`drafting-legal` has no knob. A legal pad is yellow.

`stock` is the one knob here that changes `color-scheme`: `blueprint` is the
dark one and the other two are prints of the same drawing on light stock.

`drafting-typewriter` takes its whole page from `ribbon`, syntax colours
included — each is the ribbon mixed toward the paper, which is what a
typewriter actually gives you.

## Notes

All four set the seven `--code-*` variables. The defaults in `base.css` are
written for a dark ground and are unreadable on any of this stock.

Nothing animates the backdrop, so there is no `prefers-reduced-motion` block:
the grids, the rules and the paper grain are static, and Palmcast already swaps
any transition for a cross fade.

`drafting-erase` masks `::view-transition-old(palmcast-surface)` rather than the
new one, because the slide being rubbed out is the one doing the moving. That is
also why it sets `--transition-lift: 1`.

## Licence

MIT, matching Palmcast.
