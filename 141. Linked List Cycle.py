'''
https://leetcode.com/problems/linked-list-cycle/
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''
'''
2 Pointers.
Time:O(n)
Space:O(1)
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast = head.next
        slow = head
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False

'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        d = set()
        while head:
            if head in d:
                return True
            d.add(head)
            head = head.next
        return False
