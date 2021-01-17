'''
https://leetcode.com/problems/maximal-rectangle/
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
'''
'''
Time:O(n^3)
Space:O(n^2)
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        area = 0
        dp = [[0for _ in range(len(matrix[0])+1)]for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='0':    continue
                width = dp[i][j] = dp[i][j-1]+1 if j else 1
                for k in range(i,-1,-1):
                    width = min(width, dp[k][j])
                    area = max(area, width*(i-k+1))
        return area
