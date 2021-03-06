class Solution(object):
    """ Solution for Leetcode problem 31: Next Permutation. """

    def next_permutation(self, nums):
        """Given a permutation, find the next one (in place).

        e.g. given (2,3,1,4), find (2,3,4,1)
        
        :type nums: List[int]
        :rtype: void (do not return anything, modify nums in-place instead)
        

        (idea)
        * think of the permutation as an integer

        * want to make the number higher
            ie want to replace ...a...b... such that b > a with ...b...a...

        * want the next higher number, so want to swap ...a...b... where
            a as far right as possible
            b as small as possible (while b > a)

        example: consider 13542
            * note the decreasing sequence 542, no swaps here yield an increase
            * will want to swap 3
            * 4 is smallest possible with 4 > 3
            * get 14532
            * note 532 is again sorted (holds in general)
            * reverse 532 to 235 to get as small a number as possible
        """

        # traverse the decreasing sequence to find 'a' (see example)
        for i in range(1, len(nums)):
            if nums[~i] < nums[~(i-1)]:

                # traverse again to find 'b' (see example)
                for j in range(i):
                    if nums[~j] > nums[~i]: break

                # swap 'a' and 'b'
                nums[~i], nums[~j] = nums[~j], nums[~i]
                break
        else:
            # else reverse the whole sequence
            i = len(nums)

        # reverse the tail (after 'b' with index ~i)
        for k in range(i//2):
            nums[~k], nums[~(i-1-k)] = nums[~(i-1-k)], nums[~k]


import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 31: Next Permutation. """
    
    def test(self):
        cases = [
            {'nums': [1,2,3], 'exp_nums': [1,3,2]},
            {'nums': [3,2,1], 'exp_nums': [1,2,3]},
            {'nums': [1,1,5], 'exp_nums': [1,5,1]},

            {'nums': [2,1,4,3], 'exp_nums': [2,3,1,4]},
            {'nums': [2,4,3,1], 'exp_nums': [3,1,2,4]},
            {'nums': [4,3,2,1], 'exp_nums': [1,2,3,4]}
        ]

        for case in cases:
            nums = case['nums']
            Solution().next_permutation(nums)
            self.assertEqual(case['exp_nums'], nums)

if __name__ == '__main__':
    unittest.main()