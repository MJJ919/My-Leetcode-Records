'''
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.

Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        d = defaultdict(ListNode)
        prefix = 0
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur:
            prefix += cur.val
            d[prefix] = cur
            cur = cur.next
        prefix = 0
        cur = dummy
        while cur:
            prefix += cur.val
            if prefix in d:
                cur.next = d[prefix].next
            cur = cur.next
        return dummy.next            
