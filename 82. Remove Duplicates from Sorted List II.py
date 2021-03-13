'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode('0')
        dummy.next = head
        p = dummy; q = head
        while q:
            if q.next and q.next.val==q.val:
                while q.next and q.next.val == q.val:
                    q = q.next
                p.next = q.next
            else:
                p = p.next
            q = q.next
        return dummy.next
