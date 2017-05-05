from django.test import TestCase
from django.urls import reverse
from tests.setuptest import SetupTestCase
from players.models import Player


class PlayerAlreadyExistsViewTests(SetupTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('player_already_exists')
        self.send_player_exists = {'nickname': self.player.username}
        self.send_no_player_exists = {'nickname': 'player2'}
        self.response_player_exists = {'player_already_exists': True}
        self.response_no_player_exists = {'player_already_exists': False}

    def test_player_exists(self):
        response = self.client.get(self.url, self.send_player_exists)
        self.assertJSONEqual(str(response.content, encoding='utf8'), self.response_player_exists)

    def test_no_player_exists(self):
        response = self.client.get(self.url, self.send_no_player_exists)
        self.assertJSONEqual(str(response.content, encoding='utf8'), self.response_no_player_exists)


class PlayerRegisterViewTests(TestCase):

    def setUp(self):
        self.url = reverse('player_register')
        self.send_data = {'nickname': 'player2', 'password': 'password2', 'tagline': 'tagline2'}

    def test_player_registration(self):
        response = self.client.post(self.url, self.send_data)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'player_register': True, 'token': Player.objects.get(username='player2').token})
        response = self.client.post(self.url, self.send_data)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'player_register': False,
                                                                      'fields': 'nickname, password, tagline',
                                                                      'info': 'password and tagline require a string of max 255 chars. Nickname must be unique and require a string of max 150 chars'})


class PlayerLoginViewTests(SetupTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('player_login')
        self.send_data_true = {'nickname': 'player', 'password': 'password'}
        self.send_data_false = {'nickname': 'player2', 'password': 'password2'}

    def test_player_login_true(self):
        response = self.client.post(self.url, self.send_data_true)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'player_login': True, 'token': Player.objects.get(username='player').token})

    def test_player_login_false(self):
        response = self.client.post(self.url, self.send_data_false)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'player_login': False,
                                                                      'fields': 'nickname, password',
                                                                      'info': 'wrong nickname and/or password'})
