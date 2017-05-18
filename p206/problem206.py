# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head): 
        return self.reverseList_recursive(head)

    # refactored based on the Leetcode model solution
    def reverseList_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next: return head
        new_head = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

    # refactored based on the Leetcode model solution
    def reverseList_iterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        slow, fast = head, head.next

        while fast:
            faster = fast.next
            fast.next = slow
            slow, fast = fast, faster

        head.next = None
        return slow


        


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