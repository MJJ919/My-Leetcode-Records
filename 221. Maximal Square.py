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
        return s*shttps://leetcode.com/problems/maximal-square/
