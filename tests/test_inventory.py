import pytest
from pages.login_page import LoginPage

@pytest.fixture
def logged_in_page(page):
    """Fixture to log in before each test."""
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    return page

def test_sort_low_to_high(logged_in_page):
    logged_in_page.select_option(".product_sort_container", "lohi")
    prices = [float(p.inner_text().replace('$', ''))
              for p in logged_in_page.locator(".inventory_item_price").all()]
    assert prices == sorted(prices)

def test_sort_high_to_low(logged_in_page):
    logged_in_page.select_option(".product_sort_container", "hilo")
    prices = [float(p.inner_text().replace('$', ''))
              for p in logged_in_page.locator(".inventory_item_price").all()]
    assert prices == sorted(prices, reverse=True)


def test_product_display(logged_in_page):
    assert logged_in_page.locator(".inventory_item").count() == 6