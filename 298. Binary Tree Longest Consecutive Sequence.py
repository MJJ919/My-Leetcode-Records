'''
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The longest consecutive path need to be from parent to child (cannot be the reverse).
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def helper(node, val, count):
            if not node:    return
            if node:
                if node.val==val+1:
                    count+=1
                else:
                    count = 1
                self.res = max(self.res, count)
                helper(node.left, node.val, count)
                helper(node.right, node.val, count)
            return count
        
        self.res = 0
        helper(root, 0, 0)      
        return self.res
