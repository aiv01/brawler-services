from django.test import TestCase
from django.urls import reverse
from tests.setuptest import PlayersSetupTestCase
from players.models import Player


class PlayerAlreadyExistsViewTests(PlayersSetupTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('player_already_exists')
        self.send_player_exists = {'nickname': 'player'}
        self.send_no_player_exists = {'nickname': 'player2'}

    def test_player_exists(self):
        response = self.client.get(self.url, self.send_player_exists)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'player_already_exists': True})

    def test_no_player_exists(self):
        response = self.client.get(self.url, self.send_no_player_exists)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'player_already_exists': False})


class PlayerGetPhotoViewTest(PlayersSetupTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('player_get_photo')
        self.send_data = {'nickname': 'player'}
        self.send_data_wrong_nickname = {'nickname': 'player2'}

    def test_player_get_photo(self):
        response = self.client.get(self.url, self.send_data)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'photo': 'testserver{}'.format(self.player.photo.url)})

    def test_player_get_photo_no_photo(self):
        self.player.photo = None
        self.player.save()
        response = self.client.get(self.url, self.send_data)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'photo': None})

    def test_player_get_photo_wrong_nickname(self):
        response = self.client.get(self.url, self.send_data_wrong_nickname)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'error': 'player with this nickname does not exists'})


class PlayerGetAudioViewTest(PlayersSetupTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('player_get_audio')
        self.send_data = {'nickname': 'player'}
        self.send_data_wrong_nickname = {'nickname': 'player2'}

    def test_player_get_audio(self):
        response = self.client.get(self.url, self.send_data)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'audio': 'testserver{}'.format(self.player.audio.url)})

    def test_player_get_audio_no_audio(self):
        self.player.audio = None
        self.player.save()
        response = self.client.get(self.url, self.send_data)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'audio': None})

    def test_player_get_audio_wrong_nickname(self):
        response = self.client.get(self.url, self.send_data_wrong_nickname)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'error': 'player with this nickname does not exists'})


class PlayerRegisterViewTests(TestCase):

    def setUp(self):
        self.url = reverse('player_register')
        self.send_data = {'nickname': 'player2', 'password': 'password2', 'tagline': 'tagline2'}

    def test_player_registration(self):
        response = self.client.post(self.url, self.send_data)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'player_register': True, 'token': str(Player.objects.get(username='player2').token)})
        response = self.client.post(self.url, self.send_data)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'player_register': False,
                                                                      'fields': 'nickname, password, tagline',
                                                                      'info': 'password and tagline require a string of max 255 chars. Nickname must be unique and require a string of max 150 chars'})


class PlayerLoginViewTests(PlayersSetupTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('player_login')
        self.send_data_true = {'nickname': 'player', 'password': 'password'}
        self.send_data_false = {'nickname': 'player2', 'password': 'password2'}

    def test_player_login_true(self):
        response = self.client.post(self.url, self.send_data_true)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'player_login': True, 'token': str(Player.objects.get(username='player').token)})

    def test_player_login_false(self):
        response = self.client.post(self.url, self.send_data_false)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'player_login': False,
                                                                      'fields': 'nickname, password',
                                                                      'info': 'wrong nickname and/or password'})


class PlayerServerAuthViewTest(PlayersSetupTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('player_server_auth')
        self.send_data_true = {'token': self.player.token, 'ip': '127.0.0.1'}
        self.send_data_false = {'token': self.player.token, 'ip': '128.1.1.2'}
        self.send_data_wrong_token = {'token': '2c16bed0-f468-4e06-b68e-f930ea994f44', 'ip': '127.0.0.1'}

    def test_player_server_auth_true(self):
        response = self.client.post(self.url, self.send_data_true)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'auth_ok': True,
                                                                      'nickname': 'player'})

    def test_player_server_auth_false(self):
        response = self.client.post(self.url, self.send_data_false)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'auth_ok': False,
                                                                      'fields': 'ip',
                                                                      'info': 'ip are not equal'})

    def test_player_server_auth_wrong_token(self):
        response = self.client.post(self.url, self.send_data_wrong_token)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'auth_ok': False,
                                                                      'fields': 'token',
                                                                      'info': 'player with this token does not exists'})


class PlayerClientAuthViewTest(PlayersSetupTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('player_client_auth')
        self.send_data_true = {'token': self.player.token, 'port': '8080'}
        self.send_data_false = {'token': self.player.token, 'port': '8080'}
        self.send_data_wrong_token = {'token': '2c16bed0-f468-4e06-b68e-f930ea994f44', 'port': '8080'}

    def test_player_client_auth_true(self):
        response = self.client.post(self.url, self.send_data_true)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'auth_ok': True})

    def test_player_client_auth_wrong_token(self):
        response = self.client.post(self.url, self.send_data_wrong_token)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'auth_ok': False,
                                                                      'fields': 'token',
                                                                      'info': 'player with this token does not exists'})

    def test_player_client_auth_false(self):
        self.player.ip = '128.1.1.2'
        self.player.save()
        response = self.client.post(self.url, self.send_data_false)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'auth_ok': False,
                                                                      'fields': 'ip',
                                                                      'info': 'ip are not equal'})
