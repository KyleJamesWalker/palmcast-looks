#!/usr/bin/env python3
"""Check every pack against what Palmcast will accept and what a picker shows.

Palmcast keys a look by its file name, and an instance may serve several packs
from one directory. Everything below exists so two packs never collide and no
look arrives in the picker without a description.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"

# src/deck.rs: lowercase letters, digits and dashes, 32 bytes at most.
NAME = re.compile(r"^[a-z0-9-]{1,32}$")
# web/looks.js cuts `name — about` to this many characters.
PICKER_WIDTH = 72
KEYFRAMES = re.compile(r"@keyframes\s+([\w-]+)")
SELECTOR = re.compile(r'html\[data-transition="([^"]+)"\]')
# base.css defines this one for every transition to use.
SHARED_KEYFRAMES = {"palmcast-hold"}


def about(css):
    """The opening comment, the way src/styles.rs reads it."""
    body = css.lstrip()
    if not body.startswith("/*") or body.startswith("/**/"):
        return ""
    comment = body[2:].split("*/")[0]
    flat = " ".join(comment.split())
    out = ""
    for sentence in flat.split(". "):
        piece = sentence + ". "
        if out and (len(out) >= 40 or len(out) + len(piece) > 140):
            break
        out += piece
    return out[:140].strip()


def check_file(path, pack, kind, failures):
    stem = path.stem
    where = path.relative_to(ROOT)

    if not NAME.match(stem):
        failures.append(f"{where}: a name is lowercase letters, digits and dashes, 32 at most")
        return
    if not stem.startswith(f"{pack}-"):
        failures.append(f"{where}: name must start with '{pack}-' so the pack sorts together")
        return

    css = path.read_text()

    summary = about(css)
    if not summary:
        failures.append(f"{where}: no opening /* comment, so the picker shows no description")
    elif len(summary) > PICKER_WIDTH - len(stem):
        room = PICKER_WIDTH - len(stem)
        failures.append(
            f"{where}: the picker cuts the description to {room} characters, "
            f"and the first sentence is {len(summary)}"
        )

    for name in KEYFRAMES.findall(css):
        if name in SHARED_KEYFRAMES:
            continue
        if not name.startswith(f"palmcast-") or pack not in name:
            failures.append(
                f"{where}: @keyframes {name} must be named palmcast-…-{pack}-… "
                "because every loaded transition shares one namespace"
            )

    if kind == "transitions":
        named = SELECTOR.findall(css)
        if named != [stem]:
            failures.append(
                f"{where}: selects data-transition={named or 'nothing'}, expected ['{stem}']"
            )


def main():
    if not PACKS.is_dir():
        sys.exit(f"no packs directory at {PACKS}")

    failures = []
    seen = {}
    packs = sorted(p for p in PACKS.iterdir() if p.is_dir())

    for pack_dir in packs:
        pack = pack_dir.name
        if not NAME.match(pack):
            failures.append(f"packs/{pack}: a pack name is lowercase letters, digits and dashes")
            continue
        for kind in ("themes", "transitions"):
            for path in sorted((pack_dir / kind).glob("*.css")):
                key = (kind, path.stem)
                if key in seen:
                    failures.append(f"{path.relative_to(ROOT)}: name already taken by {seen[key]}")
                seen[key] = str(path.relative_to(ROOT))
                check_file(path, pack, kind, failures)

    for line in failures:
        print(f"error: {line}")

    counted = f"{len(packs)} pack(s), {len(seen)} look(s)"
    if failures:
        sys.exit(f"{counted}, {len(failures)} problem(s)")
    print(f"ok: {counted}")


if __name__ == "__main__":
    main()
