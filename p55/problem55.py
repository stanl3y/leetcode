class Solution(object):
    """ Solution for Leetcode problem 55: Jump Game. """

    def can_jump(self, nums):
        """Given a list of jump lengths, decide if you can reach the end. 

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
        self.assertEqual(True, Solution().can_jump([2,3,1,1,4]))
        self.assertEqual(False, Solution().can_jump([3,2,1,0,4]))

if __name__ == '__main__':
    unittest.main()