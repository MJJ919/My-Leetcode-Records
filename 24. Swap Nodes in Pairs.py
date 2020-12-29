'''
https://leetcode.com/problems/swap-nodes-in-pairs/
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes. Only nodes itself may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
'''

'''
Time: O(n)
Space: O(1)
'''
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while head and head.next:
            first, second = head, head.next
            pre.next, second.next, first.next = second, first, second.next
            pre = first
            head = first.next
        return dummy.next
    
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:   return head
        first, second = head, head.next 
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second
