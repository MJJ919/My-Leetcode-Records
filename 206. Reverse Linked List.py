'''
https://leetcode.com/problems/reverse-linked-list/
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''
'''
Time:O(n)
Space:O(1)
Method below uses iteration and packaging(封装).
'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
        
'''
Method below uses recursive.
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return p
