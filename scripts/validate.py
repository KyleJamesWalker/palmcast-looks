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
# src/styles.rs: a declaration of a knob, and the list of choices beside it.
KNOB = re.compile(r"--knob-([\w-]+)\s*:([^;}]*)")
OPTIONS = "-options"
# src/deck.rs: a knob value a deck may write, and one a look may declare.
HEX = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
NUMBER = re.compile(r"^[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?$")


def is_time(value):
    """A duration, on src/deck.rs's terms: whole milliseconds, or up to 60s."""
    if value.endswith("ms"):
        return value[:-2].isdigit()
    if not value.endswith("s") or not NUMBER.match(value[:-1]):
        return False
    return 0.0 <= float(value[:-1]) <= 60.0


def knob_value(value):
    """Whether a deck could write this, the way src/deck.rs decides it."""
    if not value or len(value) > 32:
        return False
    share = value[:-1] if value.endswith("%") else ""
    return bool(
        HEX.match(value)
        or is_time(value)
        or NUMBER.match(value)
        or (share and NUMBER.match(share))
        or NAME.match(value)
    )


def choices(value):
    """The choices a look offers, the way src/styles.rs reads the list."""
    out = []
    for entry in value.split(","):
        words = entry.split()
        if len(words) == 1:
            out.append((words[0], words[0]))
        elif len(words) == 2:
            out.append((words[0], words[1]))
    return out


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


# A colour literal outside a data URI. Anything starting `#` that is not one is
# a typo the browser drops silently, taking the declaration with it.
COLOUR = re.compile(r"#[^\s;,(){}/'\"]+")
DATA_URI = re.compile(r"url\(\s*[\"']?data:[^)]*\)", re.S)


def check_colours(css, where, failures):
    """Every `#rrggbb` in the file is one the browser will actually read.

    A stray character inside a hex value is invisible in review and silently
    drops the whole declaration, so the theme loses a colour and says nothing.
    """
    for literal in COLOUR.findall(DATA_URI.sub("", css)):
        digits = literal[1:]
        if len(digits) in (3, 4, 6, 8) and all(c in "0123456789abcdefABCDEF" for c in digits):
            continue
        # Nothing with a digit in it is an id selector, and an id selector is
        # the only other thing in a stylesheet that opens with a hash.
        if not any(c.isdigit() for c in digits):
            continue
        failures.append(f"{where}: {literal} is not a colour the browser will read")


def check_knobs(css, where, failures):
    """The knobs a look puts its name to, on the terms src/styles.rs reads them.

    A knob nobody can turn is worse than no knob: it takes a row in the picker
    and does nothing, and the file gives no sign of it.
    """
    declared = {}
    lists = {}
    for name, raw in KNOB.findall(css):
        value = raw.strip()
        target = lists if name.endswith(OPTIONS) else declared
        if name in target:
            continue
        target[name] = value

    for name, value in declared.items():
        if not NAME.match(name):
            failures.append(f"{where}: --knob-{name} is not a name the server will read")
            continue
        if not value or len(value.encode()) > 200:
            failures.append(f"{where}: --knob-{name} has no value the server will read")
        elif "var(" in value:
            failures.append(
                f"{where}: --knob-{name} holds a var(), and the server reads that as a "
                "use rather than a declaration, so the knob never reaches the picker"
            )
        elif name + OPTIONS not in lists and not knob_value(value):
            failures.append(
                f"{where}: --knob-{name} defaults to '{value}', which a deck cannot write"
            )

    for name, value in lists.items():
        of = name[: -len(OPTIONS)]
        if of not in declared:
            failures.append(f"{where}: --knob-{name} describes a knob the file never declares")
            continue
        offered = choices(value)
        if not offered:
            failures.append(f"{where}: --knob-{name} offers nothing the server can read")
            continue
        for label, choice in offered:
            if not NAME.match(label):
                failures.append(f"{where}: --knob-{name} offers '{label}', which is not a name")
            if not knob_value(choice):
                failures.append(
                    f"{where}: --knob-{name} offers '{label} {choice}', "
                    "and a deck cannot write that value"
                )
        if declared[of] not in [choice for _, choice in offered]:
            failures.append(
                f"{where}: --knob-{of} defaults to '{declared[of]}', "
                "which is not one of the choices beside it"
            )


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

    check_colours(css, where, failures)
    check_knobs(css, where, failures)

    if kind == "transitions":
        named = set(SELECTOR.findall(css))
        if named != {stem}:
            failures.append(
                f"{where}: selects data-transition={sorted(named) or 'nothing'}, "
                f"expected only '{stem}'"
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
