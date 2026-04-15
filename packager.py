import os
from pathlib import Path

import sublime_plugin


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


class HelmPackageBuildCommand(sublime_plugin.WindowCommand):
    def is_enabled(self):
        return True

    def run(self):
        variables = self.window.extract_variables()
        file_dir = variables["file_path"]
        working_dir = (
            variables.get("project_path") or variables.get("folder") or file_dir
        )
        if pkg_root := upglob(Path(file_dir), ["Chart.yaml"]):
            print(pkg_root)
            self.window.run_command(
                "exec",
                {"cmd": ["helm", "package", str(pkg_root)], "working_dir": working_dir},
            )
            return
        print("Not found")
        return
