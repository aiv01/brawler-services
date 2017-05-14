from django.test import TestCase
from django.urls import reverse


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
