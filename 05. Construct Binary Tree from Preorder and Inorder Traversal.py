'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Given preorder and inorder traversal of a tree, construct the binary tree.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(left, right):
            if left == right:    return None
            rootval = preorder[self.preidx]
            root = TreeNode(rootval)
            
            self.preidx += 1
            idx = d[rootval]
            root.left = helper(left, idx)
            root.right = helper(idx+1, right)
            return root
        
        self.preidx = 0   
        d = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder))
