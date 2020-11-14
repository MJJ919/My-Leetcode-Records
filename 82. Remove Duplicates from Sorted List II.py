'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
'''
'''
Time:O(n)
Space:O(1)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre=dummy
        while head and head.next:
            if head.next.val==head.val:
                while head and head.next and head.next.val==head.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                head=head.next
                pre=pre.next
        return dummy.next
                
