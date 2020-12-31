'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''

'''
Method below uses one pass.
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 0 
        dummy = first = ListNode(0)
        dummy.next = head
        while head:
            head = head.next
            i += 1
        for i in range(i-n):
            first = first.next
        first.next = first.next.next
        return dummy.next
    
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fir = sec = dummy
        for i in range(n+1):
            fir = fir.next
        while fir:
            fir, sec = fir.next, sec.next
        sec.next = sec.next.next
        return dummy.next
