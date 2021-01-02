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
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.res = None
        
        def find( node):
            if not node:    return False
            left = find(node.left)
            right = find(node.right)
            mid = (node == p or node == q)
            if mid + left + right >=2:
                self.ans = node
            return mid or left or right
        
        find(root)
        return self.ans

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
