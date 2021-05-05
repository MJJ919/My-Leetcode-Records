'''
https://leetcode.com/problems/largest-plus-sign/
'''
'''
Time:O(n*n)
Space:O(n*n)
'''
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        dp = [[0 for _ in range(N)]for _ in range(N)]
        res = 0
        
        for i in range(N):
            count = 0
            for j in range(N):
                count = 0 if (i, j) in banned else count+1
                dp[i][j] = count
            
            count = 0
            for j in range(N-1, -1, -1):
                count = 0 if (i, j) in banned else count+1
                dp[i][j] = min(dp[i][j], count)
            
        for j in range(N):
            count = 0
            for i in range(N):
                count = 0 if (i, j) in banned else count+1
                dp[i][j] = min(dp[i][j], count)
            
            count = 0
            for i in range(N-1, -1, -1):
                count = 0 if (i,j) in banned else count+1
                dp[i][j] = min(dp[i][j], count)
                res = max(res, dp[i][j])
        return res
