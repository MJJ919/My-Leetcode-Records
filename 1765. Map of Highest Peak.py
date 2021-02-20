'''
https://leetcode.com/problems/map-of-highest-peak/
'''
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1 for _ in range(n)]for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    q.append([i,j])
                    height[i][j] = 0
        while q:
            i, j = q.popleft()
            for a, b in [[1,0], [-1,0], [0,1], [0,-1]]:
                if 0<=i+a<m and 0<=j+b<n and height[i+a][j+b]==-1:
                    height[i+a][j+b] = height[i][j]+1
                    q.append([i+a, j+b])
        
        return height
