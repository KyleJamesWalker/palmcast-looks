# palmcast-looks

Themes and transitions for [Palmcast](https://github.com/KyleJamesWalker/Palmcast),
grouped into packs. One pack ships here today: `townsville`, five themes and six
transitions inspired by The Powerpuff Girls.

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
./scripts/assemble.sh townsville
```

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

| Pack | Themes | Transitions |
|---|---|---|
| [townsville](packs/townsville) | `powerpuff` `blossom` `bubbles` `buttercup` `mojo` | `heart` `pow` `chemical-x` `sugar-spice` `flyover` `hotline` |

## Write a pack

Add `packs/<pack>/themes/` and `packs/<pack>/transitions/`, then run
`make check`. Palmcast's own
[themes and transitions](https://github.com/KyleJamesWalker/Palmcast#add-your-own-themes-and-transitions)
document what belongs inside a file. Four rules are specific to this repository,
and `scripts/validate.py` enforces all four.

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

## Check

```bash
make check      # validate every pack
make build      # assemble every pack into build/
make clean
```

## License

MIT, matching Palmcast. Cartoon Network owns The Powerpuff Girls and its
characters. The `townsville` pack is unofficial fan work: it ships colors,
shapes and keyframes, and carries no artwork, font or audio from the show.
