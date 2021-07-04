'''
https://leetcode.com/problems/add-two-numbers-ii/
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry = 0
        next = None
        while s1 or s2 or carry!=0:
            n1 = s1.pop() if s1 else 0
            n2 = s2.pop() if s2 else 0
            num = n1+n2+carry
            carry = num//10
            num = num%10
            cur = ListNode(num)
            if not next:
                next = cur
            else:
                cur.next = next
                next = cur
        return next
                
