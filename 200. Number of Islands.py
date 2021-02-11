'''
https://leetcode.com/problems/number-of-islands/
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
'''
'''
DFS
Time:O(M*N)
Space:O(M*N)
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        direction = [[1,0], [0,1], [-1, 0], [0, -1]]
        def find(row, col):
                if row<0 or row>=m or col<0 or col>=n or grid[row][col]=='0':
                    return
                grid[row][col] = '0'
                for [k, j] in direction:
                    find(row+k, col+j)
                
        count = 0            
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    find(i, j)
                    count += 1
        return count
