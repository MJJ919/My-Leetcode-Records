'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head1 = ListNode()
        head1.next = head
        p1, p2 = head1, head
        while p2 != None:
            if p2.val == val:
                p1.next = p2.next
            else:
                p1 = p2
            p2 = p2.next
        return head1.next
