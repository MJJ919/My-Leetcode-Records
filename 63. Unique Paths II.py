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
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:   return 0
        obstacleGrid[0][0]=1
            
        for i in range(1,m):
            obstacleGrid[i][0]=int(obstacleGrid[i][0]==0 and obstacleGrid[i-1][0]==1)
        for i in range(1, n):
            obstacleGrid[0][i]=int(obstacleGrid[0][i]==0 and obstacleGrid[0][i-1]==1)
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else:   obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]
