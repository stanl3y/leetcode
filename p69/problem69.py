class Solution(object):
    """ Solution for Leetcode problem 69: Sqrt(x). """
    def mySqrt(self, n):
        """
        :type x: int
        :rtype: int
        """
        def midpoint(a,b): return b - (b-a) // 2

        if n <= 0: return 0

        # binary search
        lo, hi = 0, n

        while lo < hi:
            mid = midpoint(lo, hi)
            if mid**2 <= n: lo = mid
            else: hi = mid - 1

        return lo

import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 69: Sqrt(x). """
    def test(self):
        # self.assertEqual(0, Solution().insert_function())

        cases = {-1:0, 0:0, 1:1, 2:1, 17:4, 1234567:1111}

        for when, expect in cases.items():
            self.assertEqual(expect, Solution().mySqrt(when))

if __name__ == '__main__':
    unittest.main()