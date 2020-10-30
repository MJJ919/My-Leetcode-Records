'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

'''
Method below uses hashtable.
Time:O(m)
Space:O(1)
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote, magazine = list(ransomNote), list(magazine)
        dict = {}
        for i in magazine:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i]+1
        for i in ransomNote:
            if i in dict and dict[i]!=0:
                dict[i] = dict[i]-1
            else:
                return False
        return True
        
'''
Time:O(m*n)
Space:O(m)
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                i = magazine.index(c)
                magazine = magazine[:i]+magazine[i+1:]
        return True
