from selenium.webdriver.chrome.webdriver import WebDriver

class Driver:
    # __drivers = dict()
    # url = ""

    __drivers = None
    url = None

    @classmethod
    def initialize(cls, url):
        cls.__drivers = dict()
        cls.url = url


    @classmethod
    def close(cls):
        for key in cls.__drivers:
            cls.__drivers[key].close()
            cls.__drivers[key].quit()


    @classmethod
    def get_instance(cls, id=0):
        if id not in cls.__drivers:
            cls.__drivers[id] = WebDriver()
            cls.__drivers[id].implicitly_wait(10)

        return cls.__drivers[id]
