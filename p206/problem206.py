# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head): 
        return self.reverseList_recursive(head)

    def reverseList_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head: return head
        self.new_head = None

        def recursion(node):
            if not node or not node.next:
                self.new_head = node
                return node
            else:
                next_node = recursion(node.next)
                next_node.next = node
                return node

        recursion(head)
        head.next = None

        return self.new_head

    def reverseList_iterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next: return head
        slow, fast, faster = head, head.next, head.next.next

        while True:
            fast.next = slow
            if faster == None: break
            slow, fast, faster = fast, faster, faster.next

        head.next = None
        return fast


        


import unittest
from linked_list import ListNode

class ProblemTest(unittest.TestCase):
    def test(self):
        # self.assertEqual(0, Solution().insert_function())
        cases = [
            { 'given': [], 'expect': [] },
            { 'given': [1], 'expect': [1] },
            { 'given': [1,2,3], 'expect': [3,2,1] },
        ]
        
        for case in cases:
            given = ListNode.array_to_linked_list(case['given'])
            answer = Solution().reverseList(given)
            answer = ListNode.linked_list_to_array(answer, [])
        
            self.assertEqual(answer, case['expect'])

if __name__ == '__main__':
    unittest.main()