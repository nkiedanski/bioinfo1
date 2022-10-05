import unittest
from exact_matches import exact_matches

class TestCatalog(unittest.TestCase):

    def test_exact_matches(self):
        larga = "AGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTC" \
                "CTAGTCCTAGTCCT"
        corta = "AGTCCT"
        self.assertEqual(exact_matches(corta, larga), (20, [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96,
                                                            102, 108, 114, 120]))


if __name__ == '__main__':
    unittest.main()