from xws.test.base.BaseTest import BaseTest
from xws.test.pages.ChatPage import ChatPage
from xws.test.pages.LoginPage import LoginPage


class TestLogin(BaseTest):

    def setUp(self):
        super().setUp()
        self.loginPage = LoginPage()
        self.loginPage.go_to()


    def test_registered_user_can_login(self):
        self.loginPage.login("bot2", "secret123")
        self.assertTrue(ChatPage().is_at(), "Could not enter the chat")


    def test_registered_user_can_not_login_without_password(self):
        self.loginPage.login("bot2", "")
        self.assertTrue(self.loginPage.is_at(), "Must be on login page")


    def test_registered_user_can_not_login_with_wrong_password(self):
        self.loginPage.login("bot2", "this is wrong password")
        self.assertTrue(self.loginPage.is_at(), "Must be on login page")


    def test_not_registered_user_can_not_login(self):
        self.loginPage.login("no_such_user", "this is wrong password")
        self.assertTrue(self.loginPage.is_at(), "Must be on login page")


    def test_user_can_not_login_without_username_and_password(self):
        self.loginPage.login("", "")
        self.assertTrue(self.loginPage.is_at(), "Must be on login page")


    def test_two_users_can_login(self):
        self.loginPage.login("bot2", "secret123")
        LoginPage(2).go_to().login("user3", "secret123")

        self.assertTrue(ChatPage().is_at(), "first user not in chat")
        self.assertTrue(ChatPage(2).is_at(), "second user not in chat")
