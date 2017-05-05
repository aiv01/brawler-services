from tests.setuptest import SetupTestCase


class PlayerStrTests(SetupTestCase):

    def test_return_str(self):
        self.assertEqual(str(self.player), 'player')
