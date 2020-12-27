'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]
'''
'''
Recursion
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.rec(root, res)
        return res
    
    def rec(self, node, res):
        if node:
            res.append(node.val)
            self.rec(node.left, res)
            self.rec(node.right, res)

'''
Iteration
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def preorderTraversal(self, root):
        res, s = [], []
        while True:
            while root:
                res.append(root.val)
                s.append(root)
                root = root.left
            if not s:
                return res
            node = s.pop()
            root = node.right
