'''
https://leetcode.com/problems/longest-valid-parentheses/
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:   return 0
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i]==')':
                if s[i-1]=='(':
                    if i>=2:
                        dp[i] = dp[i-2]+2
                    else:
                        dp[i] = 2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(':
                    if i-dp[i-1]>=2:
                        dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2 
                    else:
                        dp[i] = dp[i-1]+2
        return max(dp)
