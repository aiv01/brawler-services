from tests.setuptest import BadwordsSetupTestCase


class CreditStrTests(BadwordsSetupTestCase):

    def test_badword_return_str(self):
        self.assertEqual(str(self.badword_1), 'Badword 1')
        self.assertEqual(str(self.badword_2), 'Badword 2')
