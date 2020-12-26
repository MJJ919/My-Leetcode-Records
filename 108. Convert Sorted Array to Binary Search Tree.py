'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
'''
Preorder + BFS
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left, right):
            if left > right:
                return None
            p = (left+right)//2
            root = TreeNode(nums[p])
            root.left = helper(left, p-1)
            root.right = helper(p+1, right)
            return root
        
        return helper(0, len(nums)-1)
