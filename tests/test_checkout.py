import pytest
import re
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def logged_in_page(page):
    """Fixture to log in before each test."""
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    return page

def test_checkout_process(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_first_item_to_cart()
    cart_page.open_cart()
    cart_page.proceed_to_checkout()

    # Fill shipping info
    checkout_page.fill_shipping_info("John", "Doe", "12345")
    assert re.search(r"Total: \$\d+\.\d{2}", checkout_page.get_total_amount())
    checkout_page.complete_checkout()

    # Verify
    assert "Thank you for your order!" in checkout_page.get_confirmation_message()



def test_checkout_with_missing_info(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_first_item_to_cart()
    cart_page.open_cart()
    cart_page.proceed_to_checkout()

    # Try to continue without info
    checkout_page.continue_checkout()
    assert "Error: First Name is required" in checkout_page.get_error_message()