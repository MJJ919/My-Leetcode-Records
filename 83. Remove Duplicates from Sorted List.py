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
        cur=head
        while cur != None and cur.next!=None:
            if cur.val == cur.next.val:
                cur.next=cur.next.next
            else:
                cur = cur.next
        return head
                
