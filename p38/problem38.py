class Solution(object):
    """ Solution for Leetcode problem 38: Count and Say. """

    def countAndSay(self, n):
        """Generate the n-th term of the Count-and-Say sequence.

        :type n: int
        :rtype: str
        """

        # sequence stored as a list of integers
        nums_list = self.next_step([1], n-1)
        return "".join([ str(x) for x in nums_list ])


    def next_step(self, nums, n):
        """ Recursively generate n more terms. """

        if n == 0:
            return nums

        new_nums = []
        slow, fast = 0,0

        while slow < len(nums):
            while fast < len(nums) and nums[fast] == nums[slow]:
                fast += 1

            new_nums.extend([fast - slow, nums[slow]])
            slow = fast

        return self.next_step(new_nums, n-1)


import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 38: Count and Say. """

    def test(self):
        self.assertEqual("1", Solution().countAndSay(1))
        self.assertEqual("111221", Solution().countAndSay(5))
        self.assertEqual("13112221", Solution().countAndSay(7))


if __name__ == '__main__':
    unittest.main()

#   Note: see model solutions at..
#   https://discuss.leetcode.com/topic/32023/4-5-lines-python-solutions