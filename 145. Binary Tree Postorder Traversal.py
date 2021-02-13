'''
https://leetcode.com/problems/binary-tree-postorder-traversal/
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]
'''
'''
Recursion
Time:O(n)
Space:O(n)
'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                res.append(node.val)            
        res = []
        postorder(root)
        return res
    
'''
Iteration
Time:O(n)
Space:O(n)
'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        visited = []
        while True:
            while root:
                res.append(root.val)
                visited.append(root)
                root = root.right
            if not visited:
                return res[::-1]
            node = visited.pop()
            root = node.left
