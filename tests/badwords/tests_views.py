from tests.setuptest import BadwordsSetupTestCase
from django.urls import reverse


class BadwordJsonViewTest(BadwordsSetupTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('badwords_json')
        self.send_data_with_privileges = {'token': self.player_1.token}
        self.send_data_without_privileges = {'token': self.player_2.token}
        self.send_data_wrong_token = {'token': '2c16bed0-f468-4e06-b68e-f930ea994f44'}
        self.send_data_wrong_token_format = {'token': '1230-0034-0323-dkfm'}

    def test_badword_json(self):
        response = self.client.get(self.url)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'badwords': ['Badword 1', 'Badword 2']})

    def test_player_with_privileges_badword_json(self):
        response = self.client.post(self.url, self.send_data_with_privileges)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'badwords': [{'player': self.player_1.id, 'word': 'Badword 1'},
                                                                                   {'player': self.player_2.id, 'word': 'Badword 2'}]})

    def test_player_without_privileges_badword_json_wrong_token(self):
        response = self.client.post(self.url, self.send_data_without_privileges)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'error': 'access denied'})

    def test_player_badword_json_wrong_token(self):
        response = self.client.post(self.url, self.send_data_wrong_token)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'error': 'player with this token does not exists'})

    def test_player_badword_json_wrong_token_format(self):
        response = self.client.post(self.url, self.send_data_wrong_token_format)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'error': 'invalid token format'})

    def test_badword_json_delete(self):
        self.badword_1.delete()
        self.badword_2.delete()
        response = self.client.get(self.url)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'badwords': []})

    def test_player_badword_json_delete(self):
        self.badword_1.delete()
        self.badword_2.delete()
        response = self.client.post(self.url, self.send_data_with_privileges)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'badwords': []})
