'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to 
the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node:
                return
            if not node.left and not node.right:
                return node
            lefttail = helper(node.left)
            righttail = helper(node.right)
            
            if lefttail:
                lefttail.right = node.right
                node.right = node.left
                node.left = None
            return righttail if righttail else lefttail
        return helper(root)
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
t return anything, modify root in-place instead.
        if not root:
            return None
        node = root
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
