class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        slow, fast = 0, 0

        found = dict()

        while slow < len(s):            

            # stop on the first repeated letter
            while fast < len(s) and \
            (found.get(s[fast]) is None or found.get(s[fast]) < slow):
                found[s[fast]] = fast
                fast += 1

            max_len = max(max_len, fast - slow)

            if fast == len(s):
                break
            else:   
                slow = found[s[fast]] + 1

        return max_len

        

import unittest

class ProblemTest(unittest.TestCase):
  def test(self):
    # special case
    self.assertEqual(0, Solution().lengthOfLongestSubstring(""))

    # terminates with end of string
    self.assertEqual(4, Solution().lengthOfLongestSubstring("abcd"))

    self.assertEqual(3, Solution().lengthOfLongestSubstring("ababcab"))

    # letter with index 0 in the found dict is 'found'
    self.assertEqual(3, Solution().lengthOfLongestSubstring("dvdf"))

if __name__ == '__main__':
  unittest.main()