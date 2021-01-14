'''
https://leetcode.com/problems/number-of-islands/
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
'''
'''
DFS
Time:O(M*N)
Space:O(M*N)
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if r>=row or r<0 or c>=col or c<0 or grid[r][c]=='0':
                return 
            grid[r][c] = '0'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            
        row, col = len(grid), len(grid[0])
        num = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    num += 1
                    dfs(i, j)
        return num
