'''
https://leetcode.com/problems/invert-binary-tree/
Invert a binary tree.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)        
        return root
    
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
