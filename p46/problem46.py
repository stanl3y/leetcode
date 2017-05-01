import math

class Solution(object):
    def permute(self, nums):

        return self.permute_alter(nums)
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        partials = [[]]

        for num in nums:
            new_partials = []

            for partial in partials:
                for i in range(0, len(partial) + 1):
                    new_partials.append( partial[ :i] + [num] + partial[i: ])

            partials = new_partials 

        return partials

    ### Alternative solution ###

    def next_permutation(self, nums):
        for i in range(1, len(nums)):
            if nums[~i] < nums[~(i-1)]:
                
                for j in range(i): # array sorted, could apply binary search(?)
                    if nums[~j] > nums[~i]: break

                nums[~i], nums[~j] = nums[~j], nums[~i]
                break
        else:
            i = len(nums)

        # reverse the tail (after i)
        for k in range(i//2):
            nums[~k], nums[~(i-1-k)] = nums[~(i-1-k)], nums[~k]

        return nums

    def permute_alter(self, nums):
        nums = sorted(nums)
        result = []

        for _ in range(math.factorial(len(nums))):
            result.append(nums[:])
            nums = self.next_permutation(nums)

        return result




# OTHER APPROACHES

# IDEA: who's next?
# (-) use depth first search
#   for each partially formed permutation, in turn add each of the yet unused elements
#   see https://discuss.leetcode.com/topic/21151/simple-python-solution-dfs/2
#
# (-) recursive solution - take any as first and then permute the rest (compare above)
#   see https://discuss.leetcode.com/topic/17277/one-liners-in-python

# IDEA: in turn swap first entry with all subsequent, then second with all subsequent..
# see https://discuss.leetcode.com/topic/5881/my-elegant-recursive-c-solution-with-inline-explanation

        


import unittest

class ProblemTest(unittest.TestCase):
    def test(self):
        # self.assertEqual(0, Solution().insert_function())
        cases = [
            {'given': [1,2,3], 'expect': 
                [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2],[3,2,1]] },

            {'given': [], 'expect': [[]]}
        ]

        for case in cases:
            expect = sorted( case['expect'])
            answer = sorted( Solution().permute( case['given']))

            self.assertEqual(expect, answer)

if __name__ == '__main__':
    unittest.main()