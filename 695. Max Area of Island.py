'''
https://leetcode.com/problems/max-area-of-island/
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
'''
'''
Time:O(r*c)
Space:O(r*c)
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        def dfs(row, col):
            if row<0 or row>=m or col<0 or col>=n or grid[row][col]==0:
                return 0
            count = 1
            grid[row][col] = 0
            for [p, q] in directions:
                count += dfs(row+p, col+q)
            return count
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res = max(res, dfs(i, j))
        return res
