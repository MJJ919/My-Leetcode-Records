'''
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
'''

'''
Time: O(n+m)
Space: O(1)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float('-inf'))
        pre = dummy
        while l1 and l2:
            if l1.val>l2.val:
                pre.next = l2
                l2 = l2.next 
            else:
                pre.next = l1
                l1 = l1.next 
            pre = pre.next
        pre.next = l1 if l1 is not None else l2
        return dummy.next
