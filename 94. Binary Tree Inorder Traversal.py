'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
'''
'''
Recursion
Time:O(n)
Space:O(n)
'''
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
            
'''
Iteration
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def inorderTraversal(self, root):
        res, s = [],[]
        while True:
            while root:
                s.append(root)
                root = root.left
            if not s:
                return res
            node = s.pop()
            res.append(node.val)
            root = node.right
