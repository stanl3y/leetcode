from linked_list import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, split):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # initialize
        last_lo = root_lo = ListNode(None)
        last_hi = root_hi = ListNode(None)
        curr = head

        # append each node to the correct sequence
        while curr:
            if curr.val < split:
                last_lo.next = curr
                last_lo = last_lo.next
            else:
                last_hi.next = curr
                last_hi = last_hi.next
            curr = curr.next

        last_lo.next = root_hi.next
        last_hi.next = None
        
        return root_lo.next


import unittest

class ProblemTest(unittest.TestCase):
    def test(self):
        cases = [
            { 'given': [], 'split': 0, 'expect': [] },

            { 'given': [1,2,3], 'split': 0, 'expect': [1,2,3] },
            { 'given': [1,2,3], 'split': 4, 'expect': [1,2,3] },

            { 'given': [1,4,3,2,5,2], 'split': 3, 'expect': [1,2,2,4,3,5]}
        ]

        for case in cases:
            given = ListNode.array_to_linked_list(case['given'])
            answer = Solution().partition(given, case['split'])
            answer = ListNode.linked_list_to_array(answer, [])

            self.assertEqual(answer, case['expect'])

if __name__ == '__main__':
    unittest.main()