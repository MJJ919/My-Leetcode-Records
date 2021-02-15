'''
https://leetcode.com/problems/closest-binary-search-tree-value/
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:
Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def helper(node):
            if not node:
                return
            if abs(node.val-target)<abs(self.res-target):
                self.res = node.val
            helper(node.left)
            helper(node.right)
        
        self.res = float('inf')
        helper(root)
        return self.res
 
'''
Time:O(h)
Space:O(1)
'''
class Solution(object):
    def closestValue(self, root, target):
        closest = root.val
        while root:
            closest = min(closest, root.val, key = lambda x: abs(x - target))
            root = root.left if target < root.val else root.right
        return closest
