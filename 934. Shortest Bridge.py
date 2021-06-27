'''
https://leetcode.com/problems/shortest-bridge/
In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)
Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1
'''
'''
Time:O(mn)
Space:O(mn)
'''
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        flag = False
        q = deque()
        visited = [[False for _ in range(n)]for _ in range(m)]
        step = 0
        def dfs(r, c):
            if r==m or c==n or r<0 or c<0 or grid[r][c]==0 or visited[r][c]:
                return 
            q.append([r,c])
            visited[r][c] = True
            for row, col in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                dfs(row, col)
            
        for i in range(m):
            for j in range(n):
                if not flag and grid[i][j]==1:
                    dfs(i, j)
                    flag = True
                    break
                    
        while q:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for row, col in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                    if 0<=row<m and 0<=col<n and not visited[row][col]:
                        if grid[row][col] == 1:
                            return step
                        visited[row][col] = True
                        q.append([row, col])
            step += 1
        
