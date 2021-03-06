'''
https://leetcode.com/problems/recover-binary-search-tree/
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. 
Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            nonlocal n1, n2, pre
            if node:
                traverse(node.left)
                if pre.val >= node.val:
                    if not n1:
                        n1 = pre
                    n2 = node
                pre = node
                traverse(node.right)
                
        pre = TreeNode(float(-inf))
        n1 = None
        n2 = None
        traverse(root)
        n1.val, n2.val = n2.val, n1.val
