class Solution(object):
    """ Solution for Leetcode problem 41: First Missing Positive. """

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def swap(i1, i2):
            nums[i1], nums[i2] = nums[i2], nums[i1]

        # (imagine sorting 1,2,3 ... n)
        # idea: put each element between 1 and len(nums)
        # to its correct position, ignore other numbers

        ind = 0

        while ind < len(nums):
            if 1 <= nums[ind] <= len(nums) and nums[ nums[ind]-1] != nums[ind]:
                swap(ind, nums[ind]-1)                
            else: ind += 1

        for i in range(len(nums)):
            if not nums[i] == i+1: return i+1

        return len(nums)+1  # if the whole range present

import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 41: First Missing Positive. """
    
    def test(self):
        cases = {
            (): 1,
            (-3,-2,-1): 1,
            (1,2,3,4): 5,
            (3,4,-1,1): 2,
            (1,1): 2,
        }

        for when, expect in cases.items():
            self.assertEqual(expect, Solution().firstMissingPositive( list(when) ))

if __name__ == '__main__':
    unittest.main()