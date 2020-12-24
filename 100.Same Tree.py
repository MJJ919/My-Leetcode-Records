'''
https://leetcode.com/problems/same-tree/
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''
'''
Time:O(n)
Space:  
Best Case: Balanced Tree:   O(lg N)
Worst Case: Completely Unbalanced Tree  O(N)
'''
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not q or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and isSameTree(p.left, p.right)
