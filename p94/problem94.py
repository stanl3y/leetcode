# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.inorder = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # self.inorderTraversal_recursive(root)
        self.inorderTraversal_iterative(root)
        return self.inorder

    def inorderTraversal_recursive(self, node):
        if not node: return
        self.inorderTraversal_recursive(node.left)
        self.inorder.append(node.val)
        self.inorderTraversal_recursive(node.right)

    def inorderTraversal_iterative(self, root):
        stack = []
        stack.append(root)
        visited = set()

        while stack:
            current = stack.pop()
            if current is None: continue

            if current not in visited:
                visited.add(current)
                for x in [current.right, current, current.left]: stack.append(x)
            else:
                self.inorder.append(current.val)







import unittest

class ProblemTest(unittest.TestCase):
    def test(self):
        self.assertEqual([], Solution().inorderTraversal(None))

        # depth 0
        root = TreeNode(1)

        self.assertEqual([1], Solution().inorderTraversal( root))
        
        # depth 1
        n2 = TreeNode(2); root.left = n2
        n3 = TreeNode(3); root.right = n3

        # depth 2
        n4 = TreeNode(4); n2.left = n4
        n5 = TreeNode(5); n2.right = n5
        n6 = TreeNode(6) # not used
        n7 = TreeNode(7); n3.right = n7

        self.assertEqual([4,2,5,1,3,7], Solution().inorderTraversal( root))


if __name__ == '__main__':
    unittest.main()