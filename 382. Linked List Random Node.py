'''
https://leetcode.com/problems/linked-list-random-node/
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Example 1:
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.l = []
        while head:
            self.l.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.l)
