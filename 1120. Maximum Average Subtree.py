'''
https://leetcode.com/problems/maximum-average-subtree/
Given the root of a binary tree, find the maximum average value of any subtree of that tree.
(A subtree of a tree is any node of that tree plus all its descendants. 
The average value of a tree is the sum of its values, divided by the number of nodes.)

Example 1:
Input: [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def traverse(node):
            nonlocal res
            if not node:
                return (0, 0)
            leftval, leftcnt = traverse(node.left)
            rightval, rightcnt = traverse(node.right)
            leftavg = leftval/leftcnt if leftcnt!=0 else 0
            rightavg = rightval/rightcnt if rightcnt!=0 else 0
            res = max(res, (leftval+rightval+node.val)/(leftcnt+rightcnt+1), leftavg, rightavg)
            return (leftval+rightval+node.val, leftcnt+rightcnt+1)
        
        res = float('-inf')
        traverse(root)
        return res
