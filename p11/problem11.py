class Solution(object):
    def maxArea(self, heights):
        """
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
    def test(self):
        heights = [2,1,10,3,12,1,1,4]
        self.assertEqual(20, Solution().maxArea(heights))

if __name__ == '__main__':
    unittest.main()
        

