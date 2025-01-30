from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


def test_logout(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    logout_page = LogoutPage(page)

    login_page.login("standard_user", "secret_sauce")
    logout_page.logout()
    logout_page.wait_for_url("https://www.saucedemo.com/")
    assert "https://www.saucedemo.com/" in page.url