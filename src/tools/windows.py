import subprocess

from .base import ToolResult


class OpenAppTool:
    name = "open_app"
    description = "Open a Windows application by executable name."

    def run(self, app: str, **kwargs) -> ToolResult:
        try:
            subprocess.Popen(app)
            return ToolResult(True, f"Opened {app}")
        except Exception as exc:
            return ToolResult(False, str(exc))


class OpenUrlTool:
    name = "open_url"
    description = "Open a URL in the default browser."

    def run(self, url: str, **kwargs) -> ToolResult:
        try:
            subprocess.Popen(["start", url], shell=True)
            return ToolResult(True, f"Opened {url}")
        except Exception as exc:
            return ToolResult(False, str(exc))
