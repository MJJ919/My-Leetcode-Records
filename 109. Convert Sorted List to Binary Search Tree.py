'''
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        def helper(left, right):
            if left>right:
                return None
            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
            return root
        return helper(0, len(nums)-1)
    
'''
Time:O(nlgn)
Space:O(nlgn)
'''
class Solution:
    def findmid(self, head):
        fast = slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:    return None
        mid = self.findmid(head)
        root = TreeNode(mid.val)
        if head==mid:
            return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
