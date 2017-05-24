class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root):
        self.root = root

    def preorder(self):
        return self.traversal(lambda node: [node.right, node.left, node])

    def inorder(self):
        return self.traversal(lambda node: [node.right, node, node.left])

    def postorder(self):
        return self.traversal(lambda node: [node, node.right, node.left])


    def traversal(self, order): 
        traversal = []
        stack = []
        stack.append(self.root)
        visited = set()

        while stack:
            curr_node = stack.pop()
            if curr_node is None: continue

            if curr_node not in visited:
                visited.add(curr_node)
                for x in order(curr_node): stack.append(x)
            else:
                traversal.append(curr_node.val)
        return traversal