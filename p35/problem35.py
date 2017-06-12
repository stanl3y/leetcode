class Solution(object):
    """ Solution for Leetcode problem 35: Search Insert Position. """

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo 



import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 35: Search Insert Position. """
    
    def test(self):
        self.assertEqual(2, Solution().searchInsert([1,2,3,4], 3)) # find middle
        self.assertEqual(2, Solution().searchInsert([1,2,4,5], 3)) # insert middle

        self.assertEqual(0, Solution().searchInsert([1,2,3,4], 0)) # insert left edge
        self.assertEqual(4, Solution().searchInsert([1,2,3,4], 5)) # insert right edge



if __name__ == '__main__':
    unittest.main()