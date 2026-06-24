import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.inventory
def test_inventory_shows_six_items(logged_in: InventoryPage):
    assert logged_in.get_item_count() == 6


@pytest.mark.inventory
def test_sort_by_name_asc(logged_in: InventoryPage):
    logged_in.sort_by("az")
    names = logged_in.get_item_names()
    assert names == sorted(names)


@pytest.mark.inventory
def test_sort_by_name_desc(logged_in: InventoryPage):
    logged_in.sort_by("za")
    names = logged_in.get_item_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.inventory
def test_sort_by_price_asc(logged_in: InventoryPage):
    logged_in.sort_by("lohi")
    prices = logged_in.get_item_prices()
    assert prices == sorted(prices)


@pytest.mark.inventory
def test_sort_by_price_desc(logged_in: InventoryPage):
    logged_in.sort_by("hilo")
    prices = logged_in.get_item_prices()
    assert prices == sorted(prices, reverse=True)
