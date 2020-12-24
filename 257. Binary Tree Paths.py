'''
https://leetcode.com/problems/binary-tree-paths/
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]
'''
'''
Time:O(N)
Space:O(N)
'''
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def helper(node, path):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                res.append(path)
            path += '->'
            helper(node.left, path)
            helper(node.right, path) 
        
        res = []
        helper(root, '')
        return res
