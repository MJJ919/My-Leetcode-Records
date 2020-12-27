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
Iteration.
Time:O(k)
Space:O(k)
'''
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        s, pre = [], float('-inf')
        while s or root:
            while root:
                s.append(root)
                root = root.left
            node = s.pop()
            if node.val > target and pre <= target:
                return min(node.val, pre, key = lambda x:abs(target-x))
            pre = node.val
            root = node.right
        return pre
 
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
