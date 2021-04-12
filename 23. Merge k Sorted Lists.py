'''
https://leetcode.com/problems/merge-k-sorted-lists/
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''
'''
Time:O(nlgk)
Space:O(1)
'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        if length == 0: return None
        interval = 1
        def merge(l1, l2):
            head = pointer = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    pointer.next = l1
                    l1 = l1.next
                else:
                    pointer.next = l2
                    l2 = l2.next
                pointer = pointer.next
            if l1:
                pointer.next = l1
            if l2:
                pointer.next = l2
            return head.next
                
        while interval<length:
            for i in range(0, length-interval, interval*2):
                lists[i] = merge(lists[i], lists[i+interval])
            interval *= 2
        return lists[0]

'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        pointer = dummy
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for node in sorted(nodes):
            pointer.next = ListNode(node)
            pointer = pointer.next
        return dummy.next
