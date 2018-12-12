import time

from xws.test.base.BaseTest import BaseTest
from xws.test.pages.ChatPage import ChatPage
from xws.test.pages.LoginPage import LoginPage


class TestLogout(BaseTest):

    def test_logged_in_user_can_log_out(self):
        loginPage = LoginPage().go_to().login("bot2", "secret123")
        ChatPage().logout()
        self.assertTrue(loginPage.is_at())
