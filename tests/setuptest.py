from django.test import TestCase
from players.models import Player


class SetupTestCase(TestCase):

    def setUp(self):
        self.player = Player.objects.create_user(username='player', password='password', tagline='tagline')

    def tearDown(self):
        pass
