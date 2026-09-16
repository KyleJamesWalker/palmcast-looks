# palmcast-looks

Themes and transitions for [Palmcast](https://github.com/KyleJamesWalker/Palmcast),
grouped into packs. Seven packs ship here: thirty themes and twenty-two
transitions, from a conference palette to a CRT.

## Overview

A pack is a directory holding `themes/` and `transitions/`, both full of plain
CSS. Palmcast reads them at startup, and a deck names one by its file name.
Nothing here is a Palmcast fork or a plugin.

## Install

Palmcast takes one directory of themes and one of transitions. `assemble` builds
that pair from the packs you name, or from every pack if you name none.

```bash
git clone https://github.com/KyleJamesWalker/palmcast-looks.git
cd palmcast-looks
./scripts/assemble.sh foundry drafting
```

Name as many as you want, or none for all seven.

## Usage

Start Palmcast against the two assembled directories.

```bash
palmcast --theme-dir build/themes --transition-dir build/transitions
```

A deck then asks for a look by name.

```markdown
<!-- theme: townsville-powerpuff -->
<!-- transition: townsville-heart -->
```

Point the flags straight at one pack to skip the build step.

```bash
palmcast --theme-dir packs/townsville/themes \
         --transition-dir packs/townsville/transitions
```

## Packs

Every look is prefixed with its pack name; the short names below are what
follows the prefix.

| Pack | Themes | Transitions |
|---|---|---|
| [townsville](packs/townsville) | `powerpuff` `blossom` `bubbles` `buttercup` `mojo` | `heart` `pow` `chemical-x` `sugar-spice` `flyover` `hotline` |
| [gotham](packs/gotham) | `knight` `signal` `arkham` `joker` `gazette` | `batarang` `grapple` `blackout` `searchlight` `smoke` `gargoyle` |
| [dcla](packs/dcla) | `keynote` `stage` `sunset` `grid` | `wipe` `plot` `freeway` |
| [foundry](packs/foundry) | `dracula` `nord` `gruvbox` `solarized` `catppuccin` | — |
| [phosphor](packs/phosphor) | `crt` `teletext` `c64` `dos` | `scanline` `degauss` `powercut` |
| [drafting](packs/drafting) | `blueprint` `graph` `legal` `typewriter` | `pageturn` `erase` |
| [seasonal](packs/seasonal) | `hallow` `frost` `bloom` | `flurry` `carve` |

`foundry` ships no transitions on purpose: Palmcast already serves 34, and a
pack of syntax palettes has no motion of its own to add. Nine of the thirty
themes are for a room with the lights on — `gotham-gazette`, `dcla-keynote`,
`dcla-grid`, all four in `drafting`, `seasonal-bloom`, `townsville-bubbles` —
and `foundry` and `seasonal-frost` reach several more through a knob.

## Write a pack

Add `packs/<pack>/themes/` and `packs/<pack>/transitions/`, then run
`make check`. Palmcast's own
[themes and transitions](https://github.com/KyleJamesWalker/Palmcast#add-your-own-themes-and-transitions)
document what belongs inside a file. Five rules are specific to this repository,
and `scripts/validate.py` enforces all five.

**Prefix every file name with the pack name.** Palmcast keys a look by its file
name. Two packs that both ship `heart.css` collapse into one look, and the last
one assembled wins. The prefix also sorts a pack together in both pickers.

**Namespace every `@keyframes` name the same way.** A browser holds one keyframe
namespace, and Palmcast loads a stylesheet per transition the deck names. Write
`palmcast-in-townsville-heart`, not `palmcast-in-heart`. `palmcast-hold` is the
exception, because Palmcast defines that one for everyone.

**Open each file with a comment.** The picker reads the first sentence or two as
the description. A file without one shows its name alone.

**Keep that first sentence short.** The picker cuts `name — description` to 72
characters, so a longer file name leaves less room. `townsville-sugar-spice`
leaves 50.

**Offer a mood, not a palette.** A look declares a knob by naming a
`--knob-<name>` custom property and using it; the value in the file is the
default, so nothing can drift. Prefer one preset that swaps a coordinated set
over two colours a deck has to match by eye:

```css
.viewer, .stage {
  --knob-mood: raspberry;
  --knob-mood-options: raspberry, cherry, plum;
  --accent: var(--lit-accent, #ff4fa3);
}

@container style(--knob-mood: cherry) {
  .viewer, .stage { --lit-heading: #ff2d6a; --lit-accent: #ffb3c9; }
}
```

The default gets no block of its own — it is the `var(…, fallback)`, so a
browser without style queries shows what the file ships. Offer a preset *or* a
colour for the same thing, never both: the query writes closer to the slide and
silently wins. Every choice has to be a value a deck can write — a colour, a
time, a number, a share, or a bare word — or it is a row in the picker that
refuses the whole directive.

A transition can declare one too, after the duration, but a theme's knobs and a
transition's share one namespace on the root, and a Palmcast older than the
`cover distance=…` example ignores a transition's entirely. No pack here ships
one.

## Check

```bash
make check      # validate every pack
make build      # assemble every pack into build/
make clean
```

## License

MIT, matching Palmcast. No pack here carries artwork, a font, audio or a logo:
every one ships colors, shapes and keyframes and nothing else, and none fetches
anything over the network. Where a pack is fan work or uses somebody's published
palette, its own README says whose and on what terms — see
[townsville](packs/townsville), [gotham](packs/gotham), [dcla](packs/dcla) and
[foundry](packs/foundry).
