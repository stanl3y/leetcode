class Solution(object):
    """ Solution for Leetcode problem 11: Container With Most Water. """

    def max_area(self, heights):
        """Given a list of bars, find the two that can hold the most water.

        :type height: List[int]
        :rtype: int
        """
        
        if len(heights) < 2: return 0

        lo, hi = 0, len(heights)-1
        max_vol = 0

        while lo < hi:
            curr_vol = (hi - lo) * min(heights[lo], heights[hi])
            max_vol = max(max_vol, curr_vol)

            if heights[lo] < heights[hi]: lo += 1
            else: hi -= 1

        return max_vol


import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 11: Container With Most Water. """

    def test(self):
        heights = [2,1,10,3,12,1,1,4]
        self.assertEqual(20, Solution().max_area(heights))

if __name__ == '__main__':
    unittest.main()
        
