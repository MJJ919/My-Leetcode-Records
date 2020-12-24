'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, path):
            if not node:
                return
            path = path + str(node.val)
            if not node.left and not node.right:
                res.append(path)
            helper(node.left, path)
            helper(node.right, path)
            
        res = []
        helper(root, '')
        return sum(int(i) for i in res)
