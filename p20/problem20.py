class Solution(object):
    """ Solution for Leetcode problem 20: Valid Parentheses. """

    def is_valid_bracketing(self, string):
        """Verify whether a given bracketing is valid.

        :type s: str
        :rtype: bool
        """

        stack = []
        corresp_bracket = { "(": ")", "[": "]", "{": "}"}
        open_brackets = corresp_bracket.keys()

        for bracket in string:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if not (stack and bracket == corresp_bracket[stack.pop()]):
                    return False

        return True if not stack else False

      

import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 20: Valid Parentheses. """

    def test(self):
        # correct bracketings
        self.assertEqual(True, Solution().is_valid_bracketing(""))
        self.assertEqual(True, Solution().is_valid_bracketing("([{}])"))
        self.assertEqual(True, Solution().is_valid_bracketing("({})[]"))

        # not all brackets closed
        self.assertEqual(False, Solution().is_valid_bracketing("({}"))

        # closing the wrong bracket
        self.assertEqual(False, Solution().is_valid_bracketing("(}"))

        # closing an unopened bracket
        self.assertEqual(False, Solution().is_valid_bracketing("]"))

if __name__ == '__main__':
    unittest.main()