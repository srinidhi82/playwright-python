import pytest
from pages.login_page import LoginPage

@pytest.mark.asyncio
async def test_valid_login(page):
    login_page = LoginPage(page)
    await login_page.goto()
    await login_page.login("standard_user", "secret_sauce")
    assert await login_page.is_logged_in()

@pytest.mark.asyncio
async def test_invalid_login(page):
    login_page = LoginPage(page)
    await login_page.goto()
    await login_page.login("invalid_user", "invalid_pass")
    assert await login_page.login_error_displayed()
