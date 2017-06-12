class Solution(object):
    """ Solution for Leetcode problem 22: Generate Parentheses. """

    def generate_bracketings(self, n):
        """Generates all bracketings of n elements.

        :type n: int
        :rtype: List[str]
        """

        result = []

        def recursion(prths_part, open_used, closed_used):
            if closed_used == n:
                result.append( "".join(prths_part))
            else:
                if open_used < n:
                    prths_part.append("(")
                    recursion(prths_part, open_used + 1, closed_used)
                    prths_part.pop()

                if open_used > closed_used:
                # note in particular n >= open_used > closed_used
                    prths_part.append(")")
                    recursion(prths_part, open_used, closed_used + 1)
                    prths_part.pop()

        recursion([], 0, 0)

        return result


import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 22: Generate Parentheses. """
    
    def test(self):
        self.assertEqual([''], Solution().generate_bracketings(0))
        self.assertEqual(["()"], Solution().generate_bracketings(1))

        level3_prths = [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()",
        ]
        self.assertEqual(level3_prths, Solution().generate_bracketings(3))

if __name__ == '__main__':
    unittest.main()