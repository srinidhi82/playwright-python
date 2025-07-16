import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.asyncio
async def test_logout(page):
    login_page = LoginPage(page)
    await login_page.goto()
    await login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    await inventory_page.logout()
    assert await page.is_visible("#login-button")
