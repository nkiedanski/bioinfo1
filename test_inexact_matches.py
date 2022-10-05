import unittest
from inexact_matches import inexact_matches


class TestCatalog(unittest.TestCase):

    def test_inexact_matches(self):
        larga = "MCTTTTACM"
        corta = "ACT"
        self.assertEqual(inexact_matches(corta, larga, 1), (2, [0, 6]))

    def test_inexact_matches_no_match(self):
        larga = "MCTTTTACM"
        corta = "HHH"
        self.assertEqual(inexact_matches(corta, larga, 1), (0, []))

    def test_inexact_matches_more_mismatches_than_limit_in_one_motive(self):
        larga = "GGAACCCC"
        corta = "GGTG"
        self.assertEqual(inexact_matches(corta, larga, 2), (1, [0]))


if __name__ == '__main__':
    unittest.main()