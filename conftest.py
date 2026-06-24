import pytest
from playwright.sync_api import Page, Playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="session", autouse=True)
def set_test_id_attribute(playwright: Playwright):
    # saucedemo использует data-test, а не data-testid
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    lp = LoginPage(page)
    lp.open()
    return lp


@pytest.fixture
def logged_in(page: Page) -> InventoryPage:
    lp = LoginPage(page)
    lp.open()
    lp.login(STANDARD_USER, PASSWORD)
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)
