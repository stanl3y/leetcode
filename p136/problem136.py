from functools import reduce

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [] if not nums else reduce(lambda x,y: x^y, nums)
        

import unittest

class ProblemTest(unittest.TestCase):
    def test(self):
        # self.assertEqual(0, Solution().insert_function())
        self.assertEqual([], Solution().singleNumber([]))
        self.assertEqual(4, Solution().singleNumber([2,17,5,5,4,2,17]))

if __name__ == '__main__':
    unittest.main()