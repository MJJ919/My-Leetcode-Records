'''
https://leetcode.com/problems/palindromic-substrings/
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
'''
Time:O(n**2)
Space:O(1)
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(s,i,j):
            number = 0
            while i>=0 and j<=len(s)-1:
                if s[i]!=s[j]:
                    break
                i, j = i-1, j+1
                number += 1
            return number
        
        res = 0
        for i in range(len(s)):
            res += helper(s,i,i)
            res += helper(s,i,i+1)
        return res

'''
Time:O(n**2)
Space:O(n**2)
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [[0 for _ in range(n)]for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            res += 1
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = 1
                res += 1
        for a in range(3,n+1):
            for i in range(n-a+1):
                j = i+a-1
                if dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j] = 1
                    res += 1
        return res
