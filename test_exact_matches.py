import unittest
from exact_matches import exact_matches


class TestCatalog(unittest.TestCase):

    def test_exact_matches_continuous(self):
        larga = "ACGTACGT"
        corta = "ACGT"
        self.assertEqual(exact_matches(corta, larga), (2, [0, 4]))

    def test_no_exact_matches(self):
        larga = "JFSHGBAVA"
        corta = "AAA"
        self.assertEqual(exact_matches(corta, larga), (0, []))

    def test_exact_matches_not_continuous(self):
        larga = "CAACTAACMAAC"
        corta = "AAC"
        self.assertEqual(exact_matches(corta, larga), (3, [1, 5, 9]))


if __name__ == '__main__':
    unittest.main()