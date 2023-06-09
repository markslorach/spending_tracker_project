import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def setUp(self):
        self.merchant = Merchant("Falafel To Go")

    def test_merchant_has_name(self):
        self.assertEqual("Falafel To Go", self.merchant.name)
