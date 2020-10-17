'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
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
        if head == None:
            return head

        current = head.next
        prev = head
        
        while current != None:
            if current.val == prev.val:
                prev.next= current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next
        return head
                
                
