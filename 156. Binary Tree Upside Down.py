'''
https://leetcode.com/problems/binary-tree-upside-down/
Given the root of a binary tree, turn the tree upside down and return the new root.
You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.

The mentioned steps are done level by level, it is guaranteed that every node in the given tree has either 0 or 2 children.

Example 1:
Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]
'''
'''
Time:
Space:
'''
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:    
        if not root or not root.left:
            return root
        leftnode = self.upsideDownBinaryTree(root.left)
        root.left.right, root.left.left = root, root.right
        root.left = root.right = None
        return leftnode
