'''
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
Given an array of integers preorder, which represents the preorder 
traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.
A binary search tree is a binary tree where for every node, any descendant of Node.
left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.
A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

Example 1:
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def bstFromPreorder(self, p: List[int]) -> TreeNode:
        def construct(left, right):
            if not p:   return None
            num = p[0]
            if num>right or num<left:
                return None
            node = TreeNode(num)
            del p[0]
            node.left = construct(left, num)
            node.right = construct(num, right)
            return node
        return construct(float('-inf'), float('inf'))
