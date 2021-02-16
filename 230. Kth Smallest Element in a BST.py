'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
'''
'''
Time:O(n)
Space:O(k)
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nums = []
        stack = []
        s = 1
        while True:
            while root:
                stack.append(root)
                root = root.left
            if k<=len(nums):
                return nums[k-1]
            root = stack.pop()
            nums.append(root.val)
            root = root.right
