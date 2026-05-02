from pathlib import Path

import sublime_plugin

from .shared import upglob


class HelmLintBuildCommand(sublime_plugin.WindowCommand):
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
                {"cmd": ["helm", "lint", str(pkg_root)], "working_dir": working_dir},
            )
            return
        print("Not found")
        return
