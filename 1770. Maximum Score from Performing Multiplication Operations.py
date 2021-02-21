'''
https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.
You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.

Example 1:
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
'''
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        dp = [[float('-inf')for _ in range(m+1)]for _ in range(m+1)]
        for i in range(m+1):
            for j in range(m+1):
                if i+j>m:
                    break
                if i==0 and j==0:
                    dp[i][j] = 0
                elif i==0:
                    dp[i][j] = dp[i][j-1] + nums[-j]*multipliers[j-1]
                elif j==0:                        
                    dp[i][j] = dp[i-1][j] + nums[i-1]*multipliers[i-1]
                else:
                    dp[i][j] = max(dp[i-1][j]+nums[i-1]*multipliers[i+j-1], dp[i][j-1]+nums[-j]*multipliers[i+j-1])
        
        res = float('-inf')
        for i in range(m+1):
            res = max(res,dp[i][m-i])
        return res
