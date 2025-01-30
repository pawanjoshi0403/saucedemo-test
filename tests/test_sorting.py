import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def logged_in_page(page):
    """Fixture to log in before each test."""
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    return page

def test_sort_low_to_high(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.sort_products("lohi")
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices)


def test_sort_high_to_low(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.sort_products("hilo")
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices, reverse=True)


def test_sort_a_to_z(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    names = inventory_page.get_product_names()
    assert names == sorted(names)


def test_sort_z_to_a(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.sort_products("za")
    names = inventory_page.get_product_names()
    assert names == sorted(names, reverse=True)