class Solution(object):
    """ Solution for Leetcode problem 365: Water and Jug Problem. """
    @staticmethod
    def gcd(a, b):
        return b if (a % b == 0) else Solution.gcd(b, a % b)

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z < 0 or (z > x + y): return False

        gcd  =  Solution.gcd(x, y)
        return True if z % gcd == 0 else False



import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 365: Water and Jug Problem. """
    
    def test_gcd(self):
        cases = {
            (24, 18): 6, 
            (5,7): 1
        }

        for key, value in cases.items():
            self.assertEqual(value, Solution.gcd(key[0], key[1]))

    def test_solution(self):
        cases = {
            ((3,5), 4): True,
            ((2,6), 5): False
        }

        for key, value in cases.items():
            x, y, z = key[0][0], key[0][1], key[1]
            self.assertEqual(value, Solution().canMeasureWater(x, y, z))

if __name__ == '__main__':
  unittest.main()