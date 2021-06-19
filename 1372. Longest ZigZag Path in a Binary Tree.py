'''
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
You are given the root of a binary tree.
A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def traverse(node, split):
            nonlocal res
            if not node:
                return 0
            left = traverse(node.left, True)
            right = traverse(node.right, False)
            res = max(res, left, right)
            return 1+right if split else 1+left
        
        res = 0
        traverse(root, True)
        return res
