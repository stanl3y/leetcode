# Tests
# find 1 in [] ..want [-1,-1]
# find 3 in [0,1,2] ..want [-1,1]
# find 5 in [0,1,2,3,5,5,5,5,8,13,21,34] ..want [4,7]
# find 7 in [7,7,7]


class Solution(object):
    
    @classmethod
    def midpoint(self, a, b):
        return a + (b-a) // 2

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        # search for any occurrence of :target
        lwr, upr = 0, len(nums)-1
        mid = None
        
        while lwr <= upr:
            mid = self.midpoint(lwr,upr)

            if nums[mid] == target: 
                break
            elif: nums[mid] < target
                lwr = mid + 1
            else:
                upr = mid - 1
        else:
            return [-1, -1]  # if no element found
            
        keep = {'lwr': lwr, 'upr': upr, 'found': mid }
        
        # we have now found one target element
        # it remains to find the endopoints of its range
        
        # !! what if the element is at :lwr?
        # lower bound
        
        lwr, upr = keep['lwr'], keep['found']
        
        if nums[lwr] == target:
            lower_final = lwr
        else:
            while (upr - lwr > 1):
                mid = self.midpoint(lwr,upr)
                if nums[mid] == target:
                    upr = mid
                else:
                    lwr = mid

                
        
                
            
        
            
import unittest

class ProblemTest(unittest.TestCase):
  def test(self):
    self.assertEqual([-1,-1], Solution.searchRange([], 1))

if __name__ == '__main__':
  unittest.main()