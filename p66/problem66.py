class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digits = digits or [0]
        last = digits.pop()
        
        if last == 9:
            return self.plusOne(digits) + [0]
        else:
            return digits + [last + 1]


import unittest

class ProblemTest(unittest.TestCase):
  def test(self):
    self.assertEqual([1], Solution().plusOne([0]))
    self.assertEqual([2], Solution().plusOne([1]))
    
    self.assertEqual([1,0], Solution().plusOne([9]))
    self.assertEqual([2,0], Solution().plusOne([1,9]))
    self.assertEqual([1,0,0], Solution().plusOne([9,9]))

if __name__ == '__main__':
  unittest.main()