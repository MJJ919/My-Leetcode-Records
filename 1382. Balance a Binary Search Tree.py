'''
https://leetcode.com/problems/balance-a-binary-search-tree/
Given a binary search tree, return a balanced binary search tree with the same node values.
A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.
If there is more than one answer, return any of them.

Example 1:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            nums.append(root.val)
            traverse(root.right)
        
        def construct(nums):
            if not nums:
                return
            idx = len(nums)//2
            node = TreeNode(nums[idx])
            node.left = construct(nums[:idx])
            node.right = construct(nums[idx+1:])
            return node
        
        traverse(root)
        return construct(nums)
