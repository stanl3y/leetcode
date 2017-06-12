class Solution(object):
    """ Solution for Leetcode problem 14: Longest Common Prefix. """

    def longest_common_prefix(self, strs):
        """Find the longest common prefix of given strings.

        :type strs: List[str]
        :rtype: str
        """

        if not strs: return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
          prefix = self.prefix_of_two(prefix, strs[i])

        return prefix



    def prefix_of_two(self, first, second):
        """ Find the common prefix of two strings. """

        # find first index where strings don't match
        min_len = min(len(first), len(second))
        i = 0

        while i < min_len and first[i] == second[i]:
            i += 1

        return first[0:i]


    def longest_common_prefix_recursive(self, strs):
        """ Recursively find the longest common prefix of given strings. """

        def recursion(prefix, ind):
            if ind == len(strs):
                return prefix
            else:
                new_prefix = self.prefix_of_two(prefix, strs[ind])
                return recursion(new_prefix, ind + 1)

        if not strs: return ""
        return recursion(strs[0], 1)



import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 14: Longest Common Prefix. """
    
    def test_prefix_of_two(self):
        """ Test the prefix_of_two method. """
        self.assertEqual("", Solution().prefix_of_two("", "abcd"))
        self.assertEqual("abc", Solution().prefix_of_two("abcd", "abcefl"))
        self.assertEqual("abc", Solution().prefix_of_two("abc", "abc"))

    def test_solution(self):
        """ Test the full solution. """
        self.assertEqual("", Solution().longest_common_prefix([]))
        self.assertEqual("abcd", Solution().longest_common_prefix(["abcd"]))

        strs = ["alpha", "alpine", "alpen", "aligator", "alpruce"]
        self.assertEqual("al", Solution().longest_common_prefix(strs))

if __name__ == '__main__':
    unittest.main()


        