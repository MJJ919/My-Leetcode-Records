'''
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        pre = postorder[::-1]
        self.pos = 0
        def builder(left, right):
            if left>right:
                return None
            rootval = pre[self.pos]
            root = TreeNode(rootval)
            self.pos += 1
            idx = d[rootval]
            root.right = builder(idx+1, right)
            root.left = builder(left, idx-1)

            return root
        
        d = {num:idx for idx,num in enumerate(inorder)}
        return builder(0, len(pre)-1)
