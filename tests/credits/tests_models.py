from tests.setuptest import CreditsSetupTestCase


class CreditStrTests(CreditsSetupTestCase):

    def test_role_return_str(self):
        self.assertEqual(str(self.role_1), 'Role 1')
        self.assertEqual(str(self.role_2), 'Role 2')

    def test_credit_return_str(self):
        self.assertEqual(str(self.credit), 'Name')
