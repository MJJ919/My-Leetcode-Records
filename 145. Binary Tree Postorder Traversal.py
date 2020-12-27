'''
https://leetcode.com/problems/binary-tree-postorder-traversal/
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]
'''
'''
Recursion
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def postorderTraversal(self, root):
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
            self.rec(node.right,res)
            res.append(node.val)
'''
Iteration
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def postorderTraversal(self, root):
        res, s = [],[]
        while True:
            while root:
                res.append(root.val)
                s.append(root)
                root = root.right
            if not s:
                return res[::-1]
            node = s.pop()
            root = node.left
