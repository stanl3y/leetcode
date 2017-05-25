class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root):
        self.root = root


    ################ TRAVERSALS ################

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


    ################ TREE BUILDING ################

    @classmethod
    def from_inorder_preorder(cls, inorder, preorder):
        assumptions = [
            set(preorder) == set(inorder),
            len(preorder) == len(set(preorder)),
            len(inorder) == len(set(inorder)),
        ]
        if not all(assumptions): 
            raise ValueError("both traversals must have same length, and no duplicates")

        tree = Tree(None)
        tree.root = tree.build_from_inorder_preorder(inorder, preorder)
        return tree


    def build_from_inorder_preorder(self, inorder, preorder):
        if len(preorder) == len(inorder) == 0: return None
        curr_val = preorder[0]
        split = inorder.index(curr_val)

        curr_node = TreeNode(curr_val)
        curr_node.left = self.build_from_inorder_preorder(inorder[:split], preorder[1:split+1])
        curr_node.right = self.build_from_inorder_preorder(inorder[split+1:], preorder[split+1:])

        return curr_node        

    @classmethod
    def from_inorder_postorder(cls, inorder, postorder):
        pass

    def build_from_inorder_postorder(self, inorder, postorder):
        pass

