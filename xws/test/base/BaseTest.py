from channels.test import ChannelLiveServerTestCase

from xws.test.base.Driver import Driver


class BaseTest(ChannelLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        # print("--- setUp() in BaseTest")
        Driver.initialize(self.live_server_url)


    def tearDown(self):
        # print("--- tearDown() in BaseTest")
        Driver.close()

