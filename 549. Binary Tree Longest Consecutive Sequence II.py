'''
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
Given the root of a binary tree, return the length of the longest consecutive path in the tree.
This path can be either increasing or decreasing.

For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.
On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input: root = [1,2,3]
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def traverse(node):
            nonlocal res
            inc, dec = 1, 1
            if node.left:
                left = traverse(node.left)
                if node.val+1 == node.left.val:
                    dec = left[1]+1
                elif node.val-1 == node.left.val:
                    inc = left[0]+1
            if node.right:
                right = traverse(node.right)
                if node.val+1 == node.right.val:
                    dec = max(dec, right[1]+1)
                elif node.val-1 == node.right.val:
                    inc = max(inc, right[0]+1)
            res = max(res, inc+dec-1)
            return [inc, dec]
        
        res = 0
        traverse(root)
        return res
