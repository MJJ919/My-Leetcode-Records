'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
'''

'''
The method below uses 2 dictionaries.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())
        
'''
Method below uses FIND function.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        return [s.find(i) for i in s] == [t.find(j) for j in t]
