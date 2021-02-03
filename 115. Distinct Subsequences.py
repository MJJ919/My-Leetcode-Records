'''
https://leetcode.com/problems/distinct-subsequences/
Given two strings s and t, return the number of distinct subsequences of s which equals t.
A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
It's guaranteed the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
'''
'''
Time:O(M×N)
Space:O(M×N)
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def recurse(i, j):
            if i==len(s) or j==len(t) or len(s)-i<len(t)-j:
                return int(j==len(t))
            if (i,j) in memo:
                return memo[i,j]
            ans = recurse(i+1, j)
            if s[i]==t[j]:
                ans += recurse(i+1, j+1)
            memo[i,j] = ans 
            return ans       
        return recurse(0, 0)
        
'''
Time:O(M×N)
Space:O(M×N)
'''        
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t)+1)]for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][-1] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                ans = dp[i+1][j]
                if s[i] == t[j]:
                    ans += dp[i+1][j+1]
                dp[i][j] = ans
        return dp[0][0]
