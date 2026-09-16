from playwright.sync_api import sync_playwright


SYSTEM_PROMPT = """You are the browser based reasoning layer of the agent.
"""


class BrowserBrain:
    """Uses an existing logged-in Chrome session via remote debugging."""

    def __init__(self, endpoint: str = "http://127.0.0.1:9222") -> None:
        self.endpoint = endpoint
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.connect_over_cdp(endpoint)
        self.page = self.browser.contexts[0].pages[0]

    def respond(self, messages: list[dict[str, str]]) -> str:
        prompt = messages[-1]["content"]
        self.page.goto("https://chat.openai.com/")
        # TODO: selectors depend on current ChatGPT UI changes
        self.page.keyboard.type(prompt)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(5000)
        return "BrowserBrain response capture pending"
