'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        else:
            return None

'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        d = {root:None}
        while p not in d or q not in d:
            node = stack.pop()
            if node.left:
                d[node.left]=node
                stack.append(node.left)
            if node.right:
                d[node.right]=node
                stack.append(node.right)
        before = set()
        while p:
            before.add(p)
            p = d[p]
        while q not in before:
            q = d[q]
        return q 
