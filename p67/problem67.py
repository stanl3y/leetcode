class Solution(object):
    """ Solution for Leetcode problem 67: Add Binary. """

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # normalize strings
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        elif len(b) > len(a):
            a = "0" * (len(b) - len(a)) + a


        rev_result = []
        carry = 0

        for i in range(len(a) - 1, -1, -1):
            sum = carry + int(a[i]) + int(b[i]) # note that 0 <= sum <= 3
            carry = 1 if sum >= 2 else 0
            rev_result.append(str( sum % 2))
        if carry == 1: rev_result.append('1')

        return ''.join(reversed(rev_result))
        

import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 67: Add Binary. """
    def test(self):
        # self.assertEqual(0, Solution().insert_function())
        cases = [
            { 'when': ["1001", "100"], 'exp': "1101" },
            { 'when': ["1", "1"], 'exp': "10" },
            { 'when': ["101", "101"], 'exp': "1010"}
        ]

        for case in cases:
            self.assertEqual(case['exp'], Solution().addBinary(*case['when']))

if __name__ == '__main__':
    unittest.main()