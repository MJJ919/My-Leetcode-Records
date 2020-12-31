'''
https://leetcode.com/problems/rotate-list/
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        p1 = head
        length = 1
        while p1.next:
            p1 = p1.next
            length += 1
        p1.next = head
        p2 = head
        for i in range(length-k%length-1):
            p2 = p2.next
        new = p2.next
        p2.next = None
        return new
