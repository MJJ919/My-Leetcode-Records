'''
https://leetcode.com/problems/sort-list/
Given the head of a linked list, return the list after sorting it in ascending order.
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = a = head
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l = sorted(l)
        for i in l:
            a.val = i
            a = a.next
        return dummy.next
