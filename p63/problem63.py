from queue import Queue

# Complexity: time O(mn), space O(mn)
class Solution(object):
    """ Solution for Leetcode problem 63: Unique Paths II. """

    # Remarks
    #   * with dynamic prog could use only one dimensional grid
    #       (see https://discuss.leetcode.com/topic/10974/short-java-solution/2)
    #   * could use padding to avoid borderline testing
    #   * using dp with vectorized operations would likely be faster

    def unique_paths_with_obstacles(self, obstacles):
        """Count right-down paths in a rectangle.

        :type obstacles: List[List[int]]
        :rtype: int
        """

        # initialization
        shape = [len(obstacles), len(obstacles[0])]
        if not ( shape[0] > 0 and shape[1] > 0): return 0

        self.obstacles = obstacles
        grid = [ [0]*shape[1] for _ in range(shape[0]) ]
        queue = Queue()
        visited = set()

        # processing upper left corner
        if obstacles[0][0] or obstacles[-1][-1]: return 0
        grid[0][0] = 1
        if shape[0] > 1: queue.put((1,0))
        if shape[1] > 1: queue.put((0,1))

        # processing other squares
        while not queue.empty():
            i,j = curr_pos = queue.get()
            if obstacles[i][j] or curr_pos in visited: 
                continue

            paths_from_left  = 0 if j == 0 else grid[i][j-1]
            paths_from_above = 0 if i == 0 else grid[i-1][j]
            grid[i][j] =  paths_from_left + paths_from_above

            if j+1 < shape[1]: queue.put( (i, j+1))
            if i+1 < shape[0]: queue.put( (i+1, j))
            visited.add(curr_pos)

        return grid[-1][-1]



    def unique_paths_with_obstacles_vectorized(self, obstacles):
        """Count right-down paths in a rectangle (vectorized). """
        pass


import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 63: Unique Paths II. """
    
    def test(self):
        cases = {
            ((),(),()): 0,
            ((0,),): 1,
            ((0,0),): 1,
            ((0,),(0,)): 1,

            (   (0,0,0,0), 
                (0,1,0,0),
                (0,0,0,1),
                (0,0,0,0),
            ) : 4,
        }

        for when, expect in cases.items():
            self.assertEqual(expect, Solution().unique_paths_with_obstacles(when))

if __name__ == '__main__':
    unittest.main()