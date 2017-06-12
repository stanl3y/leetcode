from functools import reduce

class Solution(object):
    """ Solution for Leetcode problem 357: Count Numbers with Unique Digits. """
    
    def count_numbers_with_unique_digits(self, n):
        """Count all numbers less than n, with unique digits.

        :type n: int
        :rtype: int
        """

        def without_zero_of_length(k):
            """Count numbers of length k that do not contain the digit zero. """
            return reduce( lambda x,y: x*y, range(9, 9-k, -1))

        def with_zero_of_length(k):
            """Count numbers of length k that do contain the digit zero. """
            return (k-1) * reduce( lambda x,y: x*y, range(9, 9-k+1, -1))

        total = 1
        for i in range(1, min(n,9)+1):  total += without_zero_of_length(i)
        for i in range(2, min(n,10)+1): total += with_zero_of_length(i)

        return total
        
import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 357: Count Numbers with Unique Digits. """

    def test(self):
        cases = { 0:1, 1:10, 2:91, 3: 739}

        for when, expect in cases.items():
            self.assertEqual(expect, Solution().count_numbers_with_unique_digits( when))

if __name__ == '__main__':
    unittest.main()