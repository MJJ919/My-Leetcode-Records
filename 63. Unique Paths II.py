'''
https://leetcode.com/problems/unique-paths-ii/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.
'''
'''
Time:O(M×N).
Space:O(1)
'''
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return 0
        grid[0][0] = 1
        m, n = len(grid), len(grid[0])
        for i in range(1,m):
            grid[i][0]=1 if (grid[i][0]==0 and grid[i-1][0]==1) else 0
        for i in range(1,n):
            grid[0][i]=1 if (grid[0][i]==0 and grid[0][i-1]==1) else 0
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j]==0:
                    grid[i][j] = grid[i-1][j]+grid[i][j-1]
                else:
                    grid[i][j] = 0
        return grid[-1][-1]
