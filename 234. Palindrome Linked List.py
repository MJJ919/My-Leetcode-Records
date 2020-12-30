'''
https://leetcode.com/problems/palindrome-linked-list/
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a=[]
        while head:
            a.append(head.val)
            head = head.next
        return a==a[::-1]
