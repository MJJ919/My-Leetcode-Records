'''
https://leetcode.com/problems/valid-anagram/
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):  return False
        d1,d2 = defaultdict(int),defaultdict(int)
        for i in range(len(s)):
            d1[s[i]] += 1
            d2[t[i]] += 1
        return d1==d2
    
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
