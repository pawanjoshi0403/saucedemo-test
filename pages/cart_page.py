from .base_page import BasePage


class CartPage(BasePage):
    CART_BADGE = ".shopping_cart_badge"
    CHECKOUT_BUTTON = "#checkout"
    CART_ITEM = ".cart_item"
    REMOVE_BUTTON = "button:has-text('Remove')"

    def get_cart_count(self):
        return self.page.locator(self.CART_BADGE).inner_text()

    def open_cart(self):
        self.page.locator(self.CART_BADGE).wait_for(state="visible", timeout=5000)
        self.click(self.CART_BADGE)

    def proceed_to_checkout(self):
        self.page.locator("#checkout").wait_for(state="visible", timeout=5000)
        self.click(self.CHECKOUT_BUTTON)

    def remove_item_from_cart(self):
        self.click(self.REMOVE_BUTTON)