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





    # def test_exact_matches_continuous(self):
    #     larga = "AGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTC" \
    #             "CTAGTCCTAGTCCT"
    #     corta = "AGTCCT"
    #     self.assertEqual(exact_matches(corta, larga), (20, [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96,
    #                                                         102, 108, 114, 120]))
    # def test_no_exact_matches(self):
    #     larga = "AGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTC" \
    #             "CTAGTCCTAGTCCT"
    #     corta = "TTTTTTTT"
    #     self.assertEqual(exact_matches(corta,larga), (0, []))
    # def test_exact_matches_not_continuous(self):
    #     larga = "AGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTHFTRDVAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTCCTAGTC" \
    #             "CTAGTCCTAGTCCT"
    #     corta = "AGTCCT"
    #     self.assertEqual(exact_matches(corta, larga), (20, [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 72, 78, 84, 90, 96,
    #                                                         102, 108, 114, 120, 126]))



if __name__ == '__main__':
    unittest.main()