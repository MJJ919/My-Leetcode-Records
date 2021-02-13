'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
'''
'''
Recursion
Time:O(n)
Space:O(n)
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
        inorder(root)
        return res
            
'''
Iteration
Time:O(n)
Space:O(n)
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        visited = []
        res = []
        while True:
            while root:
                visited.append(root)
                root = root.left
            if not visited:
                return res
            node = visited.pop()
            res.append(node.val)
            root = node.right
        return res
