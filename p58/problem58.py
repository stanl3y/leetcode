class Solution(object):
    """ Solution for Leetcode problem 58: Length of Last Word. """

    def last_word_length(self, s):
        """Find the length of the last word in a string.
        
        :type s: str
        :rtype: int
        """
        
        # test case: "ab" (no space in front of last word)
        # test case: "  " (no last word)
        
        # (going backwards) find first non-space char
        for i in range(len(s) - 1, -2, -1):
            if i == -1 or s[i] != " ":
                break
        
        # keep going until a space or end of string
        for j in range(i, -2, -1):
            if j == -1 or s[j] == " ":
                return i - j

import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 58: Length of Last Word. """
    
    def test(self):
        self.assertEqual(0, Solution().last_word_length(""))
        self.assertEqual(0, Solution().last_word_length(" "))

        self.assertEqual(1, Solution().last_word_length("a "))
        self.assertEqual(2, Solution().last_word_length("aaa bc "))

if __name__ == '__main__':
    unittest.main()