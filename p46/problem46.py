import math

class Solution(object):
    """ Solution for Leetcode problem 46: Permutations. """

    def permute(self, nums):
        """Generate all permutations of a set of distinct integers.

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

    def permute_alter(self, nums):
        """Generate all permutations of given nums (alternative). """

        nums = sorted(nums)
        result = []

        for _ in range(math.factorial(len(nums))):
            result.append(nums[:])
            nums = self.next_permutation(nums)

        return result

    def next_permutation(self, nums):
        """Given a permutation, find the 'consecutive' one. 

            eg. given (2,4,3,1), return (3,1,2,4)
        """

        for i in range(1, len(nums)):
            if nums[~i] < nums[~(i-1)]:
                
                for j in range(i):
                    if nums[~j] > nums[~i]: break

                nums[~i], nums[~j] = nums[~j], nums[~i]
                break
        else:
            i = len(nums)

        # reverse the tail (after i)
        for k in range(i//2):
            nums[~k], nums[~(i-1-k)] = nums[~(i-1-k)], nums[~k]

        return nums



import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 46: Permutations. """
    
    def test(self):
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