import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

ITEM_1 = "Sauce Labs Backpack"
ITEM_2 = "Sauce Labs Bike Light"


@pytest.mark.cart
def test_add_item_increments_cart_badge(logged_in: InventoryPage):
    assert logged_in.get_cart_count() == 0
    logged_in.add_item_to_cart(ITEM_1)
    assert logged_in.get_cart_count() == 1


@pytest.mark.cart
def test_add_two_items_cart_badge_shows_two(logged_in: InventoryPage):
    logged_in.add_item_to_cart(ITEM_1)
    logged_in.add_item_to_cart(ITEM_2)
    assert logged_in.get_cart_count() == 2


@pytest.mark.cart
def test_remove_item_decrements_cart_badge(logged_in: InventoryPage):
    logged_in.add_item_to_cart(ITEM_1)
    logged_in.remove_item_from_cart(ITEM_1)
    assert logged_in.get_cart_count() == 0


@pytest.mark.cart
def test_cart_page_shows_added_items(logged_in: InventoryPage, cart_page: CartPage):
    logged_in.add_item_to_cart(ITEM_1)
    logged_in.go_to_cart()
    assert ITEM_1 in cart_page.get_cart_items()


@pytest.mark.cart
def test_cart_page_remove_item(logged_in: InventoryPage, cart_page: CartPage):
    logged_in.add_item_to_cart(ITEM_1)
    logged_in.go_to_cart()
    cart_page.remove_item(ITEM_1)
    assert cart_page.get_item_count() == 0


@pytest.mark.cart
def test_cart_badge_absent_when_empty(logged_in: InventoryPage, page):
    assert not page.get_by_test_id("shopping-cart-badge").is_visible()
