from django.test import TestCase
from players.models import Player
from servers.models import Server


class PlayersSetupTestCase(TestCase):

    def setUp(self):
        self.player = Player.objects.create_user(username='player', password='password', tagline='tagline',
                                                 photo='test.png', audio='test.ogg', ip='127.0.0.1')


class ServersSetupTestCase(TestCase):

    def setUp(self):
        self.server = Server.objects.create(ip='79.58.170.103', port='50010')
