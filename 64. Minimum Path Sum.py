'''
https://leetcode.com/problems/minimum-path-sum/
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''

'''
Method below uses inplace dynamic programming.
Time:O(M*N)
Space:O(1)Since no extra space needed.
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i,j=len(grid),len(grid[0])
        for a in range(1,i):
            grid[a][0] += grid[a-1][0]
        for b in range(1,j):
            grid[0][b] += grid[0][b-1]
        for a in range(1,i):
            for b in range(1,j):
                grid[a][b] += min(grid[a-1][b],grid[a][b-1])
        return grid[-1][-1]
