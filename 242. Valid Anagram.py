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
Method below uses dictionary.
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        for i in s:
            if i in dict1:
                dict1[i] = dict1[i]+1
            else:
                dict1[i]=0
        dict2 = {}
        for i in t:
            if i in dict2:
                dict2[i] = dict2[i]+1
            else:
                dict2[i]=0
        return dict1 == dict2
        
'''
Meethod below uses sorted function.
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
