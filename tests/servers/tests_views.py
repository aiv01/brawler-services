from django.test import TestCase
from django.urls import reverse
from tests.setuptest import ServersSetupTestCase


class ServerRegisterViewTests(TestCase):

    def setUp(self):
        self.url = reverse('server_register')
        self.send_data_true = {'ip': '79.36.199.38', 'port': '10050'}
        self.send_data_false = {'ip': '100', 'port': '9090909090'}

    def test_server_registration(self):
        response = self.client.post(self.url, self.send_data_true)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'server_register': True, })
        response = self.client.post(self.url, self.send_data_true)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'server_register': False,
                                                                      'fields': 'ip, port',
                                                                      'info': 'server already registered'})

    def test_server_registration_wrong_data(self):
        response = self.client.post(self.url, self.send_data_false)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'server_register': False,
                                                                      'fields': 'ip, port',
                                                                      'info': 'invalid ip and/or port'})


class ServersJsonViewTest(ServersSetupTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('servers_json')

    def test_credit_json(self):
        response = self.client.get(self.url)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'servers': [{'country': 'Italy (IT)',
                                                                                   'port': 50010,
                                                                                   'ip': '79.58.170.103'}]})

    def test_credit_json_delete(self):
        self.server.delete()
        response = self.client.get(self.url)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'servers': []})
