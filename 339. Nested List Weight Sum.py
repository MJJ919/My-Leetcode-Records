'''
https://leetcode.com/problems/nested-list-weight-sum/solution/
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.
'''
'''
Time:O(n)
Space:O(d)
'''
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(l, depth):
            s = 0
            for i in l:
                if i.isInteger():
                    s += i.getInteger()*depth
                else:
                    s += dfs(i.getList(), depth+1)
            return s
        
        return dfs(nestedList, 1)
