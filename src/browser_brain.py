from playwright.sync_api import sync_playwright


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
        self.page.wait_for_timeout(3000)

        self.page.keyboard.type(prompt)
        self.page.keyboard.press("Enter")

        response = self._wait_for_response()
        return response

    def _wait_for_response(self) -> str:
        """Basic response extraction.

        ChatGPT UI selectors can change, so this is intentionally isolated
        and can be updated without changing Agent Core.
        """

        self.page.wait_for_timeout(5000)

        selectors = [
            "div[data-message-author-role='assistant']",
            "article[data-testid]",
        ]

        for selector in selectors:
            elements = self.page.locator(selector)
            if elements.count() > 0:
                text = elements.last.inner_text()
                if text.strip():
                    return text.strip()

        return "No response extracted from browser yet"
