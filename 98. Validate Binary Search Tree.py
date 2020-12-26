'''
https://leetcode.com/problems/validate-binary-search-tree/
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
'''
Time:
Space:
'''
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        return helper(root, -float("inf"), float("inf"))
