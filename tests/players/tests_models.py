from tests.setuptest import PlayersSetupTestCase


class PlayerStrTests(PlayersSetupTestCase):

    def test_return_str(self):
        self.assertEqual(str(self.player), 'player')
