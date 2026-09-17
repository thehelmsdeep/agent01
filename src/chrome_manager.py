import os
import subprocess
import time
from pathlib import Path


class ChromeManager:
    """Starts Chrome with the user's existing profile when possible."""

    def __init__(self):
        self.chrome_paths = [
            os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
        ]

    def start(self, url="https://chatgpt.com/"):
        chrome = next((p for p in self.chrome_paths if Path(p).exists()), None)
        if not chrome:
            raise RuntimeError("Chrome executable not found")

        subprocess.Popen([
            chrome,
            "--remote-debugging-port=9222",
            url,
        ])

        time.sleep(5)
