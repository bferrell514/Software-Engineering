"""
Your Name here!
"""
import unittest

from Palindrome import Palindrome


class PalindromeTestCase(unittest.TestCase):
    _palindrome: Palindrome

    def setUp(self) -> None:
        """
        The private _palindrome object is created fresh for every
    test_* method by the setUp method.
        :return: None
        """
        self._palindrome = Palindrome()

    def test_lowercase_word_is_palindrome(self):
        self.assertTrue(self._palindrome.is_palindrome("stats"))

    def test_lowercase_word_not_palindrome(self):
        self.assertFalse(self._palindrome.is_palindrome("python"))

    def test_mixed_case_word_is_palindrome(self):
        self.assertTrue(self._palindrome.is_palindrome("Noon"))

    def test_empty_string_raises_ValueError(self):
        self.assertRaises(ValueError, self._palindrome.is_palindrome, "")

    def test_empty_string_raises_ValueError_context(self):
        """This duplicates the previous test using a different style of exception checking"""
        with self.assertRaises(ValueError):
            self._palindrome.is_palindrome("")

    # ADD YOUR TESTS BELOW -- make sure to include...
    #  - another test where a ValueError should be raised
    #  - at least three test cases that would not adequately be covered by the above tests
    # Suggestion: We haven't done anything about accented characters or whole sentences yet


if __name__ == '__main__':
    unittest.main()
