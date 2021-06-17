'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. 
If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree 
T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". 
A descendant of a node x is a node y that is on the path from node x to some leaf node.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, target):
            if not node:
                return None
            if node.val == target:
                return node
            left = dfs(node.left, target)
            right = dfs(node.right, target)
            return left if left else right
        
        def lca(root):
            if not root or root==p or root==q:
                return root
            left = lca(root.left)
            right = lca(root.right)
            if left and right:
                return root
            if left:
                return left
            if right:
                return right
            return None
        
        p = dfs(root, p.val)
        q = dfs(root, q.val)
        
        if not p or not q:
            return None
        
        return lca(root)
