class Solution(object):
    """ Solution for Leetcode problem 392: Is Subsequence. """

    def is_subsequence(self, sub_str, string):
        """Given two strings, decide if one is a substring of the other.

        :type sub_str: str
        :type string: str
        :rtype: bool
        """
        
        if len(sub_str) == 0: return True
        if len(sub_str) > len(string): return False

        sub_ind = 0

        for i in range(len(string)):
            if string[i] == sub_str[sub_ind]:
                sub_ind += 1
                if sub_ind == len(sub_str): return True
        else:
            return False

import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 392: Is Subsequence. """
    
    def test(self):
        cases = {
            ("", "abc"): True,
            ("a", ""): False,
            ("lim", "lorem ipsum"): True,
            ("lixxm", "lorem ipsum"): False,
        }

        for when, expect in cases.items():
            self.assertEqual(expect, Solution().is_subsequence( *when))

if __name__ == '__main__':
    unittest.main()