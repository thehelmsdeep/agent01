import requests


class BrowserSessionManager:
    """Checks and manages connection to an existing Chrome session."""

    def __init__(self, endpoint: str = "http://127.0.0.1:9222"):
        self.endpoint = endpoint

    def is_available(self) -> bool:
        try:
            response = requests.get(f"{self.endpoint}/json/version", timeout=3)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def status(self) -> str:
        if self.is_available():
            return "Chrome remote session available"
        return "Chrome remote session unavailable. Start Chrome with remote debugging."
