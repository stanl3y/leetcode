from tree_utils import *    # see leetcode/utils/tree_utils.py
from queue import Queue

class Solution(object):
    """ Solution to Leetcode problem 101: Symmetric Tree. 

    Definition for a binary tree node.
        class TreeNode(object):
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None
    """

    def isSymmetric(self, root):
        """
        Determines whether a given binary tree is vertically symmetric.                        

        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isSymmetric_recursive(root)


    def isSymmetric_recursive(self, root):
        """ Recursive solution. """

        def recursion(node1, node2):
            if (not node1) and (not node2): return True

            return bool(node1) and bool(node2) and node1.val == node2.val \
                and recursion(node1.left, node2.right) \
                and recursion(node1.right, node2.left)

        return recursion(root.left, root.right)

    def isSymmetric_iterative(self, root):
        """ Iterative solution. """

        queueL = Queue(); queueL.put(root.left)
        queueR = Queue(); queueR.put(root.right)

        while not (queueL.empty() or queueR.empty()):
            nodeL, nodeR = queueL.get(), queueR.get()
            if not nodeL and not nodeR: continue
            if not (nodeL and nodeR and nodeL.val==nodeR.val): return False

            queueL.put(nodeL.left)
            queueR.put(nodeR.right)
            
            queueL.put(nodeL.right)
            queueR.put(nodeR.left)

        return False if not (queueL.empty() and queueR.empty()) else True

        
import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 101: Symmetric Tree. """

    def setUp(self):
        """ Setup a test tree, using inorder-preorder. """

        self.root = TreeNode(1)

        inorderL= [3,2,5,4]
        preorderL = [2,3,4,5]
        left_subtree = Tree.from_inorder_preorder(inorderL, preorderL)

        inorderR = [4,5,2,3]
        preorderR = [2,4,5,3]
        right_subtree = Tree.from_inorder_preorder(inorderR, preorderR)

        self.root.left  = left_subtree.root
        self.root.right = right_subtree.root

        tree = Tree(self.root)
        

    def test(self):
        """ Modify the test tree and run tests accordingly. """

        # the initial tree should be symmetric
        self.assertEqual(True, Solution().isSymmetric(self.root))

        # remove a node, then check asymmetry
        n4 = self.root.right.left
        self.assertEqual(4, n4.val)

        n4.right = None   # desymmetrize
        self.assertEqual(False, Solution().isSymmetric(self.root))
        self.root.left.right.left = None    # symmetrize again

        # swap nodes, then check asymmetry
        n2 = self.root.left
        self.assertEqual(2, n2.val)

        n2.left, n2.right = n2.right, n2.left
        self.assertEqual(False, Solution().isSymmetric(self.root))


if __name__ == '__main__':
    unittest.main()