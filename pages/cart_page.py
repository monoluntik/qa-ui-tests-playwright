from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_test_id("checkout")
        self.continue_shopping = page.get_by_test_id("continue-shopping")

    def get_cart_items(self) -> list[str]:
        return self.page.get_by_test_id("inventory-item-name").all_inner_texts()

    def get_item_count(self) -> int:
        return self.page.get_by_test_id("cart-item").count()

    def remove_item(self, item_name: str):
        slug = item_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        self.page.get_by_test_id(f"remove-{slug}").click()

    def proceed_to_checkout(self):
        self.checkout_button.click()
