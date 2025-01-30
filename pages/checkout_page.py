from .base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = "[data-test='firstName']"
    LAST_NAME_INPUT = "[data-test='lastName']"
    ZIP_INPUT = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"
    FINISH_BUTTON = "[data-test='finish']"
    TOTAL_AMOUNT = "[data-test='total-label']"
    CONFIRMATION_MESSAGE = "[data-test='complete-header']"
    ERROR_MESSAGE = "[data-test='error']"

    def fill_shipping_info(self, first_name: str, last_name: str, zip_code: str):
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.ZIP_INPUT, zip_code)
        self.click(self.CONTINUE_BUTTON)

    def complete_checkout(self):
        self.click(self.FINISH_BUTTON)

    def get_total_amount(self):
        return self.get_text(self.TOTAL_AMOUNT)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)