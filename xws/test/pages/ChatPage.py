from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from xws.test.base.Driver import Driver


class ChatPage:

    def __init__(self, id=0):
        self.driver = Driver.get_instance(id)


    def is_at(self):
        h1 = self.driver.find_element_by_tag_name("h1")
        return h1.text == "Chat"


    def send_message(self, message):
        self.driver.find_element_by_id("input_message").send_keys(message)
        self.driver.find_element_by_id("input_submit").click()
        return self


    def logout(self):
        self.driver.find_element_by_link_text("Log out").click()


    def wait_for_last_message_to_contain(self, msg):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, "div.message_list ul li:last-child"),
                    msg)
            )
            return True
        except TimeoutException:
            return False