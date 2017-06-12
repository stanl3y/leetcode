from linked_list import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """ Solution for Leetcode problem 83: Remove Duplicates from Sort List. """

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        root = ListNode(None)
        root.next = head

        last = root
        current = head

        while current:
            if not last.val == current.val:
                last.next = current
                last = current

            current = current.next

        last.next = None
        return root.next
    



import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 83: Remove Duplicates from Sort List. """
    
    def test(self):
        # self.assertEqual(0, Solution().insert_function())

        cases = [
            { 'given': [], 'expect': [] },
            { 'given': [1], 'expect': [1]},
            { 'given': [1,2,3], 'expect': [1,2,3] },
            
            { 'given': [1,1,2,3], 'expect': [1,2,3] },
            { 'given': [1,2,2,3], 'expect': [1,2,3] },
            { 'given': [1,2,3,3], 'expect': [1,2,3] }
        ]

        for case in cases:
            given = ListNode.array_to_linked_list(case['given'])
            answer = Solution().deleteDuplicates(given)
            answer = ListNode.linked_list_to_array(answer, [])

            self.assertEqual(answer, case['expect'])
            #self.assertEqual([1], [])
            #self.assertEqual([], [2,2])

if __name__ == '__main__':
    unittest.main()