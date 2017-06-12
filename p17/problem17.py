class Solution(object):
    """ Solution for Leetcode problem 17: Letter Combinations.. . """

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []

        letters = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            "0": [" "]
        }

        result = [""]

        for digit in digits:
            new_result = []

            for letter in letters[digit]:
                for item in result:
                    new_result.append(item + letter)

            result = new_result

        return result



import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 17: Letter Combinations.. . """
    
    def test(self):
        cases = {
            "23": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        }

        for case, expect in cases.items():
            self.assertEqual(set(expect), set(Solution().letterCombinations(case)))

if __name__ == '__main__':
  unittest.main()