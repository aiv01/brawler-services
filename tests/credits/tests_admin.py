from tests.setuptest import CreditsSetupTestCase
from credits.admin import CreditAdmin


class CreditGetRolesTests(CreditsSetupTestCase):

    def test_credit_get_roles(self):
        get_roles = CreditAdmin.get_roles(self, self.credit)
        self.assertEqual(get_roles, 'Role 1, Role 2')
