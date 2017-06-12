class Solution(object):
    """ Solution to Leetcode problem 1: Two Sum. """

    def two_sum(self, nums, target):
        """
        Decide if two integers in a list add up to a given target.

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # idea: for each num, check if it complements a previously seen one
        #   (keeping track of them in a dictionary)
        seek = {}

        for ind, element in enumerate(nums):
          if element in seek:
            return [seek[element], ind]
          else:
            seek[target - element] = ind

        return []