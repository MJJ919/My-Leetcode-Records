'''
https://leetcode.com/problems/longest-common-subsequence/
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) 
deleted without changing the relative order of the remaining characters.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
'''
'''
Time:O(mn)
Space:O(m)
'''
class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        if len(t1)>len(t2):
            t1, t2 = t2, t1
        pre = [0 for _ in range(len(t1)+1)]
        cur = [0 for _ in range(len(t1)+1)]
        for j in range(1, len(t2)+1):
            for i in range(1, len(t1)+1):
                if t1[i-1] == t2[j-1]:
                    cur[i] = pre[i-1]+1
                else:
                    cur[i] = max(pre[i], cur[i-1])
            pre = cur[:]
        return pre[-1]
   
'''
Time:O(mn)
Space:O(mn)
'''
class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        m = len(t1)
        n = len(t2)
        memo = [[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if t1[i]==t2[j]:
                    memo[i+1][j+1] = 1 + memo[i][j]
                else:
                    memo[i+1][j+1] = max(memo[i+1][j], memo[i][j+1])
        return memo[-1][-1]
