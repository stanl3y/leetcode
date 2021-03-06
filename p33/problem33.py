import bisect

class Solution(object):
    """ Solution for Leetcode problem 33: Search in Rotated Sorted Array. """

    def search(self, nums, target):
        """Search for a number in a sorted array that has been rotated.

        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def midpoint(a, b):
            return a + (b - a) // 2

        # idea: find split, then perform binary search in sorted segment
        if not nums: return -1

        lo, hi = 0, len(nums)-1

        # find the split, if present        
        if not nums[lo] < nums[hi]:

            while hi - lo > 1:
                mid = midpoint(lo, hi)

                if nums[mid] < nums[lo]: # hit the second part
                    hi = mid 
                else: # hit the first part
                    lo = mid  
            before_split, after_split = lo, hi

            # restrict to the appropriate section
            if nums[-1] >= target:
                lo, hi = after_split, len(nums) - 1
            else:
                lo, hi = 0, before_split

        # on a sorted segment now, perform binary search (bisection)
        insert_pos = bisect.bisect_left(nums, target, lo, hi)
        return insert_pos if nums[insert_pos] == target else -1

        
import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 33: Search in Rotated Sorted Array. """

    def test(self):
        # general case
        my_nums = [4,5,6,7,0,1,2]
        
        self.assertEqual(1, Solution().search(my_nums, 5))
        self.assertEqual(4, Solution().search(my_nums, 0))
        self.assertEqual(-1, Solution().search(my_nums, 3))

        # small cases
        self.assertEqual(-1, Solution().search([], 1))
        self.assertEqual(0, Solution().search([1], 1))

        # no rotation case
        self.assertEqual(2, Solution().search([0,1,2,3,4], 2))


if __name__ == '__main__':
    unittest.main()