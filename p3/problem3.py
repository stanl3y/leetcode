class Solution(object):
    """ Solution for Leetcode problem 3: Longest Substring..  . """

    def longest_substr_len(self, string):
        """Find the length of long. substr with no duplicate chars. 

        :type s: str
        :rtype: int
        """
        max_len = 0
        slow, fast = 0, 0
        
        found = dict()

        while slow < len(string):            
            # stop on the first repeated letter
            while fast < len(string) and found.get(string[fast], -1) < slow:
                found[string[fast]] = fast
                fast += 1

            max_len = max(max_len, fast - slow)

            if fast == len(string):
                break
            else:   
                slow = found[string[fast]] + 1

        return max_len



import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 3: Longest Substring.. . """

    def test(self):
        # special case
        self.assertEqual(0, Solution().longest_substr_len(""))

        # terminates with end of string
        self.assertEqual(4, Solution().longest_substr_len("abcd"))

        # general case
        self.assertEqual(3, Solution().longest_substr_len("ababcab"))

        # letter with index 0 in the found dict is 'found'
        self.assertEqual(3, Solution().longest_substr_len("dvdf"))

if __name__ == '__main__':
    unittest.main()