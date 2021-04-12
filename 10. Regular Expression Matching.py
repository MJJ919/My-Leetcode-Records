'''
https://leetcode.com/problems/regular-expression-matching/
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

'''
'''
Time:O(n**2)
Space:O(n**2)
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)]for _ in range(len(s)+1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                first = i<len(s) and p[j] in {s[i], '.'}
                if j+1<len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or (first and dp[i+1][j])
                else:
                    dp[i][j] = first and dp[i+1][j+1]
        return dp[0][0]
'''
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first = bool(s) and p[0] in {s[0], '.'}
        if len(p)>=2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first and self.isMatch(s[1:], p))
        else:
            return first and self.isMatch(s[1:], p[1:])
