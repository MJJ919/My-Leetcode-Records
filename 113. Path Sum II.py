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
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def helper(node, target, path):
            if not node:
                return
            path.append(node.val)
            target -= node.val
            if not node.left and not node.right and target==0:
                self.res.append(path[:])  
            helper(node.left, target, path)
            helper(node.right, target, path)
            del path[-1]
        self.res = []
        helper(root, target, [])
        return self.res
