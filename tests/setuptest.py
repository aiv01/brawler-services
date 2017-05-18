from django.test import TestCase
from players.models import Player
from servers.models import Server
from credits.models import Role, Credit
from badwords.models import Badword


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


class BadwordsSetupTestCase(TestCase):

    def setUp(self):
        self.player_1 = Player.objects.create_user(username='player_1', password='password_1', is_staff=True)
        self.player_2 = Player.objects.create_user(username='player_2', password='password_2', is_staff=False)

        self.badword_1 = Badword.objects.create(word='Badword 1', player=self.player_1)
        self.badword_2 = Badword.objects.create(word='Badword 2', player=self.player_2)
