'''
https://leetcode.com/problems/word-pattern-ii/
Given a pattern and a string s, return true if s matches the pattern.
A string s matches a pattern if there is some bijective mapping of single characters to strings such 
that if each character in pattern is replaced by the string it maps to, then the resulting string is s. 
A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

Example 1:
Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
'''
class Solution:
    def wordPatternMatch(self, p: str, s: str) -> bool:
        def back(p, s, dictp):
            if not p and not s:
                return True
            if not p and s:
                return False
            for i in range(1, len(s)-len(p)+2):
                p1 = p[0]
                s1 = s[:i]
                if p1 not in dictp and s1 not in dictp.values():
                    dictp[p1] = s1
                    if back(p[1:], s[i:], dictp):
                        return True
                    del dictp[p1]
                elif p1 in dictp and dictp[p1]==s1:
                    if back(p[1:], s[i:], dictp):
                        return True
                    else:
                        pass
            return False
        return back(p, s, {})
