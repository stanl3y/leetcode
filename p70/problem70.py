class Solution(object):
    """ Solution for Leetcode problem 70: Climbing Stairs. """
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0: return 0

        # idea: given that we can take either one or two steps
        # the number of ways to climb follows the Fibonacci sequence 

        fib = [1,1]
        for _ in range(n-1):
            fib.append( fib[-2] + fib[-1] )

        return fib[n]


import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 70: Climbing Stairs. """

    def test(self):
        cases = {1:1, 2:2, 3:3, 5:8}

        for when, expect in cases.items():
            self.assertEqual(expect, Solution().climbStairs(when))

if __name__ == '__main__':
    unittest.main()