'''
https://leetcode.com/problems/number-of-provinces/
There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and
the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
'''
'''
Time:O(n**2)
Space:O(n)
'''
class Solution:
    def findCircleNum(self, isCon: List[List[int]]) -> int:
        m = len(isCon)
        visited = [0 for _ in range(m)]
        def dfs(cur):
            for j in range(m):
                if isCon[cur][j]==1 and visited[j]==0:
                    visited[j]=1
                    dfs(j)
                
        res = 0
        for i in range(m):
            if visited[i]==0:
                dfs(i)
                res += 1
        return res
