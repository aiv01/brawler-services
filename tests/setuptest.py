from django.test import TestCase
from players.models import Player
from servers.models import Server
from credits.models import Role, Credit


class PlayersSetupTestCase(TestCase):

    def setUp(self):
        self.player = Player.objects.create_user(username='player', password='password', tagline='tagline',
                                                 photo='test.png', audio='test.ogg', ip='127.0.0.1')


class ServersSetupTestCase(TestCase):

    def setUp(self):
        self.server = Server.objects.create(ip='79.58.170.103', port='50010')


class CreditsSetupTestCase(TestCase):

    def setUp(self):
        self.role_1 = Role.objects.create(role='Role 1')
        self.role_2 = Role.objects.create(role='Role 2')
        self.credit = Credit.objects.create(name='Name', surname='Surname')
        self.credit.roles.add(self.role_1, self.role_2)
