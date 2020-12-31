'''
https://leetcode.com/problems/reverse-linked-list-ii/
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        a = dummy
        for i in range(m-1):
            a = a.next
        pre, cur = a.next, a.next.next
        for i in range(m, n):
            cur.next, pre, cur = pre, cur, cur.next
        a.next.next = cur
        a.next = pre
        return dummy.next
