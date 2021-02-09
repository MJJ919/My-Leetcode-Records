'''
https://leetcode.com/problems/dungeon-game/
'''
'''
Time:O(m*n)
Space:O(m*n)
'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf') for _ in range(n)]for _ in range(m)]
        
        def getmin(curcell, row, col):
            if row>=m or col>=n:
                return float('inf')
            return max(1, dp[row][col]-curcell)
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                curcell = dungeon[i][j]
                right = getmin(curcell, i, j+1)
                down = getmin(curcell, i+1, j)
                update = min(right, down)
                if update != float('inf'):
                    dp[i][j] = update
                else:
                    dp[i][j] = max(1, 1-curcell)
        print(dp)
        return dp[0][0]
