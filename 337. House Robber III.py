'''
https://leetcode.com/problems/house-robber-iii/
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 2:
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''
'''
Bottom-up.
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper():
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            rob = node.val + left[1] + right[1]
            notrob = max(left) + max(right)
            return [rob, notrob]
        
        return max(helper(root))
