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
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

'''
Time:O(N)
Space:O(N)
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self,root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    construct(root.right, path)
                    construct(root.left, path)
        
        paths=[]
        construct(root, '')
        return paths
