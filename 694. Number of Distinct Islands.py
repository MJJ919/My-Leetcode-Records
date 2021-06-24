'''
https://leetcode.com/problems/number-of-distinct-islands/
You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only 
if one island can be translated (and not rotated or reflected) to equal the other.
Return the number of distinct islands.

Example 1:
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1
'''
'''
Time:O(mn)
Space:O(mn)
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seenisland = set()   
        def dfs(r,c):
            if r<0 or r==m or c<0 or c==n or grid[r][c]==0:
                return
            grid[r][c] = 0
            island.add((r-row,c-col))
            for newrow, newcol in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                dfs(newrow, newcol)
                     
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row, col = i, j
                    island = set()
                    dfs(i, j)
                    seenisland.add(frozenset(island))
        return len(seenisland)
