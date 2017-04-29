class Solution(object):

    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        if num < 0: return False

        hi = lo = 1
        
        while num >= 10*hi:
            hi *= 10

        while hi >= lo:
            take = hi + lo if hi > lo else hi
            q = min(9, num // take)
            num -= q * take

            hi, lo = hi / 10, lo * 10

        return True if num == 0 else False






import unittest

class ProblemTest(unittest.TestCase):
  def test(self):
    self.assertEqual(False, Solution().isPalindrome(-1))
    self.assertEqual(False, Solution().isPalindrome(-121))

    self.assertEqual(True, Solution().isPalindrome(0))
    self.assertEqual(True, Solution().isPalindrome(1))
    self.assertEqual(True, Solution().isPalindrome(7))

    self.assertEqual(True, Solution().isPalindrome(22))
    self.assertEqual(True, Solution().isPalindrome(212))

    self.assertEqual(False, Solution().isPalindrome(123))
    self.assertEqual(False, Solution().isPalindrome(10))
    self.assertEqual(False, Solution().isPalindrome(100))

if __name__ == '__main__':
  unittest.main()