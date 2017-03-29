# Tests
# find 1 in [] ..want [-1,-1]
# find 3 in [0,1,2] ..want [-1,-1]
# find 5 in [0,1,2,3,5,5,5,5,8,13,21,34] ..want [4,7]

# find 7 in [7] want [0,0]
# find 9 in [9,9,9] want [0,2]


class Solution(object):
    
    def midpoint_floor(self, a, b):
        return a + (b-a) // 2

    def midpoint_ceiling(self, a, b):
        return b - (b-a) // 2

    def find_lower_boundary(self, lwr, upr):
      while lwr <= upr:
#        print(lwr, upr)
#        input("L waiting.. ")

        if self.nums[lwr] == self.target:
          return lwr

        mid = self.midpoint_floor(lwr, upr)

        if self.nums[mid] < self.target:
          lwr = mid + 1
        elif self.nums[mid] > self.target:
          upr = mid - 1
        else:
          upr = mid # otherwise could lose the target value
      else:
        return - 1

    def find_upper_boundary(self, lwr, upr):
      while lwr <= upr:
#        print(lwr, upr)
#        input("U waiting.. ")
        if self.nums[upr] == self.target:
          return upr

        mid = self.midpoint_ceiling(lwr, upr)

        if self.nums[mid] > self.target:
          upr = mid - 1
        elif self.nums[mid] < self.target:
          lwr = mid + 1
        else:
          lwr = mid # otherwise could lose the target value
      else:
        return -1


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

        lower = self.find_lower_boundary(lwr, upr)
        upper = self.find_upper_boundary(lwr, upr)


        #print("lower only option ", lower_only_option)
        #print("upper only option ", upper_only_option)

        return [lower, upper]

                
            
        
            
import unittest

class ProblemTest(unittest.TestCase):
  def test_small_cases(self):
    self.assertEqual([-1,-1], Solution().searchRange([], 0))
    self.assertEqual([0,0], Solution().searchRange([1], 1))

  def test_not_present(self):
    self.assertEqual([-1,-1], Solution().searchRange([0,1,2], 3))
    self.assertEqual([-1,-1], Solution().searchRange([0,1,2], -3))

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
