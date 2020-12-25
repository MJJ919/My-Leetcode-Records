'''
https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:    
            return True
        return abs(self.helper(root.left)-self.helper(root.right)) < 2 and self.isBalanced(root.right) and self.isBalanced(root.left)
    
    def helper(self, node):
            if not node:
                return -1
            else:   
                return 1+max(self.helper(node.left),self.helper(node.right))
