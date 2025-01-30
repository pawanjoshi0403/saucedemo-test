import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", "inventory"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("invalid_user", "wrong_pass", "Epic sadface: Username and password do not match any user in this service"),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
])
def test_login(page, username, password, expected):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login(username, password)

    if "Epic sadface" in expected:
        assert page.locator("[data-test='error']").inner_text() == expected
    else:
        assert "/inventory.html" in page.url