from .base_page import BasePage

class LogoutPage(BasePage):
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)