from playwright.sync_api import sync_playwright

from .chrome_manager import ChromeManager


class BrowserBrain:
    """Uses local Chrome session for ChatGPT Web."""

    def __init__(self, endpoint: str = "http://127.0.0.1:9222") -> None:
        self.endpoint = endpoint
        self.playwright = sync_playwright().start()

        try:
            self.browser = self.playwright.chromium.connect_over_cdp(endpoint)
        except Exception:
            ChromeManager().start()
            self.browser = self.playwright.chromium.connect_over_cdp(endpoint)

        if not self.browser.contexts:
            raise RuntimeError("No browser context found")

        if not self.browser.contexts[0].pages:
            self.page = self.browser.contexts[0].new_page()
        else:
            self.page = self.browser.contexts[0].pages[0]

    def respond(self, messages: list[dict[str, str]]) -> str:
        prompt = messages[-1]["content"]

        self.page.goto("https://chatgpt.com/")
        self.page.wait_for_timeout(5000)

        self.page.keyboard.type(prompt)
        self.page.keyboard.press("Enter")

        return self._wait_for_response()

    def _wait_for_response(self) -> str:
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
