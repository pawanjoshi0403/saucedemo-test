from .base_page import BasePage

class InventoryPage(BasePage):
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    INVENTORY_ITEMS = "[data-test='inventory-item']"
    ITEM_PRICE = "[data-test='inventory-item-price']"
    ITEM_NAME = "[data-test='inventory-item-name']"
    ADD_TO_CART_BTN = "[data-test='add-to-cart-sauce-labs-backpack']"
    ADD_TO_CART_BTN_2 = "[data-test='add-to-cart-sauce-labs-bike-light']"

    def sort_products(self, sort_type: str):
        self.page.select_option(self.SORT_DROPDOWN, sort_type)

    def get_product_prices(self):
        return [float(price.inner_text().replace('$', ''))
                for price in self.page.locator(self.ITEM_PRICE).all()]

    def get_product_names(self):
        return [el.inner_text() for el in self.page.locator(self.ITEM_NAME).all()]

    def add_first_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BTN).first.click()

    def add_second_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BTN_2).first.click()

    def get_inventory_count(self):
        return self.page.locator(self.INVENTORY_ITEMS).count()

    def get_product_image_urls(self):
        return [img.get_attribute("src")
                for img in self.page.locator(".inventory_item_img img").all()]
