'''
https://leetcode.com/problems/plus-one-linked-list/
Given a non-negative integer represented as a linked list of digits, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list.

Example 1:
Input: head = [1,2,3]
Output: [1,2,4]

Example 2:
Input: head = [0]
Output: [1]
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        notnine, dummy.next = dummy, head
        while head:
            if head.val != 9:
                notnine = head
            head = head.next
        notnine.val += 1
        notnine = notnine.next
        while notnine:
            notnine.val = 0
            notnine = notnine.next
        return dummy if dummy.val else dummy.next

'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def plusOne(self, head):
        s = []
        while head:
            s.append(head.val)
            head = head.next
        num = int(''.join(str(i) for i in s))+1
        res = [int(i) for i in str(num)]
        dummy = l = ListNode(-1)
        for i in res:
            a = ListNode(i)
            l.next = a
            l = a
        return dummy.next
