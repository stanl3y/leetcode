class Solution(object):
    """ Solution for Leetcode problem 90: Subsets II. """

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        partial_nums = []

        def recursion(ind):
            if ind == len(nums):
                result.append(partial_nums[:])
                return

            # EITHER use the current number
            partial_nums.append(nums[ind])
            recursion(ind+1)
            partial_nums.pop()

            # OR skip the current number
            # (..and all its copies to avoid duplicates)
            while ind+1 < len(nums) and nums[ind+1] == nums[ind]:
                ind += 1
            recursion(ind+1)

        recursion(0)
        return result

import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 90: Subsets II. """
    
    def test(self):
        # self.assertEqual(0, Solution().insert_function())
        cases = [
            { 'when': [], 'expect': [[]]},
            { 'when': [1,2], 'expect': [[], [1], [2], [1,2],]},
            { 'when': [1,1,2], 'expect': [[],[1],[1,1], [2],[1,2],[1,1,2]]}
        ]

        for case in cases:
            answer = Solution().subsetsWithDup(case['when'])
            sorted_answer = sorted([ sorted(x) for x in answer])
            sorted_expect = sorted([ sorted(x) for x in case['expect']])

            self.assertEqual(sorted_expect, sorted_answer)

if __name__ == '__main__':
    unittest.main()