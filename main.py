#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea that
sounds like a joke until the business logic lands: a breakup-ghosting
service. The absurd premise (paying strangers to dump your ex) turns
real the moment the payer and the price appear.
"""

import os

PITCH = (
    "Our startup ghosts your ex for you: we write the breakup text, "
    "block their number, and mail back their hoodie, because people "
    "pay $30 to skip the one conversation they dread most."
)


def main() -> None:
    # Gate self-check: the bounty only judges 1-200 character entries.
    assert 1 <= len(PITCH) <= 200, f"pitch is {len(PITCH)} chars"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
