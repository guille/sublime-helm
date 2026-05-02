import os
from pathlib import Path


def upglob(start: Path, markers: "list[str]") -> "Path | None":
    current = start.resolve()
    if current.is_file():
        current = current.parent

    current_dev = os.stat(current).st_dev
    home = Path.home().resolve()

    # Determine the ceiling: $HOME if we start at/below it, else filesystem root
    try:
        current.relative_to(home)
        ceiling = home
    except ValueError:
        ceiling = None  # No ceiling — walk all the way to root

    while True:
        for marker in markers:
            if (current / marker).exists():
                return current
        if current == ceiling:
            return None  # Hit $HOME without finding the marker
        parent = current.parent
        if parent == current:
            return None
        if os.stat(parent).st_dev != current_dev:
            return None  # Stop at filesystem boundary
        current = parent
