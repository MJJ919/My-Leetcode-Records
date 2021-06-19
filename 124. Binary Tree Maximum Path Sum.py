'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
in the sequence has an edge connecting them. A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

'''
'''
Time:O(n)
Space:O(H)
'''
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def traverse(node):
            nonlocal res
            if not node:
                return 0
            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)
            current = node.val + left + right
            res = max(res, current)
            return node.val + max(left, right)
        
        res = float('-inf')
        traverse(root)
        return res
