from linked_list import ListNode

class Solution(object):
    """ Solution for Leetcode problem 24: Swap Nodes in Pairs. 

    Definition for singly-linked list.
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
    """

    def swap_pairs(self, head):
        """Swap consecutive pairs of nodes in a linked list.

        :type head: ListNode
        :rtype: ListNode
        """

        root = ListNode(None)
        root.next = head

        current = root

        while current.next and current.next.next:
            first = current.next
            second = first.next
            third = second.next

            current.next = second
            second.next = first
            first.next = third

            current = current.next.next

        return root.next


import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 24: Swap Nodes in Pairs. """

    def test(self):
        cases = [
            [[], []],
            [[1], [1]],
            [[1,2], [2,1]],
            [[1,2,3], [2,1,3]],
            [[1,2,3,4], [2,1,4,3]]
        ]

        for each_case in cases:
            given, expect = each_case

            link_list = ListNode.array_to_linked_list(given)
            answer = Solution().swap_pairs(link_list)
            answer_list = ListNode.linked_list_to_array(answer, [])

            self.assertEqual(expect, answer_list)

if __name__ == '__main__':
    unittest.main()