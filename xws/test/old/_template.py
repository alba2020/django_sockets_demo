from channels.test import ChannelLiveServerTestCase
# from selenium.webdriver.firefox.webdriver import WebDriver
from django.core.management import call_command
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import time

from django.contrib.auth.models import User

class MySeleniumTests(ChannelLiveServerTestCase):
    fixtures = ['users.json']
    login_url = "http://localhost:8081/log_in/"

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

        # call_command('loaddata', 'users.json', verbosity=1)

    def test_login(self):
        # print("test")
        # for u in User.objects.all():
        #     print(u)
        # print("--")

        print("live server url: %s" % self.live_server_url)
        print("live server ws url: %s" % self.live_server_ws_url)
        # time.sleep(3)

        self.selenium.get(self.live_server_url + '/log_in/')

        self.selenium.execute_script("localStorage.setItem('ws_url', '%s')" % self.live_server_ws_url)

        username_input = self.selenium.find_element_by_id("id_username")
        username_input.send_keys("bot2")
        password_input = self.selenium.find_element_by_id("id_password")
        password_input.send_keys("secret123")
        self.selenium.find_element_by_tag_name("button").click();
        # time.sleep(1)
        # WebDriverWait(self.selenium, 10)

        h3 = self.selenium.find_element_by_tag_name("h3")
        assert h3.text == 'messages'

        self.selenium.find_element_by_id("input_message").send_keys("hello from bot")
        self.selenium.find_element_by_id("input_submit").click()

        time.sleep(2)
        # self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        # username_input = self.selenium.find_element_by_name("username")
        # username_input.send_keys('myuser')
        # password_input = self.selenium.find_element_by_name("password")
        # password_input.send_keys('secret')
        # self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
