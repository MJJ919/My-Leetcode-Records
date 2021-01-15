'''
https://leetcode.com/problems/walls-and-gates/
You are given an m x n grid rooms initialized with these three possible values.
-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
'''
'''
'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def dfs(r,c, dis):
            if r<0 or r>=row or c<0 or c>= col or rooms[r][c]==-1:
                return
            if dis<=rooms[r][c]:
                rooms[r][c] = dis
                for i,j in ((0,1),(0,-1),(1,0),(-1,0)):
                    dfs(r+i, c+j, dis+1)
                
        
        row, col = len(rooms), len(rooms[0])
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
        return rooms
