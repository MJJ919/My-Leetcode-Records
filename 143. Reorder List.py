'''
https://leetcode.com/problems/reorder-list/
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        pre, cur = None, slow
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        p1, p2 = head, pre
        while p2.next:
            p1.next, p1 = p2, p1.next
            p2.next, p2 = p1, p2.next
