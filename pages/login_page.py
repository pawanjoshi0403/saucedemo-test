from .base_page import BasePage

class LoginPage(BasePage):
    @property
    def username_field(self):
        return self.page.locator('[data-test="username"]')

    @property
    def password_field(self):
        return self.page.locator('[data-test="password"]')

    def login(self, username: str, password: str):
        self.fill('[data-test="username"]', username)
        self.fill('[data-test="password"]', password)
        self.click('[data-test="login-button"]')

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")  # Navigate to the login page

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
