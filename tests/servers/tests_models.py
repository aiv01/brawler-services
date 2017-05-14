from tests.setuptest import ServersSetupTestCase


class PlayerStrTests(ServersSetupTestCase):

    def test_return_str(self):
        self.assertEqual(str(self.server), '79.58.170.103:50010')
