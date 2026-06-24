import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

ITEM = "Sauce Labs Backpack"


def _go_to_checkout_step1(logged_in, cart_page, checkout_page):
    logged_in.add_item_to_cart(ITEM)
    logged_in.go_to_cart()
    cart_page.proceed_to_checkout()


@pytest.mark.checkout
def test_checkout_happy_path(
    logged_in: InventoryPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage,
):
    _go_to_checkout_step1(logged_in, cart_page, checkout_page)
    checkout_page.fill_info("John", "Doe", "12345")
    checkout_page.click_continue()
    checkout_page.click_finish()
    assert "Thank you" in checkout_page.get_complete_header()


@pytest.mark.checkout
def test_checkout_overview_shows_total(
    logged_in: InventoryPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage,
):
    _go_to_checkout_step1(logged_in, cart_page, checkout_page)
    checkout_page.fill_info("Jane", "Smith", "99999")
    checkout_page.click_continue()
    assert "Total" in checkout_page.get_summary_total()


@pytest.mark.checkout
def test_checkout_empty_first_name_shows_error(
    logged_in: InventoryPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage,
):
    _go_to_checkout_step1(logged_in, cart_page, checkout_page)
    checkout_page.fill_info("", "Doe", "12345")
    checkout_page.click_continue()
    assert checkout_page.is_error_visible()
    assert "first name is required" in checkout_page.get_error_text().lower()


@pytest.mark.checkout
def test_checkout_empty_last_name_shows_error(
    logged_in: InventoryPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage,
):
    _go_to_checkout_step1(logged_in, cart_page, checkout_page)
    checkout_page.fill_info("John", "", "12345")
    checkout_page.click_continue()
    assert checkout_page.is_error_visible()
    assert "last name is required" in checkout_page.get_error_text().lower()


@pytest.mark.checkout
def test_checkout_empty_postal_code_shows_error(
    logged_in: InventoryPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage,
):
    _go_to_checkout_step1(logged_in, cart_page, checkout_page)
    checkout_page.fill_info("John", "Doe", "")
    checkout_page.click_continue()
    assert checkout_page.is_error_visible()
    assert "postal code is required" in checkout_page.get_error_text().lower()
