'''
https://leetcode.com/problems/guess-number-higher-or-lower-ii/
'''
'''
Time:O(n**3)
Space:O(n**2)
'''
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for _ in range(n+1)]for _ in range(n+1)]
        for len in range(2, n+1):
            for start in range(1, n-len+2):
                minres = float('inf')
                for piv in range(start, start+len-1):
                    res = piv+max(dp[start][piv-1], dp[piv+1][start+len-1])
                    minres = min(res, minres)
                dp[start][start+len-1] = minres
        return dp[1][n]
