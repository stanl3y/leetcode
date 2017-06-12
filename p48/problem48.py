class Solution(object):
    """ Solution for Leetcode problem 48: Rotate Image. """

    @staticmethod
    def rot_CCW(i, j, matrix_side):
        """Rotate a point in a matrix by 90 deg CCW. """

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

    def rotate_matrix(self, matrix):
        """Rotate a matrix by 90 deg clockwise (in place).

        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        self.matrix_len = len(matrix)

        def rot_CCW(i, j):
            return Solution.rot_CCW(i, j, self.matrix_len)

        def get_matrix(i, j):
            return matrix[i][j]

        def set_matrix(i, j, val):
            matrix[i][j] = val

        def rotate_point(i, j):
            """ Rotate a point and its three images in other quadrants. """
            aside = get_matrix(i, j)

            for _ in range(3):
                new_val = get_matrix(*rot_CCW(i,j))
                set_matrix(i, j, new_val)
                i, j = rot_CCW(i, j)

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

        # for each point in the upper-left quadrant
        # rotate this point and its corresponding three images under rotation
        for i in range(half_len):
            for j in range(half_len):
                rotate_point(i, j)

        # in the odd case, rotate the central cross also
        if len(matrix) % 2 == 1:
            for i in range(half_len):
                rotate_point(i, len(matrix)//2 ) # indexing starts at zero



import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 48: Rotate Image. """
    
    def test_even(self):
        """ Test a matrix with even side length. """

        matrix = [
            [1,2],
            [3,4]  
        ]

        exp_matrix = [
            [3,1],
            [4,2]
        ]

        Solution().rotate_matrix(matrix)
        self.assertEqual(exp_matrix, matrix)

    def test_odd(self):
        """ Test a matrix with odd side length. """

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

        Solution().rotate_matrix(matrix)
        self.assertEqual(expect, matrix)

    def test_rot_CCW(self):
        """ Test the rot_CCW method. """

        self.assertEqual((1,0), Solution.rot_CCW(*(0,0),2))
        self.assertEqual((1,1), Solution.rot_CCW(*(1,0),2))

        self.assertEqual((1,0), Solution.rot_CCW(*(0,1),3))
        self.assertEqual((2,0), Solution.rot_CCW(*(0,0),3))

if __name__ == '__main__':
    unittest.main()
