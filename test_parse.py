import unittest
import links
from parse_module import *

class TestParse(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1_voyager(self):
        page = get_page(links.VOYAGER)
        self.voyager_flag = parse_voyager_page(page)
        self.assertEqual(self.voyager_flag, "19770905")
    
    def test_2_rfc(self):
        page = get_page(links.RFC_1149)
        self.rfc_flag = parse_rfc_page(page)
        self.assertEqual(self.rfc_flag, "19900401")

    def test_3_unicode(self):
        page = get_page(links.UNICODE)
        self.unicode_flag = parse_unicode_page(page)
        self.assertEqual(self.unicode_flag, "1F9E0")

    def test_4_bitcoin(self):
        page = get_page(links.BITCOIN)
        self.bitcoin_flag = parse_bitcoin_page(page)
        self.assertEqual(self.bitcoin_flag, "20090103")

    def test_5_isbn(self):
        page = get_page(links.ICBN)
        self.icbn_flag = parse_icbn_page(page)
        self.assertEqual(self.icbn_flag, "0131103628")

if (__name__ == "__main__"):
    unittest.main()