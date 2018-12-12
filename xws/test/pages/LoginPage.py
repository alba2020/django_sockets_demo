from xws.test.base.Driver import Driver


class LoginPage:

    def __init__(self, id=0):
        self.driver = Driver.get_instance(id)


    def go_to(self):
        self.driver.get('%s%s' % (Driver.url, '/log_in/'))
        return self


    def login(self, username, password):
        username_input = self.driver.find_element_by_id("id_username")
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_id("id_password")
        password_input.send_keys(password)

        self.driver.find_element_by_tag_name("button").click();
        return self


    def is_at(self):
        h1 = self.driver.find_element_by_tag_name("h1")
        return h1.text == "Login"

