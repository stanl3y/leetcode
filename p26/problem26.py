class Solution(object):
    """ Solution for Leetcode problem 26: Remove Duplicates from Sort. Array. """

    def removeDuplicates(self, nums):
        """
        Counts unique elements and moves them to the left.

        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0

        storeIndex = 1
        lastNum = nums[0]

        for i in range(1, len(nums)):
            currentNum = nums[i]

            if currentNum != lastNum:
                lastNum = currentNum
                nums[storeIndex] = currentNum
                storeIndex += 1

        return storeIndex

# Complexity
# time: O(n), space: O(1) ?
        
# Notes
# - if only interested in unique elements, consider: set(nums)
# - 


import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 26: Remove Duplicates from Sort. Array. """
  
    def test(self):
        self.assertEqual(0, Solution().removeDuplicates([]))
        self.assertEqual(1, Solution().removeDuplicates([1]))
        self.assertEqual(3, Solution().removeDuplicates([1,2,3]))
        self.assertEqual(3, Solution().removeDuplicates([1,2,2,2,3]))
        self.assertEqual(4, Solution().removeDuplicates([1,1,1,2,2,3,4,4,4]))

if __name__ == '__main__':
    unittest.main()


# question: use variables (eg. currentNum) or array pointers (eg. nums[i])?
# 
# class Solution(object):
#   def removeDuplicates(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if nums == []: return 0
# 
#     storeIndex = 1
# 
#     for i in range(1, len(nums)):
#       if nums[i] != nums[storeIndex-1]:
#         nums[storeIndex] = nums[i]
#         storeIndex += 1
# 
#     return storeIndex