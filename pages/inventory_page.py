class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.menu_button = "#react-burger-menu-btn"
        self.logout_link = "#logout_sidebar_link"
        self.cart_badge = ".shopping_cart_badge"
        self.add_to_cart_button = ".inventory_item button"

    async def logout(self):
        await self.page.click(self.menu_button)
        await self.page.click(self.logout_link)

    async def add_first_item_to_cart(self):
        await self.page.click(self.add_to_cart_button)

    async def is_cart_badge_visible(self):
        return await self.page.is_visible(self.cart_badge)
