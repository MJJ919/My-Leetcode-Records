'''
https://leetcode.com/problems/stone-game/
Alex and Lee play a game with piles of stones.  
There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
Alex and Lee take turns, with Alex starting first.  
Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  
This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.
'''
'''
Time:O(n**2)
Space:O(n**2)
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0 for _ in range(n)]for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for d in range(2, n+1):
            for i in range(n-d+1):
                j = i+d-1
                dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
        return  dp[0][n-1]
 
'''
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        
        @lru_cache(None)
        def dp(i, j):
            if i>j:
                return 0
            if (n-i-j)%2 == 1:
                return max(piles[i]+dp(i+1, j), piles[j]+dp(i, j-1))
            else:
                return min(-piles[i]+dp(i+1, j), -piles[j]+dp(i, j-1))
        return dp(0, n-1)>0
