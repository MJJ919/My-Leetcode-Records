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
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        l = self.values(head)
        
        def buildtree(i, j):
            if i>j:
                return None
            mid = (i+j)//2
            node = TreeNode(l[mid])
            
            if i == j:
                return node
            node.left = buildtree(i, mid-1)
            node.right = buildtree(mid+1, j)
            return node
        
        return buildtree(0, len(l)-1)
        
    def values(self, head):
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l
