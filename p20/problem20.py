class Solution(object):
    """ Solution for Leetcode problem 20: Valid Parentheses. """

    def isValid(self, string):
        """
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
    self.assertEqual(True, Solution().isValid(""))
    self.assertEqual(True, Solution().isValid("([{}])"))
    self.assertEqual(True, Solution().isValid("({})[]"))

    # not all brackets closed
    self.assertEqual(False, Solution().isValid("({}"))

    # closing the wrong bracket
    self.assertEqual(False, Solution().isValid("(}"))

    # closing an unopened bracket
    self.assertEqual(False, Solution().isValid("]"))

if __name__ == '__main__':
  unittest.main()