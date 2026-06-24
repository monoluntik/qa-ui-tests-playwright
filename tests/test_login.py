import pytest
from pages.login_page import LoginPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


@pytest.mark.login
def test_login_standard_user_success(login_page: LoginPage, page):
    login_page.login(VALID_USER, VALID_PASS)
    assert page.url == "https://www.saucedemo.com/inventory.html"


@pytest.mark.login
def test_login_locked_out_user(login_page: LoginPage):
    login_page.login("locked_out_user", VALID_PASS)
    assert login_page.is_error_visible()
    assert "locked out" in login_page.get_error_text().lower()


@pytest.mark.login
def test_login_wrong_password(login_page: LoginPage):
    login_page.login(VALID_USER, "wrong_password")
    assert login_page.is_error_visible()
    assert "username and password do not match" in login_page.get_error_text().lower()


@pytest.mark.login
def test_login_empty_username(login_page: LoginPage):
    login_page.login("", VALID_PASS)
    assert login_page.is_error_visible()
    assert "username is required" in login_page.get_error_text().lower()


@pytest.mark.login
def test_login_empty_password(login_page: LoginPage):
    login_page.login(VALID_USER, "")
    assert login_page.is_error_visible()
    assert "password is required" in login_page.get_error_text().lower()


@pytest.mark.login
def test_login_both_fields_empty(login_page: LoginPage):
    login_page.login("", "")
    assert login_page.is_error_visible()
