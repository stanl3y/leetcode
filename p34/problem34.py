# Tests
# find 1 in [] ..want [-1,-1]
# find 3 in [0,1,2] ..want [-1,-1]
# find 5 in [0,1,2,3,5,5,5,5,8,13,21,34] ..want [4,7]

# find 7 in [7] want [0,0]
# find 9 in [9,9,9] want [0,2]


class Solution(object):
    """ Solution for Leetcode problem 34: Search for a Range. """

    def midpoint(self, a, b):
        return a + (b-a) // 2

    def key_lower(self, mid_val, level): return mid_val < level
    def key_upper(self, mid_val, level): return mid_val <= level 


    def narrow_down(self, lwr, upr, key_func):      
      while(upr - lwr) > 1:
        mid = self.midpoint(lwr, upr)
        if key_func(self.nums[mid], self.target):
          lwr = mid
        else:
          upr = mid

      return {'lwr': lwr, 'upr': upr}

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1,-1]

        self.nums = nums
        self.target = target

        lwr, upr = 0, len(nums) - 1

        if nums[lwr] == target:
          lower_only_option = lwr
        else:
          lower_only_option = self.narrow_down(lwr, upr, self.key_lower)['upr']

        if nums[upr] == target:
          upper_only_option = upr
        else:
          upper_only_option = self.narrow_down(lwr, upr, self.key_upper)['lwr']

        #print("lower only option ", lower_only_option)
        #print("upper only option ", upper_only_option)

        if nums[lower_only_option] == target and \
            nums[upper_only_option] == target:
            return [lower_only_option, upper_only_option]
        else:
            return [-1,-1]


                
            
        
            
import unittest

class ProblemTest(unittest.TestCase):
  """ Tests for Leetcode problem 34: Search for a Range. """
  
  def test_small_cases(self):
    self.assertEqual([-1,-1], Solution().searchRange([], 0))
    self.assertEqual([0,0], Solution().searchRange([1], 1))

  def test_not_present(self):
    self.assertEqual([-1,-1], Solution().searchRange([0,1,2], 3))

  def test_near_boundary(self):
    self.assertEqual([0,2], Solution().searchRange([9,9,9], 9))

  def test_general_case(self):
    self.assertEqual([4,7], 
      Solution().searchRange([0,1,2,3,5,5,5,5,8,13,21,34], 5))



if __name__ == '__main__':
  unittest.main()



# alternatively
#   if nums[mid] < target:
#        lwr = mid + 1
#        if nums[lwr] == target: break        
