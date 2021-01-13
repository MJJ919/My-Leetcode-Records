'''
https://leetcode.com/problems/bomb-enemy/
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:
Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
'''
'''
Time:O(W⋅H⋅(W+H))
Space:O(1)
'''
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        def bomb(r,c):
            kill = 0
            row1 = row2 = r; col1 = col2 = c;
            while row1>=0:
                if grid[row1][c]=='E':
                    kill += 1
                elif grid[row1][c]=='W':
                    break
                row1 -= 1
            while row2<=len(grid)-1:
                if grid[row2][c]=='E':
                    kill += 1
                elif grid[row2][c]=='W':
                    break
                row2 += 1
            while col1>=0:
                if grid[r][col1]=='E':
                    kill += 1
                elif grid[r][col1]=='W':
                    break
                col1 -= 1
            while col2<=len(grid[0])-1:
                if grid[r][col2]=='E':
                    kill += 1
                elif grid[r][col2]=='W':
                    break
                col2 += 1
            return kill
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='0':
                    res = max(res, bomb(i,j))
        return res
