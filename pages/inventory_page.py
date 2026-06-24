from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_dropdown = page.get_by_test_id("product-sort-container")
        self.cart_badge = page.get_by_test_id("shopping-cart-badge")
        self.cart_link = page.get_by_test_id("shopping-cart-link")

    def get_item_names(self) -> list[str]:
        return self.page.get_by_test_id("inventory-item-name").all_inner_texts()

    def get_item_prices(self) -> list[float]:
        texts = self.page.get_by_test_id("inventory-item-price").all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)

    def add_item_to_cart(self, item_name: str):
        slug = item_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        self.page.get_by_test_id(f"add-to-cart-{slug}").click()

    def remove_item_from_cart(self, item_name: str):
        slug = item_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        self.page.get_by_test_id(f"remove-{slug}").click()

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def go_to_cart(self):
        self.cart_link.click()

    def get_item_count(self) -> int:
        return self.page.get_by_test_id("inventory-item").count()
