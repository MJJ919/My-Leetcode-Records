'''
https://leetcode.com/problems/minimum-sideway-jumps/
'''
'''
Time:O(n**3)
Space:O(n)
'''
class Solution:
    def minSideJumps(self, o: List[int]) -> int:
        length = len(o)-1
        dp = [[0 for _ in range(3)]for _ in range(length)]
        dp[0][0] = dp[0][2] = 1
        for i in range(1, length):
            for j in range(3):
                if j == o[i]-1 or j == o[i+1] -1:
                    dp[i][j] = float('inf')
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][(j+1)%3] + 1, dp[i-1][(j+2)%3] + 1)
        return min(dp[-1])
