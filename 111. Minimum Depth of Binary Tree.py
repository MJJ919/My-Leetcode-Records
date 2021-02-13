'''
https://leetcode.com/problems/minimum-depth-of-binary-tree/
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif not root.left:
            return self.minDepth(root.right)+1
        elif not root.right:
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def helper(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                self.res = min(self.res, depth)
            helper(node.left, depth+1)
            helper(node.right, depth+1)
        
        self.res = float('inf')
        helper(root, 1)
        return self.res if self.res!=float('inf') else 0
