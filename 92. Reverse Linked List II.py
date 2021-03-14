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
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        for _ in range(left-1):
            p = p.next
        pre, cur = p.next, p.next.next
        for _ in range(right-left):
            cur.next, pre, cur = pre, cur, cur.next
        p.next.next,p.next = cur, pre
        return dummy.next
