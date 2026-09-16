# seasonal

Three themes and two transitions for the few weeks a year they suit. The
thinnest pack here, and it knows it.

```bash
palmcast --theme-dir packs/seasonal/themes \
         --transition-dir packs/seasonal/transitions
```

## Themes

| Name | Look |
|---|---|
| `seasonal-hallow` | Orange over violet, a low moon behind the hill, bats crossing it. |
| `seasonal-frost` | Snow coming down over a blue hour, in three times of day. |
| `seasonal-bloom` | **The light one.** Petals off the tree on a bright day. |

## Transitions

| Name | Motion |
|---|---|
| `seasonal-flurry` | Both slides turn a little as one is carried off and the other drifts in. |
| `seasonal-carve` | The next slide opens through a jagged hole cut in the middle. |

## Knobs

```markdown
<!-- theme: seasonal-frost hour=day drift=still -->
```

| Theme | Knob | Choices |
|---|---|---|
| `seasonal-hallow` | `mood` | `pumpkin` · `witch` · `blood` |
| `seasonal-frost` | `hour` | `night` · `dusk` · `day` |
| `seasonal-bloom` | `mood` | `blossom` · `meadow` · `wisteria` |
| all three | `drift` | `calm` · `normal` · `brisk` · `still` |

`drift` works the same way here as in `townsville`: it is the time the backdrop
takes to cross itself, and `still` stops it. `seasonal-frost hour=day` is a
light theme; the other two `hour` values are not.

## Notes

`seasonal-frost` and `seasonal-bloom` set the seven `--code-*` variables,
because either can end up on a light ground. `seasonal-hallow` never does and
inherits the defaults in `base.css`.

Every drifting backdrop stops for a reader who asked for less motion.

## Licence

MIT, matching Palmcast.
