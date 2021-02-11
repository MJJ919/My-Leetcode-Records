'''
https://leetcode.com/problems/walls-and-gates/
You are given an m x n grid rooms initialized with these three possible values.
-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
'''
'''
Time:O(mn)
Space:O(mn)
'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def find(row, col, step):
            if row<0 or row>=m or col<0 or col>=n or rooms[row][col] == -1:   return
            if rooms[row][col]>=step:
                rooms[row][col] = step
                for [p, q] in direction:
                    find(row+p, col+q, step+1)
                
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    find(i, j, 0)
