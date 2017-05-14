from tests.setuptest import CreditsSetupTestCase
from django.urls import reverse


class CreditJsonViewTest(CreditsSetupTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('credits_json')

    def test_credit_json(self):
        response = self.client.get(self.url)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'credits': [{'name': 'Name', 'surname': 'Surname',
                                                                                   'other_info': None, 'roles': ['Role 1', 'Role 2']}]})

    def test_credit_json_delete(self):
        self.credit.delete()
        response = self.client.get(self.url)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'credits': []})
