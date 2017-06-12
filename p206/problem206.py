class Solution(object):
    """ Solution for Leetcode problem 206: Reverse Linked List. 

    Definition for singly-linked list.
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
    """

    def reverse_list(self, head): 
        return self.reverse_list_recursive(head)

    # refactored based on the Leetcode model solution
    def reverse_list_recursive(self, head):
        """Reverse a given linked list (recursively).

        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next: return head
        new_head = self.reverse_list_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

    # refactored based on the Leetcode model solution
    def reverse_list_iterative(self, head):
        """Reverses a given linked list.

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
    """ Tests for Leetcode problem 206: Reverse Linked List. """
    
    def test(self):
        cases = [
            { 'given': [], 'expect': [] },
            { 'given': [1], 'expect': [1] },
            { 'given': [1,2,3], 'expect': [3,2,1] },
        ]
        
        for case in cases:
            given = ListNode.array_to_linked_list(case['given'])
            answer = Solution().reverse_list(given)
            answer = ListNode.linked_list_to_array(answer, [])
        
            self.assertEqual(answer, case['expect'])

if __name__ == '__main__':
    unittest.main()