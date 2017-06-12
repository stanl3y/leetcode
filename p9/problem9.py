class Solution(object):
    """ Solution for Leetcode problem 9: Palindrome Number. """

    def is_palindrome(self, num):
        """
        Determines whether a given integer is a palindrome.

        :type x: int
        :rtype: bool
        """

        if num < 0: return False

        hi = lo = 1
        
        while num >= 10*hi:
            hi *= 10

        while hi >= lo:
            take = hi + lo if hi > lo else hi
            q = min(9, num // take)
            num -= q * take

            hi, lo = hi / 10, lo * 10

        return True if num == 0 else False






import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 9: Palindrome Number. """

    def test(self):
        # negative nums are not considered palindromes
        self.assertEqual(False, Solution().is_palindrome(-1))
        self.assertEqual(False, Solution().is_palindrome(-121))

        # single-digits nums are palindromes
        self.assertEqual(True, Solution().is_palindrome(0))
        self.assertEqual(True, Solution().is_palindrome(1))
        self.assertEqual(True, Solution().is_palindrome(7))

        # more examples of palindromes
        self.assertEqual(True, Solution().is_palindrome(22))
        self.assertEqual(True, Solution().is_palindrome(212))

        # some non-examples of palindromes
        self.assertEqual(False, Solution().is_palindrome(123))
        self.assertEqual(False, Solution().is_palindrome(10))
        self.assertEqual(False, Solution().is_palindrome(100))

if __name__ == '__main__':
    unittest.main()