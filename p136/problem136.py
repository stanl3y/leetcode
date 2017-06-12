from functools import reduce

class Solution(object):
    """ Solution for Leetcode problem 136: Single Number. """
    
    def single_number(self, nums):
        """ Given pairs of nums with one (single) extra, find the singleton.

        :type nums: List[int]
        :rtype: int
        """

        # perform binary XOR on the given numbers
        # numbers that appear twice will cancel, singleton remains
        return [] if not nums else reduce(lambda x,y: x^y, nums)
        

import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 136: Single Number. """

    def test(self):
        self.assertEqual([], Solution().single_number([]))
        self.assertEqual(4, Solution().single_number([2,17,5,5,4,2,17]))

if __name__ == '__main__':
    unittest.main()