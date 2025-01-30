import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# def test_slow_execution(page):
#     page.set_default_timeout(10000)

@pytest.fixture
def logged_in_page(page):
    """Fixture to log in before each test."""
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    return page

def test_product_display(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    assert inventory_page.get_inventory_count() == 6
    images_urls = inventory_page.get_product_image_urls()

    expected_images = [
        "/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg",
        "/static/media/bike-light-1200x1500.37c843b0.jpg",
        "/static/media/bolt-shirt-1200x1500.c2599ac5.jpg",
        "/static/media/sauce-pullover-1200x1500.51d7ffaf.jpg",
        "/static/media/red-onesie-1200x1500.2ec615b2.jpg",
        "/static/media/red-tatt-1200x1500.30dadef4.jpg"
    ]

    # Assert that the images displayed are incorrect
    assert images_urls == expected_images


def test_product_details(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    first_item_name = inventory_page.get_product_names()[0]
    assert first_item_name.strip() != ""

def test_incorrect_product_ui(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("visual_user", "secret_sauce")

    images_urls = inventory_page.get_product_image_urls()

    expected_images = [
        "/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg",
        "/static/media/bike-light-1200x1500.37c843b0.jpg",
        "/static/media/bolt-shirt-1200x1500.c2599ac5.jpg",
        "/static/media/sauce-pullover-1200x1500.51d7ffaf.jpg"
        "/static/media/red-onesie-1200x1500.2ec615b2.jpg"
        "/static/media/red-tatt-1200x1500.30dadef4.jpg"
    ]

    # Assert that the images displayed are incorrect
    assert images_urls != expected_images