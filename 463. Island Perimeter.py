'''
https://leetcode.com/problems/island-perimeter/
You are given row x col grid representing a map where grid[i][j] = 1 
represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island 
(i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        
        def find(r, c):
            return search(r-1, c)+search(r+1, c)+search(r, c+1)+search(r, c-1)
        
        def search(r, c):
            if r<0 or r==m:
                return 1
            if c<0 or c==n:
                return 1
            return 1-grid[r][c]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res += find(i, j)
        return res
