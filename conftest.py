import pytest_asyncio
from playwright.async_api import async_playwright
from pages.login_page import LoginPage

@pytest_asyncio.fixture
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # <--- changed here
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await browser.close()

@pytest_asyncio.fixture
async def login(page):
    async def _login(username, password):
        login_page = LoginPage(page)
        await login_page.goto()
        await login_page.login(username, password)
    return _login

    
