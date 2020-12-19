'''
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
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = defaultdict(int), defaultdict(int)
        for i in s:
            d1[i] += 1
        for j in t:
            d2[j] += 1
        return d1 == d2
        
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
