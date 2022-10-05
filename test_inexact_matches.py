import unittest
from inexact_matches import inexact_matches


class TestCatalog(unittest.TestCase):

    def test_exact_matches_continuous(self):
        larga = "MAACCT"
        corta = "ACT"
        self.assertEqual(inexact_matches(corta, larga, 1), (2, [2,3]))




if __name__ == '__main__':
    unittest.main()