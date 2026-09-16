# foundry

The catch-all: five well-known developer palettes, for a deck that is mostly
code. Themes only — Palmcast already ships 34 transitions, and none of these
has motion of its own to add.

```bash
palmcast --theme-dir packs/foundry/themes
```

## Themes

| Name | Palette |
|---|---|
| `foundry-dracula` | [Dracula](https://draculatheme.com) — `#282a36` under six brights. |
| `foundry-nord` | [Nord](https://www.nordtheme.com) — polar night under the aurora, the coolest ground here. |
| `foundry-gruvbox` | [Gruvbox](https://github.com/morhetz/gruvbox) — warm and retro, both grounds in one file. |
| `foundry-solarized` | [Solarized](https://ethanschoonover.com/solarized/) — the pair everyone already knows. |
| `foundry-catppuccin` | [Catppuccin](https://catppuccin.com) — all four flavours in one file. |

## Knobs

```markdown
<!-- theme: foundry-catppuccin flavor=latte -->
```

| Theme | Knob | Choices |
|---|---|---|
| `foundry-dracula` | `accent` | `pink` · `purple` · `cyan` · `green` |
| `foundry-nord` | `accent` | `frost` · `green` · `purple` · `orange` |
| `foundry-gruvbox` | `mode` | `dark` · `light` |
| `foundry-solarized` | `mode` | `dark` · `light` |
| `foundry-catppuccin` | `flavor` | `mocha` · `macchiato` · `frappe` · `latte` |

`mode` and `flavor` swap the whole palette, `color-scheme` and the seven
`--code-*` variables together, so `latte` and `light` are real light themes and
not a filter over a dark one. The first choice in each row is what the file
ships and has no `@container style()` block of its own.

## Notes

Every theme here sets all seven `--code-*` variables. That is the point of the
pack: these are syntax palettes first and deck palettes second.

**The hues are each palette's own; some of the lightnesses are not.** A slide is
read from the back of a room, not from 60cm away, and a few values that are
comfortable in an editor do not survive a projector. Where one fell below 4.5:1
against the block it is printed on, it was moved along its own hue until it
cleared — Gruvbox's red and light yellow, Nord's purple, Catppuccin latte's
green, peach and yellow, and most of Solarized, which publishes one accent set
for both grounds and needed a darker one for the light. Comments are held to
3:1 rather than 4.5:1, because every palette here de-emphasises them on purpose
and a pack of real palettes has to ship them that way.

## Licence

MIT, matching Palmcast. Dracula, Nord, Gruvbox, Solarized and Catppuccin are
each MIT-licensed and belong to their authors. This pack carries colour values
only — no code, no fonts, no assets — and is not endorsed by any of them.
