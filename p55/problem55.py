class Solution(object):
    """ Solution for Leetcode problem 55: Jump Game. """

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        need_to_jump = 0

        for i in range( len(nums)-2, -1, -1):
            need_to_jump += 1

            if nums[i] >= need_to_jump:
                need_to_jump = 0

        return True if not need_to_jump else False
        

import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 55: Jump Game. """
  
    def test(self):
        #self.assertEqual(0, Solution().insert_function())
        self.assertEqual(True, Solution().canJump([2,3,1,1,4]))
        self.assertEqual(False, Solution().canJump([3,2,1,0,4]))

if __name__ == '__main__':
    unittest.main()