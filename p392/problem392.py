class Solution(object):
    def isSubsequence(self, sub_str, string):
        """
        :type sub_str: str
        :type string: str
        :rtype: bool
        """
        if len(sub_str) == 0: return True
        if len(sub_str) > len(string): return False

        sub_ind = 0

        for i in range(len(string)):
            if string[i] == sub_str[sub_ind]:
                sub_ind += 1
                if sub_ind == len(sub_str): return True
        else:
            return False

import unittest

class ProblemTest(unittest.TestCase):
    def test(self):
        cases = {
            ("", "abc"): True,
            ("a", ""): False,
            ("lim", "lorem ipsum"): True,
            ("lixxm", "lorem ipsum"): False,
        }

        for when, expect in cases.items():
            self.assertEqual(expect, Solution().isSubsequence( *when))

if __name__ == '__main__':
    unittest.main()
        

