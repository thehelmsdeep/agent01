import subprocess
import os


class ChromeLauncher:
    def __init__(self, chrome_path=None, profile_dir=None, port=9222):
        self.chrome_path = chrome_path or os.getenv("CHROME_PATH")
        self.profile_dir = profile_dir or os.getenv("CHROME_PROFILE")
        self.port = port

    def launch(self):
        if not self.chrome_path:
            raise RuntimeError("CHROME_PATH is not configured")

        command = [
            self.chrome_path,
            f"--remote-debugging-port={self.port}",
        ]

        if self.profile_dir:
            command.append(f"--user-data-dir={self.profile_dir}")

        subprocess.Popen(command)
        return True
