class Solution(object):
    """ Solution for Leetcode problem 12: Integer to Roman. """

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digits = {
                0: {1: "I", 5: "V"},
                1: {1: "X", 5: "L"},
                2: {1: "C", 5: "D"},
                3: {1: "M"}
        }

        def level(x):
            return digits[curr_level][x]

        def translate(dig):
            if dig == 9:
                return level(1) + digits[curr_level+1][1]
            elif dig > 4:
                return level(5) + translate(dig - 5)
            elif dig == 4:
                return level(1) + level(5)
            else:
                return dig * level(1)



        curr_level = 0
        rev_result = []

        num_list = [int(x) for x in list(str(num))]
        
        for dig in reversed(num_list):
            rev_result.append(translate(dig))
            curr_level += 1

        return "".join(reversed(rev_result))





        



import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 12: Integer to Roman. """
    
  def test(self):

    
    cases = {}
    cases.update({1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M" })
    cases.update({2: "II", 9: "IX", 49: "XLIX", 94: "XCIV"})

    for integer, roman in cases.items():
      self.assertEqual(roman, Solution().intToRoman(integer))

if __name__ == '__main__':
  unittest.main()