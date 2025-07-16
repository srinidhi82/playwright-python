class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.inventory_container = "#inventory_container"
        self.error_message = "[data-test='error']"

    async def goto(self):
        await self.page.goto("https://www.saucedemo.com")

    async def login(self, username, password):
        await self.page.fill(self.username_input, username)
        await self.page.fill(self.password_input, password)
        await self.page.click(self.login_button)

    async def is_logged_in(self):
        return await self.page.is_visible(self.inventory_container)

    async def login_error_displayed(self):
        return await self.page.is_visible(self.error_message)
