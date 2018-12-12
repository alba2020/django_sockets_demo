import time
from faker import Faker
from selenium.common.exceptions import TimeoutException

from xws.test.base.BaseTest import BaseTest
from xws.test.pages.ChatPage import ChatPage
from xws.test.pages.LoginPage import LoginPage


class TestMessages(BaseTest):

    def setUp(self):
        super().setUp()
        LoginPage().go_to().login("bot2", "secret123")


    def test_user_can_write_message(self):
        ChatPage().send_message("hello")


    def test_user_can_see_his_message(self):
        fake = Faker()
        msg = fake.sentence()
        chatPage = ChatPage().send_message(msg)

        self.assertTrue(chatPage.wait_for_last_message_to_contain(msg), "last message is wrong")


    def test_two_users_can_see_messages_of_each_other(self):
        #login second user
        LoginPage(2).go_to().login("user3", "secret123")
        fake = Faker()
        msg1 = fake.sentence()

        chatPage = ChatPage()
        chatPage2 = ChatPage(2)

        chatPage.send_message(msg1)
        self.assertTrue(chatPage2.wait_for_last_message_to_contain(msg1), "user does not see message")

        msg2 = fake.sentence()
        chatPage.send_message(msg2)
        self.assertTrue(chatPage.wait_for_last_message_to_contain(msg2), "user does not see message")
