class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        options = {}
        for index, element in enumerate(nums):

          if element in options:
            return [options[element], index]
          else:
            options[target - element] = index

