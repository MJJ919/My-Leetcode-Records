'''
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(node, path, depth):
            if node:
                if len(path) == depth:
                    path.append([])
                path[depth].append(node.val)
                helper(node.left, path, depth+1)
                helper(node.right, path, depth+1)
        
        path = []
        helper(root, path, 0)
        return path[::-1]
