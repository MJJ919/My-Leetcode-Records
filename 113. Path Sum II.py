'''
https://leetcode.com/problems/path-sum-ii/
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
'''
Time:
Space:
'''
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def helper(node, res, sum, path):
            if not node:
                return
            sum -= node.val
            path.append(node.val)
            if not node.left and not node.right and sum == 0:
                    res.append(list(path))
            helper(node.left, res, sum, path)
            helper(node.right, res, sum, path)
            del path[-1]
            
        res = []
        helper(root, res, sum, [])
        return res
