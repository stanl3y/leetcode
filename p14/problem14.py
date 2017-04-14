class Solution(object):
    """ solves Leetcode problem #14: Longest Common Prefix """

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""

        # return self.longestCommonPrefixRecursive(strs)
        prefix = strs[0]

        for i in range(1, len(strs)):
          prefix = self.prefixOfTwo(prefix, strs[i])

        return prefix



    def prefixOfTwo(self, first, second):
      # find first index where strings don't match
      min_len = min(len(first), len(second))
      i = 0

      while i < min_len and first[i] == second[i]:
        i += 1

      return first[0:i]


#    def longestCommonPrefixRecursive(self, strs):
#        self.strs = strs
#        return self.recursive_solution(strs[0], 1)
#
#
#
#    def recursive_solution(self, prefix, ind):
#        if ind == len(self.strs):
#            return prefix
#        else:
#            new_prefix = self.prefixOfTwo(prefix, self.strs[ind])
#            return self.recursive_solution(new_prefix, ind + 1)



import unittest

class ProblemTest(unittest.TestCase):
  def test(self):
    self.assertEqual("", Solution().prefixOfTwo("", "abcd"))
    self.assertEqual("abc", Solution().prefixOfTwo("abcd", "abcefl"))
    self.assertEqual("abc", Solution().prefixOfTwo("abc", "abc"))

  def test_solution(self):
    self.assertEqual("", Solution().longestCommonPrefix([]))

    strs = ["alpha", "alpine", "alpen", "aligator", "alpruce?"]
    self.assertEqual("al", Solution().longestCommonPrefix(strs))

if __name__ == '__main__':
  unittest.main()


        