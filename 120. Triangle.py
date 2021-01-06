'''
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
'''
'''
Time:O(n)
Space:O(n*n)
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        res = [[float('inf')for _ in range(n)]for _ in range(n)]
        res[0][0] = triangle[0][0]
        for i in range(1,n):
            for j in range(len(triangle[i])):
                val = res[i-1][j] if j==0 else min(res[i-1][j-1], res[i-1][j-1])
                res[i][j] = triangle[i][j]+val
        return min(res[-1])
