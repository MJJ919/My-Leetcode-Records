'''
https://leetcode.com/problems/wildcard-matching/
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
'''
'''
Time:O(min(S,P)
Space:O(1)
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star = temp = -1
        
        while s_idx<s_len:
            if p_idx<p_len and p[p_idx] in {s[s_idx], '?'}:
                s_idx += 1
                p_idx += 1
            elif p_idx<p_len and p[p_idx] == '*':
                star = p_idx
                temp = s_idx
                p_idx += 1
            elif star == -1:
                return False
            else:
                p_idx = star + 1
                s_idx = temp + 1
                temp = s_idx
        return all(x == '*' for x in p[p_idx:])
            
'''
Time:O(min(S,P))
Space:
'''
class Solution:
    def remove(self, p):
        if p == '': return p
        p1 = [p[0]]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1)
    
    def pair(self, s, p):
        dp = self.dp
        if (s, p) in dp:
            return dp[(s, p)]
        
        if p == s or p == '*':
            dp[(s, p)] = True
        elif p == '' or s == '':
            dp[(s, p)] = False
        elif p[0] == s[0] or p[0] == '?':
            dp[(s, p)] = self.pair(s[1:], p[1:])
        elif p[0] == '*':
            dp[(s, p)] = self.pair(s, p[1:]) or self.pair(s[1:], p)
        else:
            dp[(s, p)] = False
        return dp[(s, p)]
        
    def isMatch(self, s: str, p: str) -> bool:
        p = self.remove(p)
        self.dp = {}
        return self.pair(s, p)
