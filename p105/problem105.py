from tree_utils import *

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        assumptions = [
            set(preorder) == set(inorder),
            len(preorder) == len(set(preorder)),
            len(inorder) == len(set(inorder)),
        ]
        if not all(assumptions): 
            raise ValueError("both traversals must have same length, and no duplicates")

        return self.buildTree_recursive(preorder, inorder)


    def buildTree_recursive(self, preorder, inorder):
        if len(preorder) == len(inorder) == 0: return None
        curr_val = preorder[0]
        split = inorder.index(curr_val)

        curr_node = TreeNode(curr_val)
        curr_node.left = self.buildTree_recursive(preorder[1:split+1], inorder[:split])
        curr_node.right = self.buildTree_recursive(preorder[split+1:], inorder[split+1:])

        return curr_node


import unittest

class ProblemTest(unittest.TestCase):
    def test(self):
        preorder = [1,2,4,5,10,11,3,7,14]
        inorder = [4,2,10,5,11,1,3,14,7]

        root = Solution().buildTree(preorder, inorder)
        tree = Tree(root)

        # using already existing methods from file utils for testing
        self.assertEqual(preorder, tree.preorder())
        self.assertEqual(inorder, tree.inorder())

if __name__ == '__main__':
    unittest.main()