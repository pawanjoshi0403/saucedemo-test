from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 5000

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, text):
        self.page.fill(selector, text)

    def get_text(self, selector):
        return self.page.locator(selector).inner_text()

    def wait_for_url(self, url):
        self.page.wait_for_url(url)