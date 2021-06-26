'''
https://leetcode.com/problems/number-of-closed-islands/
Given a 2D grid consists of 0s (land) and 1s (water).  
An island is a maximal 4-directionally connected group of 0s and a closed 
island is an island totally (all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.

Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
'''
'''
Time:O(mn)
Space:O(mn)
'''
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            nonlocal flag
            if r<0 or r==m or c<0 or c==n or grid[r][c]==1:
                return
            if r==0 or c==0 or r==m-1 or c==n-1 and grid[r][c]==0:
                flag = False
            grid[r][c] = 1
            for row, col in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                dfs(row, col)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    flag = True
                    dfs(i, j)
                    if flag:
                        count += 1
        return count
