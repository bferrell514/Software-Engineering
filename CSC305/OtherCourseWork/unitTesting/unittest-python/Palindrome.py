"""
Your Name here!
"""


class Palindrome:
    """
    A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward,
    such as madam or kayak. Sentence-length palindromes may be written when allowances are made for adjustments to
    capital letters, punctuation, and word dividers, such as “A man, a plan, a canal, Panama!”,
    “Was it a car or a cat I saw?” or “No 'x' in Nixon” -- https://en.wikipedia.org/wiki/Palindrome

    If you wish to develop this code further, take a look at https://docs.python.org/3/library/unicodedata.html
    -- specifically the normalize function (try the NFKD form) to help strip accents -- you'll probably also
    use the lower() method of your normalized string. You could then create a new string by filtering in only
    the characters you want (try re.sub(), https://docs.python.org/3/library/re.html)
    """

    def is_palindrome(self, text: str) -> bool:
        """
        Determine whether a string is a palindrome

        :param text: string to be tested if it is a palindrome
        :returns true if the text is a palindrome
        :raises ValueError: if there are no alphanumeric characters in the text
        """
        if len(text) == 0:
            raise ValueError
        # use the slicing operator to reverse the string; if it is
        # the same forwards and backwards, it is a palindrome!
        return text[::-1] == text
