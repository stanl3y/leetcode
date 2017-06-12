class Solution(object):
    """ Solution for Leetcode problem 26: Remove Duplicates from Sort. Array. """
    
    # Complexity
    # time: O(n), space: O(1)
    
    # Notes
    # - if only interested in unique elements, consider: set(nums)

    def remove_duplicates(self, nums):
        """Counts unique elements and moves them to the left (in-place).

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

import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 26: Remove Duplicates from Sort. Array. """
  
    def test(self):
        self.assertEqual(0, Solution().remove_duplicates([]))
        self.assertEqual(1, Solution().remove_duplicates([1]))
        self.assertEqual(3, Solution().remove_duplicates([1,2,3]))
        self.assertEqual(3, Solution().remove_duplicates([1,2,2,2,3]))
        self.assertEqual(4, Solution().remove_duplicates([1,1,1,2,2,3,4,4,4]))

if __name__ == '__main__':
    unittest.main()