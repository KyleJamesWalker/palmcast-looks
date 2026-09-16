# phosphor

Four themes and three transitions for a terminal, or a talk that wishes it were
one. Monospace throughout, and a live-coding demo looks at home in any of them.

```bash
palmcast --theme-dir packs/phosphor/themes \
         --transition-dir packs/phosphor/transitions
```

## Themes

| Name | Look |
|---|---|
| `phosphor-crt` | One tube, four phosphors. Scanlines, bloom round the type, curvature falling into the corners. |
| `phosphor-teletext` | Eight saturated colours on black, a rainbow header bar, blocky caps. |
| `phosphor-c64` | Blue on blue with the lighter border, uppercase, no anti-aliasing it can avoid. |
| `phosphor-dos` | Sixteen colours and a double rule drawn round the screen. |

## Transitions

| Name | Motion |
|---|---|
| `phosphor-scanline` | A bright line runs top to bottom with the next slide behind it. |
| `phosphor-degauss` | The tube wobbles, the colour bends, and it settles. |
| `phosphor-powercut` | Down to a line, then a dot, then back out of it. |

## Knobs

```markdown
<!-- theme: phosphor-crt tube=amber scanlines=coarse -->
```

| Theme | Knob | Choices |
|---|---|---|
| `phosphor-crt` | `tube` | `green` · `amber` · `white` · `ice` |
| | `scanlines` | `fine` · `coarse` · `off` |
| `phosphor-teletext` | `page` | `news` · `sport` · `weather` |
| `phosphor-dos` | `scheme` | `edit` · `vga` · `turbo` |

`phosphor-crt` takes its whole palette from `tube`, the syntax colours
included: each one is the chosen phosphor mixed toward white or black, so a
fifth tube would be one line. `scanlines=off` is for a projector that is
already doing its own moiré.

`phosphor-c64` has no knob. It is one machine and it had one screen.

## Notes

Nothing here animates the backdrop, so there is no `prefers-reduced-motion`
block to write: the scanlines and the raster are static, and Palmcast already
swaps any transition for a cross fade.

`phosphor-c64` lightens its type. The machine drew `#7869c4` on `#40318d`,
which is about 1.8:1 and unreadable across a room; the hue is kept and the
lightness is not.

## Licence

MIT, matching Palmcast. Commodore, IBM and Ceefax are nobody's here: these are
colours and shapes recalled, not assets copied, and the pack carries no
artwork, font or ROM from any machine.
