'''
https://leetcode.com/problems/linked-list-cycle-ii/
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        d = set()
        while head:
            if head in d:
                return head
            d.add(head)
            head = head.next
        return None
    
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        def getinter(head):
            fast = slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if slow == fast:
                    return fast
            return None
          
        intersection = getinter(head)
        if not intersection:
            return None
        p = head
        while p != intersection:
            p = p.next
            intersection = intersection.next
        return p
