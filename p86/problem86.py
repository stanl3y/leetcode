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
        root_lo = ListNode(None)
        root_hi = ListNode(None)

        last_lo = root_lo
        last_hi = root_hi
        
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

        last_lo.next = None
        last_hi.next = None

        # join lists if both exist
        # or return one
        if root_lo.next and root_hi.next:
            last_lo.next = root_hi.next
            return root_lo.next
        else:
            return root_lo.next or root_hi.next



        


import unittest

class ProblemTest(unittest.TestCase):
    def test(self):
        # self.assertEqual(0, Solution().insert_function())

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