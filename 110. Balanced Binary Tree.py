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
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def traverse(node):
            if not node:
                return -1
            return 1+max(traverse(node.left), traverse(node.right))
            
        if not root:
            return True
        return abs(traverse(root.left)-traverse(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
