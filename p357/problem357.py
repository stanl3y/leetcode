from functools import reduce

class Solution(object):
    """ Solution for Leetcode problem 357: Count Numbers with Unique Digits. """
    
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        def without_zero_of_length(k):
            return reduce( lambda x,y: x*y, range(9, 9-k, -1))

        def with_zero_of_length(k):
            return (k-1) * reduce( lambda x,y: x*y, range(9, 9-k+1, -1))

        total = 1
        for i in range(1, min(n,9)+1):  total += without_zero_of_length(i)
        for i in range(2, min(n,10)+1): total += with_zero_of_length(i)

        return total
        
import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 357: Count Numbers with Unique Digits. """

    def test(self):
        # self.assertEqual(0, Solution().insert_function())
        cases = { 0:1, 1:10, 2:91, 3: 739}

        for when, expect in cases.items():
            self.assertEqual(expect, Solution().countNumbersWithUniqueDigits( when))



if __name__ == '__main__':
    unittest.main()