'''
https://leetcode.com/problems/out-of-boundary-paths/
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. 
You are allowed to move the ball to one of the four adjacent four cells in the grid 
(possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, 
return the number of paths to move the ball out of the grid boundary. 
Since the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
'''
'''
Time:O(move*m*n)
Space:O(mn)
'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9+7
        dp = [[0 for _ in range(n)]for _ in range(m)]
        dp[startRow][startColumn] = 1
        count = 0
        for _ in range(1, maxMove+1):
            temp = [[0 for _ in range(n)]for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i==0:
                        count += dp[i][j]%mod
                    if i==m-1:
                        count += dp[i][j]%mod
                    if j==0:
                        count += dp[i][j]%mod
                    if j==n-1:
                        count += dp[i][j]%mod
                    if i>0:
                        temp[i][j] += dp[i-1][j]%mod
                    if i<m-1:
                        temp[i][j] += dp[i+1][j]%mod
                    if j>0:
                        temp[i][j] += dp[i][j-1]%mod
                    if j<n-1:
                        temp[i][j] += dp[i][j+1]%mod
            dp = temp
        return count%mod
      
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = [[[-1 for _ in range(n)]for _ in range(m)]for _ in range(maxMove+1)]
        mod = 10**9+7
        
        def find(row, col, move):
            if row<0 or row==m or col<0 or col==n:
                return 1
            if move==0:
                return 0
            if memo[move][row][col]>=0:  return memo[move][row][col]
            memo[move][row][col] = (find(row-1, col, move-1)%mod + find(row+1, col, move-1)%mod + find(row, col-1, move-1)%mod + find(row, col+1, move-1)%mod) %mod
            return memo[move][row][col]
        
        return find(startRow, startColumn, maxMove)
