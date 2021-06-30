'''
https://leetcode.com/problems/reverse-nodes-in-k-group/
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
 
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        n = 0
        p = head
        while p:
            p = p.next
            n += 1
            
        def reverseBetween(head, left, right):
            dummy = ListNode(0)
            dummy.next = head
            pre = dummy
            cur = head
            for _ in range(left-1):
                pre, cur = cur, cur.next
            p1 = cur
            p2 = cur.next
            for _ in range(right-left):
                p2.next, p1, p2 = p1, p2, p2.next
            pre.next.next = p2
            pre.next = p1
            return dummy.next
        
        i = 1
        while i+k<=n+1:
            head = reverseBetween(head, i, i+k-1)
            i += k
        return head
