'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:    
            return head
        p = head
        while p.next != None:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def deleteDuplicates(self, head):
        l = []
        dummy = ListNode(-1)
        dummy.next = head
        while head:
            if head.val not in l:
                l.append(head.val)
                pre = head
            else:
                pre.next = head.next
            head = head.next
        return dummy.next
