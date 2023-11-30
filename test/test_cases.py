import unittest

from src.rabin_karp import rabin_karp_matcher


class TestRabinKarpMatcher(unittest.TestCase):
    def test_basic_matching(self):
        haystack = "ababcababcabc"
        needle = "abc"
        result = rabin_karp_matcher(haystack, needle)
        self.assertEqual(result, [2, 7, 10])

    def test_no_match(self):
        haystack = "abcdefg"
        needle = "xyz"
        result = rabin_karp_matcher(haystack, needle)
        self.assertEqual(result, [])

    def test_multiple_matches(self):
        haystack = "ababababab"
        needle = "ab"
        result = rabin_karp_matcher(haystack, needle)
        self.assertEqual(result, [0, 2, 4, 6, 8])


if __name__ == "__main__":
    unittest.main()
