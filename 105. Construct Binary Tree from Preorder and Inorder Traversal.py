'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:    return None
            rootval = preorder[self.preidx]
            root = TreeNode(rootval)
            
            self.preidx += 1
            idx = d[rootval]
            root.left = helper(left, idx-1)
            root.right = helper(idx+1, right)
            return root
        
        self.preidx = 0   
        d = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)
