'''
https://leetcode.com/problems/one-edit-distance/
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:
Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
 
Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.

Example 2:
Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.

'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s)-len(t))>1 or s==t:
            return False
        flag = False
        i, j = 0,0
        while i<len(s) and j<len(t):
            if s[i] != t[j]:
                if flag:    return False
                flag = True
                if len(s)<len(t):   i -= 1
                elif len(s)>len(t): j -= 1
            i, j = i+1, j+1
        return True

'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def isOneEditDistance(self, s, t):
        m, n = len(s), len(t)
        if m < n:
            return self.isOneEditDistance(t,s)
        if m-n > 1: return False
        for i in range(n):
            if s[i] != t[i]:
                if m == n:   return s[i+1:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:]
        return n+1 == m
