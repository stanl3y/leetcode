class Solution(object):
    """ Solution for Leetcode problem 66: Plus One. """

    def plus_one(self, digits):
        """Add one to an integer represented in a list.

        :type digits: List[int]
        :rtype: List[int]
        """
        
        digits = digits or [0]
        last = digits.pop()
        
        if last == 9:
            return self.plus_one(digits) + [0]
        else:
            return digits + [last + 1]


import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 66: Plus One. """
    
    def test(self):
        self.assertEqual([1], Solution().plus_one([0]))
        self.assertEqual([2], Solution().plus_one([1]))
        
        self.assertEqual([1,0], Solution().plus_one([9]))
        self.assertEqual([2,0], Solution().plus_one([1,9]))
        self.assertEqual([1,0,0], Solution().plus_one([9,9]))

if __name__ == '__main__':
    unittest.main()