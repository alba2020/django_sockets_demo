class LoginPage:

    def __init__(self, driver, url, ws_url):
        self.driver = driver
        self.url = url
        self.ws_url = ws_url


    def go_to(self):
        self.driver.get('%s%s' % (self.url, '/log_in/'))
        # self.driver.execute_script("localStorage.setItem('ws_url', '%s')" % self.ws_url)


    def login(self, username, password):
        username_input = self.driver.find_element_by_id("id_username")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_id("id_password")
        password_input.send_keys(password)
        self.driver.find_element_by_tag_name("button").click();


    def is_at(self):
        h1 = self.driver.find_element_by_tag_name("h1")
        return h1.text == "Login"
