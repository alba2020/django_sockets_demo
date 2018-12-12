from faker import Faker

from xws.test.base.BaseTest import BaseTest
from xws.test.pages.ChatPage import ChatPage
from xws.test.pages.LoginPage import LoginPage


class LoggedInUserTest(BaseTest):

    def setUp(self):
        print("setUp() in LoggedInUserTest")
        loginPage = LoginPage(self.driver, self.live_server_url, self.live_server_ws_url)
        loginPage.go_to()
        loginPage.login("bot2", "secret123")

        self.chatPage = ChatPage(self.driver, self.live_server_url, self.live_server_ws_url)

        self.fake = Faker()
