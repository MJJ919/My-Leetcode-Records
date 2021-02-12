'''
https://leetcode.com/problems/pacific-atlantic-water-flow/
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, 
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
'''
'''
'''
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:  return[]
        m, n = len(matrix), len(matrix[0])
        visited_p = [[False for _ in range(n)]for _ in range(m)]
        visited_a = [[False for _ in range(n)]for _ in range(m)]
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        res = []
        
        def dfs(row, col, visited):
            visited[row][col] = True
            for (p,q) in directions:
                if row+p<0 or col+q<0 or row+p>=m or col+q>=n or visited[row+p][col+q]==True or matrix[row][col]>matrix[row+p][col+q]:  continue
                else:
                    dfs(row+p, col+q, visited)
            
        for i in range(m):
            dfs(i, 0, visited_p)
            dfs(i, n-1, visited_a)
        for j in range(n):
            dfs(0, j, visited_p)
            dfs(m-1, j, visited_a)
        
        for i in range(m):
            for j in range(n):
                if visited_a[i][j] and visited_p[i][j]:
                    res.append([i, j])
        return res
