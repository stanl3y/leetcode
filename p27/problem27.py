class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        storeIndex = 0

        for num in nums:
            if num != val:
                nums[storeIndex] = num
                storeIndex += 1

        return storeIndex


import unittest

class ProblemTest(unittest.TestCase):
  def test(self):

    cases = [
      {'nums': [], 'rem': 1, 'exp_nums': [], 'exp_len': 0},
      {'nums': [1,2,3], 'rem': 4, 'exp_nums': [1,2,3], 'exp_len': 3},
      {'nums': [1,1,1], 'rem': 1, 'exp_nums': [], 'exp_len': 0},
      {'nums': [1,2,3,3,2,1], 'rem': 2, 'exp_nums': [1,3,3,1], 'exp_len': 4}      
    ]

    for case in cases:
        nums = case['nums']
        answer = Solution().removeElement(nums, case['rem'])

        self.assertEqual(case['exp_len'], answer)
        self.assertEqual(case['exp_nums'], nums[:answer])

if __name__ == '__main__':
  unittest.main()