class Solution(object):
    """ Solution for Leetcode problem 39: Combination Sum. """

    def combinationSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums = sorted(nums)
        self.result = []

        self.recursion(target, [], 0)
        return self.result
    
    def recursion(self, rem, so_far, cut_off):
        if rem == 0: 
            self.result.append(so_far)
            return

        for i in range(cut_off, len(self.nums)):
            if rem - self.nums[i] >= 0:
                self.recursion(rem - self.nums[i], so_far + [self.nums[i]], i)
            else: break



        


import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 39: Combination Sum. """
    def test(self):

        cases = [
            {'input': [[2,3,6,7], 7], 'exp': [[7], [2,2,3]] },
            {'input': [[2,3,4,5], 8], 'exp': [[2,2,2,2], [2,2,4], [2,3,3], [3,5], [4,4]]}
        ]

        for each_case in cases:
            expect = self.sort_list( each_case['exp'])
            answer = self.sort_list( Solution().combinationSum( *each_case['input'] ))

            self.assertEqual(expect, answer)

    def sort_list(self, mylist):
        return sorted( [ sorted(x) for x in mylist ])


if __name__ == '__main__':
    unittest.main()