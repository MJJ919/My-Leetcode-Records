'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
'''
Time:
Space:
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.rec(root, res)
        return res
    
    def rec(self, node, res):
        if node:
            self.rec(node.left, res)
            res.append(node.val)
            self.rec(node.right, res)
