'''
https://leetcode.com/problems/unique-binary-search-trees-ii/
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
'''
'''
Time:
Space:
'''
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def construct(left, right):
            res = []
            if left>right:
                res.append(None)
            for i in range(left, right+1):
                leftside = construct(left, i-1)
                rightside = construct(i+1, right)
                for leftnode in leftside:
                    for rightnode in rightside:
                        node = TreeNode(i)
                        node.left = leftnode
                        node.right = rightnode
                        res.append(node)
            return res
        
        
        return construct(1, n)
