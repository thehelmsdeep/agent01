import os
import subprocess


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
            profile_path = os.path.normpath(self.profile_dir)
            profile_name = os.path.basename(profile_path)

            # Chrome expects --user-data-dir to point to the parent
            # "User Data" directory, while the selected profile is
            # specified separately with --profile-directory.
            if profile_name.lower() == "default":
                user_data_dir = os.path.dirname(profile_path)
                command.append(f"--user-data-dir={user_data_dir}")
                command.append("--profile-directory=Default")
            else:
                command.append(f"--user-data-dir={profile_path}")

        subprocess.Popen(command)
        return True
