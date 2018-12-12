
from xws.test.base.BaseTest import BaseTest
from xws.test.pages.ChatPage import ChatPage
from xws.test.pages.LoginPage import LoginPage


class TestLogin(BaseTest):
    def test_registered_user_can_login(self):
        loginPage = LoginPage(self.driver, self.live_server_url, self.live_server_ws_url)
        loginPage.go_to()
        loginPage.login("bot2", "secret123")
        chatPage = ChatPage(self.driver, self.live_server_url, self.live_server_ws_url)
        self.assertTrue(chatPage.is_at(), "Could not enter the chat")


    def test_registered_user_can_not_login_without_password(self):
        loginPage = LoginPage(self.driver, self.live_server_url, self.live_server_ws_url)
        loginPage.go_to()
        loginPage.login("bot2", "")
        self.assertTrue(loginPage.is_at(), "Must be on login page")


    def test_registered_user_can_not_login_with_wrong_password(self):
        loginPage = LoginPage(self.driver, self.live_server_url, self.live_server_ws_url)
        loginPage.go_to()
        loginPage.login("bot2", "this is wrong password")
        self.assertTrue(loginPage.is_at(), "Must be on login page")


    def test_not_registered_user_can_not_login(self):
        loginPage = LoginPage(self.driver, self.live_server_url, self.live_server_ws_url)
        loginPage.go_to()
        loginPage.login("no_such_user", "this is wrong password")
        self.assertTrue(loginPage.is_at(), "Must be on login page")


    def test_user_can_not_login_without_username_and_password(self):
        loginPage = LoginPage(self.driver, self.live_server_url, self.live_server_ws_url)
        loginPage.go_to()
        loginPage.login("", "")
        self.assertTrue(loginPage.is_at(), "Must be on login page")
