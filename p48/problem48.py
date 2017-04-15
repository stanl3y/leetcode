class Solution(object):

    @staticmethod
    def rotCCW(i, j, matrix_side):
        shift = (matrix_side - 1) / 2

        # convert matrix notation into Cartesian
        (x, y) = (i, j)

        # center at origin
        (x, y) = (x - shift, y - shift)

        # rotate
        (x, y) = (-y, x)

        # shift back
        (x, y) = (x + shift, y + shift)

        # return to matrix notation
        (i, j) = (int(x), int(y))

        return (i,j)

    def rotateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        self.matrix_len = len(matrix)

        def rotCCW(i, j):
            return Solution.rotCCW(i, j, self.matrix_len)

        def get_matrix(i, j):
            return matrix[i][j]

        def set_matrix(i, j, val):
            matrix[i][j] = val



        def rotatePoint(i, j):
            aside = get_matrix(i, j)

            for _ in range(3):
                new_val = get_matrix(*rotCCW(i,j))
                set_matrix(i, j, new_val)
                i, j = rotCCW(i, j)

            set_matrix(i, j, aside)

        # even case
        # 2 2 1 1
        # 2 2 1 1
        # 3 3 4 4
        # 3 3 4 4

        # odd case
        # 2 2 x 1 1
        # 2 2 x 1 1 
        # x x 0 x x 
        # 3 3 x 4 4 
        # 3 3 x 4 4


        half_len = len(matrix) // 2

        for i in range(half_len):
            for j in range(half_len):
                rotatePoint(i, j)

        if len(matrix) % 2 == 1:
            for i in range(half_len):
                rotatePoint(i, len(matrix)//2 ) # indexing starts at zero






      

import unittest

class ProblemTest(unittest.TestCase):
    def test_even(self):
        matrix = [
          [1,2],
          [3,4]  
        ]

        exp_matrix = [
          [3,1],
          [4,2]
        ]
        Solution().rotateMatrix(matrix)
        self.assertEqual(exp_matrix, matrix)

    def test_odd(self):
        matrix = [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ]

        expect = [
          [7,4,1],
          [8,5,2],
          [9,6,3]
        ]

        Solution().rotateMatrix(matrix)
        self.assertEqual(expect, matrix)

    def test_rotCCW(self):
        self.assertEqual((1,0), Solution.rotCCW(*(0,0),2))
        self.assertEqual((1,1), Solution.rotCCW(*(1,0),2))

        self.assertEqual((1,0), Solution.rotCCW(*(0,1),3))
        self.assertEqual((2,0), Solution.rotCCW(*(0,0),3))

if __name__ == '__main__':
  unittest.main()
