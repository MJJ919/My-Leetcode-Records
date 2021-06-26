'''
https://leetcode.com/problems/making-a-large-island/
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
'''
'''
Time:O(n*n)
Space:O(n*n)
'''
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = [i for i in range(m*n)]
        size = [1 for _ in range(m*n)]
        res = 0
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            r1, r2 = find(i), find(j)
            if r1==r2:
                return 
            if size[r1]>=size[r2]:
                size[r1] += size[r2]
                parent[r2] = r1
            else:
                size[r2] += size[r1]
                parent[r1] = r2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    for r, c in ((i+1,j), (i-1,j), (i,j-1), (i,j+1)):
                        if r==m or r<0 or c==n or c<0 or grid[r][c]==0:
                            continue
                        union(r*n+c, i*n+j)
                    res = max(res, size[find(i*n+j)])
        print(size)
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    d = {}
                    for r, c in ((i+1,j), (i-1,j), (i,j-1), (i,j+1)):
                        if r==m or r<0 or c==n or c<0 or grid[r][c]==0:
                            continue
                        d[find(r*n+c)] = size[find(r*n+c)]
                    res = max(res, sum(i for i in d.values())+1)
        return res
