class Solution(object):
    """ Solution for Leetcode problem 13: Roman to Integer. """
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        summands = []

        for i, part in enumerate(s):
            val = value[part]

            subtract = (i+1) < len(s) and value[part] < value[s[i+1]]
            sign = -1 if subtract else 1

            summands.append(sign * val)

        return sum(summands)



import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 13: Roman to Integer. """
    
  def test(self):
        cases = {0: ""}
        cases.update({1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M" })
        cases.update({2: "II", 9: "IX", 49: "XLIX", 94: "XCIV"})

        for integer, roman in cases.items():
          self.assertEqual(integer, Solution().romanToInt(roman))

if __name__ == '__main__':
  unittest.main()