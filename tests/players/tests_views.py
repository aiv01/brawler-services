from django.test import TestCase
from players.models import Player


class TestSetup(TestCase):
    def setUp(self):
        player = Player.objects.create(nickname='player', password='password', photo=)


class PlayerAlreadyExistsViewTest(TestCase):
