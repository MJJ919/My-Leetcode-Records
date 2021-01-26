'''
https://leetcode.com/problems/isomorphic-strings/submissions/
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            a, b = s[i], t[i]
            if a not in d1:
                d1[a] = i
            if b not in d2:
                d2[b] = i
            if d1[a]!=d2[b]:
                return False
        return True
                   
'''
Time:O(n)
Spaec:O(1)
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        return len(s)==len(t) and len(set(zip(s,t)))==len(set(s))==len(set(t))

'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        return [s.find(i) for i in s] == [t.find(j) for j in t]
