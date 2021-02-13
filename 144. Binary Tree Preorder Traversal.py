'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]
'''
'''
Recursion
Time:O(n)
Space:O(n)
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def preorder(node):
            if node:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return res

'''
Iteration
Time:O(n)
Space:O(n)
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        visited = []
        while True:
            while root:
                visited.append(root)
                res.append(root.val)
                root = root.left
            if not visited:
                return res
            node = visited.pop()
            root = node.right
