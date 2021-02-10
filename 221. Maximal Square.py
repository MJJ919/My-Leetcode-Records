'''
https://leetcode.com/problems/maximal-square/
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
'''
'''
Time:O(mn)
Space:O(mn)
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        s = 0
        dp = [[0]*(len(matrix[0])+1)for _ in range(len(matrix)+1)] 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    dp[i+1][j+1]=min(dp[i][j+1], dp[i+1][j], dp[i][j])+1
                    s = max(s, dp[i+1][j+1])
        return s*s
    
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)]for _ in range(m)]
        res = 0
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            res = max(res, dp[i][0])
        for j in range(1, n):
            dp[0][j] = int(matrix[0][j])
            res = max(res, dp[0][j])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]=='1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1  
                    res = max(res, dp[i][j])
        print(dp)
        return res*res
