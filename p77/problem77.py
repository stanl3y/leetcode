import time
class Solution(object):
    """ Solution for Leetcode problem 77: Combinations. """

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.combinations(list(range(1,n+1)), k)


    def combinations(self, nums, size):
        nums.sort()
        result = []
        partial_nums = []

        if size > len(nums): return []

        def recursion(ind):
            if len(partial_nums) == size:
                result.append(partial_nums[:])
                return
            elif ind == len(nums): return

            # use the current number
            partial_nums.append(nums[ind])
            recursion(ind+1)
            partial_nums.pop()

            # skip the current number
            # (..and all its copies to avoid duplicates)
            while ind+1 < len(nums) and nums[ind+1] == nums[ind]:
                ind +=1
            recursion(ind+1)

        recursion(0)
        return result


        
import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 77: Combinations. """

    def test(self):
        cases = [
            { 'when': [[], 2], 'expect': [] },
            { 'when': [[1], 2], 'expect': [] },
            { 'when': [[1,2,3], 2], 'expect': [[1,2], [1,3], [2,3]] },
            { 'when': [[3,3,3], 3], 'expect': [[3,3,3]] },
            { 'when': [[1,2,2,2], 2], 'expect': [[1,2], [2,2]]},
        ]

        for case in cases:
            answer = Solution().combinations(*case['when'])
            sorted_answer = sorted([ sorted(x) for x in answer])
            sorted_expect = sorted([ sorted(x) for x in case['expect']])

            self.assertEqual(sorted_expect, sorted_answer)


if __name__ == '__main__':
    unittest.main()