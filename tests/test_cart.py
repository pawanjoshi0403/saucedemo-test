import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def logged_in_page(page):
    """Fixture to handle login before each test."""
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    return page

def test_add_to_cart_and_checkout(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    # Add item
    inventory_page.add_first_item_to_cart()
    assert logged_in_page.locator(".shopping_cart_badge").text_content() == "1"

    # Proceed to checkout
    cart_page.open_cart()
    cart_page.proceed_to_checkout()

    # Fill details using POM methods
    checkout_page.fill_shipping_info("John", "Doe", "12345")
    assert "Total: $32.39" in checkout_page.get_total_amount()

    # Complete checkout
    checkout_page.complete_checkout()
    assert "Thank you for your order!" in logged_in_page.locator("[data-test='complete-header']").text_content()

def test_remove_from_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)

    # Add and remove item
    inventory_page.add_first_item_to_cart()
    cart_page.remove_item_from_cart()

    # Assert cart is empty
    assert not logged_in_page.locator(".shopping_cart_badge").is_visible()

def test_add_multiple_products_to_cart_and_checkout(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    # Add item
    inventory_page.add_first_item_to_cart()
    inventory_page.add_second_item_to_cart()
    assert logged_in_page.locator(".shopping_cart_badge").text_content() == "2"

    # Proceed to checkout
    cart_page.open_cart()
    cart_page.proceed_to_checkout()

    # Fill details using POM methods
    checkout_page.fill_shipping_info("John", "Doe", "12345")
    assert "Total: $43.18" in checkout_page.get_total_amount()

    # Complete checkout
    checkout_page.complete_checkout()
    assert "Thank you for your order!" in logged_in_page.locator("[data-test='complete-header']").text_content()