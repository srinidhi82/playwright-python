import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.asyncio
async def test_add_to_cart(page):
    login_page = LoginPage(page)
    await login_page.goto()
    await login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    await inventory_page.add_first_item_to_cart()
    assert await inventory_page.is_cart_badge_visible()
