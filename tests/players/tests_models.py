from tests.setuptest import PlayersSetupTestCase, PlayerDefaultImagesSetupTestCase


class PlayerStrTests(PlayersSetupTestCase):

    def test_return_str(self):
        self.assertEqual(str(self.player), 'player')


class PlayerDefaultImagesStrTests(PlayerDefaultImagesSetupTestCase):

    def test_return_str(self):
        self.assertEqual(str(self.default_image_1), 'Title 1')
        self.assertEqual(str(self.default_image_2), 'Title 2')
