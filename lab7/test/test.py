import unittest
from lab7.src.search import compute_lps, kmp_search

class TestKMP(unittest.TestCase):
    def test_compute_lps_basic(self):
        self.assertEqual(compute_lps("ABABCABAB"), [0, 0, 1, 2, 0, 1, 2, 3, 4])
        self.assertEqual(compute_lps("AAAA"), [0, 1, 2, 3])
        self.assertEqual(compute_lps("ABCDE"), [0, 0, 0, 0, 0])
        self.assertEqual(compute_lps("AABAACAABAA"), [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5])
        self.assertEqual(compute_lps(""), [])

    def test_kmp_search_found(self):
        self.assertEqual(kmp_search("ABC ABCDAB ABCDABCDABDE", "ABCDABD"), [15])
        self.assertEqual(kmp_search("AAAAABAAABA", "AAAA"), [0, 1])
        self.assertEqual(kmp_search("ABC ABCDAB ABCDABCDABDE", "AB"), [0, 4, 8, 11, 15, 19])

    def test_kmp_search_not_found(self):
        self.assertEqual(kmp_search("ABCDEFG", "HIJ"), [])
        self.assertEqual(kmp_search("A", "AA"), [])

    def test_kmp_search_empty_needle(self):
        self.assertEqual(kmp_search("ABC", ""), [])

    def test_kmp_search_full_match(self):
        self.assertEqual(kmp_search("HELLO", "HELLO"), [0])

    def test_kmp_search_repeated_pattern(self):
        self.assertEqual(kmp_search("ABABABAB", "ABAB"), [0, 2, 4])

if __name__ == '__main__':
    unittest.main()
