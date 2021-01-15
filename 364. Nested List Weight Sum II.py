'''
https://leetcode.com/problems/nested-list-weight-sum-ii/
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:
Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.
'''
'''
Time:O(n)
Space:O(depth)
'''
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        cache, self.maxlevel = defaultdict(int), 0
        self.dfs(nestedList, 1, cache)
        res = 0
        for depth, num in cache.items():
            res += num*(self.maxlevel-depth+1)
        return res
    
    def dfs(self, l, depth, cache):
            self.maxlevel = max(self.maxlevel, depth)
            for i in l:
                if i.isInteger():
                    cache[depth] += i.getInteger()
                else:   
                    self.dfs(i.getList(), depth+1, cache)
 
 class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        total, level = 0, 0
        while nestedList:
            nextlevel = []
            for i in nestedList:
                if i.isInteger():
                    level += i.getInteger()
                else:
                    for j in i.getList():
                        nextlevel.append(j)
            total += level
            nestedList = nextlevel
        return total
