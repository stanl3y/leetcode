from tree_utils import *

import unittest

class ProblemTest(unittest.TestCase):
    def test_traversals(self):
        # initializing a test tree
        # depth 0
        root = TreeNode(1)
        tree = Tree(root)
        
        # depth 1
        root.left = n2 = TreeNode(2)
        root.right = n3 = TreeNode(3)

        # depth 2
        n2.left = n4 = TreeNode(4)
        n2.right = n5 = TreeNode(5)
        n3.right = n7 = TreeNode(7)
        
        # depth 3
        n5.left = n10 = TreeNode(10)
        n5.right = n11 = TreeNode(11)
        n7.left = n14 = TreeNode(14)

        # expected traversal for the tree
        exp_preorder = [1,2,4,5,10,11,3,7,14]
        exp_inorder = [4,2,10,5,11,1,3,14,7]
        exp_postorder = [4,10,11,5,2,14,7,3,1]
        self.assertEqual(exp_preorder, tree.preorder())
        self.assertEqual(exp_inorder, tree.inorder())
        self.assertEqual(exp_postorder, tree.postorder())


if __name__ == '__main__':
    unittest.main()